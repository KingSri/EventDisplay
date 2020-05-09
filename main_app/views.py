from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.utils.safestring import mark_safe
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Event, Comment
from .forms import EventForm, CommentForm
from django.template.loader import render_to_string


# Create your views here.

def home(request):
    return render(request, 'home.html')

def index(request):
    #is there a way I can filter based on user
    # event = Event.objects.filter(user=request.user).filter(#filter by date or other parameters)
    event = Event.objects.all()
    return render(request, 'event/index.html', {'event': event})

def about(request):
    return render(request, 'about.html')

# <---------Viewing Event Details--------->
@login_required
def event_detail(request, event_id):
    event = Event.objects.get(id=event_id)

    is_liked = False
    if event.likes.filter(id=request.user.id).exists():
        is_liked = True

    comment= Comment.objects.filter(event_id = event_id)
    comment_form = CommentForm()
    context = {
    'event': event,
    'comment': comment,
    'comment_form': comment_form,
    'total_likes': event.total_likes(),
    'is_liked': is_liked,
    }
    return render(request,'event/detail.html', context)

# <---------Creating an Event--------->

@login_required
def new_event(request):
    if request.method =='POST':
        print("form")
        form = EventForm(request.POST)
        print(form)
        if form.is_valid():
            event = form.save(commit=False)
            print("EVENT BEFORE SAVE")
            print(event)
            event.user = request.user
            event.save()
            print("EVENT AFTER SAVE")
            print(event)
            # print(event.id)
        return redirect('index')
    else:
        form = EventForm()
    context = {'form': form}
    return render(request, 'event/event_form.html', context)

# <---------Updating an Event--------->

@login_required
def update_event(request, event_id):
    event = Event.objects.get(id=event_id)
    if request.method =="POST":
        form = EventForm(request.POST, instance=event)
        if form.is_valid():
            event = form.save()
            return redirect('detail', event.id)
    else:
        form = EventForm(instance=event)
    return render(request, 'event/event_form.html', {'form': form})

# <---------Deleting an Event--------->

@login_required
def delete_event(request, event_id):
    Event.objects.get(id=event_id).delete()
    return redirect('index')

# <-----Signing in--------->

def signup(request):
  error_message = ''
  if request.method == 'POST':
    # This is how to create a 'user' form object
    # that includes the data from the browser
    form = UserCreationForm(request.POST)
    if form.is_valid():
      # This will add the user to the database
      user = form.save()
      # This is how we log a user in via code
      login(request, user)
      return redirect('index')
    else:
      error_message = 'Invalid sign up - please try again'
  # A bad POST or a GET request, so render signup.html with an empty form
  form = UserCreationForm()
  context = {'form': form, 'error_message': error_message}
  return render(request, 'registration/signup.html', context)

# <-----Comments--------->
@login_required
def new_comment(request, event_id):
    if request.method =='POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            event = Event.objects.get(id = event_id)
            print(event)
            comment.event = event
            comment.author = User.objects.get(id = request.user.id)
            comment.save()
        return redirect('detail', event.id)
    else:
        form = CommentForm()
    context = {'form': form}
    return render(request, 'comment/comment_form.html', context)

# <---------Liking an event--------->
def like_event(request):
    # event = get_object_or_404(Event, id=request.POST.get('event_id'))
    event = get_object_or_404(Event, id=request.POST.get('id'))
    is_liked = False
    if event.likes.filter(id=request.user.id).exists():
        event.likes.remove(request.user)
        is_liked=False
    else:
        event.likes.add(request.user)
        is_liked = True
    context = {
        'event': event,
        'is_liked': is_liked,
        'total_likes': event.total_likes(),
    }
    if request.is_ajax():
        html = render_to_string('event/like_section.html', context, request=request)
        return JsonResponse({'form':html})

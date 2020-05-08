from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.utils.safestring import mark_safe
from .models import Event
from .forms import EventForm


# Create your views here.

def home(request):
    return render(request, 'home.html')

def index(request):
    event = Event.objects.filter(user=request.user)
    return render(request, 'event/index.html', {'event': event})

def about(request):
    return render(request, 'about.html')

# <---------Viewing Event Details--------->
def event_detail(request, event_id):
    event = Event.objects.get(id=event_id)
    context = {'event': event}
    return render(request,'event/detail.html', context)


# <---------Creating an Event--------->

@login_required
def new_event(request):
    if request.method =='POST':
        form = EventForm(request.POST)
        if form.is_valid():
            event = form.save(commit=False)
            event.user = request.user
            event.save()
        return redirect('detail', event.id)
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






    # attempt at building calendar

# class ViewCalendar(generic.ListView):
#     model = Event
#     template_name = 'sricalendar/templates/calendar.html'
#
#     def context_data(self, **kwargs):
#         context = super().context_data(**kwargs)
#
#         e = get_date(self.request.GET.get('day', None))
#
#         cal = Calendar(e.year, e.month)
#
#         html_cal = cal.monthformat(withyear=True)
#         context['calendar'] = mark_safe(html_cal)
#         return context
#
# def get_date(req_day):
#     if req_day:
#         year, month = (int(x) for x in req_day.split('-'))
#         return date(year, month, day=1)
#     return datetime.today()

from django.urls import path
from . import views
from django.conf.urls import url
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [

    path('', views.home, name='home'),
    path('index/', views.index, name='index'),
    path('about/', views.about, name='about'),
    path('event/new/', views.new_event, name='new_event'),
    path('event/<int:event_id>/', views.event_detail, name='detail'),
    path('event/<int:event_id>/update/', views.update_event, name='update_event'),
    path('event/<int:event_id>/delete/', views.delete_event, name='delete_event'),
    url(r'^like/$', views.like_event, name='like_event'),
    # <----------------Create a comment---------------->
    path('new_comment/<int:event_id>/', views.new_comment, name='new_comment'),
    # <----------------Signup for an account---------------->
    path('accounts/signup', views.signup, name='signup'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

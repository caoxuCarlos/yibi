from django.urls import path
from . import views
urlpatterns = [
    path('',views.leave_message,name='message'),
]
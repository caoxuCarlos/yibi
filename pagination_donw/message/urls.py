from django.urls import path
from .views import (
    MessageListView,
    MessageDetailView,
    MessageCreateView,
    MessageUpdateView,
    MessageDeleteView,
    UserMessageListView
)
from . import views
urlpatterns = [
    path('',MessageListView.as_view(),name='message'),
    path('user/<str:username>',UserMessageListView.as_view(),name='user-message'),
    path('message/<int:pk>/',MessageDetailView.as_view(),name='message-detail'),
    path('message/<int:pk>/update',MessageUpdateView.as_view(),name='message-update'),
    path('message/<int:pk>/delete',MessageDeleteView.as_view(),name='message-delete'),
    path('message/new/',MessageCreateView.as_view(),name='message-create'),
]
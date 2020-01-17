from django.shortcuts import render,get_object_or_404
from django.contrib.auth.models import User
from .models import Message
from django.contrib.auth.mixins import LoginRequiredMixin,UserPassesTestMixin
from django.views.generic import (
ListView,
DetailView,
CreateView,
UpdateView,
DeleteView,
)



# Create your views here.

def leave_message(request):
    context={
        'messages':Message.objects.all()
    }
    return render(request,'message/message_page.html',context)

class MessageListView(ListView):
    # create a variable named model to tell our listview
    # what model to query in order to create the list
    model = Message
    # By default, it will try to find the following url:
    # <app>/<model>_<viewtype>.html
    # so we need to change template name.
    template_name = 'message/message_page.html'
    # Now we need to let the class know that
    # we want the variable called messages instead.
    context_object_name = 'messages'
    ordering = ['-date_posted']
    paginate_by = 5


class UserMessageListView(ListView):
    model = Message
    template_name = 'message/user_message.html'
    context_object_name = 'messages'
    paginate_by = 5

    def get_queryset(self):
        user = get_object_or_404(User,username=self.kwargs.get('username'))
        return Message.objects.filter(author=user).order_by('-date_posted')


class MessageDetailView(DetailView):
    model = Message

class MessageCreateView(LoginRequiredMixin,CreateView):
    model = Message
    fields = ['title','content']

    def form_valid(self, form):
           form.instance.author =self.request.user
           return super().form_valid(form)

class MessageUpdateView(LoginRequiredMixin,UserPassesTestMixin,UpdateView):
    model = Message
    fields = ['title','content']

    def form_valid(self, form):
           form.instance.author =self.request.user
           return super().form_valid(form)
    def test_func(self):
        message = self.get_object()
        if self.request.user == message.author:
            return True
        else:
            return False


class MessageDeleteView(LoginRequiredMixin,UserPassesTestMixin,DeleteView):
    model = Message
    success_url = '/message'
    def test_func(self):
        message = self.get_object()
        if self.request.user == message.author:
            return True
        else:
            return False



from django.shortcuts import render
from .models import Message

# Create your views here.
def leave_message(request):
    context={
        'messages':Message.objects.all()
    }
    return render(request,'message/message_page.html',context)
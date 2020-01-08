from django.shortcuts import render
from .models import Post

posts = [
    {
        'title':'She is laughing.',
        'author':'Carlos',
        'content':'I sneezed and she laughed.'
    },
    {
        'title': 'She is laughing 2.',
        'author': 'Carlos',
        'content': 'I sneezed and she laughed 2.'
    }
]


# Create your views here.
def welcome(request):
    context = {
        'posts':Post.objects.all()
        # 'posts':posts
    }
    return render(request, 'main_page/welcome.html',context)
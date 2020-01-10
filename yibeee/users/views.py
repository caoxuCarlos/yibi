from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from .forms import UserRegisterForm

# Create your views here.
def register(request):
    if request.method == 'POST':
        # creat a form that have request.POST data
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save() # save the user
            # the validated form data will be in
            # form.cleaned_data dictionary
            username = form.cleaned_data.get('username')
            # the below one is a "flashed message"
            messages.success(request,f'Account created for {username}!')
            return redirect('/') # the 1st para in redirect is the name we gave to our URL patten
    else:
        # just create a blank form
        form = UserRegisterForm()
    return render(request, 'users/register.html',{'form':form})

# more messages options
# messages.debug
# messages.info
# messages.success
# messages.warning
# messages.error
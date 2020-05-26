from django.shortcuts import render, redirect
# from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from .forms import UserSignUpForm

# Create your views here.
def signUp(request):
    if request.method == 'POST':
        signUpForm = UserSignUpForm(request.POST)
        if signUpForm.is_valid():
            signUpForm.save()
            username = signUpForm.cleaned_data.get('username')
            messages.success(request, f'Welcome { username }!')
            return redirect('/posts/')
    else:
        signUpForm = UserSignUpForm()
    return render(
        request,
        'users/sign_up.html',
        {
            'form': signUpForm
        }
    )


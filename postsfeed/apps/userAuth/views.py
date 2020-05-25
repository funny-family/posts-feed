from django.shortcuts import render, redirect
from .authForms import UserSignInForm, UserSignUpForm
from django.contrib.auth import authenticate, get_user_model, login, logout

# Create your views here.
def signInView(request):
    next = request.GET.get('next')
    signInForm = UserSignInForm(request.POST or None)
    if signInForm.is_valid():
        username = signInForm.cleaned_data.get('username')
        password = signInForm.cleaned_data.get('password')
        user = authenticate(username = username, password = password)
        login(request, user)
        if next:
            return redirect(next)
        return redirect('/posts/')
    context = {
        'form': signInForm
    }
    return render(request, 'auth/sign-in.html', context)

def signUpView(request):
    next = request.GET.get('next')
    signUpForm = UserSignUpForm(request.POST or None)
    if signUpForm.is_valid():
        user = signUpForm.save(commit = False)
        password = signUpForm.cleaned_data.get('password')
        user.set_password(password)
        user.save()
        newUser = authenticate(username = user.username, password = password)
        login(request, user)
        if next:
            return redirect(next)
        return redirect('/signin/')
    context = {
        'form': signUpForm
    }
    return render(request, 'auth/sign-up.html', context)

def logOutView(request):
    logout(request)
    return redirect('/signin/')

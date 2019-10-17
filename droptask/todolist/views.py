from django.shortcuts import render, redirect
from todolist.models import Tasklist, User
from todolist.forms import TaskForm, UserForm, UserProfileInfoForm

from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth import authenticate, login, logout


def index(request):
    content = {'index_text': "Welcome to DropTask page"}
    return render(request, 'index.html', content)


@login_required
def todolist(request):
    if request.method == 'POST':
        form = TaskForm(request.POST or None)
        if form.is_valid():
            form.save()
        return redirect('todolist')
    else:
        all_task = Tasklist.objects.all
        return render(request, 'todolist.html', {'all_task': all_task})


def contact(request):
    content = {'contact_text': "Welcome to contact us page"}
    return render(request, 'contact.html', content)


def about(request):
    content = {'about_text': "Welcome to about us page"}
    return render(request, 'about.html', content)


def register(request):
    registered = False

    if request.method == 'POST':
        user_form = UserForm(data=request.POST or None)
        profile_form = UserProfileInfoForm(data=request.POST or None)

        if user_form.is_valid() and profile_form.is_valid():

            user = user_form.save()
            user.set_password(user.password)
            user.save()

            profile = profile_form.save(commit=False)
            profile.user = user

            if 'profile_pics' in request.FILES:
                profile.profile_pics = request.FILES['profile_pics']

            profile.save()

            registered = True
        else:
            print(user_form.errors, profile_form.errors)
    else:
        user_form = UserForm()
        profile_form = UserProfileInfoForm()

    return render(request, 'register.html',
                  {'user_form': user_form,
                   'profile_form': profile_form,
                   'registered': registered})


@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('index'))


def user_login(request):

    if request.method == 'POST':
        username = request.POST.get['username']
        password = request.POST.get['password']

        user = authenticate(username=username, password=password)

        if user:
            if user.is_active:
                login(request, user)
                return HttpResponseRedirect(reverse('index'))
            else:
                return HttpResponse("Account not active")
        else:
            print("login failed")
            print("Username or password is wrong")
            return HttpResponse("Invalid details provided")
    else:
        return render(request, 'login.html', {})

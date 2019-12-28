from django.shortcuts import render
from django.urls import reverse
from django.views.generic import TemplateView
from register_login.forms import UserForm, UserProfileInfoForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect, HttpResponse
from .forms import FilmListForm
from db.models import Film

def index(request):
    if request.method == 'POST':
        title_form = request.POST.get('title')
        year_form = request.POST.get('year')

        if title_form and year_form:
            film = Film.objects.filter(title__icontains = title_form, year = int(year_form))
            if film:
                count = len(film)
                count_message = f"I have found {count} positions."
            else:
                film = Film.objects.all()
                count = len(film)
                count_message = f"I have found 0 movies for your request so let me show you my whole collection of {count} positions."
        elif title_form:
            film = Film.objects.filter(title__icontains = title_form)
            if film:
                count = len(film)
                count_message = f"I have found {count} positions."
            else:
                film = Film.objects.all()
                count = len(film)
                count_message = f"I have found 0 movies for your request so let me show you my whole collection of {count} positions."
        elif year_form:
            film = Film.objects.filter(year = int(year_form))
            if film:
                count = len(film)
                count_message = f"I have found {count} positions."
            else:
                film = Film.objects.all()
                count = len(film)
                count_message = f"I have found 0 movies for your request so let me show you my whole collection of {count} positions."
        else:
            film = Film.objects.all()
            count = len(film)
            count_message = f"I have found 0 movies for your request so let me show you my whole collection of {count} positions."

        return render(request, 'register_login/index.html',{'film':film,
                                                        'count_message':count_message})
    else:
        return render(request, 'register_login/index.html',{})

@login_required
def user_logout(request):
    logout(request)

    return HttpResponseRedirect(reverse('index'))

def user_login(request):
    warning = ''
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username = username, password = password)

        if user:
            if user.is_active:
                login(request, user)
                return HttpResponseRedirect(reverse('index'))
            else:
                return HttpResponse('ACCOUNT NOT ACTIVE')
        else:
            warning = 'Invalid login details supplied.'
            return render(request, 'register_login/login.html', {'warning':warning})

    else:
        return render(request, 'register_login/login.html', {})

def register(request):
    warning = ''
    registered = False

    if request.method == "POST":
        user_form = UserForm(data=request.POST)
        profile_form = UserProfileInfoForm(data=request.POST)

        if user_form.is_valid() and profile_form.is_valid():

            user = user_form.save()
            user.set_password(user.password)

            profile = profile_form.save(commit = False)
            profile.user = user

            if 'profile_pic' in request.FILES:
                profile.profile_pic = request.FILES['profile_pic']

                profile.save()

                registered = True

            warning = 'Succesfully added'

        else:
            print(user_form.errors, profile_form.errors)
    else:
        user_form = UserForm()
        profile_form = UserProfileInfoForm()

    return render(request, 'register_login/registration.html', {'user_form':user_form,
                                                                'profile_form':profile_form,
                                                                'registered':registered,
                                                                'warning':warning})

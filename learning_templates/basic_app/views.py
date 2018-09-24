from django.shortcuts import render
from . import forms
from basic_app.forms import NewUserForm
from basic_app.forms import UserForm, UserProfileInfoForm
from django.core.urlresolvers import reverse
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout

from django.http import HttpResponseRedirect, HttpResponse


# Create your views here.
def index(request):
    context={'text':"hello world", 'number':100, 'title':'asdAAA'}
    return render(request,'basic_app/index.html', context)


@login_required
def special(request):
    return HttpResponse('Logged')

@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('index'))


def other(request):
    return render(request,'basic_app/other.html')

def relative(request):
    return render(request,'basic_app/relative_url_templates.html')

def new_user_form(request):
    form = NewUserForm()

    if request.method == 'POST':
        form = NewUserForm(request.POST)
        if form.is_valid():
            form.save()

            return index(request)

        else: print ('invalid FOrm')
    context = {'form': form}

    return render(request,'basic_app/new_user_form.html', context)


def register(request):
    registered = False

    if request.method == 'POST':
        user_form = UserForm(data=request.POST)
        profile_form = UserProfileInfoForm(data=request.POST)

        if user_form.is_valid and profile_form.is_valid():
            user = user_form.save()
            user.set_password(user.password)
            user.save()

            profile = profile_form.save(commit=False)
            profile.user = user

            if 'profile_pic' in request.FILES:
                profile.profile_pic = request.FILES['profile_pic']

            profile.save()

            registered = True

        else:
            print ('ERROR')
            print (user_form.errors, profile_form.errors)

    else:
        user_form = UserForm()
        profile_form = UserProfileInfoForm()

    context = {'user_form':user_form, 'profile_form': profile_form, 'registered':registered}
    return render(request, 'basic_app/registration.html', context)



def user_login(request):

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username=username,password=password)

        if user:
            if user.is_active:
                login(request,user)
                return HttpResponseRedirect(reverse('index'))
            else:
                return HttpResponse('Account not active.')
        else:
            print ('someone tried to loggin and failed')
            return HttpResponse('invalid login')
    else:
        return render(request, 'basic_app/login.html',{})



def date_generator_form(request):
    return render(request, 'basic_app/date_generator_form.html',{})

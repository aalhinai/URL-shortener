from django.shortcuts import render, render_to_response

from URLshortenerApp.forms import *
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from django.views.decorators.csrf import csrf_protect
from django.http import HttpResponseRedirect
from django.template import RequestContext

from django.contrib import auth
from django.views.decorators.csrf import csrf_exempt


# Create your views here.
#ABD: Added for the first index template
def  index(request):
      return render_to_response('index.html')




#ABD: Added for athurization and login
@csrf_protect
def login(request):
    #c = {}
    #c.update(csrf(request))
    return render_to_response('registration/login.html')



def auth_view(request):
    username = request.POST.get('username', ' ')
    password = request.POST.get('password', ' ')
    user = auth.authenticate(username=username, password=password)

    if user is not None:
       auth.login(request, user)
       return HttpResponseRedirect('home.html')

    else:
       return HttpResponseRedirect('index.html')


@csrf_protect
def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = User.objects.create_user(
            username=form.cleaned_data['username'],
            password=form.cleaned_data['password1'],
            email=form.cleaned_data['email']
            )
            return HttpResponseRedirect('/register/success/')
    else:
        form = RegistrationForm()
    variables = RequestContext(request, {
    'form': form
    })

    return render_to_response(
    'registration/register.html',
    variables,
    )



def register_success(request):
    return render_to_response(
    'registration/success.html'
    )



def logout_page(request):
    logout(request)
    return HttpResponseRedirect('/')


@login_required
def home(request):
    return render_to_response(
    'home.html',
    { 'user': request.user }
    )

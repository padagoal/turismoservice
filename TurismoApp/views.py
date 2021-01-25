from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import authenticate, logout,login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from TurismoApp.models import Profile
from TurismoTour.models import Tour
from TurismoBlog.models import Post
from TurismoBus.models import *
# Create your views here.


def index(request):
    username = request.user.username
    logueo_user = False
    if request.user.is_authenticated:
        logueo_user = True

    listaTour = Tour.objects.filter(is_from_staff=True,tour_active=True)[:3]
    listaPosteo = Post.objects.order_by('-id')[:6]
    listBus = listBusesIndex()
    response = {
        'logueo_user':logueo_user,
        'username':username,
        'listaTour':listaTour,
        'listaPosteo':listaPosteo,
        'listBus':listBus
        }
    return render(request,'travelix/main_detalle.html',response)


def history(request):
    return render(request,'travelix/history.html',{'titulo': 'Historia'})


def metas(request):
    return render(request,'travelix/metas.html',{'titulo': 'Objetivos y Metas'})


def contact(request):
    return render(request,'travelix/contact.html',{'titulo':'Contacto'})


def dashboard(request):
    if not request.user.is_authenticated:
        return HttpResponse("NOOOO NO NO !!")
    return HttpResponse("DASH !!")


def login_user(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['pass']
        user = authenticate(username=username,password=password)
        if user is None:
            return HttpResponse('Sin Acceso')
        else:
            login(request,user)
            return redirect("/")

    return render(request,'Login_v5/index.html')


def register(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['pass']
        email = request.POST['email']
        User.objects.create_user(username=username,password=password,email=email)
        user = authenticate(username=username, password=password)
        if user is None:
            return HttpResponse('Sin Acceso')
        else:
            login(request, user)
            return redirect("/")

    return render(request,'Login_v5/register.html')


@login_required(login_url='/login')
def edit_user(request):
    if request.method == 'POST':
        user = request.user
        name_user = request.POST["user_name"]
        lastname_user = request.POST["lastname"]
       # date_birth_user = request.POST["datebirth"]
        telephone_user = request.POST["phone"]
        #ci_user = request.POST["ci"]
        profile, created = Profile.objects.get_or_create(user=request.user)
        user.profile.name_user = name_user
        user.profile.lastname_user = lastname_user
        #user.profile.date_birth_user = date_birth_user
        user.profile.telephone_user = telephone_user
        #if ci_user > 0:
        #    user.profile.CI_user = ci_user
        #    user.profile.is_customer = True
        user.save()
        return redirect("/profile")
    #usuario = User.objects.get_or_create(pk=request.user)

    return render(request, 'Login_v5/edit_user.html',{
        'usuario': request.user
    })


def profile_user(request):
    return render(request,'Login_v5/profile.html')


def logout_user(request):
    logout(request)
    return redirect('/')

def listBusesIndex():
    bus = Bus.objects.all().order_by('ciudad_partida_desc')[:10]
    listBus = []
    for data in bus:
        busDto = BusDto()
        busDto.ciudad_partida_desc = data.ciudad_partida_desc
        busDto.ciudad_destino_desc = data.ciudad_destino_desc
        busDto.ciudad_partida = Ciudad.objects.get(pk=data.ciudad_partida)
        busDto.ciudad_destino = Ciudad.objects.get(pk=data.ciudad_destino)
        busDto.precio = data.precio
        busDto.ruta = data.ruta
        listBus.append(busDto)

    return listBus

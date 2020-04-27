from django.shortcuts import render, get_object_or_404, redirect
from .models import Film, DodatkoweInfo, Ocena
from .form import FilmForm, DodatkoweInfoForm, OcenaForm
from django.contrib.auth.decorators import login_required
from django.core.exceptions import ObjectDoesNotExist
from rest_framework import viewsets
from django.contrib.auth.models import User
from .serializers import UserSerializer, FilmSerializer

class UserView(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class FilmView(viewsets.ModelViewSet):
    queryset = Film.objects.all()
    serializer_class = FilmSerializer

def wszystkie_filmy(request):
    # return HttpResponse("<h1>To jest nasz pierwszy test</h1>")
    filmy = ["Avatar", "Titanic"]
    wszystkie = Film.objects.all()
    return render(request, 'filmy.html', {'wszystkie' : wszystkie})

@login_required
def nowy_film(request):

    czy_nowy = True
    form_film = FilmForm(request.POST or None, request.FILES or None)
    form_dodatkowe = DodatkoweInfoForm(request.POST or None)

    if all((form_film.is_valid(), form_dodatkowe.is_valid())):
        film = form_film.save(commit=False)
        dodatkowe = form_dodatkowe.save()
        film.dodatkowe = dodatkowe
        film.save()
        return redirect(wszystkie_filmy)

    return render(request, 'film_form.html', {'form' : form_film, 'form_dodatkowe' : form_dodatkowe, 'czy_nowy' : czy_nowy})

@login_required
def edytuj_film(request, id):
    czy_nowy = False
    film = get_object_or_404(Film, pk=id)

    oceny = Ocena.objects.filter(film=film)
    aktorzy = film.aktorzy.all() # <---------- !!!!

    try:
        dodatkowe = DodatkoweInfo.objects.get(film=film.id)
    except ObjectDoesNotExist:
        dodatkowe = None

    film.dodatkowe = dodatkowe
    form_film = FilmForm(request.POST or None, request.FILES or None, instance=film)
    form_dodatkowe = DodatkoweInfoForm(request.POST or None, instance=dodatkowe)
    form_ocena = OcenaForm(request.POST or None)

    if request.method == 'POST':
        if 'gwiazdki' in request.POST:
            ocena = form_ocena.save(commit=False)
            ocena.film = film
            ocena.save()

    if all((form_film.is_valid(), form_dodatkowe.is_valid())):
        film = form_film.save(commit=False)
        dodatkowe = form_dodatkowe.save();
        film.dodatkowe = dodatkowe
        film.save()
        return redirect(wszystkie_filmy)

    return render(request, 'film_form.html', {'form' : form_film, 'form_dodatkowe' : form_dodatkowe,
                    'czy_nowy' : czy_nowy, 'oceny' : oceny, 'form_ocena' : form_ocena, 'aktorzy' : aktorzy})

@login_required
def usun_film(request, id):
    film = get_object_or_404(Film, pk=id)

    if request.method == "POST":
        film.delete()
        return redirect(wszystkie_filmy)

    return render(request, 'potwierdz.html', {'film' : film})
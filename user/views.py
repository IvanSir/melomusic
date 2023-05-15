from django.contrib import messages
from django.contrib.auth import authenticate, get_user_model, login, logout
from django.http import JsonResponse
from django.shortcuts import redirect, render
from rest_framework import status, viewsets
from rest_framework.decorators import action
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.renderers import JSONRenderer, TemplateHTMLRenderer
from rest_framework.response import Response
from django.conf import settings

from music.models import Music
from user.forms import CustomUserCreationForm

from .serializers import CustomUserSerializer


def registerUser(request):
    """Register user view"""
    new_song_for_player = (
        Music.objects.filter(published=True).order_by("-created").first()
    )
    form = CustomUserCreationForm()

    if request.method == "POST":
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            try:
                user = form.save(commit=False)
                user.email = user.email.lower()
                user.save()
                messages.success(request, "User account was created!")
                login(request, user, backend=settings.AUTHENTICATION_BACKENDS[0])
                return redirect("home")
            except Exception as e:
                messages.error(request, "An error has occurred during registration")

        else:
            error = list(form.errors.values())[0]
            messages.error(request, error[0])

    context = {"form": form, "player": new_song_for_player}
    return render(request, "user/auth.html", context)


def loginUser(request):
    """Login user view"""
    if request.user.is_authenticated:
        return redirect("home")

    new_song_for_player = (
        Music.objects.filter(published=True).order_by("-created").first()
    )
    if request.method == "POST":
        email = request.POST["email"]
        password = request.POST["password"]

        try:
            user = get_user_model().objects.get(email=email, password=password)
            login(request, user, backend=settings.AUTHENTICATION_BACKENDS[0])
            return redirect(request.GET["next"] if "next" in request.GET else "home")
            
        except:
            messages.error(request, "User does not exist or password is invalid!")

    context = {"player": new_song_for_player}
    return render(request, "user/auth.html", context)


def logoutUser(request):
    """Logout user viwe"""
    logout(request)
    messages.success(request, "Successfully Logged out !")
    return redirect("home")

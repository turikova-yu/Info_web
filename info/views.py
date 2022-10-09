from django.shortcuts import render
from .models import *

def index(request):

# Home
    home = Home.objects.latest('update_time')

# About
    about = About.objects.latest('updated')
    profiles = Profile.objects.filter(about=about)

# Skills
    categories = Category.objects.all()

# Portfolios
    portfolios = Portfolio.objects.all()

    context = {
        'home' : home,
        'about' : about,
        'profiles' : profiles,
        'categories' : categories,
        'portfolios' : portfolios,
    }

    return render(request, 'info/main.html', context)

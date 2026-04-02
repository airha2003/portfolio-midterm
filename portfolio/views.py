from .models import Portfolio
from django.shortcuts import render





def home(request):
    # This remains your landing page
    return render(request, 'portfolio/home.html')

def about(request):
    return render(request, 'portfolio/about.html')

def skills(request):
    return render(request, 'portfolio/skills.html')

def resume(request):
    return render(request, 'portfolio/resume.html')

def profile_view(request,email):
    return render(request, 'portfolio/profile.html',{'email':email})

def portfolio(request):
    # Move your database logic here so projects show up on the Portfolio page
    projects = Portfolio.objects.all()
    return render(request, 'portfolio/portfolio.html', {'projects': projects})
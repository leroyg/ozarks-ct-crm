from django.shortcuts import render
from django.http import HttpResponse

def sports(request):
    return render(request, 'sports/teams.html')

def home(request):
    return render(request, 'sports/dashboard.html')

def trainer(request):
    return render(request, 'sports/trainer.html')

def team(request):
    return render(request, 'sports/team.html')
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import Profile, Project, Review

# Create your views here.

def index(request):
    all = Project.objects.all()
    return render(request, 'index.html', { "all":all})

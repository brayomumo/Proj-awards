from django.contrib import admin
from .models import Profile, Project, Review

# Register your models here.
admin.site.register(Project)
admin.site.register(Review)
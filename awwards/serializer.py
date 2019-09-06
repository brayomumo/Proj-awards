from rest_framework import serializers
from .models import Profile, Project

class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = ('profile_picture','prof_user', 'bio', 'all_projects')


class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = ('title', 'details', 'link', 'design', 'usability', 'content')
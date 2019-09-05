from django.test import TestCase
from .models import Project

# Create your tests here.
class test_projects(TestCase):
    def setUp(self):
        self.proj1 = Project(title="The grand proj",description="the grand coded project")

    def test_instance(self):
        self.assertTrue(isinstance(self.proj1, Project))

    def test_save_method(self):
        self.proj1.save_project()
        proj = Project.objects.all()
        self.assertTrue(len(proj) > 0 )
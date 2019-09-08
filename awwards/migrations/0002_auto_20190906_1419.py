# -*- coding: utf-8 -*-
# Generated by Django 1.11.24 on 2019-09-06 14:19
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('awwards', '0001_initial'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Review',
        ),
        migrations.AlterModelOptions(
            name='project',
            options={'ordering': ['-id']},
        ),
        migrations.AddField(
            model_name='profile',
            name='all_projects',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='awwards.Project'),
        ),
        migrations.AddField(
            model_name='profile',
            name='bio',
            field=models.TextField(default=''),
        ),
        migrations.AddField(
            model_name='profile',
            name='contact_info',
            field=models.CharField(blank=True, max_length=200),
        ),
        migrations.AddField(
            model_name='profile',
            name='prof_user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='profile',
            name='profile_Id',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='profile',
            name='profile_picture',
            field=models.ImageField(blank=True, upload_to='prof_pics/'),
        ),
        migrations.AddField(
            model_name='project',
            name='content',
            field=models.IntegerField(choices=[(0, 0), (1, 1), (2, 2), (3, 3), (4, 4), (5, 5), (6, 6), (7, 7), (8, 8), (9, 9), (10, 10)], default=0),
        ),
        migrations.AddField(
            model_name='project',
            name='design',
            field=models.IntegerField(choices=[(0, 0), (1, 1), (2, 2), (3, 3), (4, 4), (5, 5), (6, 6), (7, 7), (8, 8), (9, 9), (10, 10)], default=0),
        ),
        migrations.AddField(
            model_name='project',
            name='details',
            field=models.TextField(default=''),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='project',
            name='image',
            field=models.ImageField(blank=True, upload_to='project_pics'),
        ),
        migrations.AddField(
            model_name='project',
            name='link',
            field=models.CharField(default='No Bio', max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='project',
            name='title',
            field=models.CharField(default='project title', max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='project',
            name='usability',
            field=models.IntegerField(choices=[(0, 0), (1, 1), (2, 2), (3, 3), (4, 4), (5, 5), (6, 6), (7, 7), (8, 8), (9, 9), (10, 10)], default=0),
        ),
        migrations.AddField(
            model_name='project',
            name='user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='project',
            name='user_project_id',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='project',
            name='vote_submissions',
            field=models.IntegerField(default=0),
        ),
    ]

# Generated by Django 3.2.4 on 2021-06-14 18:45

import uuid

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('mentee', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='MentorDepartment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('uid', models.UUIDField(default=uuid.uuid4, editable=False, unique=True)),
                ('label', models.CharField(max_length=32)),
            ],
        ),
        migrations.CreateModel(
            name='MentorDesignation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('uid', models.UUIDField(default=uuid.uuid4, editable=False, unique=True)),
                ('label', models.CharField(max_length=32)),
            ],
        ),
        migrations.CreateModel(
            name='MentorDiscipline',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('uid', models.UUIDField(default=uuid.uuid4, editable=False, unique=True)),
                ('label', models.CharField(max_length=32)),
            ],
        ),
        migrations.CreateModel(
            name='MentorResponsibility',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('uid', models.UUIDField(default=uuid.uuid4, editable=False, unique=True)),
                ('description', models.TextField(max_length=256)),
            ],
        ),
        migrations.CreateModel(
            name='Mentor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('uid', models.UUIDField(default=uuid.uuid4, editable=False, unique=True)),
                ('is_verified', models.BooleanField(default=False)),
                ('profile_completed', models.BooleanField(default=False)),
                ('about_self', models.TextField(blank=True, max_length=512)),
                ('specialization', models.TextField(blank=True, max_length=256)),
                ('expected_min_mentorship_duration', models.DurationField(blank=True, null=True)),
                ('expected_max_mentorship_duration', models.DurationField(blank=True, null=True)),
                ('is_accepting_mentorship_requests', models.BooleanField(default=True)),
                ('other_responsibility', models.TextField(blank=True, max_length=512)),
                ('rating', models.DecimalField(decimal_places=2, max_digits=3, null=True)),
                ('accepted_mentee_types', models.ManyToManyField(to='mentee.MenteeDesignation')),
                ('department', models.ForeignKey(null=True, on_delete=django.db.models.deletion.RESTRICT,
                                                 related_name='mentors_with_department', to='mentor.mentordepartment')),
                ('designation', models.ForeignKey(null=True, on_delete=django.db.models.deletion.RESTRICT,
                                                  related_name='mentors_with_designation',
                                                  to='mentor.mentordesignation')),
                ('discipline', models.ForeignKey(null=True, on_delete=django.db.models.deletion.RESTRICT,
                                                 related_name='mentors_with_discipline', to='mentor.mentordiscipline')),
                ('responsibilities', models.ManyToManyField(to='mentor.MentorResponsibility')),
                (
                'user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]

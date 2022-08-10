
# Create your views here.
from django.shortcuts import render
from typing import FrozenSet
from django import template
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from django.db.models.query import QuerySet
from django.forms.models import inlineformset_factory
from django.shortcuts import get_object_or_404, redirect, render, redirect, resolve_url
from django.template import loader
from django.http import HttpResponse, HttpResponseRedirect, request
from django.urls import reverse
from django.views import generic
from django.views.generic.edit import CreateView, FormView, UpdateView
from django.views.generic.list import ListView
from django.contrib import messages
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.conf import settings 
# from bootstrap_datepicker_plus import DatePickerInput
from django.core.mail import send_mail
from django.views.generic import TemplateView

# Create your views here.



class IndexView(TemplateView):
    template_name = "firsttune/index.html"
    

class Post1View(TemplateView):
    template_name = "firsttune/post1.html"

class EducationView(TemplateView):
    template_name = "firsttune/education.html"

class InformationView(TemplateView):
    template_name = "firsttune/information.html"

class AfricaView(TemplateView):
    template_name = "firsttune/africa.html"

class AboutView(TemplateView):
    template_name = "firsttune/about.html"


# class TeamView(TemplateView):
#     template_name = 'michael/team.html'

# class ContactView(TemplateView):
#     template_name = 'michael/contact.html'

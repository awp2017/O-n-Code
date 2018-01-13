# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.views.generic import DetailView
from django.shortcuts import render
from models import Problem

# Create your views here.

from onCode.models import UserProfile

from django.views.generic import ListView


# Create your views here.
class LeaderboardView(ListView):
    #import pdb;pdb.set_trace()
    model = UserProfile
    template_name = 'leaderboard-view.html'
    context_object_name = 'users'
    ordering = ['-score']
    
    
    

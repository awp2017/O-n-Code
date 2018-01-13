# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from models import *
from django.shortcuts import render
from django.views.generic import DetailView, ListView, CreateView, UpdateView, DeleteView

# Create your views here.

from django.views.generic import ListView


# Create your views here.
class LeaderboardView(ListView):
    #import pdb;pdb.set_trace()
    model = UserProfile
    template_name = 'leaderboard-view.html'
    context_object_name = 'users'
    ordering = ['-score']
    

class ProblemDetailView(DetailView):
    template_name = 'problem.html'
    model = Problem
    context_object_name = 'problem'

class ViewComments(ListView):
    template_name = 'viewComment.html'
    model = Comment
    context_object_name = 'Comment'
    def get_queryset(self, *args, **kwargs):
        return Comment.objects.filter(problem_id=self.kwargs.get('pk'))

class AddComment(CreateView):
    template_name = 'addComment.html'
    model = Comment
    context_object_name = 'Comment'

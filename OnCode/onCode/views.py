# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from models import *
from django.shortcuts import render
from django.urls import reverse
from django.views.generic import DetailView, ListView, CreateView, UpdateView, DeleteView
from onCode.forms import UserEditForm
from django.urls import reverse
from forms import *

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

class UserProfileDetailView(DetailView):
    template_name = 'user-profile-details.html'
    model = UserProfile
    context_object_name = 'userprofile'

class ProblemsListView(ListView):
    model = Problem
    template_name = 'problems-view-list.html'
    context_object_name = 'problems'   
    
    
class UserCreateView(CreateView):
    form_class = UserCreateForm
    template_name = 'user-create-view.html'
    model = User

    def get_success_url(self, *args, **kwargs):
        profile = UserProfile(user_pk = self.object, score=0)
        profile.save()
        return reverse(
            'edit_user_profile_view', 
            kwargs={
                'pk': self.object.pk
            }
        )

class UserUpdateView(UpdateView):
    template_name = 'user-edit-profile-view.html'
    form_class = UserEditForm
    model = UserProfile
    
    
    def get_success_url(self, *args, **kwargs):
        return reverse(
            'user-profile-view',
            kwargs={
                'pk': self.kwargs['pk']
            }
        )
        
        
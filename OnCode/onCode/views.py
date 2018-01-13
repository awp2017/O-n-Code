# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from models import *
from django.shortcuts import render
from django.urls import reverse
from django.views.generic import DetailView, ListView, CreateView, UpdateView, DeleteView
from forms import *
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import redirect


# Create your views here.
class LeaderboardView(ListView):
    # import pdb;pdb.set_trace()
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
        profile = UserProfile(user_pk=self.object, score=0)
        profile.save()
        return reverse(
            'edit_user_profile_view',
            kwargs={
                'pk': self.object.pk
            }
        )


class AddComment(CreateView):
    template_name = 'addComment.html'
    model = Comment
    form_class = AddCommentForm

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.user_id = User.objects.get(pk=self.request.user.id)
        self.object.problem_id = Problem.objects.get(pk=self.kwargs.get('pk'))
        self.object.save()
        return super(AddComment, self).form_valid(form)

    def get_success_url(self):
        return reverse(
            'view_comment',
            kwargs={
                'pk': self.kwargs.get('pk')
            }
        )


def login_view(request):
    context = {}
    if request.method == 'GET':
        form = LoginForm()
    elif request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            user = authenticate(username=form.cleaned_data['username'],
                                password=form.cleaned_data['password'])
            if user:
                login(request=request,
                      user=user)
                return redirect('problem_list_view')
            else:
                context['error_message'] = 'Wrong username or password!'
    context['form'] = form
    return render(request, 'login.html', context)


def logout_view(request):
    if request.method == 'GET':
        logout(request)
        return redirect('login')


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

# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from models import *
from django.shortcuts import render
from django.urls import reverse
from django.views.generic import DetailView, ListView, CreateView, UpdateView, DeleteView
from forms import *
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import redirect
from django.contrib.auth.mixins import LoginRequiredMixin


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
    
    def get_context_data(self, **kwargs):
        context = super(ProblemDetailView, self).get_context_data(**kwargs)
        context['data'] = {
            'is_logged_user' : self.request.user.is_authenticated,
            'is_problem_resolved' : ResolvedProblems.objects.filter(problem_id = Problem.objects.get(pk = self.kwargs.get('pk')))
                        .filter(user_id = User.objects.get(pk = self.request.user.pk)).exists() 
        }
        
        return context
        


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
    
    def get_context_data(self, **kwargs):

        context = super(UserProfileDetailView, self).get_context_data(**kwargs)
        context['data'] = {
            'resolved_problems':ResolvedProblems.objects.filter(user_id = self.kwargs['pk']),
            'is_logged_user':self.request.user.is_authenticated
        }
        
        return context


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


class AddComment(LoginRequiredMixin, CreateView):
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


class UserUpdateView(LoginRequiredMixin, UpdateView):
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


class GetInput(DetailView):
    model = Rezolvari
    template_name = "getInput.html"
    context_object_name = "rezolvari"
    #

    # def get_context_data(self, **kwargs):
    #     context = super(GetInput, self).get_context_data(**kwargs)
    #     context['x'] =  Rezolvari.objects.filter(problem=self.kwargs.get('pk'))
    # def get_queryset(self, *args, **kwargs):
    #     return Rezolvari.objects.filter(problem=self.kwargs.get('pk'))


class SubmitSolution(LoginRequiredMixin, UpdateView):
    model = User
    template_name = "submitSolution.html"
    context_object_name = "user"
    form_class = SubmitSolutionForm

    def form_valid(self, form):
        # import pdb;pdb.set_trace()
        user_id = self.request.user.id
        self.object = form.save(commit=False)
        raspuns = form.cleaned_data['answer']
        answer = Rezolvari.objects.get(problem=self.kwargs.get('pk')).answer
        pk = self.kwargs.get('pk')
        user = UserProfile.objects.get(pk=user_id)
        score = user.score
        problem = Problem.objects.get(pk=self.kwargs.get('pk'))
        difficultate = problem.difficulty
        difficulties = {'1': 25, '2': 50, '3': 75, '4': 100}
        if answer == raspuns:
            problrez = ResolvedProblems(user_id=User.objects.get(pk=user_id), problem_id=problem)
            problrez.save()
            score += difficulties[str(difficultate)]
        user.score = score
        user.save()
        return super(SubmitSolution, self).form_valid(form)


    def get_success_url(self):
        return reverse('problem_detail', kwargs={'pk': self.kwargs.get('pk')})


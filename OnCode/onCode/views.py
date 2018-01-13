# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.views.generic import DetailView
from django.shortcuts import render
from models import Problem

# Create your views here.

class ProblemView(DetailView):
    model = Problem
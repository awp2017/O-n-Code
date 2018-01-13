# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models
from django.contrib.auth.models import User

difficulties = [('1','Low'), ('2','Medium'), ('3', 'High'),  ('4', 'God')]

# Create your models here.
class Problem(models.Model):
    title = models.CharField(max_length=50)
    content = models.CharField(max_length=350)
    difficulty = models.CharField(max_length=50, choices=difficulties)
    hints = models.CharField(max_length=100)
    
    def __str__(self):
        return self.title

class Rezolvari(models.Model):
    test = models.CharField(max_length=150000)
    answer = models.CharField(max_length=150000)
    problem = models.ForeignKey(Problem, on_delete=models.CASCADE)
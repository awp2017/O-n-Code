# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.

class Comment(models.Model):
    problem_id = models.ForeignKey(Problem, blank=True)
    user_id = models.ForeignKey(User, blank=True)
    text = models.CharField(max_length=200)
    
    def __str__(self):
        return self.text

# -*- coding: utf-8 -*-
from django.shortcuts import render

def about(request):
      return render(request, 'covid_app/about.html')
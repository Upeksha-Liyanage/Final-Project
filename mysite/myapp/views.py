# -*- coding: utf-8 -*-
from __future__ import unicode_literals


from django.shortcuts import render, render_to_response

# Create your views here.
def index(request):
	return render_to_response('index.html')

def network(request):
	return render_to_response('network.html')

def compile(request):
    return render_to_response('compile.html')



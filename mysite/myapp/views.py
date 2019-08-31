# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render, render_to_response
import os

# Create your views here.
def index(request):
	return render_to_response('index.html')

def compile(request):
	return render_to_response('compile.html')

# def folder(request):
# 	spath = r"/home"

# def folder(path):
#     # subprocess.check_call(['xdg-open', '--', path])
# 	# file = open("/home")
# 	file="/"
#     path=os.getcwd()+file
#     fp=open(path,'r+')
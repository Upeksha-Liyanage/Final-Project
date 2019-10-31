# -*- coding: utf-8 -*-
from __future__ import unicode_literals


from django.shortcuts import render, render_to_response
from django.http import HttpResponse
import os

# Create your views here.
def index(request):
	return render_to_response('index.html')

def network(request):
	return render_to_response('network.html')

def configure(request):
    return render_to_response('graph.html')

def compile(request):
	
    return render(request, 'compile.html', {'what':'Django File Upload'})
 
def upload(request):
    if request.method == 'POST':
        handle_uploaded_file(request.FILES['file'], str(request.FILES['file']))
        return HttpResponse("Successful")
 
    return HttpResponse("Failed")
 
def handle_uploaded_file(file, filename):
    if not os.path.exists('upload/'):
        os.mkdir('upload/')
 
    with open('upload/' + filename, 'wb+') as destination:
        for chunk in file.chunks():
            destination.write(chunk)



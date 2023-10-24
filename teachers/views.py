from django.http import HttpResponse
from django.shortcuts import render

def welcome(request):
    return HttpResponse('Welcome to Emobilis')

def about(request):
    return HttpResponse('About Emobilis')

def services(request):
    return HttpResponse('Emobilis Services')

def contact(request):
    return HttpResponse('Contact Emobilis')


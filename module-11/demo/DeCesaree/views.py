from django.shortcuts import render, HttpResponse

def home(request):
    return HttpResponse("DeCesare says Hello!")

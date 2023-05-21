import re
from django.utils.timezone import datetime
from django.http import HttpResponse
from django.shortcuts import render
from django.shortcuts import redirect
from hello.forms import LogMessageForm
from hello.models import LogMessage
from django.views.generic import ListView


def index(request):
    return render(request,'index.html')
def index1(request):
    return render(request,'index1.html')
def index2(request):
    return render(request,'index2.html')
def index3(request):
    return render(request,'index3.html')
def groom(request):
    return render(request,'groom.html')
def bride(request):
    return render(request,'bride.html')






    # Filter the name argument to letters only using regular expressions. URL arguments
    # can contain arbitrary text, so we restrict to safe characters only.
    
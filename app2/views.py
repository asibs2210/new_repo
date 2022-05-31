from django.shortcuts import render
from django.http import HttpResponse


def indexview(request):
  return HttpResponse('Success')

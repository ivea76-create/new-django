from django.shortcuts import render

# Create your views here.
"""
视图views就是一个python函数
需要用到HttpRequest类
请求和返回响应
"""
from django.http import HttpRequest
from django.http import HttpResponse


def index(request):
    return HttpResponse('ok')


def hi(request):
    return HttpResponse('hi')

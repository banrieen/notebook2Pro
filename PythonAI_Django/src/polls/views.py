# -*- coding: UTF-8 -*-

'''
Created on 2018年3月22日

@author: lizhen
'''

from django.http import HttpResponse


def index(request):
    return HttpResponse("Hello, World banrieen,You are at the polls index.")


    
    
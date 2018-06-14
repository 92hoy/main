#-*- coding: utf-8 -*-
from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_protect
from django.db import connections

# 호출 상태
def main(request):

    #resDataJson = api_coSpaces()

    context = {}
    #context['resDataJson'] = resDataJson

    return render(request, 'main/index.html', context)

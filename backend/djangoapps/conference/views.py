#-*- coding: utf-8 -*-
from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_protect
from django.db import connections

from backend.djangoapps.common.api.views import api_coSpaces
from backend.djangoapps.common.api.views import api_coSpaceId
from backend.djangoapps.common.api.views import api_activeCall

# 컨퍼런스 목록
def conferenceRoom(request):

    context = {}

    return render(request, 'conference/conferenceRoom.html', context)

# 진행중인 회의 관리
def activeCall(request):

    resDataJson = api_activeCall()

    context = {}
    context['resDataJson'] = resDataJson

    return render(request, 'conference/activeCall.html', context)

# 진행중인 회의 관리
def template(request):

    #resDataJson = api_activeCall()

    context = {}
    #context['resDataJson'] = resDataJson

    return render(request, 'conference/template.html', context)

# 컨퍼런스 제공
def reserveConference(request):

    #resDataJson = api_activeCall()

    context = {}
    #context['resDataJson'] = resDataJson

    return render(request, 'conference/reserveConference.html', context)

# 컨퍼런스 제공 (달력)
def reserveConferenceCal(request):

    #resDataJson = api_activeCall()

    context = {}
    #context['resDataJson'] = resDataJson

    return render(request, 'conference/reserveConferenceCal.html', context)

#-*- coding: utf-8 -*-
from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_protect
from django.db import connections
from django.conf import settings
from django.utils import translation
from django.utils.translation import ugettext as _
import math

from backend.djangoapps.common.api.views import api_coSpaces


def commList(request):

    page_size = int(request.POST.get('page_size'))
    curr_page = int(request.POST.get('curr_page'))
    search_str = request.POST.get('search_str')

    realList = api_coSpaces(search_str)

    totalLength = len(realList)
    totalPage = ( math.floor((totalLength - 1) / page_size) ) + 1
    boardList = []

    startIndex = ((curr_page * page_size) - page_size)
    endIndex = (curr_page * page_size) - 1

    print("startIndex = ", startIndex)
    print("endIndex = ", endIndex)
    print("len(realList) = ", len(realList))

    try:
        for n in range(startIndex, endIndex+1):
            print(n)
            boardDict = {}
            print("realList[n]['name'] = ",realList[n]['name'])
            boardDict['id'] = realList[n]['id']
            boardDict['name'] = realList[n]['name']
            boardDict['autoGenerated'] = realList[n]['autoGenerated']
            if 'uri' in realList:
                boardDict['uri'] = realList[n]['uri']
            else:
                boardDict['uri'] = ''
            boardDict['callId'] = realList[n]['callId']
            boardList.append(boardDict)
    except BaseException:
        pass

    context = {}
    context['totalPage'] = totalPage
    context['curr_data'] = boardList

    return JsonResponse(context)

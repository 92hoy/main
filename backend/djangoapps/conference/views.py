#-*- coding: utf-8 -*-
from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_protect, csrf_exempt
from django.db import connections
import json

from backend.djangoapps.common.api.views import api_coSpaces
from backend.djangoapps.common.api.views import api_coSpaceId
from backend.djangoapps.common.api.views import api_activeCall
from backend.djangoapps.common.api.views import api_activeCallId
from backend.djangoapps.common.api.views import api_activeCallLegs
from backend.djangoapps.common.api.views import api_coSpaces_POST

# 컨퍼런스 목록
def conferenceRoom(request):

    context = dict()
    context['data'] = api_coSpaces()

    return render(request, 'conference/conferenceRoom.html', context)


# 컨퍼런스 추가
@csrf_exempt
def conferenceRoomAdd(request):

    res = api_coSpaces_POST(request)

    return JsonResponse({'msg': 'success'})


# 진행중인 회의 관리
def activeCall(request):

    resDataJson = api_activeCall()

    res_list = list()

    for data in resDataJson:
        reData = dict()
        coSpaceId = api_activeCallId(data['@id'])
        data_coSpaceId = api_coSpaceId(coSpaceId)
        data_activeCallLegs = api_activeCallLegs(data['@id'])

        reData['name'] = data['name']
        reData['callId'] = data_coSpaceId['coSpace']['callId']
        reData['cv'] = data_activeCallLegs['callLegs']['@total']
        res_list.append(reData)

    context = {}
    context['data'] = res_list

    return render(request, 'conference/activeCall.html', context)


# 진행중인 회의 관리
def template(request):
    with connections['default'].cursor() as cur:
        query = '''
            SELECT seq, title
              FROM cms_template
             WHERE delete_yn = 'N';
        '''
        cur.execute(query)
        data_tup = cur.fetchall()

    data_list = list()
    for data in data_tup:
        data_dict = dict()
        data_dict['seq'] = data[0]
        data_dict['conference_name'] = data[1]
        data_list.append(data_dict)

    context = {'data': data_list}

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

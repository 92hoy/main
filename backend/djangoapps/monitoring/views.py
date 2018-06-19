#-*- coding: utf-8 -*-
from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_protect
from django.db import connections

from backend.djangoapps.common.api.views import api_mornitoringStatus

# 호출 상태
def callStatus(request):

    #resDataJson = api_coSpaces()

    context = {}
    #context['resDataJson'] = resDataJson

    return render(request, 'monitoring/callStatus.html', context)

# 네트워크 상태
def networkStatus(request):

    resDataJson = api_mornitoringStatus()

    if request.is_ajax():
        context = {}
        context['audioBitRateOutgoing'] = resDataJson['status']['audioBitRateOutgoing']
        context['audioBitRateIncoming'] = resDataJson['status']['audioBitRateIncoming']
        context['videoBitRateOutgoing'] = resDataJson['status']['videoBitRateOutgoing']
        context['videoBitRateIncoming'] = resDataJson['status']['videoBitRateIncoming']
        return JsonResponse(context)

    context = {}

    return render(request, 'monitoring/networkStatus.html', context)

# 시스템 상태
def systemStatus(request):

    resDataJson = api_mornitoringStatus()

    print(resDataJson['status']['hostId'])
    print(resDataJson['status']['softwareVersion'])
    print(resDataJson['status']['uptimeSeconds'])
    print(resDataJson['status']['cdrTime'])
    print(resDataJson['status']['activated'])
    print(resDataJson['status']['clusterEnabled'])
    print(resDataJson['status']['cdrCorrelatorIndex'])
    print(resDataJson['status']['callLegsActive'])
    print(resDataJson['status']['callLegsMaxActive'])
    print(resDataJson['status']['callLegsCompleted'])
    print(resDataJson['status']['audioBitRateOutgoing'])
    print(resDataJson['status']['audioBitRateIncoming'])
    print(resDataJson['status']['videoBitRateOutgoing'])
    print(resDataJson['status']['videoBitRateIncoming'])

    context = {}
    context['hostId'] = resDataJson['status']['hostId']
    context['softwareVersion'] = resDataJson['status']['softwareVersion']
    context['uptimeSeconds'] = resDataJson['status']['uptimeSeconds']
    context['cdrTime'] = resDataJson['status']['cdrTime']
    context['activated'] = resDataJson['status']['activated']
    context['clusterEnabled'] = resDataJson['status']['clusterEnabled']
    context['cdrCorrelatorIndex'] = resDataJson['status']['cdrCorrelatorIndex']
    context['callLegsActive'] = resDataJson['status']['callLegsActive']
    context['callLegsMaxActive'] = resDataJson['status']['callLegsMaxActive']
    context['callLegsCompleted'] = resDataJson['status']['callLegsCompleted']
    context['audioBitRateOutgoing'] = resDataJson['status']['audioBitRateOutgoing']
    context['audioBitRateIncoming'] = resDataJson['status']['audioBitRateIncoming']
    context['videoBitRateOutgoing'] = resDataJson['status']['videoBitRateOutgoing']
    context['videoBitRateIncoming'] = resDataJson['status']['videoBitRateIncoming']

    return render(request, 'monitoring/systemStatus.html', context)

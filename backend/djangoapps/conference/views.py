#-*- coding: utf-8 -*-
from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_protect, csrf_exempt
from django.db import connections
from backend.models import CmsTemplate

import json

from backend.djangoapps.common.api.views import api_coSpaces
from backend.djangoapps.common.api.views import api_coSpaceId
from backend.djangoapps.common.api.views import api_coSpaces_POST
from backend.djangoapps.common.api.views import api_coSpaceDel
from backend.djangoapps.common.api.views import api_activeCall
from backend.djangoapps.common.api.views import api_activeCallId
from backend.djangoapps.common.api.views import api_activeCallLegs
from backend.djangoapps.common.api.views import api_callLegProfiles_POST
from backend.djangoapps.common.api.views import api_callLegProfiles_Id
from backend.djangoapps.common.api.views import api_callLegProfiles_Update
from backend.djangoapps.common.api.views import api_callLegProfiles_Delete
from backend.djangoapps.common.api.views import api_callProfiles_POST
from backend.djangoapps.common.api.views import api_callProfiles_Id
from backend.djangoapps.common.api.views import api_callProfiles_Update
from backend.djangoapps.common.api.views import api_callProfiles_Delete


# 컨퍼런스 목록
def conferenceRoom(request):

    context = dict()
    context['data'] = api_coSpaces()
    template_data = CmsTemplate.objects.values_list('seq', 'title').filter(delete_yn='N')
    template_list = list()
    for seq, title in template_data:
        template_list.append({'seq': seq, 'title': title})
    context['template'] = template_list
    return render(request, 'conference/conferenceRoom.html', context)

def activecall_monitoring(request):


    return render(request,'conference/activecall_monitoring.html')

# 컨퍼런스 추가
@csrf_exempt
def conferenceRoomAdd(request):

    print(request.POST.get('name'))
    res = api_coSpaces_POST(request)
    # if res.status_code == 200:
        # data_insert = CmsCospace(cospace_id=)
    header = res.headers['Location']
    location = header.split('/')[-1]

    return JsonResponse({'code': res.status_code})


# 컨퍼런스 상세
def conferenceRoomDetail(request):
    coSpaceId = request.POST.get('coSpaceId')
    print("coSpaceId--- id----->",coSpaceId)

    resDataJson = api_coSpaceId(coSpaceId)
    print("api_coSpaceId(coSpaceId) --->resDataJson===",resDataJson)

    resDataJson['coSpace']['id'] = resDataJson['coSpace'].pop('@id')

    return JsonResponse({'data': resDataJson})


# 컨퍼런스 업데이트
@csrf_exempt
def conferenceRoomUpdate(request):
    coSpaceId = request.POST.get('@id')
    res = api_coSpaceId(coSpaceId, request)
    print('conferenceRoomUpdate s ------------------------->')
    print(res.status_code)
    print('conferenceRoomUpdate e ------------------------->')

    return JsonResponse({'code': res.status_code})


# 컨퍼런스 삭제
def conferenceRoomDel(request):
    res = api_coSpaceDel(request)

    status = 'success'
    if res:
        print('<<<<<======================== conferenceRoomDel error ')
        print(res)
        print('conferenceRoomDel error ========================>>>>>>')
        status = 'fail'

    return JsonResponse({'status': status})


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
    template_data = CmsTemplate.objects.values_list('seq', 'title').filter(delete_yn='N')
    template_list = list()
    for seq, title in template_data:
        template_list.append({'seq': seq, 'title': title})

    context = {'data': template_list}

    return render(request, 'conference/template.html', context)


# 템플릿 추가
def templateAdd(request):
    user_id = request.session['user_id']
    req_data = request.POST.get('data')
    req_json = json.loads(req_data)

    print('templateAdd DEBUG s -----------------------------------')
    print(req_json)
    print('templateAdd DEBUG e -----------------------------------')

    r1 = api_callLegProfiles_POST(req_json['callLegProfiles'])
    r2 = api_callProfiles_POST(req_json['callProfiles'])
    template_name = req_json['template_name']

    r1_header = r1.headers['Location']
    callLegProfiles_id = r1_header.split('/')[-1]
    r2_header = r2.headers['Location']
    callProfiles_id = r2_header.split('/')[-1]

    if r1.status_code == 200 and r2.status_code == 200:
        template_insert = CmsTemplate.objects.create(title=template_name, calllegprofile=callLegProfiles_id, callprofile=callProfiles_id, delete_yn='N', regist_id=user_id)
        print('templateAdd success s ====================')
        print('callLegProfiles_id : ', callLegProfiles_id)
        print('callProfiles_id : ', callProfiles_id)
        print('templateAdd success e ====================')

        return JsonResponse({'status': 'success'})
    else:
        return JsonResponse({'status': 'fail'})


# 템플릿 상세
def templateDetail(request):
    template_seq = request.POST.get('template_seq')
    template_db = CmsTemplate.objects.get(seq=template_seq)

    resDataJson_callLegProfile = api_callLegProfiles_Id(template_db.calllegprofile)
    resDataJson_callLegProfile['callLegProfile']['id'] = resDataJson_callLegProfile['callLegProfile'].pop('@id')
    resDataJson_callProfiles = api_callProfiles_Id(template_db.callprofile)
    resDataJson_callProfiles['callProfile']['id'] = resDataJson_callProfiles['callProfile'].pop('@id')

    print('templateDetail s ------------------------->')
    print('resDataJson_callLegProfile = ', resDataJson_callLegProfile)
    print('resDataJson_callProfiles = ', resDataJson_callProfiles)
    print('templateDetail e ------------------------->')

    return JsonResponse({'template_name': template_db.title, 'template_seq': template_db.seq,
                         'callLegProfile_data': resDataJson_callLegProfile['callLegProfile'],
                         'callProfile_data': resDataJson_callProfiles['callProfile']})


# 템플릿 업데이트
def templateUpdate(request):
    user_id = request.session['user_id']
    req_data = request.POST.get('data')
    req_json = json.loads(req_data)

    print('templateAdd DEBUG s -----------------------------------')
    print(req_json)
    print('templateAdd DEBUG e -----------------------------------')

    template_model = CmsTemplate.objects.get(seq=req_json['template_seq'])

    r1 = api_callLegProfiles_Update(template_model.calllegprofile, req_json['callLegProfiles'])
    r2 = api_callProfiles_Update(template_model.callprofile, req_json['callProfiles'])

    if r1.status_code == 200 and r2.status_code == 200:
        template_model.title = req_json['template_name']
        template_model.modify_id = user_id

        template_model.save()
        print('templateUpdate success s ====================')
        print('r1.status_code : ', r1.status_code)
        print('r2.status_code : ', r2.status_code)
        print('templateUpdate success e ====================')

        return JsonResponse({'status': 'success'})
    else:
        return JsonResponse({'status': 'fail'})


# 템플릿 삭제
def templateDel(request):
    user_id = request.session['user_id']
    template_arr = request.POST.getlist('del_arr[]')
    err_list = list()
    for seq in template_arr:
        template_model = CmsTemplate.objects.get(seq=seq)
        r1 = api_callLegProfiles_Delete(template_model.calllegprofile)
        r2 = api_callProfiles_Delete(template_model.callprofile)

        if r1.status_code == 200 and r2.status_code == 200:
            template_model.delete_yn = 'Y'
            template_model.modify_id = user_id
            template_model.save()
        else:
            err_list.append(template_model.title)

        print('templateDel success s ====================')
        print('template_seq : ', seq)
        print('r1.status_code : ', r1.status_code)
        print('r2.status_code : ', r2.status_code)
        print('template_model : ', template_model)
        print('templateDel success e ====================')

    return JsonResponse({'err_list': err_list})


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

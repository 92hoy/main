#-*- coding: utf-8 -*-
from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_protect, csrf_exempt
from django.db import connections
from backend.models import CmsTemplate
import datetime

import json

from backend.djangoapps.common.api.views import api_coSpaces
from backend.djangoapps.common.api.views import api_coSpaceId
from backend.djangoapps.common.api.views import api_coSpaces_POST
from backend.djangoapps.common.api.views import api_coSpaceDel
from backend.djangoapps.common.api.views import api_activeCall
from backend.djangoapps.common.api.views import api_activeCallId
from backend.djangoapps.common.api.views import api_activeCallLegs
from backend.djangoapps.common.api.views import api_callLegs
from backend.djangoapps.common.api.views import api_callLegs_update
from backend.djangoapps.common.api.views import api_callLegs_delete
from backend.djangoapps.common.api.views import api_callLegProfiles_POST
from backend.djangoapps.common.api.views import api_callLegProfiles_Id
from backend.djangoapps.common.api.views import api_callLegProfiles_Update
from backend.djangoapps.common.api.views import api_callLegProfiles_Delete
from backend.djangoapps.common.api.views import api_callProfiles_POST
from backend.djangoapps.common.api.views import api_callProfiles_Id
from backend.djangoapps.common.api.views import api_callProfiles_Update
from backend.djangoapps.common.api.views import api_callProfiles_Delete
from backend.djangoapps.common.api.views import api_users
from backend.djangoapps.common.api.views import api_usersId


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


# 컨퍼런스 추가
@csrf_exempt
def conferenceRoomAdd(request):

    print(request.POST.get('name'))
    res = api_coSpaces_POST(request)
    if res.status_code == 200:
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
        coSpaceId = api_activeCallId(data['@id'])['call']['coSpace']
        data_coSpaceId = api_coSpaceId(coSpaceId)
        data_activeCallLegs = api_activeCallLegs(data['@id'])

        reData['id'] = data['@id']
        reData['name'] = data['name']
        reData['callId'] = data_coSpaceId['coSpace']['callId']
        reData['coSpaceId'] = data_coSpaceId['coSpace']['@id']
        reData['cv'] = len(data_activeCallLegs)
        res_list.append(reData)

    context = {}

    with connections['default'].cursor() as cur:
        query = '''
            SELECT ep_id,
                   ep_name,
                   ep_type,
                   ip,
                   sip,
                   hdevice,
                   mslync,
                   username,
                   recodingdevice,
                   audioonly,
                   gmt_time,
                   ifnull(ep_group_name, '') as ep_group_name,
                   a.order_no as order_no
              FROM cms_endpoint a
                   JOIN cms_endpoint_group b ON a.ep_group_seq = b.ep_group_seq;
        '''
        cur.execute(query)
        ep_data = cur.fetchall()

    data_list = list()
    for data2 in ep_data:
        data_dict = dict()
        data_dict['ep_id'] = data2[0]
        data_dict['ep_name'] = data2[1]
        data_dict['ep_type'] = data2[2]
        data_dict['ip'] = data2[3]
        data_dict['sip'] = data2[4]
        data_dict['hdevice'] = data2[5]
        data_dict['mslync'] = data2[6]
        data_dict['username'] = data2[7]
        data_dict['recodingdevice'] = data2[8]
        data_dict['audioonly'] = data2[9]
        data_dict['gmt_time'] = data2[10]
        data_dict['ep_group_name'] = data2[11]
        data_dict['order_no'] = data2[12]
        data_list.append(data_dict)

    resDataJson2 = api_users()
    acano_list = list()

    for data3 in resDataJson2:
        reData = dict()
        res_user = api_usersId(data3['@id'])

        reData['userJid'] = res_user['user']['userJid']
        reData['name'] = res_user['user']['name']
        reData['email'] = res_user['user']['email']
        reData['tenant'] = res_user['user']['tenant'] if 'tenant' in res_user['user'] else ''
        acano_list.append(reData)

    context = {'data' : res_list ,'data2': data_list,'data3': acano_list}

    return render(request, 'conference/activeCall.html', context)


# active call 모니터링 정보
def activecall_monitoring(request, call_id):
    call_data = api_activeCallId(call_id)
    coSpace_data = api_coSpaceId(call_data['call']['coSpace'])
    callLegs_data = api_activeCallLegs(call_id)

    time_now = datetime.datetime.now()

    call_data['call']['locked'] = 'Yes' if call_data['call']['locked'] == 'true' else 'No'
    call_data['call']['recording'] = 'Yes' if call_data['call']['recording'] == 'true' else 'No'

    callLegs_list = list()
    for data in callLegs_data:
        callLeg = api_callLegs(data['@id'])
        call_sec = callLeg['callLeg']['status']['durationSeconds']
        dur_time = datetime.timedelta(seconds=int(call_sec))
        join_time = time_now - dur_time

        callLeg['callLeg']['status']['durationSeconds'] = join_time.strftime('%H:%M')
        conf_key_list = ['rxAudioMute', 'txVideoMute', 'rxVideoMute', 'txAudioMute', 'presentationContributionAllowed', 'presentationViewingAllowed']

        for key_data in conf_key_list:
            if key_data not in callLeg['callLeg']['configuration'].keys():
                callLeg['callLeg']['configuration'][key_data] = 'true'

        callLegs_list.append(callLeg)

    sec = call_data['call']['durationSeconds']
    conference_time = datetime.timedelta(seconds=int(sec))

    context = {'calls': call_data, 'coSpace': coSpace_data, 'callLegs_list': callLegs_list, 'duration_time': conference_time}

    print('activecall_monitoring debug start --------------------------')
    print('call_id : ', call_id)
    print('call_data : ', call_data)
    print('coSpace_data : ', coSpace_data)
    print('callLegs_list : ', callLegs_list)
    print('activecall_monitoring debug end --------------------------')

    return render(request, 'conference/activecall_monitoring.html', context)


# active call monitoring update
def activecall_monitoring_userUpdate(request):
    error_data = api_callLegs_update(request)
    status = 'success' if len(error_data) == 0 else 'fail'

    print('activecall_monitoring_userUpdate debug start --------------------------')
    print('error_date : ', error_data)
    print('status : ', status)
    print('activecall_monitoring_userUpdate debug end --------------------------')

    return JsonResponse({'status': status})


def activecall_monitoring_userUpdateAll(request):
    call_id = request.POST.get('call_id')
    callLeg_data = api_activeCallLegs(call_id)

    error_list = list()
    for data in callLeg_data:
        api_status = api_callLegs_update(request, data['@id'])
        if len(api_status) != 0:
            error_list.append(api_status)

    status = 'success' if len(error_list) == 0 else 'fail'

    return JsonResponse({'status': status})


# active call disconnect
def activecall_monitoring_userDel(request):
    user_uid = request.POST.get('user_uid')
    del_status = api_callLegs_delete(user_uid)
    status = 'success' if len(del_status) == 0 else 'fail'

    print('activecall_monitoring_userDel debug start --------------------------')
    print('error_date : ', del_status)
    print('status : ', status)
    print('activecall_monitoring_userDel debug end --------------------------')

    return JsonResponse({'status': status})


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
    with connections['default'].cursor() as cur:
        query = '''
            SELECT ep_id,
                   ep_name,
                   ep_type,
                   ip,
                   sip,
                   hdevice,
                   mslync,
                   username,
                   recodingdevice,
                   audioonly,
                   gmt_time,
                   ifnull(ep_group_name, '') as ep_group_name,
                   a.order_no as order_no
              FROM cms_endpoint a
                   JOIN cms_endpoint_group b ON a.ep_group_seq = b.ep_group_seq;
        '''
        cur.execute(query)
        ep_data = cur.fetchall()

    data_list = list()
    for data2 in ep_data:
        data_dict = dict()
        data_dict['ep_id'] = data2[0]
        data_dict['ep_name'] = data2[1]
        data_dict['ep_type'] = data2[2]
        data_dict['ip'] = data2[3]
        data_dict['sip'] = data2[4]
        data_dict['hdevice'] = data2[5]
        data_dict['mslync'] = data2[6]
        data_dict['username'] = data2[7]
        data_dict['recodingdevice'] = data2[8]
        data_dict['audioonly'] = data2[9]
        data_dict['gmt_time'] = data2[10]
        data_dict['ep_group_name'] = data2[11]
        data_dict['order_no'] = data2[12]
        data_list.append(data_dict)

    resDataJson2 = api_users()
    acano_list = list()

    for data3 in resDataJson2:
        reData = dict()
        res_user = api_usersId(data3['@id'])

        reData['userJid'] = res_user['user']['userJid']
        reData['name'] = res_user['user']['name']
        reData['email'] = res_user['user']['email']
        reData['tenant'] = res_user['user']['tenant'] if 'tenant' in res_user['user'] else ''
        acano_list.append(reData)


    context = {'data2': data_list,'data3': acano_list}
    #context['resDataJson'] = resDataJson

    return render(request, 'conference/reserveConference.html', context)

def reserveConference_add(request):

    if request.is_ajax():
        start_date= request.POST.get('start_date')
        end_date= request.POST.get('end_date')
        conferencename= request.POST.get('conferencename')
        callid= request.POST.get('callid')
        bandwidth= request.POST.get('bandwidth')
        userpassword= request.POST.get('userpassword')

        #---------reserve insert-----------

        with connections['default'].cursor() as cur:
            query = '''
                INSERT INTO kotech_cisco_cms.cms_resv_cospace
                                  (start_date,
                                  end_date,
                                  resv_name,
                                  passcode,
                                  call_id,
                                  bandwidth
                                  )
                      VALUES ('{start_date}',
                              '{end_date}',
                              '{resv_name}',
                              '{passcode}',
                              '{call_id}',
                              '{bandwidth}'
                              )

            '''.format(start_date=start_date, end_date=end_date, resv_name=conferencename, call_id=callid, bandwidth=bandwidth, passcode=userpassword)
            cur.execute(query)

        #--------- seq 추출-----------

        with connections['default'].cursor() as cur:
            query = '''
                select max(resv_seq)
                from cms_resv_cospace
            '''
            cur.execute(query)
            seq = cur.fetchall()
            pk_seq = seq[0][0]
            print("seq=", seq, "pk_seq=", pk_seq)

        #---------endpoint insert-----------

        endpoint_id = request.POST.getlist('endpoint_id[]')
        print("endpoint_id==",endpoint_id)

        for data in endpoint_id:
            with connections['default'].cursor() as cur:
                query = '''
                     insert into kotech_cisco_cms.cms_resv_cospace_endpoint
                                  (resv_seq,
                                   ep_id)
                     VALUES ('{pk_seq}',
                              '{ep_id}')
                 '''.format(ep_id=data, pk_seq=pk_seq)
                cur.execute(query)


    return JsonResponse({'return':'success'})


# 컨퍼런스 제공 (달력)
def reserveConferenceCal(request):

    #resDataJson = api_activeCall()

    context = {}
    #context['resDataJson'] = resDataJson

    return render(request, 'conference/reserveConferenceCal.html', context)

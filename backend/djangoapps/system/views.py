#-*- coding: utf-8 -*-
from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_protect
from django.views.decorators.csrf import csrf_exempt
from django.db import connections

from backend.djangoapps.common.core.views import coreJson
from backend.djangoapps.common.api.views import api_users
from backend.djangoapps.common.api.views import api_usersId
from backend.djangoapps.common.api.views import api_cdrReceivers
from backend.djangoapps.common.api.views import api_cdr_POST
from backend.djangoapps.common.api.views import api_cdr_id
from backend.djangoapps.common.api.views import api_cdr_del


# 호출 상태
def cdr(request):

    resDataJson = api_cdrReceivers()
    return_data = list()
    if resDataJson['cdrReceivers']['@total'] != '1':
        return_data = resDataJson['cdrReceivers']['cdrReceiver']
    else:
        return_data.append(resDataJson['cdrReceivers']['cdrReceiver'])

    context = {'data': return_data}

    return render(request, 'system/cdr.html', context)

@csrf_exempt
def cdr_add(request):

    print(request.POST.get('@id'))
    print(request.POST.get('uri'))

    res = api_cdr_POST(request)

    return JsonResponse({'code': res.status_code})

def cdr_del(request):

    res = api_cdr_del(request)
    print("res", res)
    status = 'success'
    print("success")
    if res:
        print('<<<<<======================== api_cdr_del error ')
        print(res)
        print('api_cdr_del error ========================>>>>>>')
        status = 'fail'

    return JsonResponse({'status': status})


def cdr_detail(request):

    cdr_id = request.POST.get('uri')
    print("uri uri-uri-uri-uri-->",cdr_id)

    resDataJson = api_cdr_id(cdr_id)
    print("resDataJson--cdr_id>", resDataJson)

    resDataJson['cdrReceiver']['id'] = resDataJson['cdrReceiver'].pop('@id')

    return JsonResponse({'data': resDataJson})

# 네트워크 상태
def ldap(request):

    #resDataJson = api_coSpaces()

    context = {}
    #context['resDataJson'] = resDataJson

    return render(request, 'system/ldap.html', context)


# 시스템 상태
@csrf_exempt
def account(request):
    #-=-=-=-=-=-=-=-Account 생성-=-=-=-=-=-=-=-=-=-=-
    if request.is_ajax():
        user_id = request.POST.get('user_id')
        user_pw = request.POST.get('user_pw')
        user_name = request.POST.get('user_name')
        role = request.POST.get('role')
        print ("account id->", user_id)
        print ("account pw->", user_pw)
        print ("account name->", user_name)
        print ("account role->", role)

        lock = 0

        with connections['default'].cursor() as cur:
            query = '''
                select user_id
                FROM cms_manager
                WHERE user_id ='{user_id}'
            '''.format(user_id=user_id)
            cur.execute(query)
            rows = cur.fetchall()

        print (query)
        print ("rows ->",rows)
        print("before len rows =>",len(rows))

        #-------검증--------------------------

        if len(rows) != 0:
            print("if rows =>",len(rows))
            print("before",lock)
            lock = 1
            print("after",lock)

            return JsonResponse({"return": "fail"})
        #-------검증--------------------------


        with connections['default'].cursor() as cur:
            query = '''
                  INSERT INTO kotech_cisco_cms.cms_manager
                              (user_id,
                              user_name,
                              user_pwd,
                              user_role)
                  VALUES ('{user_id}','{user_name}','{user_pwd}','{user_role}')
            '''.format(user_id=user_id,user_name=user_name,user_pwd=user_id,user_role=role)
            cur.execute(query)

        return JsonResponse({"return": "success"})
    #-=-=-=-=-=-=-=-Account 생성-=-=-=-=-=-=-=-=-=-=-

    with connections['default'].cursor() as cur:
        query = '''
            SELECT user_id, user_pwd, user_name, code_name
              FROM cms_manager a JOIN cms_code_detail b ON a.user_role = b.detail_code
             WHERE a.delete_yn = 'N' AND b.delete_yn = 'N';
        '''
        cur.execute(query)
        user_data = cur.fetchall()

    data_list = list()
    # dict 변환
    for data in user_data:
        data_dict = dict()
        data_dict['user_id'] = data[0]
        data_dict['user_pwd'] = data[1]
        data_dict['user_name'] = data[2]
        data_dict['code_name'] = data[3]
        data_list.append(data_dict)
    context = {'data': data_list}

    return render(request, 'system/account.html', context)

def account_del(request):

    id = request.POST.getlist('del_arr[]')
    print(id)
    for data in id:
        with connections['default'].cursor() as cur:
            query = '''
                 delete FROM cms_manager
                 WHERE user_id ='{user_id}'
             '''.format(user_id=data)
            print(query)
            cur.execute(query)
            print(query)

    return JsonResponse({"return" : "success"})

def account_detail(request):
    if request.is_ajax():
        user_id = request.POST.get('user_id')

        with connections['default'].cursor() as cur:
            query = '''
                SELECT user_id,
                       user_name,
                       user_pwd,
                       user_role
                  FROM cms_manager
                  where user_id = '{user_id}';
            '''.format(user_id=user_id)
            cur.execute(query)

            print(query)
            rows = cur.fetchall()

        data_dict2 = dict()
        data_dict2['user_id'] = rows[0][0]
        data_dict2['user_name'] = rows[0][1]
        data_dict2['user_pwd'] = rows[0][2]
        data_dict2['user_role'] = rows[0][2]

        print(rows)

    return JsonResponse({"rows":data_dict2})

def account_update(request):
    if request.is_ajax():
        user_id = request.POST.get('user_id')
        user_pw = request.POST.get('user_pw')
        user_name = request.POST.get('user_name')
        user_role = request.POST.get('user_role')

        print ("user_id-->",user_id)
        print ("user_name-->",user_name)
        print ("role-->",user_role)


        with connections['default'].cursor() as cur:
            query = '''
                  update cms_manager
                  set user_name = '{user_name}',
                      user_role='{user_role}'
                  where user_id ='{user_id}'
            '''.format(user_id=user_id,user_name=user_name, user_role=user_role)
            print(query)
            cur.execute(query)

    return JsonResponse({"return":"success"})


# 시스템 상태
@csrf_exempt
def endPoint(request):

    if request.is_ajax():
        name= request.POST.get('name')
        device_type= request.POST.get('device_type')
        ip= request.POST.get('ip')
        sip= request.POST.get('sip')
        h_323= request.POST.get('h_323')
        mslync= request.POST.get('mslync')
        user_name= request.POST.get('user_name')
        recording_device= request.POST.get('recording_device')
        group_name= request.POST.get('group_name')
        sortno= request.POST.get('sortno')
        print ("ip-->",ip)
        print ("sip-->",sip)
        print ("device_type-->",device_type)
        print ("group_name-->",group_name)
        print ("sortno-->",sortno)

        lock = 0

        with connections['default'].cursor() as cur:
            query = '''
                select ep_id
                FROM cms_endpoint
                WHERE ep_id ='{ep_id}'
            '''.format(ep_id=name)
            cur.execute(query)
            rows = cur.fetchall()

            print (query)
            print ("rows ->",rows)
            print ("before len rows =>",len(rows))

            if len(rows) != 0:
                print("if rows =>",len(rows))
                print("before",lock)
                lock = 1
                print("after",lock)

                return JsonResponse({"return": "fail"})
        print(" not fail")



        with connections['default'].cursor() as cur:
            query = '''
                  INSERT INTO kotech_cisco_cms.cms_endpoint
                              (ep_id,
                              ep_type,
                              ip,
                              sip,
                              hdevice,
                              mslync,
                              username,
                              recodingdevice,
                              ep_group_seq,
                              order_no
                              )
                  VALUES ('{ep_id}',
                          '{ep_type}',
                          '{ip}',
                          '{sip}',
                          '{hdevice}',
                          '{mslync}',
                          '{username}',
                          '{recodingdevice}',
                          '{ep_group_seq}',
                          '{order_no}')
            '''.format(ep_id=name, ep_type=device_type, ip=ip, sip=sip, hdevice=h_323, mslync=mslync,
                       username=user_name, recodingdevice=recording_device, ep_group_seq=group_name, order_no=sortno)
            cur.execute(query)

        return JsonResponse({"return": "success"})


    with connections['default'].cursor() as cur:
        query = '''
            SELECT ep_group_name,ep_group_seq
              FROM cms_endpoint_group;
        '''
        cur.execute(query)
        ep_data2 = cur.fetchall()

        data_list2 = list()
        for data2 in ep_data2:
            data_dict2=dict()
            data_dict2['ep_group_name'] = data2[0]
            data_dict2['ep_group_seq'] = data2[1]
            data_list2.append(data_dict2)

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
    for data in ep_data:
        data_dict = dict()
        data_dict['ep_id'] = data[0]
        data_dict['ep_name'] = data[1]
        data_dict['ep_type'] = data[2]
        data_dict['ip'] = data[3]
        data_dict['sip'] = data[4]
        data_dict['hdevice'] = data[5]
        data_dict['mslync'] = data[6]
        data_dict['username'] = data[7]
        data_dict['recodingdevice'] = data[8]
        data_dict['audioonly'] = data[9]
        data_dict['gmt_time'] = data[10]
        data_dict['ep_group_name'] = data[11]
        data_dict['order_no'] = data[12]
        data_list.append(data_dict)

    context = {'data': data_list, 'data2': data_list2}

    return render(request, 'system/endPoint.html', context)

#endPoint 삭제
@csrf_exempt
def endPoint_del(request):

    name = request.POST.getlist('del_arr[]')
    print("name",name)
    for data in name:
        with connections['default'].cursor() as cur:
            query = '''
                 delete FROM cms_endpoint
                 WHERE ep_id ='{ep_id}'
             '''.format(ep_id=data)
            cur.execute(query)

    return JsonResponse({"return": "success"})

def endPoint_detail(request):

    if request.is_ajax():
        ep_id= request.POST.get('ep_id')

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
                       a.ep_group_seq as ep_group_seq,
                       a.order_no as order_no
                  FROM cms_endpoint a
                       JOIN cms_endpoint_group b ON a.ep_group_seq = b.ep_group_seq
                  where ep_id = '{ep_id}';
            '''.format(ep_id=ep_id)
            cur.execute(query)
            print(query)
            rows = cur.fetchall()

        data_dict4 = dict()
        data_dict4['ep_id'] = rows[0][0]
        data_dict4['ep_name'] = rows[0][1]
        data_dict4['ep_type'] = rows[0][2]
        data_dict4['ip'] = rows[0][3]
        data_dict4['sip'] = rows[0][4]
        data_dict4['hdevice'] = rows[0][5]
        data_dict4['mslync'] = rows[0][6]
        data_dict4['username'] = rows[0][7]
        data_dict4['recodingdevice'] = rows[0][8]
        data_dict4['audioonly'] = rows[0][9]
        data_dict4['gmt_time'] = rows[0][10]
        data_dict4['ep_group_name'] = rows[0][11]
        data_dict4['ep_group_seq'] = rows[0][12]
        data_dict4['order_no'] = rows[0][12]

        #print(rows)

    return JsonResponse({"rows":data_dict4})
@csrf_exempt
def endPoint_update(request):
    if request.is_ajax():
        name= request.POST.get('detail_ep_id')
        device_type= request.POST.get('device_type')
        ip= request.POST.get('ip')
        sip= request.POST.get('sip')
        h_323= request.POST.get('h_323')
        mslync= request.POST.get('mslync')
        user_name= request.POST.get('user_name')
        recording_device= request.POST.get('recording_device')
        group_name= request.POST.get('group_name')
        sortno= request.POST.get('sortno')
        print ("ip-->",ip)
        print ("sip-->",sip)
        print ("device_type-->",device_type)
        print ("group_name-->",group_name)
        print ("sortno-->",sortno)

        with connections['default'].cursor() as cur:
            query = '''
                  update cms_endpoint
                  set ep_type = '{ep_type}',
                      ip='{ip}',
                      sip='{sip}',
                      hdevice='{hdevice}',
                      mslync='{mslync}',
                      username='{username}',
                      recodingdevice='{recodingdevice}',
                      ep_group_seq='{ep_group_seq}',
                      order_no='{order_no}'
                  where ep_id ='{ep_id}'
            '''.format(ep_id=name, ep_type=device_type, ip=ip, sip=sip, hdevice=h_323, mslync=mslync,
                       username=user_name, recodingdevice=recording_device, ep_group_seq=group_name, order_no=sortno)
            print(query)
            cur.execute(query)



    return JsonResponse({"return":"success"})

# 시스템 상태
def endPointGroup(request):
    with connections['default'].cursor() as cur:
        query = '''
          SELECT ep_group_seq, ep_group_name, order_no FROM cms_endpoint_group;
        '''
        cur.execute(query)
        ep_group = cur.fetchall()

    data_list = list()
    for data in ep_group:
        data_dict = dict()
        data_dict['ep_group_seq'] = data[0]
        data_dict['ep_group_name'] = data[1]
        data_dict['order_no'] = data[2]
        data_list.append(data_dict)

    context = {'data': data_list}
    #context['resDataJson'] = resDataJson

    return render(request, 'system/endPointGroup.html', context)

def endPointGroup_add(request):

    if request.is_ajax():

        ep_group_name = request.POST.get('ep_group_name')
        order_no = request.POST.get('order_no')
        regist_id = request.POST.get('regist_id')

        print ("ep_group_name ->", ep_group_name)
        print ("order_no ->", order_no)
        print ("regist_id ->", regist_id)

        lock = 0

        with connections['default'].cursor() as cur:
            query = '''
                select ep_group_name
                FROM cms_endpoint_group
                WHERE ep_group_name ='{ep_group_name}'
            '''.format(ep_group_name=ep_group_name)
            cur.execute(query)
            rows = cur.fetchall()

        print (query)
        print ("rows ->",rows)
        print("before len rows =>",len(rows))

        #-------검증--------------------------

        if len(rows) != 0:
            print("if rows =>",len(rows))
            print("before",lock)
            lock = 1
            print("after",lock)

            return JsonResponse({"return": "fail"})

        #  생성
        with connections['default'].cursor() as cur:
            query = '''
                  INSERT INTO kotech_cisco_cms.cms_endpoint_group
                              (ep_group_name,
                              order_no)
                  VALUES ('{ep_group_name}','{order_no}')
            '''.format(ep_group_name=ep_group_name,order_no=order_no)
            print(query)
            cur.execute(query)

    return JsonResponse({"return": "success"})

def endPointGroup_del(request):
    print("endPointGroup_del")
    name = request.POST.getlist('del_arr[]')

    print(name)
    for data in name:
        with connections['default'].cursor() as cur:
            query = '''
                 delete FROM cms_endpoint_group
                 WHERE ep_group_name ='{ep_group_name}'
             '''.format(ep_group_name=data)
            print(query)
            cur.execute(query)

    return JsonResponse({"return" : "success"})



# 시스템 상태
def acanoClient(request):

    resDataJson = api_users()

    acano_list = list()

    for data in resDataJson:
        reData = dict()
        res_user = api_usersId(data['@id'])

        reData['userJid'] = res_user['user']['userJid']
        reData['name'] = res_user['user']['name']
        reData['email'] = res_user['user']['email']
        reData['tenant'] = res_user['user']['tenant'] if 'tenant' in res_user['user'] else ''
        acano_list.append(reData)

    context = {'data': acano_list}

    return render(request, 'system/acanoClient.html', context)


# 시스템 상태
def logoManagement(request):

    #resDataJson = api_coSpaces()

    context = {}
    #context['resDataJson'] = resDataJson

    return render(request, 'system/logoManagement.html', context)


# 시스템 상태
def commandManagement(request):

    jsonData = coreJson()
    print(jsonData['callcommand']['txVideoMute'])
    print(jsonData['callcommand']['rxVideoMute'])
    print(jsonData['callcommand']['txAudioMute'])
    print(jsonData['callcommand']['rxAudioMute'])
    print(jsonData['callcommand']['presentationContributionAllowed'])
    print(jsonData['callcommand']['presentationViewingAllowed'])
    print(jsonData['callcommand']['videoMode'])

    context = {}
    context['cc_txVideoMute'] = jsonData['callcommand']['txVideoMute']
    context['cc_rxVideoMute'] = jsonData['callcommand']['rxVideoMute']
    context['cc_txAudioMute'] = jsonData['callcommand']['txAudioMute']
    context['cc_rxAudioMute'] = jsonData['callcommand']['rxAudioMute']
    context['cc_presentationContributionAllowed'] = jsonData['callcommand']['presentationContributionAllowed']
    context['cc_presentationViewingAllowed'] = jsonData['callcommand']['presentationViewingAllowed']
    context['cc_videoMode'] = jsonData['callcommand']['videoMode']

    return render(request, 'system/commandManagement.html', context)


#-*- coding: utf-8 -*-
from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_protect
from django.db import connections


# 호출 상태
def cdr(request):

    #resDataJson = api_coSpaces()

    context = {}
    #context['resDataJson'] = resDataJson

    return render(request, 'system/cdr.html', context)


# 네트워크 상태
def ldap(request):

    #resDataJson = api_coSpaces()

    context = {}
    #context['resDataJson'] = resDataJson

    return render(request, 'system/ldap.html', context)


# 시스템 상태
def account(request):
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


# 시스템 상태
def endPoint(request):
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
                   b.order_no as order_no
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

    context = {'data': data_list}

    return render(request, 'system/endPoint.html', context)


# 시스템 상태
def endPointGroup(request):

    #resDataJson = api_coSpaces()

    context = {}
    #context['resDataJson'] = resDataJson

    return render(request, 'system/endPointGroup.html', context)


# 시스템 상태
def acanoClient(request):

    #resDataJson = api_coSpaces()

    context = {}
    #context['resDataJson'] = resDataJson

    return render(request, 'system/acanoClient.html', context)


# 시스템 상태
def logoManagement(request):

    #resDataJson = api_coSpaces()

    context = {}
    #context['resDataJson'] = resDataJson

    return render(request, 'system/logoManagement.html', context)


# 시스템 상태
def commandManagement(request):

    #resDataJson = api_coSpaces()

    context = {}
    #context['resDataJson'] = resDataJson

    return render(request, 'system/commandManagement.html', context)

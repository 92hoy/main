#-*- coding: utf-8 -*-
from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_protect
from django.db import connections

#UTIL
import json
import requests
import xmltodict

from django.conf import settings
from backend.djangoapps.common.util.views import dictfetchall
from backend.djangoapps.common.api.views import api_coSpaces

def sample(request):

    """
    making logic
    """

    """
    with connections['default'].cursor() as cur:
        query = '''
            select *
            FROM table
            where sample = '{page}'
        '''.format(page=page)
        cur.execute(query)
        rows = cur.fetchall()
    """

    context = {}
    context['sample_key'] = 'sample_val'

    print("-------------------------> DEBUG [s]")
    print(settings.TIME_ZONE)
    print("-------------------------> DEBUG [e]")

    return render(request, 'sample/sample.html', context)
    #return JsonResponse({'a':'b'})

def apiTest(request):

    resDataJson = api_coSpaces()

    context = {}
    context['resDataJson'] = resDataJson

    return render(request, 'sample/apiTest.html', context)
    #return JsonResponse({'a':'b'})

def vuejs(request):

    """
    making logic
    """

    """
    with connections['default'].cursor() as cur:
        query = '''
            select *
            FROM table
            where sample = '{page}'
        '''.format(page=page)
        cur.execute(query)
        rows = cur.fetchall()
    """

    context = {}
    context['sample_key'] = 'sample_val'

    print("-------------------------> DEBUG [s]")
    common_sample()
    print(settings.TIME_ZONE)
    print("-------------------------> DEBUG [e]")

    return render(request, 'sample/vuejs.html', context)
    #return JsonResponse({'a':'b'})

def vueService(request):

    with connections['default'].cursor() as cur:
        query = '''
            select
                id,
                email,
                DATE_FORMAT(regist_date,'%Y-%c-%e') as regist_date
            from sample_user
        '''
        cur.execute(query)
        rows = dictfetchall(cur)

        print("----------------> s")
        print(rows)
        print("----------------> e")

    context = {}
    #context['helloData'] = rows
    context['helloData'] = '18'

    return render(request, 'sample/vueService.html', context)
    #return JsonResponse({'a':'b'})

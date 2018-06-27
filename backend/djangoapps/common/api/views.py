#-*- coding: utf-8 -*-
from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_protect
from django.db import connections
from django.conf import settings

#UTIL
import json
import requests
import xmltodict

#from backend.djangoapps.common.api.views import api_coSpaces
def api_coSpaces():

    Authorization = settings.AUTHORIZATION

    # requests GET
    url = 'https://14.63.53.22:449/api/v1/coSpaces'
    headers = {
        'Authorization': Authorization
    }
    r = requests.get(url, headers=headers, verify=False)
    r.encoding = None
    resData = str(r.text)

    # xml to json
    o = xmltodict.parse(resData)
    resData = json.dumps(o)
    resDataJson = json.loads(resData)

    print("-------------------> DEBUG[s]")
    print("total = ", resDataJson['coSpaces']['@total']) #total
    print("realTotal = ", len(resDataJson['coSpaces']['coSpace'])) #total
    requestCnt = (int(resDataJson['coSpaces']['@total']) / 20) + 1
    resDataList = list()

    for n in range(0, int(requestCnt)):
        url = 'https://14.63.53.22:449/api/v1/coSpaces?offset={offset}&limit=20'.format(offset=n*20)
        res = requests.get(url, headers=headers, verify=False)
        res.encoding = None
        res_data = str(res.text)
        res_o = xmltodict.parse(res_data)
        res_data = json.dumps(res_o)
        res_data_json = json.loads(res_data)
        resDataList.append(res_data_json['coSpaces']['coSpace'])

    print(resDataList)
    totDataList = list()
    for list_data in resDataList:
        for data in list_data:
            totDataList.append(data)

    for n in range(0, len(totDataList)):
        if 'uri' not in totDataList[n]:
            totDataList[n]['uri'] = ''
        if 'secondaryUri' not in totDataList[n]:
            totDataList[n]['secondaryUri'] = ''
        if 'cdrTag' not in totDataList[n]:
            totDataList[n]['cdrTag'] = ''

    return totDataList


# from backend.djangoapps.common.api.views import api_coSpaceId
def api_coSpaceId(id):

    Authorization = settings.AUTHORIZATION

    # requests GET
    url = 'https://14.63.53.22:449/api/v1/coSpaces/' + id
    headers = {
        'Authorization': Authorization
    }
    r = requests.get(url, headers=headers, verify=False)
    r.encoding = None
    resData = str(r.text)

    # xml to json
    o = xmltodict.parse(resData)
    resData = json.dumps(o)
    resDataJson = json.loads(resData)

    print("-------------------> DEBUG[s]")
    print(resDataJson)
    print("-------------------> DEBUG[e]")

    return resDataJson

#from backend.djangoapps.common.api.views import api_activeCall
def api_activeCall():
    Authorization = settings.AUTHORIZATION

    # requests GET
    url = 'https://14.63.53.22:449/api/v1/calls'
    headers = {
        'Authorization': Authorization
    }

    r = requests.get(url, headers=headers, verify=False)
    r.encoding = None
    resData = str(r.text)

    # xml to json
    o = xmltodict.parse(resData)
    resData = json.dumps(o)
    resDataJson = json.loads(resData)

    print("-------------------> DEBUG[s]")
    print(resDataJson)
    print("-------------------> DEBUG[e]")

    requestCnt = (int(resDataJson['calls']['@total']) / 20) + 1
    resDataList = list()

    for n in range(0, int(requestCnt)):
        url = 'https://14.63.53.22:449/api/v1/calls?offset={offset}&limit=20'.format(offset=n*20)
        res = requests.get(url, headers=headers, verify=False)
        res.encoding = None
        res_data = str(res.text)
        res_o = xmltodict.parse(res_data)
        res_data = json.dumps(res_o)
        res_data_json = json.loads(res_data)
        resDataList.append(res_data_json['calls']['call'])

    totDataList = list()
    for list_data in resDataList:
        for data in list_data:
            totDataList.append(data)

    return totDataList


#from backend.djangoapps.common.api.views import api_activeCallId
def api_activeCallId(id):
    Authorization = settings.AUTHORIZATION

    # requests GET
    headers = {
        'Authorization': Authorization
    }
    url = 'https://14.63.53.22:449/api/v1/calls/' + id

    r = requests.get(url, headers=headers, verify=False)
    r.encoding = None
    resData = str(r.text)

    # xml to json
    o = xmltodict.parse(resData)
    resData = json.dumps(o)
    resDataJson = json.loads(resData)

    if id is not None:
        return resDataJson['call']['coSpace']
    print("-------------------> DEBUG[s]")
    print(resDataJson)
    print("-------------------> DEBUG[e]")

    return resDataJson['calls']['call']


#from backend.djangoapps.common.api.views import api_activeCallLegs
def api_activeCallLegs(id):
    Authorization = settings.AUTHORIZATION

    # requests GET
    url = 'https://14.63.53.22:449/api/v1/calls/{id}/callLegs'.format(id=id)
    headers = {
        'Authorization': Authorization
    }
    r = requests.get(url, headers=headers, verify=False)
    r.encoding = None
    resData = str(r.text)

    # xml to json
    o = xmltodict.parse(resData)
    resData = json.dumps(o)
    resDataJson = json.loads(resData)

    print("-------------------> DEBUG[s]")
    print(resDataJson)
    print("-------------------> DEBUG[e]")

    return resDataJson

#from backend.djangoapps.common.api.views import api_templateLegPro
def api_templateLegPro(id):

    Authorization = settings.AUTHORIZATION

    # requests GET
    url = 'https://14.63.53.22:449/api/v1/callLegProfiles/' + id
    headers = {
        'Authorization': Authorization
    }
    r = requests.get(url, headers=headers, verify=False)
    r.encoding = None
    resData = str(r.text)

    # xml to json
    o = xmltodict.parse(resData)
    resData = json.dumps(o)
    resDataJson = json.loads(resData)

    print("-------------------> DEBUG[s]")

    print("-------------------> DEBUG[e]")

    return resDataJson

#from backend.djangoapps.common.api.views import api_templatePro
def api_templatePro(id):

    Authorization = settings.AUTHORIZATION

    # requests GET
    url = 'https://14.63.53.22:449/api/v1/callProfiles/' + id
    headers = {
        'Authorization': Authorization
    }
    r = requests.get(url, headers=headers, verify=False)
    r.encoding = None
    resData = str(r.text)

    # xml to json
    o = xmltodict.parse(resData)
    resData = json.dumps(o)
    resDataJson = json.loads(resData)

    print("-------------------> DEBUG[s]")

    print("-------------------> DEBUG[e]")

    return resDataJson

#from backend.djangoapps.common.api.views import api_mornitoringStatus
def api_mornitoringStatus():

    Authorization = settings.AUTHORIZATION

    # requests GET
    url = 'https://14.63.53.22:449/api/v1/system/status'
    headers = {
        'Authorization': Authorization
    }
    r = requests.get(url, headers=headers, verify=False)
    r.encoding = None
    resData = str(r.text)

    # xml to json
    o = xmltodict.parse(resData)
    resData = json.dumps(o)
    resDataJson = json.loads(resData)

    print("-------------------> DEBUG[s]")
    print(resDataJson)
    print("-------------------> DEBUG[e]")

    return resDataJson


#from backend.djangoapps.common.api.views import api_users
def api_users():

    Authorization = settings.AUTHORIZATION

    # requests GET
    url = 'https://14.63.53.22:449/api/v1/users'
    headers = {
        'Authorization': Authorization
    }

    r = requests.get(url, headers=headers, verify=False)
    r.encoding = None
    resData = str(r.text)

    # xml to json
    o = xmltodict.parse(resData)
    resData = json.dumps(o)
    resDataJson = json.loads(resData)

    print("-------------------> DEBUG[s]")
    print(resDataJson)
    print("-------------------> DEBUG[e]")
    requestCnt = (int(resDataJson['users']['@total']) / 20) + 1
    resDataList = list()

    for n in range(0, int(requestCnt)):
        url = 'https://14.63.53.22:449/api/v1/users?offset={offset}&limit=20'.format(offset=n*20)
        res = requests.get(url, headers=headers, verify=False)
        res.encoding = None
        res_data = str(res.text)
        res_o = xmltodict.parse(res_data)
        res_data = json.dumps(res_o)
        res_data_json = json.loads(res_data)
        resDataList.append(res_data_json['users']['user'])

    print(resDataList)
    totDataList = list()
    for list_data in resDataList:
        for data in list_data:
            totDataList.append(data)

    return totDataList


#from backend.djangoapps.common.api.views import api_usersId
def api_usersId(id):

    Authorization = settings.AUTHORIZATION

    # requests GET
    headers = {
        'Authorization': Authorization,
    }

    url = 'https://14.63.53.22:449/api/v1/users/' + id

    r = requests.get(url, headers=headers, verify=False)
    r.encoding = None
    resData = str(r.text)

    # xml to json
    o = xmltodict.parse(resData)
    resData = json.dumps(o)
    resDataJson = json.loads(resData)

    print("-------------------> DEBUG[s]")
    print(resDataJson)
    print("-------------------> DEBUG[e]")

    return resDataJson


#from backend.djangoapps.common.api.views import api_cdrReceivers
def api_cdrReceivers():
    Authorization = settings.AUTHORIZATION

    # requests GET
    url = 'https://14.63.53.22:449/api/v1/system/cdrReceivers'
    headers = {
        'Authorization': Authorization
    }

    r = requests.get(url, headers=headers, verify=False)
    r.encoding = None
    resData = str(r.text)

    # xml to json
    o = xmltodict.parse(resData)
    resData = json.dumps(o)
    resDataJson = json.loads(resData)

    print("-------------------> DEBUG[s]")
    print(resDataJson)
    print("-------------------> DEBUG[e]")

    return resDataJson
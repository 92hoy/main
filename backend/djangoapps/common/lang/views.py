#-*- coding: utf-8 -*-
from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_protect
from django.db import connections
from django.conf import settings
from django.utils import translation
from django.utils.translation import ugettext as _

def transLangEN(request):

    if translation.LANGUAGE_SESSION_KEY in request.session:
        del request.session[translation.LANGUAGE_SESSION_KEY]

    userLanguage = 'en'
    translation.activate(userLanguage)
    request.session[translation.LANGUAGE_SESSION_KEY] = userLanguage
    return JsonResponse({'return':'success'})

def transLangKO(request):

    if translation.LANGUAGE_SESSION_KEY in request.session:
        del request.session[translation.LANGUAGE_SESSION_KEY]

    userLanguage = 'ko'
    translation.activate(userLanguage)
    request.session[translation.LANGUAGE_SESSION_KEY] = userLanguage
    return JsonResponse({'return':'success'})

def transLangJP(request):

    if translation.LANGUAGE_SESSION_KEY in request.session:
        del request.session[translation.LANGUAGE_SESSION_KEY]

    userLanguage = 'ja'
    translation.activate(userLanguage)
    request.session[translation.LANGUAGE_SESSION_KEY] = userLanguage
    return JsonResponse({'return':'success'})

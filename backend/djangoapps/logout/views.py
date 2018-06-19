#-*- coding: utf-8 -*-
from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.shortcuts import redirect
from django.views.decorators.csrf import csrf_protect
from django.db import connections
from django.utils import translation

def logout(request):

    if 'user_id' in request.session:
        del request.session['user_id']
    if 'language' in request.session:
        del request.session['language']
    if 'user_role' in request.session:
        del request.session['user_role']
    if 'user_name' in request.session:
        del request.session['user_name']
    if translation.LANGUAGE_SESSION_KEY in request.session:
        del request.session[translation.LANGUAGE_SESSION_KEY]
    return redirect('/login')

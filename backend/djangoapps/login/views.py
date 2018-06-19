#-*- coding: utf-8 -*-
from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.shortcuts import redirect
from django.views.decorators.csrf import csrf_protect
from django.db import connections
from django.utils.translation import ugettext as _
from django.conf import settings
from django.utils import translation
from django.core.exceptions import ObjectDoesNotExist

from backend.models import CmsManager

def login(request):

    if request.is_ajax():

        inputId = request.POST.get('inputId')
        inputPw = request.POST.get('inputPw')

        if inputId =='' and inputPw == '' :
            return JsonResponse({'result':'error0'})

        print("----------------------> s")
        print("inputId = ", inputId)
        print("inputPw = ", inputPw)
        print("----------------------> e")

        try:
            userObject = CmsManager.objects.get(user_id=inputId)
            if userObject.user_pwd == inputPw:
                request.session['user_id'] = userObject.user_id
                request.session['user_name'] = userObject.user_name
                request.session['language'] = userObject.language
                request.session['user_role'] = userObject.user_role
                request.session[translation.LANGUAGE_SESSION_KEY] = userObject.language
                translation.activate(userObject.language)

                return JsonResponse({'result':'success'})
            else:
                return JsonResponse({'result':'error2'})
        except ObjectDoesNotExist:
            return JsonResponse({'result':'error1'})

    context = {}

    return render(request, 'login/login.html', context)

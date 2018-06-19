#-*- coding: utf-8 -*-
from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.shortcuts import redirect
from django.views.decorators.csrf import csrf_protect
from django.db import connections
from django.utils import translation
from backend.models import CmsManager

# 호출 상태
def main(request):

    # session validate
    if 'user_id' not in request.session:
        return redirect('/login')

    userObject = CmsManager.objects.get(user_id=request.session['user_id'])
    print(userObject.language)

    # lang validate
    translation.activate(userObject.language)

    context = {}
    #context['user_name'] = userObject.user_name
    #context['user_role'] = userObject.user_role

    return render(request, 'main/index.html', context)

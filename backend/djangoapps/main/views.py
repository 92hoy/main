#-*- coding: utf-8 -*-
from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.shortcuts import redirect
from django.views.decorators.csrf import csrf_protect
from django.db import connections
from django.utils import translation

# 호출 상태
def main(request):

    # session validate
    if 'user_id' not in request.session:
        return redirect('/login')

    # lang validate
    userLanguage = request.session[translation.LANGUAGE_SESSION_KEY]
    translation.activate(userLanguage)

    print(request.session[translation.LANGUAGE_SESSION_KEY])
    context = {}

    return render(request, 'main/index.html', context)

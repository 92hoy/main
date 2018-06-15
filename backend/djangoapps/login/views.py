#-*- coding: utf-8 -*-
from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.shortcuts import redirect
from django.views.decorators.csrf import csrf_protect
from django.db import connections
#from django.utils import translation
#from django.utils.translation import ugettext as _
from django.utils.translation import ugettext as _

def login(request):

    from django.conf import settings
    print(settings.LANGUAGE_CODE)

    print(_('helloworld'))
    print(_('good day'))

    if request.is_ajax():

        inputId = request.POST.get('inputId')
        inputPw = request.POST.get('inputPw')

        print("----------------------> s")
        print("inputId = ", inputId)
        print("inputPw = ", inputPw)
        print("----------------------> e")

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

        request.session['user_id'] = 'test'

        return JsonResponse({'result':'success'})
        return JsonResponse({'result':'fail'})

    context = {}

    return render(request, 'login/login.html', context)

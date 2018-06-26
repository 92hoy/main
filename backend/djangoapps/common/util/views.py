#-*- coding: utf-8 -*-
from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_protect
from django.views.decorators.csrf import csrf_exempt
from django.db import connections
from django.conf import settings

#UTIL
import json
import requests
import xmltodict

#from backend.djangoapps.common.util.views import dictfetchall
def dictfetchall(cursor):
    "Returns all rows from a cursor as a dict"
    desc = cursor.description
    return [
        dict(zip([col[0] for col in desc], row))
        for row in cursor.fetchall()
    ]

def get_file_ext(filename):
    filename_split = filename.split('.')
    file_ext_index = len(filename_split)
    file_ext = filename_split[file_ext_index - 1]
    return file_ext

def common_single_file_upload(file_object):

    UPLOAD_DIR = settings.FILE_UPLOAD

    file_name = str(file_object).strip()
    file_name_enc = str(uuid.uuid4()).replace('-', '')
    file_ext = get_file_ext(file_name).strip()
    file_byte_size = file_object.size
    file_size = str(file_byte_size / 1024) + "KB"
    file_dir = UPLOAD_DIR + file_name_enc + '.' + file_ext

    fp = open(file_dir, 'wb')
    for chunk in file_object.chunks():
        fp.write(chunk)
    fp.close()

    with connections['default'].cursor() as cur:
        query = '''
        INSERT INTO iriyong_file_store
                    (file_origin_name,
                     file_encode_name,
                     file_ext,
                     file_path,
                     file_size)
        VALUES      ('{file_name}',
                     '{file_name_enc}',
                     '{file_ext}',
                     '{UPLOAD_DIR}',
                     '{file_size}')
        '''.format(
            file_name=file_name,
            file_name_enc=file_name_enc,
            file_ext=file_ext,
            UPLOAD_DIR=UPLOAD_DIR,
            file_size=file_size)
        cur.execute(query)

@csrf_exempt
def fileUpload(request):

    if 'file' in request.FILES:
        fileObject = request.FILES['file']
        #common_single_file_upload(fileObject)

    return JsonResponse({'a':'b'})

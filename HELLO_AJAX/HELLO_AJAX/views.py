from django.shortcuts import render
from django.http.response import JsonResponse
import json
from django.views.decorators.csrf import csrf_exempt
from HELLO_AJAX.daoemp import DaoEmp

@csrf_exempt
def ajax(request):
    dict = json.loads(request.body)
    # do something
    print(dict['e_id'])

    context = {
        'result': dict,
    }
    return JsonResponse(context)


@csrf_exempt
def ajax_selectlist(request):
    de = DaoEmp()
    list = de.selectList()

    json = {
        'list': list,
    }
    return JsonResponse(json)

@csrf_exempt
def ajax_select(request):
    dict = json.loads(request.body)
    e_id = dict['e_id']
    # param(json변수)말고 json 데이터를 직접 받았으면
    # e_id = request.POST['e_id']
    
    de = DaoEmp()
    vo = de.selectOne(e_id)

    # json으로 하면 local variable 'json' referenced before assignment
    # context로 바꿔주니 동작함
    context = {
        'vo': vo,
    }
    return JsonResponse(context)

@csrf_exempt
def ajax_insert(request):
    dict = json.loads(request.body)
    e_id = dict['e_id']
    e_name = dict['e_name']
    gen = dict['gen']
    addr = dict['addr']
    
    de = DaoEmp()
    cnt = de.insert(e_id, e_name, gen, addr)
    
    context = None
    list = None
    if cnt == 1:
        list = de.selectList()
        context = {
            'cnt': cnt,
            'list': list,
        }
    else:
        context = {
            'cnt': cnt,
        }
    
    return JsonResponse(context)


@csrf_exempt
def ajax_update(request):
    dict = json.loads(request.body)
    e_id = dict['e_id']
    e_name = dict['e_name']
    gen = dict['gen']
    addr = dict['addr']
    
    de = DaoEmp()
    cnt = de.update(e_id, e_name, gen, addr)
    
    context = None
    list = None
    if cnt == 1:
        list = de.selectList()
        context = {
            'cnt': cnt,
            'list': list,
        }
    else:
        context = {
            'cnt': cnt,
        }
    
    return JsonResponse(context)


@csrf_exempt
def ajax_delete(request):
    dict = json.loads(request.body)
    e_id = dict['e_id']
    
    de = DaoEmp()
    cnt = de.delete(e_id)

    context = None
    list = None
    if cnt == 1:
        list = de.selectList()
        context = {
            'cnt': cnt,
            'list': list,
        }
    else:
        context = {
            'cnt': cnt,
        }
    
    return JsonResponse(context)


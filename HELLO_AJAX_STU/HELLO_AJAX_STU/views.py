import json

from django.http.response import HttpResponse, JsonResponse
import pymysql

from HELLO_AJAX_STU.daostudent import DaoStudent
from django.views.decorators.csrf import csrf_exempt


def index(request):
    # return redirect("static/student.html") # 서버측에서 바꾼거
    return HttpResponse("<script>location.href='static/student.html';</script>") # 클라이언트 측에서 바꾼거


@csrf_exempt
def ajax_selectlist(request):
    ds = DaoStudent()
    list = ds.selectList()

    json = {
        'list': list,
    }
    return JsonResponse(json)

@csrf_exempt
def ajax_select(request):
    dict = json.loads(request.body)
    s_id = dict['s_id']
    # param(json변수)말고 json 데이터를 직접 받았으면
    # s_id = request.POST['s_id']
    
    ds = DaoStudent()
    vo = ds.selectOne(s_id)

    # json으로 하면 local variable 'json' referenced before assignment
    # context로 바꿔주니 동작함
    context = {
        'vo': vo,
    }
    return JsonResponse(context)

@csrf_exempt
def ajax_insert(request):
    dict = json.loads(request.body)
    s_id = dict['s_id']
    s_name = dict['s_name']
    mobile = dict['mobile']
    grade = dict['grade']
    
    ds = DaoStudent()
    cnt = ds.insert(s_id, s_name, mobile, grade)
    
    context = None
    list = None
    if cnt == 1:
        list = ds.selectList()
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
    s_id = dict['s_id']
    s_name = dict['s_name']
    mobile = dict['mobile']
    grade = dict['grade']
    
    ds = DaoStudent()
    cnt = ds.update(s_id, s_name, mobile, grade)
    
    context = None
    list = None
    if cnt == 1:
        list = ds.selectList()
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
    s_id = dict['s_id']
    
    ds = DaoStudent()
    cnt = ds.delete(s_id)

    context = None
    list = None
    if cnt == 1:
        list = ds.selectList()
        context = {
            'cnt': cnt,
            'list': list,
        }
    else:
        context = {
            'cnt': cnt,
        }
    
    return JsonResponse(context)


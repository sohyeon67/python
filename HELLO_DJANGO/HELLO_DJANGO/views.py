from django.http.response import HttpResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
import pymysql


def index(request):
    return HttpResponse("Hello, Django")

def param(request):
    menu = request.GET.get('menu', '탕수육')
    return HttpResponse("PARAM " + menu)

@csrf_exempt
def post(request):
    # menu = request.POST.get('menu', '김치찌개')
    menu = request.POST['menu']
    return HttpResponse("POST " + menu)

def forw(request):
    a = "홍길동"
    b = ["전우치", "일지매"]
    c = [
            {'e_id':1,'e_name':1,'gen':1,'addr':1},
            {'e_id':2,'e_name':2,'gen':2,'addr':2},
            {'e_id':3,'e_name':3,'gen':3,'addr':3}
        ]
    return render(request, 'forw.html', {'a':a, 'b':b, 'c':c})

def emp(request):
    
    conn = pymysql.connect(host='localhost', user='root', password='python',
                       port=3305, db='python', charset='utf8')
 
    curs = conn.cursor(pymysql.cursors.DictCursor)
     
    sql = "select * from emp"
    curs.execute(sql)
     
    emps = curs.fetchall()
    
    curs.close()
    conn.close()
    
    return render(request, 'emp.html', {'emps':emps})




from django.shortcuts import render
import pymysql

from HELLO_DJ_EMP.daoemp import DaoEmp


def emp_list(request):
    de = DaoEmp()
    list = de.selectList()
    
    return render(request, 'emp_list.html', {'list':list})

def emp_detail(request):
    e_id = request.GET.get('e_id', '')
    de = DaoEmp()
    vo = de.selectOne(e_id)
    
    return render(request, 'emp_detail.html', {'vo':vo})

def emp_mod(request):
    e_id = request.GET.get('e_id', '')
    de = DaoEmp()
    vo = de.selectOne(e_id)
    
    return render(request, 'emp_mod.html', {'vo':vo})

def emp_mod_act(request):
    e_id = request.POST['e_id']
    e_name = request.POST['e_name']
    gen = request.POST['gen']
    addr = request.POST['addr']
    
    de = DaoEmp()
    cnt = de.update(e_id, e_name, gen, addr)
    
    return render(request, 'emp_mod_act.html', {'cnt':cnt})

def emp_add(request):
    return render(request, 'emp_add.html')

def emp_add_act(request):
    e_id = request.POST['e_id']
    e_name = request.POST['e_name']
    gen = request.POST['gen']
    addr = request.POST['addr']
    
    de = DaoEmp()
    cnt = de.insert(e_id, e_name, gen, addr)
    
    return render(request, 'emp_add_act.html', {'cnt':cnt})

def emp_del_act(request):
    e_id = request.POST['e_id']
    
    de = DaoEmp()
    cnt = de.delete(e_id)
    
    return render(request, 'emp_del_act.html', {'cnt':cnt})
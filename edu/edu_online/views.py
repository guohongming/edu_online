# Create your views here.
from django.http import HttpResponse
from django.shortcuts import render,reverse,redirect
# Create your views here.
from django.contrib.auth.models import User,Permission,Group #从auth系统导入User，Permission，Group 表
from django.contrib.auth import login,logout,authenticate #导入login，logout，authenticate三个方法
from django.views.decorators.csrf import csrf_exempt
from django.contrib import auth
import json


def index(request):
    context = {
        'user_id':request.user.id,
        'user_name':request.user.username
    }
    # 把上下文传递到模板里
    print(context)
    return render(request, 'index.html', context)


def detail(request):
    context = {
    }
    # 把上下文传递到模板里
    return render(request, 'tem.html', context)


def sign_in(request):
    context = {
    }
    # 把上下文传递到模板里
    return render(request, 'signin.html', context)


def signup(request):
    context = {
    }
    # 把上下文传递到模板里
    return render(request, 'signup.html', context)


@csrf_exempt
def login(request):
    # request_json = json.loads(request.body)
    username = request.POST.get("username")
    password = request.POST.get("password")
    user_obj = auth.authenticate(request, username=username, password=password)
    if user_obj:
        # 用户名和密码正确
        auth.login(request, user_obj)  # 给该次请求设置了session数据，并在响应中回写cookie
        return redirect("/index/")
    else:
        return HttpResponse(False)


@csrf_exempt
def logout(request):
    auth.logout(request)
    # request_json = json.loads(request.body)
    return redirect("/index/")


@csrf_exempt
def register(request):
    data = request.POST
    username = data.get("username")
    password = data.get("password")
    # 校验注册，名字不可重复
    u = User.objects.filter(username=username).first()
    if u:
        info = '该用户名已被注册'
        return HttpResponse(json.dumps({'success':False,'msg':info}),content_type='application/json')
    else:
        # 注册成功，创建用户
        User.objects.create_user(
            username=username,
            password=password
        )
        # 重定向到登录页面
        return redirect("/signin/")
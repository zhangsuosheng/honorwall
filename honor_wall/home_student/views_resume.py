from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from home.models import Student_message_uneditable,Student_message_editable,Links
from django.http import HttpResponse,HttpResponseRedirect

import time

# 引入同一个包下自定义的aes文件，用来AES加密
from home_student import aes

@login_required
def resume(request):
    userid=request.session.get('userid')
    userrelname = request.session.get('username', '')
    try:
        userlink=Links.objects.get(student=userid)
    except Links.DoesNotExist:
        return render(request, "student_center_resume.html", {'userrelname': userrelname})
    return render(request,"student_center_resume.html", {'userrelname': userrelname,'userlink':userlink})

@login_required
def generate_resume(request):
    userrelname=request.session.get('username')
    userid = request.session.get('userid')
    student_message_uneditable=Student_message_uneditable.objects.get(student_id=userid)
    student_message_editable=Student_message_editable.objects.get(student_id=userid)
    return render(request,"student_resume.html",locals())

@login_required
def generate_link(request):
    userid= request.session.get('userid')
    try:
        userlink=Links.objects.get(student_id=userid)
    except Links.DoesNotExist:
        aes_machine = aes.prpcrypt('xjtuxjtuxjtuxjtu')  # 密钥：xjtuxjtuxjtuxjtu
        miwen = aes_machine.encrypt(userid)
        timestamp = int(time.time())
        print(timestamp)
        Links.objects.create(student_id=userid, date=timestamp, use_times=3, link=miwen)
        return HttpResponseRedirect("/student/resume")
    return HttpResponseRedirect("/student/resume")
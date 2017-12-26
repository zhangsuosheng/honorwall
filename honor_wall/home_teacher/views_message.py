from django.shortcuts import render
from home.models import Competition_type,Student_message_editable,Student_message_uneditable,Honor_competition,Honor_patent,Honor_paper_magazine,Honor_paper_meeting,Honor_scholarship,Honor_experience,Message,Teacher
from django.http import HttpResponse,HttpRequest,HttpResponseRedirect
from django.db.models import Q
from django.core.paginator import Paginator,EmptyPage,PageNotAnInteger
from django.views.decorators.csrf import csrf_protect
from django.views.decorators.csrf import csrf_exempt
from datetime import datetime
import json

def message_out_2(request):
    title=request.POST.get("title","")
    class_=request.POST.get("class","")
    if class_=="竞赛":
        class_=1
    elif class_=="期刊论文":
        class_=2
    elif class_ == "会议论文":
        class_ = 3
    elif class_ == "专利":
        class_ = 4
    elif class_ == "奖学金":
        class_ = 5
    elif class_ == "社会经历":
        class_ = 6
    elif class_=="其他":
        class_=7
    content=request.POST.get("summernote","")
    file=request.FILES.get("stu_provefile_contest","")
    try:
        teacher_id = request.session.get('sessionid', '')
        teacher = Teacher.objects.get(teacher_id=teacher_id)
        message=Message(teacher=teacher,message_title=title,message_type=class_,message_content=content,message_file=file)
        message.save()
    except:
        render (request,"404.html")
    return HttpResponseRedirect("./message_outed")

def re_message(request,id):
    return render(request,"teacher_center_message_out.html",{"already":1,"id":id})

def article_get(request):
    try:
        id=request.POST.get("id",1)
        message=Message.objects.get(id=id)
    except:
        return render(request,"404.html")

    return HttpResponse(json.dumps({"title":message.message_title,"type":message.message_type,"content":message.message_content}))

def delete(request):
    try:
        id=request.POST.get("id",1)
        print (id)
        message=Message.objects.get(id=id)
        message.delete()
    except:
        return render(request,"404.html")
    return HttpResponse("1")

def change(request):
    try:
        id=request.POST.get("id",1)
        title=request.POST.get("title","")
        type=request.POST.get("type","")
        content=request.POST.get("content","")
        message=Message.objects.get(id=id)
        message.message_title=title
        message.message_type=type
        message.message_content=content
        message.message_date=datetime.now()
        message.save()
    except:
        return render(request,"404.html")
    return HttpResponse("1")

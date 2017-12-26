from django.shortcuts import render
from home.models import Competition_type,Student_message_editable,Student_message_uneditable,Honor_competition,Honor_patent,Honor_paper_magazine,Honor_paper_meeting,Honor_scholarship,Honor_experience
from django.http import HttpResponse,HttpRequest
from django.db.models import Q
from django.core.paginator import Paginator,EmptyPage,PageNotAnInteger
from django.views.decorators.csrf import csrf_protect
from django.views.decorators.csrf import csrf_exempt
import json

@csrf_protect
def search(request):
    id=request.POST.get('id',"")
    name = request.POST.get('name', "")
    grade = request.POST.get('grade', "")
    field = request.POST.get('field', "")
    classroom = request.POST.get('classroom', "")
    # print(id + name + grade +field + classroom)
    try:
        if(id !=""):
            id=int(id)
            if name !="":
                if grade!="":
                    grade=int(grade)
                    if field!="":
                        if classroom!="":
                            classroom=int(classroom)
                            obj=Student_message_uneditable.objects.filter(student_id=id,student_name__contains=name,student_grade=grade,student_field=field,student_classname=classroom)
                        else:
                            obj=Student_message_uneditable.objects.filter(student_id=id,student_name__contains=name,student_grade=grade,student_field=field)
                    else:
                        if classroom!="":
                            classroom=int(classroom)
                            obj=Student_message_uneditable.objects.filter(student_id=id, student_name__contains=name, student_grade=grade, student_classname=classroom)
                        else:
                            obj=Student_message_uneditable.objects.filter(student_id=id, student_name__contains=name, student_grade=grade)
                else:
                    if field!="":
                        if classroom!="":
                            classroom=int(classroom)
                            obj = Student_message_uneditable.objects.filter(student_id=id, student_name__contains=name,student_field=field,student_classname=classroom)
                        else:
                            obj = Student_message_uneditable.objects.filter(student_id=id, student_name__contains=name,student_field=field)
                    else:
                        if classroom!="":
                            classroom=int(classroom)
                            obj = Student_message_uneditable.objects.filter(student_id=id, student_name__contains=name,student_classname=classroom)
                        else:
                            obj = Student_message_uneditable.objects.filter(student_id=id, student_name__contains=name)
            else:
                if grade !="":
                    grade=int(grade)
                    if field != "":
                        if classroom != "":
                            classroom = int(classroom)
                            obj = Student_message_uneditable.objects.filter(student_id=id, student_grade=grade, student_field=field,
                                                             student_classname=classroom)
                        else:
                            obj = Student_message_uneditable.objects.filter(student_id=id, student_grade=grade, student_field=field)
                    else:
                        if classroom != "":
                            classroom = int(classroom)
                            obj = Student_message_uneditable.objects.filter(student_id=id, student_grade=grade, student_classname=classroom)
                        else:
                            obj = Student_message_uneditable.objects.filter(student_id=id, student_grade=grade)
                else:
                    if field != "":
                        if classroom != "":
                            classroom = int(classroom)
                            obj = Student_message_uneditable.objects.filter(student_id=id, student_field=field, student_classname=classroom)
                        else:
                            obj = Student_message_uneditable.objects.filter(student_id=id, student_field=field)
                    else:
                        if classroom != "":
                            classroom = int(classroom)
                            obj = Student_message_uneditable.objects.filter(student_id=id, student_classname=classroom)
                        else:
                            obj = Student_message_uneditable.objects.filter(student_id=id)
        else:
            if name !="":
                if grade!="":
                    grade=int(grade)
                    if field!="":
                        if classroom!="":
                            classroom=int(classroom)
                            obj=Student_message_uneditable.objects.filter(student_name__contains=name,student_grade=grade,student_field=field,student_classname=classroom)
                        else:
                            obj=Student_message_uneditable.objects.filter(student_name__contains=name,student_grade=grade,student_field=field)
                    else:
                        if classroom!="":
                            classroom=int(classroom)
                            obj=Student_message_uneditable.objects.filter( student_name__contains=name, student_grade=grade, student_classname=classroom)
                        else:
                            obj=Student_message_uneditable.objects.filter( student_name__contains=name, student_grade=grade)
                else:
                    if field!="":
                        if classroom!="":
                            classroom=int(classroom)
                            obj = Student_message_uneditable.objects.filter( student_name__contains=name,student_field=field,student_classname=classroom)
                        else:
                            obj = Student_message_uneditable.objects.filter(student_name__contains=name,student_field=field)
                    else:
                        if classroom!="":
                            classroom=int(classroom)
                            obj = Student_message_uneditable.objects.filter(student_name__contains=name,student_classname=classroom)
                        else:
                            print(name)
                            obj = Student_message_uneditable.objects.filter(student_name__contains=name)
            else:
                if grade !="":
                    grade=int(grade)
                    if field != "":
                        if classroom != "":
                            classroom = int(classroom)
                            obj = Student_message_uneditable.objects.filter(student_grade=grade, student_field=field,student_classname=classroom)
                        else:
                            obj = Student_message_uneditable.objects.filter( student_grade=grade, student_field=field)
                    else:
                        if classroom != "":
                            classroom = int(classroom)
                            obj = Student_message_uneditable.objects.filter( student_grade=grade, student_classname=classroom)
                        else:
                            obj = Student_message_uneditable.objects.filter( student_grade=grade)
                else:
                    if field != "":
                        if classroom != "":
                            classroom = int(classroom)
                            obj = Student_message_uneditable.objects.filter(student_field=field, student_classname=classroom)
                        else:
                            obj = Student_message_uneditable.objects.filter( student_field=field)
                    else:
                        if classroom != "":
                            classroom = int(classroom)
                            obj = Student_message_uneditable.objects.filter( student_classname=classroom)
                        else:
                            obj = Student_message_uneditable.objects.all()
    except:
        pass
    message=[]
    for i in obj:
        return_message={"id":i.student_id,"name":i.student_name,"grade":i.student_grade,"field":i.student_field,"classroom":i.student_classname}
        message.append(return_message)
    return HttpResponse(json.dumps(message))

def studentmessagechange_2(request,id):
    try:
        student_obj=Student_message_uneditable.objects.get(student_id=id)
        student_edit_obj=Student_message_editable.objects.get(student=student_obj)
        competition=Honor_competition.objects.filter(student=student_obj)
        paper_magazine=Honor_paper_magazine.objects.filter(student=student_obj)
        paper_meeting=Honor_paper_meeting.objects.filter(student=student_obj)
        patent=Honor_patent.objects.filter(student=student_obj)
        experience=Honor_experience.objects.filter(student=student_obj)
        scholarship=Honor_scholarship.objects.filter(student=student_obj)
    except:
        return render(request,"404.html")
    message=[]
    for i in competition:
        if i.honor_competition_is_checked==0:
            state="未审核"
        elif i.honor_competition_is_checked==1:
            state="审核通过"
        elif i.honor_competition_is_checked==2:
            state="正在审核"
        elif i.honor_competition_is_checked==-1:
            state="审核不通过"
        return_message={'id':i.id,'class':"竞赛",'name':i.competition_name,'time':str(i.honor_competition_submit_time),'state':state}
        message.append(return_message)
    for i in paper_magazine:
        if i.honor_paper_magazine_is_checked==0:
            state="未审核"
        elif i.honor_paper_magazine_is_checked==1:
            state="审核通过"
        elif i.honor_paper_magazine_is_checked==2:
            state="正在审核"
        elif i.honor_paper_magazine_is_checked==-1:
            state="审核不通过"
        return_message = {'id': i.id, 'class': "期刊论文", 'name': i.honor_paper_magazine_papername,
                          'time': str(i.honor_paper_magazine_submit_time), 'state': state}
        message.append(return_message)
    for i in paper_meeting:
        if i.honor_paper_meeting_is_checked==0:
            state="未审核"
        elif i.honor_paper_meeting_is_checked==1:
            state="审核通过"
        elif i.honor_paper_meeting_is_checked==2:
            state="正在审核"
        elif i.honor_paper_meeting_is_checked==-1:
            state="审核不通过"
        return_message = {'id': i.id, 'class': "会议论文", 'name': i.honor_paper_meeting_papername,
                          'time': str(i.honor_paper_meeting_submit_time), 'state': state}
        message.append(return_message)
    for i in patent:
        if i.honor_patent_is_checked==0:
            state="未审核"
        elif i.honor_patent_is_checked==1:
            state="审核通过"
        elif i.honor_patent_is_checked==2:
            state="正在审核"
        elif i.honor_patent_is_checked==-1:
            state="审核不通过"
        return_message = {'id': i.id, 'class': "专利", 'name': i.honor_patent_name,
                          'time': str(i.honor_patent_submit_time), 'state': state}
        message.append(return_message)
    for i in scholarship:
        if i.honor_scholarship_is_checked==0:
            state="未审核"
        elif i.honor_scholarship_is_checked==1:
            state="审核通过"
        elif i.honor_scholarship_is_checked==2:
            state="正在审核"
        elif i.honor_scholarship_is_checked==-1:
            state="审核不通过"
        return_message = {'id': i.id, 'class': "奖学金", 'name': i.honor_scholarship_name,
                          'time': str(i.honor_scholarship_submit_time), 'state': state}
        message.append(return_message)
    for i in experience:
        if i.honor_experience_is_checked==0:
            state="未审核"
        elif i.honor_experience_is_checked==1:
            state="审核通过"
        elif i.honor_experience_is_checked==2:
            state="正在审核"
        elif i.honor_experience_is_checked==-1:
            state="审核不通过"
        return_message = {'id': i.id, 'class': "社会经历", 'name': i.honor_experience_name,
                          'time': str(i.honor_experience_submit_time), 'state': state}
        message.append(return_message)
    if student_obj.student_sex==0:
        sex="女"
    else:
        sex="男"
    if student_obj.student_state==1:
        student={"student_name":student_obj.student_name,"student_sex":sex,"student_id":student_obj.student_id,"student_field":student_obj.student_field,"student_classname":student_obj.student_classname,"student_faculty":student_obj.student_faculty,"student_grade":student_obj.student_grade,"student_state":student_obj.student_state}
    else:
        student={"student_name":student_obj.student_name,"student_sex":sex,"student_id":student_obj.student_id,"student_field":student_obj.student_field,"student_classname":student_obj.student_classname,"student_faculty":student_obj.student_faculty,"student_grade":student_obj.student_grade}
    student_edit={"student_nickname":student_edit_obj.student_nickname,"student_political_state":student_edit_obj.student_political_state,"student_people":student_edit_obj.student_people}
    return render(request,"teacher_center_studentmessagechange_2.html",{"student":student,"student_edit":student_edit,"message":message})


def save(request):
    if request.method=="POST":
        try:
            id=int(request.POST.get("id",""))
            name=request.POST.get("name","")
            sex=request.POST.get("sex","")
            grade=int(request.POST.get("grade",""))
            field=request.POST.get("field","")
            classroom=int(request.POST.get("classroom",""))
            faculty=request.POST.get("faculty","")
            nickname=request.POST.get("nickname","")
            political=request.POST.get("political","")
            people=request.POST.get("people","")
            state=int(request.POST.get("state",None))
        except:
            return render(request,"404.html")

        # try:
        stu=Student_message_uneditable.objects.get(student_id=id)
        stu_edit=Student_message_editable.objects.get(student=stu)
        stu.student_name = name
        stu.student_id = id
        stu.student_sex = sex
        stu.student_field = field
        stu.student_classname = classroom
        stu.student_faculty=faculty
        stu.student_grade=grade
        stu.student_state=state
        stu_edit.student_nickname=nickname
        stu_edit.student_political_state=political
        stu_edit.student_people=people
        stu.save()
        stu_edit.save()

        # except:
        #     return render(request,"404.html")

    return HttpResponse("")

def submit(request):
    if request.method=="POST":
        try:
            name=request.POST.get("name","")
            competition_level=request.POST.get("competition_level","")
            level = request.POST.get("level", "")
            points = request.POST.get("points",0)
            if points=="":
                points=0
            message = request.POST.get("message", "")
            is_true=request.POST.get("is","")
        except:
            return render(request,"404.html")
        try:
            # com=Competition_type(competition_class="竞赛奖项",competition_name=name,competition_competition_level=competition_level,competition_level=level,competition_point=points,competition_introduce=message)
            if int(is_true)==1:
                print (2)
                com = Competition_type( competition_name=name,competition_competition_level=competition_level, competition_level=level,competition_point=points, competition_introduce=message)
                com.save()
            else:
                print (1)
                com = Competition_type.objects.filter(competition_name=name)[0]
                com.competition_competition_level=competition_level
                com.competition_level=level
                com.points=points
                com.message=message
                com.save()
        except:
            return render(request,"404.html")

    return HttpResponse("1")

def getcompetition(request):
    mes=Competition_type.objects.all()
    message=[]
    for m in mes:
        message.append(m.competition_name)
    return HttpResponse(json.dumps(message))

def delete(request):
    try:
        name=request.POST.get("name","")
        message=Competition_type.objects.get(competition_name=name)
        message.delete()
    except:
        return render(request,"404.html")

    return HttpResponse("1")


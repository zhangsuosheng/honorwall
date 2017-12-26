from django.shortcuts import render
from home.models import Competition_type,Message,Student_message_editable,Student_message_uneditable,Honor_competition,Honor_patent,Honor_paper_magazine,Honor_paper_meeting,Honor_scholarship,Honor_experience,Teacher
from django.http import HttpResponse,HttpRequest
from django.db.models import Q
from django.core.paginator import Paginator,EmptyPage,PageNotAnInteger
# Create your views here.
level_name={1:"国际级",2:"国家级",3:"西北赛区级(包括其他赛区级",4:"省级",5:"校级",-1:"不分级",0:"其他"}
#基本跳转函数
def index(request):
    request.session["sessionid"]=13123122
    return render(request, "teacher_center_checking.html",{'competition':1})

def checking(request):
    return render(request, "teacher_center_checking.html",{'competition':1})
def checking_where(request,where=1):
    if str(where)=='1':
        return render(request, "teacher_center_checking.html",{'competition':1})
    elif str(where)=='2':
        return render(request, "teacher_center_checking.html",{'magazinepaper':1})
    elif str(where)=='3':
        return render(request, "teacher_center_checking.html",{'meetingpaper':1})
    elif str(where)=='4':
        return render(request, "teacher_center_checking.html",{'patent':1})
    elif str(where)=='5':
        return render(request, "teacher_center_checking.html",{'prize':1})
    elif str(where)=='6':
        return render(request, "teacher_center_checking.html",{'experience':1})
    elif str(where)=='7':
        return render(request, "teacher_center_checking.html",{'already':1})
    else:
        return render(request, "404.html")

def already(request):
    return render(request,"teacher_center_already.html")

def competitionadd(request):
    message=Competition_type.objects.all()
    return render(request, "teacher_center_competitionadd.html",{"message":message,"count":0})

def letter_checked(request):
    return render(request, "teacher_center_letter_checked.html")

def lettergenerate(request):
    return render(request, "teacher_center_lettergenerate.html")

def message_out(request):
    return render(request, "teacher_center_message_out.html")

def message_outed(request):
    try:
        teacher_id = request.session.get('sessionid', '')
        teacher = Teacher.objects.get(teacher_id=teacher_id)
        message=Message.objects.filter(teacher=teacher)
    except:
        return render(request,"404.html")

    return render(request, "teacher_center_message_outed.html",{"message":message})

def setting(request):
    return render(request, "teacher_center_setting.html")

def studentmessagechange(request):
    return render(request, "teacher_center_studentmessagechange.html")



def competition(request,id=1,already=None):
    # return HttpResponse(already)
    class message_return():
        pass
    try:
        com = Honor_competition.objects.get(id=id)
        message_return.is_checked = com.honor_competition_is_checked
        if message_return.is_checked==0:
            com.honor_competition_is_checked=2
            com.save()
    except:
        return render(request, "404.html")

    message_return.student=com.student
    message_return.competition_name=com.competition_name
    message_return.competition_competition_level=level_name[com.competition_competition_level]
    message_return.competition_level=com.competition_level
    message_return.honor_competition_get_time=com.honor_competition_get_time
    message_return.honor_competition_teacher=com.honor_competition_teacher
    message_return.honor_competition_award=com.honor_competition_award
    message_return.honor_competition_message=com.honor_competition_message
    message_return.competition_point=com.competition_point

    if message_return.is_checked==1:
        message_return.is_checked='审核通过'
    elif message_return.is_checked==0:
        message_return.is_checked='未审核'
    elif message_return.is_checked==-1:
        message_return.is_checked='审核不通过'
    elif message_return.is_checked==2:
        message_return.is_checked='正在审核'
    #文件(怎么处理查一下)
    message_return.honor_competition_confirm_file=com.honor_competition_confirm_file
    return render(request, "teacher_center_competition.html",{"message":message_return,'id':id,'already':already})

def experience(request,id=1,already=None):
    class message_return():
        pass
    try:
        com = Honor_experience.objects.get(id=id)
        message_return.is_checked = com.honor_experience_is_checked
        if message_return.is_checked==0:
            com.honor_experience_is_checked=2
            com.save()
    except:
        return render(request, "404.html")

    message_return.student=com.student
    message_return.honor_experience_name=com.honor_experience_name
    message_return.honor_experience_authority=com.honor_experience_authority
    message_return.honor_experience_start=com.honor_experience_start
    message_return.honor_experience_end=com.honor_experience_end
    message_return.honor_experience_note=com.honor_experience_note
    message_return.honor_experience_point=com.honor_experience_point

    if message_return.is_checked==1:
        message_return.is_checked='审核通过'
    elif message_return.is_checked==0:
        message_return.is_checked='未审核'
    elif message_return.is_checked==-1:
        message_return.is_checked='审核不通过'
    elif message_return.is_checked==2:
        message_return.is_checked='正在审核'
    #文件(怎么处理查一下)
    message_return.honor_experience_confirm_file=com.honor_experience_confirm_file
    return render(request, "teacher_center_experience.html",{"message":message_return,'id':id,'already':already})


def magazinepaper(request,id=1,already=None):
    class message_return():
        pass
    try:
        com = Honor_paper_magazine.objects.get(id=id)
        message_return.is_checked = com.honor_paper_magazine_is_checked
        if message_return.is_checked == 0:
            com.honor_paper_magazine_is_checked=2
            com.save()
    except:
        return render(request, "404.html")


    message_return.student = com.student
    message_return.honor_paper_magazine_type=com.honor_paper_magazine_type
    message_return.honor_paper_magazine_magazinename=com.honor_paper_magazine_magazinename
    message_return.honor_paper_magazine_papername=com.honor_paper_magazine_papername
    message_return.honor_paper_magazine_status=com.honor_paper_magazine_status
    message_return.honor_paper_magazine_page_begin=com.honor_paper_magazine_page_begin
    message_return.honor_paper_magazine_ISBNcode=com.honor_paper_magazine_ISBNcode
    message_return.honor_paper_magazine_page_number=com.honor_paper_magazine_page_number
    message_return.honor_paper_magazine_date_publish=com.honor_paper_magazine_date_publish
    if com.honor_paper_magazine_is_firstauthor:
        message_return.honor_paper_magazine_is_firstauthor="是"
    else:
        message_return.honor_paper_magazine_is_firstauthor="不是"
    message_return.honor_paper_magazine_quotetimes=com.honor_paper_magazine_quotetimes
    message_return.honor_paper_magazine_impactfactors=com.honor_paper_magazine_impactfactors
    message_return.honor_paper_magazine_searching=com.honor_paper_magazine_searching
    message_return.honor_paper_magazine_people=com.honor_paper_magazine_people
    message_return.honor_paper_magazine_abstract=com.honor_paper_magazine_abstract
    message_return.honor_paper_magazine_point=com.honor_paper_magazine_point

    if message_return.is_checked==1:
        message_return.is_checked='审核通过'
    elif message_return.is_checked==0:
        message_return.is_checked='未审核'
    elif message_return.is_checked==-1:
        message_return.is_checked='审核不通过'
    elif message_return.is_checked==2:
        message_return.is_checked='正在审核'

    #文件(怎么处理查一下)
    message_return.honor_paper_magazine_confirm_file=com.honor_paper_magazine_confirm_file
    return render(request, "teacher_center_magazinepaper.html",{"message":message_return,'id':id,'already':already})

def meetingpaper(request,id=1,already=None):
    class message_return():
        pass
    try:
        com = Honor_paper_meeting.objects.get(id=id)
        message_return.is_checked = com.honor_paper_meeting_is_checked
        if message_return.is_checked == 0:
            com.honor_paper_meeting_is_checked=2
            com.save()
    except:
        return render(request, "404.html")


    message_return.student = com.student
    message_return.honor_paper_meeting_type=com.honor_paper_meeting_type
    message_return.honor_paper_meeting_papername=com.honor_paper_meeting_papername
    message_return.honor_paper_meeting_meetingname=com.honor_paper_meeting_meetingname
    message_return.honor_paper_meeting_address=com.honor_paper_meeting_address
    message_return.honor_paper_meeting_date=com.honor_paper_meeting_date
    message_return.honor_paper_meeting_people=com.honor_paper_meeting_people
    if com.honor_paper_meeting_is_firstauthor:
        message_return.honor_paper_meeting_is_firstauthor="是"
    else:
        message_return.honor_paper_meeting_is_firstauthor="不是"
    message_return.honor_paper_meeting_point=com.honor_paper_meeting_point

    if message_return.is_checked==1:
        message_return.is_checked='审核通过'
    elif message_return.is_checked==0:
        message_return.is_checked='未审核'
    elif message_return.is_checked==-1:
        message_return.is_checked='审核不通过'
    elif message_return.is_checked==2:
        message_return.is_checked='正在审核'

    #文件(怎么处理查一下)
    message_return.honor_paper_meeting_confirm_file=com.honor_paper_meeting_confirm_file
    return render(request, "teacher_center_meetingpaper.html",{"message":message_return,'id':id,'already':already})

def patent(request,id=1,already=None):
    class message_return():
        pass
    try:
        com = Honor_patent.objects.get(id=id)
        message_return.is_checked = com.honor_patent_is_checked
        if message_return.is_checked == 0:
            com.honor_patent_is_checked=2
            com.save()
    except:
        return render(request, "404.html")


    message_return.student = com.student
    message_return.honor_patent_type=com.honor_patent_type
    message_return.honor_patent_name=com.honor_patent_name
    message_return.honor_patent_number=com.honor_patent_number
    message_return.honor_patent_date_apply=com.honor_patent_date_apply
    message_return.honor_patent_date_auth=com.honor_patent_date_auth
    message_return.honor_patent_legalstatus=com.honor_patent_legalstatus
    if com.honor_patent_firstman:
        message_return.honor_patent_firstman="是"
    else:
        message_return.honor_patent_firstman="不是"
    message_return.honor_patent_people=com.honor_patent_people

    message_return.honor_patent_point=com.honor_patent_point

    if message_return.is_checked==1:
        message_return.is_checked='审核通过'
    elif message_return.is_checked==0:
        message_return.is_checked='未审核'
    elif message_return.is_checked==-1:
        message_return.is_checked='审核不通过'
    elif message_return.is_checked==2:
        message_return.is_checked='正在审核'

    #文件(怎么处理查一下)
    message_return.honor_patent_confirm_file=com.honor_patent_confirm_file
    return render(request, "teacher_center_patent.html",{"message":message_return,'id':id,'already':already})

def prize(request,id=1,already=None):
    class message_return():
        pass
    try:
        com = Honor_scholarship.objects.get(id=id)
        message_return.is_checked = com.honor_scholarship_is_checked
        if message_return.is_checked == 0:
            com.honor_scholarship_is_checked=2
            com.save()
    except:
        return render(request, "404.html")


    message_return.student = com.student
    message_return.honor_scholarship_name=com.honor_scholarship_name
    message_return.honor_scholarship_year=com.honor_scholarship_year
    message_return.honor_scholarship_moneyperyear=com.honor_scholarship_moneyperyear
    message_return.honor_scholarship_authority=com.honor_scholarship_authority
    message_return.honor_scholarship_point=com.honor_scholarship_point

    if message_return.is_checked==1:
        message_return.is_checked='审核通过'
    elif message_return.is_checked==0:
        message_return.is_checked='未审核'
    elif message_return.is_checked==-1:
        message_return.is_checked='审核不通过'
    elif message_return.is_checked==2:
        message_return.is_checked='正在审核'

    #文件(怎么处理查一下)
    message_return.honor_scholarship_confirm_file=com.honor_scholarship_confirm_file
    return render(request, "teacher_center_prize.html",{"message":message_return,'id':id,'already':already})




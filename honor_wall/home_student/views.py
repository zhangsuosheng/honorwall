#正常用库
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from home.models import Student_message_editable, Student_honorwall, Honor_competition, Honor_patent, Honor_paper_meeting, Honor_experience, Honor_paper_magazine, Honor_scholarship
#测试用库
from django.urls import reverse
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib import auth
from django.contrib.auth.models import User
##################################################################################
# 测试用函数
##################################################################################



#分页器
def dispage(request,page):
    if page == "":
        page = 1

    page = int(page)
    test_list = [i for i in range(1, 500)]  # 生成一个有500条数据的表
    paginator = Paginator(test_list, 10)  # 把这个列表分割成10个为一页的分页器
    try:
        # 获取指定页面的数据
        contacts = paginator.page(page)
    except PageNotAnInteger:
        # 如果获取的页面不是整数,page取第一页
        page = 1
        contacts = paginator.page(page)
    except EmptyPage:
        # 如果获取的页面超出范围，则显示最后一页
        page = paginator.num_pages
        contacts = paginator.page(page)
        # 根据当前所在页产生长度为10的页码，放入列表中
    paper_list = make_paper_list(page, paginator.num_pages, 10)
    return render(request, "my_honorwall.html", {"page": page, "contacts": contacts, "paper_list": paper_list})

#输入一个数字，生成以它为中心的一个数列
def make_paper_list(page, max_page, long):
    if (page-5 > 0) & (page+3 < max_page):
        return [i for i in range(page-5,page-5+long)]
    if (page-5 <= 0) & (page+3 < max_page):
        return [i for i in range(1, min(1+long, 1+max_page))]
    if (page - 5 <= 0) & (page + 3 >= max_page):
        return [i for i in range(1,max_page+1)]
    if (page - 5 > 0) & (page + 3 >= max_page):
        return [i for i in range(max_page+1-long, max_page+1)]


#################################################################################################
#正常函数
##############################################################################################

@login_required
def honor(request):
    userrelname = request.session.get('username', '')
    user_id = request.session.get('userid', '')
    message_contact = Student_message_editable.objects.get(student__student_message_editable__student_id=user_id)

    competitions = Honor_competition.objects.all().filter(student__student_message_editable__student_id=user_id,honor_competition_is_checked=1).order_by("honor_competition_check_time")
    patents = Honor_patent.objects.all().filter(student__student_message_editable__student_id=user_id,honor_patent_is_checked=1).order_by("honor_patent_check_time")
    scholarships = Honor_scholarship.objects.all().filter(student__student_message_editable__student_id=user_id,honor_scholarship_is_checked=1).order_by("honor_scholarship_check_time")
    paper_magazines = Honor_paper_magazine.objects.all().filter(student__student_message_editable__student_id=user_id,honor_paper_magazine_is_checked=1).order_by("honor_paper_magazine_check_time")
    paper_meetings = Honor_paper_meeting.objects.all().filter(student__student_message_editable__student_id=user_id,honor_paper_meeting_is_checked=1).order_by("honor_paper_meeting_check_time")
    experiences = Honor_experience.objects.all().filter(student__student_message_editable__student_id=user_id,honor_experience_is_checked=1).order_by("honor_experience_check_time")
    return render(request, "my_honorwall.html", {'userrelname': userrelname,
                                                 'message_contact': message_contact,
                                                 'patents': patents,
                                                 'competitions': competitions,
                                                 'scholarships': scholarships,
                                                 'paper_magazines': paper_magazines,
                                                 'paper_meetings': paper_meetings,
                                                 'experiences': experiences,
                                                 })
    #dispage(request,"student_center_honor.html")





@login_required
def status(request):
    userrelname = request.session.get('username', '')
    user_id = request.session.get('userid', '')
    result=[]
    competitions = Honor_competition.objects.all().filter(student__student_message_editable__student_id=user_id).order_by("honor_competition_check_time")
    patents = Honor_patent.objects.all().filter(student__student_message_editable__student_id=user_id).order_by("honor_patent_check_time")
    scholarships = Honor_scholarship.objects.all().filter(student__student_message_editable__student_id=user_id).order_by("honor_scholarship_check_time")
    paper_magazines = Honor_paper_magazine.objects.all().filter(student__student_message_editable__student_id=user_id).order_by("honor_paper_magazine_check_time")
    paper_meetings = Honor_paper_meeting.objects.all().filter(student__student_message_editable__student_id=user_id).order_by("honor_paper_meeting_check_time")
    experiences = Honor_experience.objects.all().filter(student__student_message_editable__student_id=user_id).order_by("honor_experience_check_time")
    #id代表属性设置：A-competitions, B-patents, C-scholarship, D- paper_magazines,E- paper_meetings, F- paper_experience
    for each in competitions:
        result.append(
            ["A-%d" % each.id, each.competition_name, each.honor_competition_get_time, each.honor_competition_submit_time,
             each.get_honor_competition_is_checked_display])
    for each in patents:
        result.append(
            ["B-%d" % each.id, each.honor_patent_name, each.honor_patent_date_auth, each.honor_patent_submit_time,
             each.get_honor_patent_is_checked_display])
    for each in scholarships:
        result.append(
            ["C-%d" % each.id, each.honor_scholarship_name, each.honor_scholarship_year, each.honor_scholarship_submit_time,
             each.get_honor_scholarship_is_checked_display])
    for each in paper_magazines:
        result.append(
            ["D-%d" % each.id, "%s——%s" % (each.honor_paper_magazine_magazinename,each.honor_paper_magazine_papername),
             each.honor_paper_magazine_date_publish, each.honor_paper_magazine_submit_time, each.get_honor_paper_magazine_is_checked_display])
    for each in paper_meetings:
        result.append(
            ["E-%d" % each.id, "%s——%s" % (each.honor_paper_meeting_meetingname,each.honor_paper_meeting_papername), each.honor_paper_meeting_date, each.honor_paper_meeting_submit_time,
             each.get_honor_paper_meeting_is_checked_display()])
    for each in experiences:
        result.append(
            ["F-%d" % each.id, each.honor_experience_name, each.honor_experience_end, each.honor_experience_submit_time,
             each.get_honor_experience_is_checked_display])


    return render(request, "student_center_status.html", {'userrelname': userrelname,
                                                          'result': result,
                                                          });





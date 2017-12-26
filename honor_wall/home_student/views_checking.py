from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from home.models import Honor_competition,Honor_patent,Honor_paper_magazine,Honor_paper_meeting,Honor_scholarship,Honor_experience
import os
import re
import time
from django.conf import settings
from django.core.files.base import ContentFile
from django.core.files.storage import default_storage


@login_required
def checking(request):
    userrelname = request.session.get('username', '')
    return render(request,"student_center_checking.html",{'userrelname':userrelname});


@login_required
#竞赛审核数据上传
def contest(request):
    userid=request.session.get('userid')
    #证明文件上传到服务器项目目录，其他信息写入服务器数据库
    file = request.FILES.get('file')  # 从POST中获取证明文件
    if file is None:
        return HttpResponse("证明材料不能为空")
    elif file.size < 20480000:  # 修改用户照片
        file.name = re.sub(".+\.", repr(int(time.time())) + ".", file.name)  # 将文件名改为当前时间戳的整数部分

        #文件要在项目目录中存储的位置
        dir=(os.path.abspath(os.path.join(os.path.dirname('settings.py'),os.path.pardir)) + "/honor_wall/user/student/provefile/contest/"+userid).replace("\\", "/")

        print (dir)
        if(os.path.exists(dir)):
            print("exists")
            Honor_competition.objects.create(student_id=userid, competition_name=request.POST.get('name'),
                                             competition_competition_level=request.POST.get('grade'),
                                             competition_level=request.POST.get('level'),
                                             honor_competition_get_time=request.POST.get('time'),
                                             honor_competition_teacher=request.POST.get('teacher'),
                                             honor_competition_award=request.POST.get('company'),
                                             honor_competition_message=request.POST.get('info'),
                                             honor_competition_confirm_file=file.name)
            path = default_storage.save(dir+"/"+file.name,ContentFile(file.read()))  # 存储文件第一步，这里要设置文件在项目目录里的路径
            print ("path:" + path)
        else:
            print("makedir")
            os.makedirs(dir)
            Honor_competition.objects.create(student_id=userid, competition_name=request.POST.get('name'),
                                             competition_competition_level=request.POST.get('grade'),
                                             competition_level=request.POST.get('level'),
                                             honor_competition_get_time=request.POST.get('time'),
                                             honor_competition_teacher=request.POST.get('teacher'),
                                             honor_competition_award=request.POST.get('company'),
                                             honor_competition_message=request.POST.get('info'),
                                             honor_competition_confirm_file=file.name)
            path = default_storage.save(dir+"/"+file.name,ContentFile(file.read()))  # 存储文件第一步，这里要设置文件在项目目录里的路径
            print ("path:"+path)
        print ("修改成功！")
    else:
        print("文件过大，不要超过2M")
    return HttpResponseRedirect("/student/checking")







@login_required
#期刊论文审核数据上传
def magazine(request):
    userid=request.session.get('userid')
    #证明文件上传到服务器项目目录，其他信息写入服务器数据库
    file = request.FILES.get('file')  # 从POST中获取证明文件
    if file is None:
        return HttpResponse("证明材料不能为空")
    elif file.size < 20480000:  # 修改用户照片
        file.name=re.sub(".+\.",repr(int(time.time()))+".",file.name)#将文件名改为当前时间戳的整数部分
        dir=(os.path.abspath(os.path.join(os.path.dirname('settings.py'),os.path.pardir)) + "/honor_wall/user/student/provefile/magazine/"+userid).replace("\\", "/")
        print (dir)
        if(os.path.exists(dir)):
            print("exists")
            Honor_paper_magazine.objects.create(student_id=userid, honor_paper_magazine_type=request.POST.get('type'),
                                                honor_paper_magazine_magazinename=request.POST.get('magainename'),
                                                honor_paper_magazine_papername=request.POST.get('papername'),
                                                honor_paper_magazine_status=request.POST.get('status'),
                                                honor_paper_magazine_page_begin=request.POST.get('page'),
                                                honor_paper_magazine_ISBNcode=request.POST.get('ISBN'),
                                                honor_paper_magazine_page_number=request.POST.get('volume'),
                                                honor_paper_magazine_date_publish=request.POST.get('time'),
                                                honor_paper_magazine_is_firstauthor=request.POST.get('firstauthor'),
                                                honor_paper_magazine_quotetimes=request.POST.get('usetimes'),
                                                honor_paper_magazine_impactfactors=request.POST.get('impact'),
                                                honor_paper_magazine_searching=request.POST.get('usinginfo'),
                                                honor_paper_magazine_people=request.POST.get('otherauthors'),
                                                honor_paper_magazine_abstract=request.POST.get('quto'),
                                                honor_paper_magazine_confirm_file=file.name)
            path = default_storage.save(dir+"/"+file.name,ContentFile(file.read()))  # 存储文件第一步，这里要设置文件在项目目录里的路径
            print ("path:" + path)
        else:
            print("makedir")
            os.makedirs(dir)
            Honor_paper_magazine.objects.create(student_id=userid, honor_paper_magazine_type=request.POST.get('type'),
                                                honor_paper_magazine_magazinename=request.POST.get('magainename'),
                                                honor_paper_magazine_papername=request.POST.get('papername'),
                                                honor_paper_magazine_status=request.POST.get('status'),
                                                honor_paper_magazine_page_begin=request.POST.get('page'),
                                                honor_paper_magazine_ISBNcode=request.POST.get('ISBN'),
                                                honor_paper_magazine_page_number=request.POST.get('volume'),
                                                honor_paper_magazine_date_publish=request.POST.get('time'),
                                                honor_paper_magazine_is_firstauthor=request.POST.get('firstauthor'),
                                                honor_paper_magazine_quotetimes=request.POST.get('usetimes'),
                                                honor_paper_magazine_impactfactors=request.POST.get('impact'),
                                                honor_paper_magazine_searching=request.POST.get('usinginfo'),
                                                honor_paper_magazine_people=request.POST.get('otherauthors'),
                                                honor_paper_magazine_abstract=request.POST.get('quto'),
                                                honor_paper_magazine_confirm_file=file.name)
            path = default_storage.save(dir+"/"+file.name,ContentFile(file.read()))  # 存储文件第一步，这里要设置文件在项目目录里的路径
            print ("path:"+path)
        print ("修改成功！")
    else:
        print("文件过大，不要超过2M")
    return HttpResponseRedirect("/student/checking")




@login_required
#会议论文审核数据上传
def meeting(request):
    userid = request.session.get('userid')
    # 证明文件上传到服务器项目目录，其他信息写入服务器数据库
    file = request.FILES.get('file')  # 从POST中获取证明文件
    if file is None:
        return HttpResponse("证明材料不能为空")
    elif file.size < 20480000:  # 修改用户照片
        file.name = re.sub(".+\.", repr(int(time.time())) + ".", file.name)  # 将文件名改为当前时间戳的整数部分
        dir = (os.path.abspath(os.path.join(os.path.dirname('settings.py'),
                                            os.path.pardir)) + "/honor_wall/user/student/provefile/meeting/" + userid).replace(
            "\\", "/")
        print (dir)
        if (os.path.exists(dir)):
            print("exists")
            Honor_paper_meeting.objects.create(student_id=userid, honor_paper_meeting_type=request.POST.get('type'),
                                                honor_paper_meeting_meetingname=request.POST.get('meetingname'),
                                                honor_paper_meeting_papername=request.POST.get('papername'),
                                                honor_paper_meeting_address=request.POST.get('address'),
                                                honor_paper_meeting_date=request.POST.get('date'),
                                                honor_paper_meeting_is_firstauthor=request.POST.get('firstauthor'),
                                                honor_paper_meeting_people=request.POST.get('otherauthors'),
                                                honor_paper_meeting_confirm_file=file.name)
            path = default_storage.save(dir + "/" + file.name, ContentFile(file.read()))  # 存储文件第一步，这里要设置文件在项目目录里的路径
            print ("path:" + path)
        else:
            print("makedir")
            os.makedirs(dir)
            Honor_paper_meeting.objects.create(student_id=userid, honor_paper_meeting_type=request.POST.get('type'),
                                               honor_paper_meeting_meetingname=request.POST.get('meetingname'),
                                               honor_paper_meeting_papername=request.POST.get('papername'),
                                               honor_paper_meeting_address=request.POST.get('address'),
                                               honor_paper_meeting_date=request.POST.get('date'),
                                               honor_paper_meeting_is_firstauthor=request.POST.get('firstauthor'),
                                               honor_paper_meeting_people=request.POST.get('otherauthors'),
                                               honor_paper_meeting_confirm_file=file.name)
            path = default_storage.save(dir + "/" + file.name, ContentFile(file.read()))  # 存储文件第一步，这里要设置文件在项目目录里的路径
            print ("path:" + path)
        print ("修改成功！")
    else:
        print("文件过大，不要超过2M")
    return HttpResponseRedirect("/student/checking")




@login_required
#专利审核数据上传
def patent(request):
    userid = request.session.get('userid')
    # 证明文件上传到服务器项目目录，其他信息写入服务器数据库
    file = request.FILES.get('file')  # 从POST中获取证明文件
    if file is None:
        return HttpResponse("证明材料不能为空")
    elif file.size < 20480000:  # 修改用户照片
        file.name = re.sub(".+\.", repr(int(time.time())) + ".", file.name)  # 将文件名改为当前时间戳的整数部分
        dir = (os.path.abspath(os.path.join(os.path.dirname('settings.py'),
                                            os.path.pardir)) + "/honor_wall/user/student/provefile/patent/" + userid).replace(
            "\\", "/")
        print (dir)
        if (os.path.exists(dir)):
            print("exists")
            Honor_patent.objects.create(student_id=userid, honor_patent_type=request.POST.get('type'),
                                        honor_patent_name=request.POST.get('name'),
                                        honor_patent_number=request.POST.get('number'),
                                        honor_patent_date_apply=request.POST.get('applydate'),
                                        honor_patent_date_auth=request.POST.get('passdate'),
                                        honor_patent_legalstatus=request.POST.get('status'),
                                        honor_patent_firstman=request.POST.get('firstauthor'),
                                        honor_patent_people=request.POST.get('otherauthors'),
                                        honor_patent_confirm_file=file.name)
            path = default_storage.save(dir + "/" + file.name, ContentFile(file.read()))  # 存储文件第一步，这里要设置文件在项目目录里的路径
            print ("path:" + path)
        else:
            print("makedir")
            os.makedirs(dir)
            Honor_patent.objects.create(student_id=userid, honor_patent_type=request.POST.get('type'),
                                        honor_patent_name=request.POST.get('name'),
                                        honor_patent_number=request.POST.get('number'),
                                        honor_patent_date_apply=request.POST.get('applydate'),
                                        honor_patent_date_auth=request.POST.get('passdate'),
                                        honor_patent_legalstatus=request.POST.get('status'),
                                        honor_patent_firstman=request.POST.get('firstauthor'),
                                        honor_patent_people=request.POST.get('otherauthors'),
                                        honor_patent_confirm_file=file.name)
            path = default_storage.save(dir + "/" + file.name, ContentFile(file.read()))  # 存储文件第一步，这里要设置文件在项目目录里的路径
            print ("path:" + path)
        print ("修改成功！")
    else:
        print("文件过大，不要超过2M")
    return HttpResponseRedirect("/student/checking")



@login_required
#奖学金审核数据上传
def scholarship(request):
    userid=request.session.get('userid')
    # 证明文件上传到服务器项目目录，其他信息写入服务器数据库
    file = request.FILES.get('file')  # 从POST中获取证明文件
    if file is None:
        return HttpResponse("证明材料不能为空")
    elif file.size < 20480000:  # 修改用户照片
        file.name = re.sub(".+\.", repr(int(time.time())) + ".", file.name)  # 将文件名改为当前时间戳的整数部分
        dir = (os.path.abspath(os.path.join(os.path.dirname('settings.py'),
                                            os.path.pardir)) + "/honor_wall/user/student/provefile/scholarship/" + userid).replace(
            "\\", "/")
        print (dir)
        if (os.path.exists(dir)):
            print("exists")
            Honor_scholarship.objects.create(student_id=userid,
                                             honor_scholarship_name=request.POST.get('name'),
                                             honor_scholarship_year=request.POST.get('year'),
                                             honor_scholarship_moneyperyear=request.POST.get('number'),
                                             honor_scholarship_authority=request.POST.get('company'),
                                             honor_scholarship_confirm_file=file.name)
            path = default_storage.save(dir + "/" + file.name, ContentFile(file.read()))  # 存储文件第一步，这里要设置文件在项目目录里的路径
            print ("path:" + path)
        else:
            print("makedir")
            os.makedirs(dir)
            Honor_scholarship.objects.create(student_id=userid,
                                             honor_scholarship_name=request.POST.get('name'),
                                             honor_scholarship_year=request.POST.get('year'),
                                             honor_scholarship_moneyperyear=request.POST.get('number'),
                                             honor_scholarship_authority=request.POST.get('company'),
                                             honor_scholarship_confirm_file=file.name)
            path = default_storage.save(dir + "/" + file.name, ContentFile(file.read()))  # 存储文件第一步，这里要设置文件在项目目录里的路径
            print ("path:" + path)
        print ("修改成功！")
    else:
        print("文件过大，不要超过2M")
    return HttpResponseRedirect("/student/checking")




@login_required
#社会经历审核数据上传
def experience(request):
    userid = request.session.get('userid')
    # 证明文件上传到服务器项目目录，其他信息写入服务器数据库
    file = request.FILES.get('file')  # 从POST中获取证明文件
    if file is None:
        return HttpResponse("证明材料不能为空")
    elif file.size < 20480000:  # 修改用户照片
        file.name = re.sub(".+\.", repr(int(time.time())) + ".", file.name)  # 将文件名改为当前时间戳的整数部分
        dir = (os.path.abspath(os.path.join(os.path.dirname('settings.py'),
                                            os.path.pardir)) + "/honor_wall/user/student/provefile/experience/" + userid).replace(
            "\\", "/")
        print (dir)
        if (os.path.exists(dir)):
            print("exists")
            Honor_experience.objects.create(student_id=userid,
                                            honor_experience_name=request.POST.get('name'),
                                            honor_experience_authority=request.POST.get('company'),
                                            honor_experience_start=request.POST.get('startdate'),
                                            honor_experience_end=request.POST.get('enddate'),
                                            honor_experience_note=request.POST.get('info'),
                                            honor_experience_confirm_file=file.name)
            path = default_storage.save(dir + "/" + file.name, ContentFile(file.read()))  # 存储文件第一步，这里要设置文件在项目目录里的路径
            print ("path:" + path)
        else:
            print("makedir")
            os.makedirs(dir)
            Honor_experience.objects.create(student_id=userid,
                                            honor_experience_name=request.POST.get('name'),
                                            honor_experience_authority=request.POST.get('company'),
                                            honor_experience_start=request.POST.get('startdate'),
                                            honor_experience_end=request.POST.get('enddate'),
                                            honor_experience_note=request.POST.get('info'),
                                            honor_experience_confirm_file=file.name)
            path = default_storage.save(dir + "/" + file.name, ContentFile(file.read()))  # 存储文件第一步，这里要设置文件在项目目录里的路径
            print ("path:" + path)
        print ("修改成功！")
    else:
        print("文件过大，不要超过2M")
    return HttpResponseRedirect("/student/checking")
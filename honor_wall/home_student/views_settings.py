from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from home.models import Student_message_editable,Student_honorwall#导入数据表
from django.http import HttpResponse,HttpResponseRedirect
import os
from django.conf import settings
from django.core.files.base import ContentFile
from django.core.files.storage import default_storage

@login_required
def settings(request):
    try:
        # 获取学生的姓名，用来显示当前用户
        userrelname = request.session.get('username', '')
        # 从session中读取学生的学号，用来在表中查询该学生的信息
        userid = request.session.get('userid')
        # 获取表中的某一条数据，用：表名.objects.get(查询条件（等号左边是列名，右边是具体值）)
        student_message_editable = Student_message_editable.objects.get(student_id=userid)
    except Exception:
        return render(request, "student_center_settings.html")
    # 向前端页面将当前函数中所有的变量传到html中，直接用render_to_response()和locals()
    return render(request, "student_center_settings.html", locals())

@login_required
def upload(request):
    if request.method=="POST":
        userid = request.session.get('userid')
        student_message_editable = Student_message_editable.objects.get(student_id=userid)
        student_message_editable.student_nickname=request.POST.get('nickname')
        student_message_editable.student_sign=request.POST.get('sign')
        if(request.POST.get('name_status')=="on"):
            student_message_editable.student_name_conceal=1;
        else:
            student_message_editable.student_name_conceal=0;
        if (request.POST.get('sex_status') == "on"):
            student_message_editable.student_sex_conceal = 1;
        else:
            student_message_editable.student_sex_conceal = 0;
        if (request.POST.get('phone_status') == "on"):
            student_message_editable.student_contact_conceal = 1;
        else:
            student_message_editable.student_contact_conceal = 0;
        student_message_editable.save()


        # 传用户荣誉墙头像
        stu_photo = request.FILES.get('head')  # 从POST中获取该文件
        if stu_photo is None:
            print("修改成功，未修改照片")
        elif stu_photo.size < 20480000:  # 修改用户照片
            stu_photo.name = userid + ".jpg"  # 将文件名改为“学号.jpg”
            stu_photo_path = (os.path.abspath(os.path.join(os.path.dirname('settings.py'),
                                                           os.path.pardir)) + "/honor_wall/user/student/head/" + stu_photo.name).replace(
                "\\", "/")  # 项目目录中学生旧的照片的绝对路径
            # 1、 os.path.abspath(os.path.join(os.path.dirname('settings.py'),os.path.pardir))用于获取项目所在目录的绝对路径
            # 2、 后面加上的/honor_wall/user/student/photo/+ stu_photo.name是该文件在项目中的绝对路径
            # 3、 .replace("\\", "/")是为了把stu_photo_path中的所有“\”替换为“/”，这样得到的文件路径在windows和linux中普适
            try:
                os.remove(stu_photo_path)  # 删除项目目录中的旧的照片
            except FileNotFoundError:
                print ("没有旧照片")
            student_honorwall=Student_honorwall.objects.get(student_id=userid)
            student_honorwall.student_portrait = stu_photo  # 传上来新的照片
            student_honorwall.save()
            print ("修改成功！")
        else:
            print("文件过大，不要超过2M")
    return HttpResponseRedirect("/student/settings")

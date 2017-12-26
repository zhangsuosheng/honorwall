from django.contrib.auth.decorators import login_required
from django.shortcuts import render,render_to_response
from django.http import HttpResponse,HttpResponseRedirect
import os
from django.conf import settings
from django.core.files.base import ContentFile
from django.core.files.storage import default_storage

#要读取home这个APP下的models.py文件，引入其中的Student_message_uneditable和Student_message_editable两张数据表
from home.models import Student_message_uneditable,Student_message_editable

@login_required
def index(request):
    # 从session中读取学生的学号，用来在表中查询该学生的信息
    userid = request.session.get('userid')

    # 读取学生的姓名，用于导航栏中显示当前用户
    userrelname=request.session.get('username')
    # 获取表中的某一条数据，用：表名.objects.get(查询条件（等号左边是列名，右边是具体值）)
    try:
        student_message_uneditable = Student_message_uneditable.objects.get(student_id=userid)
        student_message_editable = Student_message_editable.objects.get(student_id=userid)
    except (Student_message_editable.DoesNotExist,Student_message_uneditable.DoesNotExist) as e:
        return render(request, "student_center.html")
    #向前端页面将当前函数中所有的变量传到html中，直接用render_to_response()和locals()
    return render(request,"student_center.html",locals())


@login_required
def upload(request):
    # 从session中读取学生的学号，用来在表中查询该学生的信息
    userid = request.session.get('userid')
    if request.method == "POST":
        print ("this is POST")
        student_message_editable = Student_message_editable.objects.get(student=userid)
        print(userid)
        student_message_editable.student_birthday = request.POST.get('birthday')
        student_message_editable.student_address = request.POST.get('address')
        student_message_editable.student_birthplace = request.POST.get('birthplace')
        student_message_editable.student_political_state = request.POST.get('politicalstatus')
        student_message_editable.student_people = request.POST.get('nation')
        student_message_editable.student_document_type = request.POST.get('idcardtype')
        student_message_editable.student_document_number = request.POST.get('idcardnum')
        student_message_editable.student_phone_number = request.POST.get('phone')
        student_message_editable.student_email = request.POST.get('email')
        # 传文件
        stu_photo = request.FILES.get('photo')  # 从POST中获取该文件
        if stu_photo is None:
            print("修改成功，未修改照片")
        elif stu_photo.size < 20480000:  # 修改用户照片
            stu_photo.name = userid + ".jpg"  # 将文件名改为“学号.jpg”
            stu_photo_path = (os.path.abspath(os.path.join(os.path.dirname('settings.py'),
                                                           os.path.pardir)) + "/honor_wall/user/student/photo/" + stu_photo.name).replace(
                "\\", "/")  # 项目目录中学生旧的照片的绝对路径
            print(stu_photo_path)
            # 1、 os.path.abspath(os.path.join(os.path.dirname('settings.py'),os.path.pardir))用于获取项目所在目录的绝对路径
            # 2、 后面加上的/honor_wall/user/student/photo/+ stu_photo.name是该文件在项目中的绝对路径
            # 3、 .replace("\\", "/")是为了把stu_photo_path中的所有“\”替换为“/”，这样得到的文件路径在windows和linux中普适
            try:
                os.remove(stu_photo_path)  # 删除项目目录中的旧的照片
            except FileNotFoundError:
                print ("没有旧照片")
            student_message_editable.student_photo = stu_photo  # 传上来新的照片
            print ("修改成功！")
        else:
            print("文件过大，不要超过2M")
        student_message_editable.save()
        return HttpResponseRedirect("/student")

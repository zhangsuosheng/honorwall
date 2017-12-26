from django.core.paginator import Paginator,EmptyPage,PageNotAnInteger
from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from home.models import Student_honorwall#导入数据表
from home.models import Honor_competition,Honor_paper_magazine,Honor_paper_meeting,Honor_patent,Honor_scholarship,Honor_experience

@login_required
def honor(request):
    try:
        userrelname = request.session.get('username', '')
        userid = request.session.get('userid')
        student_honorwall = Student_honorwall.objects.get(student_id=userid)
        honor_competition = Honor_competition.objects.all().filter(student_id=userid)
        honor_magazine = Honor_paper_magazine.objects.all().filter(student_id=userid)
        honor_meeting = Honor_paper_meeting.objects.all().filter(student_id=userid)
        honor_patent = Honor_patent.objects.all().filter(student_id=userid)
        honor_scholarship = Honor_scholarship.objects.all().filter(student_id=userid)
        honor_experience = Honor_experience.objects.all().filter(student_id=userid)
    except Exception:
        return render(request, "student_center_honor.html")
    # 向前端页面将当前函数中所有的变量传到html中，直接用render_to_response()和locals()
    #return render(request,'student_center_honor.html',{'student_honorwall':student_honorwall,'userrelname':userrelname})
    return render(request, "student_center_honor.html", locals())
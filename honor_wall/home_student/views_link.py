
from django.shortcuts import render
from home.models import Student_message_uneditable,Student_message_editable,Links,Honor_competition,Honor_patent,Honor_paper_meeting,Honor_paper_magazine,Honor_experience,Honor_scholarship
from django.http import HttpResponse,HttpResponseRedirect

from home_student import aes

def linkcheck(request,miwen):
    aes_machine = aes.prpcrypt('xjtuxjtuxjtuxjtu')  # 密钥：xjtuxjtuxjtuxjtu
    mingwen = aes_machine.decrypt(miwen)
    try:
        userlink = Links.objects.get(student=mingwen)
    except Links.DoesNotExist:
        return HttpResponse(u'您所访问的连接不存在或可用次数已用完')
    if userlink.use_times<1:
        userlink.delete()
        return HttpResponse(u'您所访问的连接不存在或可用次数已用完')
    userlink.use_times = userlink.use_times - 1
    userlink.save()
    userid=userlink.student_id
    student_message_editable=Student_message_editable.objects.get(student_id=userid)
    competitions=Honor_competition.objects.filter(student_id=userid)
    patents=Honor_patent.objects.filter(student_id=userid)
    paper_magazines=Honor_paper_magazine.objects.filter(student_id=userid)
    paper_meetings=Honor_paper_meeting.objects.filter(student_id=userid)
    scholarships=Honor_scholarship.objects.filter(student_id=userid)
    experiences=Honor_experience.objects.filter(student_id=userid)
    return render(request,"my_honorwall.html",locals())
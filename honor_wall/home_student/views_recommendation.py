from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from home.models import Recommendation

@login_required
def recommendation(request):
    userid = request.session.get('userid')
    userrelname = request.session.get('username', '')
    if request.method=="POST":
        if (request.POST.get('paper') == "on"):
            Recommendation.objects.create(student_id=userid, company=request.POST.get('company'),
                                          position=request.POST.get('position'), paper=1)
        else:
            Recommendation.objects.create(student_id=userid, company=request.POST.get('company'),
                                          position=request.POST.get('position'), paper=0)
        return HttpResponseRedirect("/student/recommendation")

    else:
        userrelname = request.session.get('username', '')
        apply_record=Recommendation.objects.all().filter(student_id=userid)
        return render(request,"student_center_recommendation.html",locals())
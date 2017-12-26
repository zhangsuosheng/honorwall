
from django.conf.urls import url
from home_teacher import views,views_checking,views_studentchange,views_message

urlpatterns = [
    #这是跳转用的
    url(r'^$', views.index,name="teacher_center"),
    url(r'^already$',views.already),
    url(r'^checking$', views.checking),#审核页
    url(r'^checkingwhere=([1-7])$',views.checking_where),#审核页
    url(r'^competitionid=([0-9]*)(already)?$',views.competition),#竞赛审核详细
    url(r'^competitionadd$',views.competitionadd),#奖项添加
    url(r'^experienceid=([0-9]*)(already)?$',views.experience),#社会经历审核详细
    url(r'^letter_checked$',views.letter_checked),#推荐信审核详细
    url(r'^lettergenerate$',views.lettergenerate),#推荐信生成详细
    url(r'^magazinepaperid=([0-9]*)(already)?$',views.magazinepaper),#期刊论文审核详细
    url(r'^meetingpaperid=([0-9]*)(already)?$',views.meetingpaper),#会议论文审核详细
    url(r'^message_out$',views.message_out),#信息发布页
    url(r'^message_outed$',views.message_outed),#已发布信息页
    url(r'^patentid=([0-9]*)(already)?$',views.patent),#专利审核详细
    url(r'^prizeid=([0-9]*)(already)?$',views.prize),#奖学金审核详细
    url(r'^setting$',views.setting),#设置页
    url(r'^studentmessagechange$',views.studentmessagechange),#学生信息查询
    url(r'^competitionid=([0-9]*)(message)$',views.competition),#竞赛审核详细
    url(r'^experienceid=([0-9]*)(message)$', views.experience),  # 社会经历审核详细
    url(r'^magazinepaperid=([0-9]*)(message)$', views.magazinepaper),  # 期刊论文审核详细
    url(r'^meetingpaperid=([0-9]*)(message)$', views.meetingpaper),  # 会议论文审核详细
    url(r'^prizeid=([0-9]*)(message)$', views.prize),  # 奖学金审核详细
    url(r'^patentid=([0-9]*)(message)$', views.patent),  # 专利审核详细

    #这是自定义的
    #views_checking文件中审核界面涉及到的函数跳转
    url(r'^checking/mytable_competition/select=(.*)page=([0-9]*)$',views_checking.checking_mytable_competition),#竞赛信息表的动态刷新
    url(r'^checking/mytable_already/select=(.*)page=([0-9]*)$',views_checking.checking_mytable_already),#已审核信息表的动态刷新
    url(r'^checking/mytable_magazinepaper/page=([0-9]*)$',views_checking.checking_mytable_magazinepaper),#期刊论文信息表的动态刷新
    url(r'^checking/mytable_meetingpaper/page=([0-9]*)$',views_checking.checking_mytable_meetingpaper),#会议论文信息表的动态刷新
    url(r'^checking/mytable_patent/page=([0-9]*)$', views_checking.checking_mytable_patent),  # 专利信息表的动态刷新
    url(r'^checking/mytable_prize/page=([0-9]*)$', views_checking.checking_mytable_prize),  # 奖学金信息表的动态刷新
    url(r'^checking/mytable_experience/page=([0-9]*)$', views_checking.checking_mytable_experience),  # 社会经历信息表的动态刷新
    url(r'^competitionsuccessid=([0-9]*)(already)?$',views_checking.competition_success),#竞赛审核通过
    url(r'^competitionfailid=([0-9]*)(already)?$', views_checking.competition_fail),  # 竞赛审核未通过
    url(r'^competitionnextid=([0-9]*)(already)?$', views_checking.competition_next),  # 竞赛审核下一个
    url(r'^meetingpapersuccessid=([0-9])*(already)?$', views_checking.meetingpaper_success),  # 期刊论文通过
    url(r'^meetingpaperfailid=([0-9]*)(already)?$', views_checking.meetingpaper_fail),  # 期刊论文未通过
    url(r'^meetingpapernextid=([0-9]*)(already)?$', views_checking.meetingpaper_next),  # 期刊论文下一个
    url(r'^magazinepapersuccessid=([0-9]*)(already)?$',views_checking.magazinepaper_success),#会议论文通过
    url(r'^magazinepaperfailid=([0-9]*)(already)?$', views_checking.magazinepaper_fail),  # 会议论文未通过
    url(r'^magazinepapernextid=([0-9]*)(already)?$', views_checking.magazinepaper_next),  # 会议论文下一个
    url(r'^patentsuccessid=([0-9]*)(already)?$',views_checking.patent_success),#专利通过
    url(r'^patentfailid=([0-9]*)(already)?$', views_checking.patent_fail),  # 专利未通过
    url(r'^patentnextid=([0-9]*)(already)?$', views_checking.patent_next),  # 专利下一个
    url(r'^prizesuccessid=([0-9]*)(already)?$',views_checking.prize_success),#奖学金通过
    url(r'^prizefailid=([0-9]*)(already)?$', views_checking.prize_fail),  # 奖学金未通过
    url(r'^prizenextid=([0-9]*)(already)?$', views_checking.prize_next),  # 奖学金下一个
    url(r'^experiencesuccessid=([0-9]*)(already)?$',views_checking.experience_success),#社会经历通过
    url(r'^experiencefailid=([0-9]*)(already)?$', views_checking.experience_fail),  # 社会经历未通过
    url(r'^experiencenextid=([0-9]*)(already)?$', views_checking.experience_next),  # 社会经历下一个


    #views_studentchange.py中涉及到的
    url(r'^search$',views_studentchange.search),#学生查询
    url(r'^studentmessagechange_2/id=([0-9]*)$',views_studentchange.studentmessagechange_2),#学生信息修改
    url(r'^save$',views_studentchange.save),#学生信息修改
    url(r'^submit$',views_studentchange.submit),#竞赛奖项存储
    url(r'^getcompetition',views_studentchange.getcompetition),#获取所有竞赛奖项信息
    url(r'^delete',views_studentchange.delete),#竞赛信息删除

    #views_message.py中涉及到的
    url(r'^message_out_2$',views_message.message_out_2),#信息发布
    url(r'^re_message_outid=([0-9]*)$',views_message.re_message),#编辑信息跳转
    url(r'^article_get$',views_message.article_get),#文章信息获取
    url(r'article_delete',views_message.delete),#文章删除/撤销
    url(r'article_change',views_message.change),#文章修改

]
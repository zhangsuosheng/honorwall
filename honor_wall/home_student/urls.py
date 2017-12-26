
from django.conf.urls import url
from home_student import views,views_myhonorwall,views_index,views_settings,views_honor,views_recommendation,views_checking,views_resume

urlpatterns = [

    #
    # url(r'^$', views_index.index, name="student_center"),
    # url(r'^honor$', views.honor, name="student_center_honor"),
    # url(r'^resume$', views.resume, name="student_center_resume"),
    # url(r'^recommendation$', views.recommendation, name="student_center_recommendation"),
    # url(r'^checking$', views.checking, name="student_center_checking"),
    # url(r'^status$', views.status, name="student_center_status"),
    # url(r'^settings$', views.settings, name="student_center_settings"),
    # url(r'^my_honorwall/$', views_myhonorwall.myhonorwall, name="student_center_honorwall"),

    url(r'^dispage/(\d+)/',views.dispage, name="dispage"),#测试用

    url(r'^$', views_index.index, name="student_center"),
    url(r'^honor$', views_honor.honor, name="student_center_honor"),
    url(r'^resume$', views_resume.resume, name="student_center_resume"),
    url(r'^recommendation$', views_recommendation.recommendation, name="student_center_recommendation"),
    url(r'^checking$', views_checking.checking, name="student_center_checking"),
    url(r'^status$', views.status, name="student_center_status"),
    url(r'^settings$', views_settings.settings, name="student_center_settings"),
    url(r'^my_honorwall$', views.honor, name="student_center_honorwall"),

    url(r'^upload$',views_index.upload,name="student_center_upload"),
    url(r'^settings/upload$',views_settings.upload, name="student_center_settings_upload"),
    url(r'^checking/contest$',views_checking.contest),
    url(r'^checking/magazine$',views_checking.magazine),
    url(r'^checking/meeting$',views_checking.meeting),
    url(r'^checking/patent$',views_checking.patent),
    url(r'^checking/scholarship$',views_checking.scholarship),
    url(r'^checking/experience$',views_checking.experience),
    url(r'^resume/generate_resume$',views_resume.generate_resume,name="student_center_resume_generate_resume"),
    url(r'^resume/generate_link$',views_resume.generate_link,name="generate_link")
]



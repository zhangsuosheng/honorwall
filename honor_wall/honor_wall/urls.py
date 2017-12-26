"""honor_wall URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function vie、、、、、】、、、、、、、、、、、、、、、、、、、、、、、、、、、、、、、、、、、、、、、、、、、、、、、、、、、、、、、、、、、、、、、、、、、、、、、、、、、、、、、、、、、、、、、、、、、、、、、、、、、、、、、、、、、、、、、、、、、、、、、、、、、、、、、、、、、、、、、、、、、、、、、、、、、、、、、、、、、、、、、、、、、、、、、、、、、、、、、、、、、、、、、、、、、、、、、、、、、、、、、、、、、、、、、、、、、、、、、、、、、、、、、、、、、、、、、、、、、、、、、、、、、、、、、、、、、、、、、、、、、、、、、、、、


、、



ws
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
from home import views
from django.views.decorators.cache import cache_page

from django.conf import settings
from django.conf.urls.static import static

#张所晟加的，用来加密连接访问
from home_student import views_link

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', views.index, name="index"),
    url(r'^student/', include('home_student.urls')),
    url(r'^teacher/', include('home_teacher.urls')),

    url(r'^logout/$', views.logout, name="logout"),
    url(r'^login/$', views.student_login, name="login"),
    url(r'^score/(?P<score_type>.+)/$', cache_page(60*5)(views.score_data)),

    url(r'^inform/paper=(?P<id>[0-9]*)/$', views.inform_page),
    url(r'^inform?(?P<page>[0-9]*)/$', views.inform),
    url(r'^award/(?P<award_type>\D+)?(?P<page>[0-9]*)/$', views.award),

    #张所晟加的，使用加密连接访问学生个人主页
    url(r'^link/(?P<miwen>\w+)/$',views_link.linkcheck,name="linkcheck")





]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)#张所晟加的，配置图片访问路径

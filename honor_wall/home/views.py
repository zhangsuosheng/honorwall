from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.shortcuts import render
from django.contrib import auth
from django.contrib.auth.models import User

from django.http import HttpResponse, HttpResponseRedirect
# from django.contrib.auth.decorators import login_required
from home.models import Student_honorwall, Message, Competition_type, Honor_paper_magazine,\
    Honor_paper_meeting, Honor_patent, Honor_competition
# Create your views here.


# 返回主页

def index(request):
    # 主页积分榜显示，获取积分榜的数据
    score_all = Student_honorwall.objects.all()
    message = []
    for i in score_all.values("student__student_name",
                              "student_competition_score",
                              "student_paper_score",
                              "student_patent_score",
                              "student_scholarship_score",
                              "student_experience_score",
                              "student__student_message_editable__student_name_conceal",
                              "student__student_message_editable__student_nickname",
                              ):
        student_score = i["student_competition_score"] + \
                        i["student_paper_score"] + \
                        i["student_patent_score"] + \
                        i["student_scholarship_score"] + \
                        i["student_experience_score"]
        if i["student__student_message_editable__student_name_conceal"]:
            message.append(["%s(昵称)" % i["student__student_message_editable__student_nickname"], student_score])
        else:
            message.append([i["student__student_name"], student_score])
    # 取总积分排名前10名
    message = sorted(message, key=lambda x: x[1], reverse=1)[:10]
    times = 0
    # 给每一条用户信息加上排名
    for each in message:
        times += 1
        each.append(times)

    # 主页通知显示，取前5条通知(按时间排序)
    informs = Message.objects.all().order_by("-message_date")[:5]


    # 主页竞赛显示，从老师添加的竞赛表中获取竞赛（按添加时间排序）
    competition_list_unsolved = [i.competition_name for i in Competition_type.objects.all().filter(competition_class="竞赛").order_by("competition_id")[:20]]
    # 从竞赛表中去除重复元素（竞赛名称）后取5个竞赛显示
    competition_list_solved = sorted(set(competition_list_unsolved), key=competition_list_unsolved.index)[:5]

    # 主页论文显示,共显示六条信息，三条期刊论文，三条会议论文
    paper_magazine = Honor_paper_magazine.objects.all().filter(honor_paper_magazine_is_checked=1).order_by("honor_paper_magazine_check_time")[:3]
    paper_meeting = Honor_paper_meeting.objects.all().filter(honor_paper_meeting_is_checked=1).order_by("honor_paper_meeting_check_time")[:3]

    # 主页专利显示，共显示六条信息
    patent_list = Honor_patent.objects.all().filter(honor_patent_is_checked=1).order_by("honor_patent_check_time")
    username = request.session.get('username', '')
    user_type = request.session.get('usertype', -1)
    # return HttpResponse(user_type)
    return render(request, "index.html", {"username": username,
                                          "user_type": user_type,
                                          "name_score_times": message,
                                          "informs": informs,
                                          "competition_list": competition_list_solved,
                                          "paper_magazine": paper_magazine,
                                          "paper_meeting": paper_meeting,
                                          "patent_list": patent_list,
                                          })


# 积分榜路由

def score(request):
    score_all = Student_honorwall.objects.all()
    message = []
    for i in score_all.values("student__student_name",
                              "student_competition_score",
                              "student_paper_score",
                              "student_patent_score",
                              "student_scholarship_score",
                              "student_experience_score",
                              ):
        message.append([i["student__student_name"], i["student_competition_score"]])
    # 根据分数排序
    message = sorted(message, key=lambda x: x[1], reverse=1)
    times = 0
    # 给每一条用户信息加上排名号
    for each in message:
        times += 1
        each.append(times)
    username = request.session.get('username', '')
    user_type = request.session.get('usertype', -1)
    return render(request, "honor_score_range_all.html", {"username": username,
                                                          "user_type": user_type,
                                                          "message": message,
                                                          })


def score_data(request, score_type):

    message = []
    username = request.session.get('username', '')
    user_type = request.session.get('usertype', -1)
    if score_type == "all":
        score_all = Student_honorwall.objects.all()
        for i in score_all.values("student__student_name",
                                  "student_competition_score",
                                  "student_paper_score",
                                  "student_patent_score",
                                  "student_scholarship_score",
                                  "student_experience_score",
                                  ):
            student_score = i["student_competition_score"] +\
                  i["student_paper_score"] +\
                  i["student_patent_score"] +\
                  i["student_scholarship_score"] +\
                  i["student_experience_score"]
            message.append([i["student__student_name"], student_score])
        # 根据分数排序由大到小
        message = sorted(message, key=lambda x: x[1], reverse=1)
        times = 0
        # 给每一条用户信息加上排名号
        for each in message:
            times += 1
            each.append(times)
        return render(request, "honor_score_range_all.html", {"message": message, "score_type": "总积分", "username": username, "user_type": user_type})
    if score_type == "competition":
        score_all = Student_honorwall.objects.all().order_by("-student_competition_score")
        for i in score_all.values("student__student_name",
                                  "student_competition_score",
                                  "student_paper_score",
                                  "student_patent_score",
                                  "student_scholarship_score",
                                  "student_experience_score",
                                  ):
            student_score = i["student_competition_score"]
            message.append([i["student__student_name"], student_score])

        times = 0
        # 给每一条用户信息加上排名号
        for each in message:
            times += 1
            each.append(times)
        return render(request, "honor_score_range_all.html", {"message": message,
                                                              "score_type": "竞赛",
                                                              "username": username,
                                                              "user_type": user_type,
                                                              })
    if score_type == "paper":
        score_all = Student_honorwall.objects.all().order_by("-student_paper_score")
        for i in score_all.values("student__student_name",
                                  "student_competition_score",
                                  "student_paper_score",
                                  "student_patent_score",
                                  "student_scholarship_score",
                                  "student_experience_score",
                                  ):
            student_score = i["student_paper_score"]
            message.append([i["student__student_name"], student_score])

        times = 0
        # 给每一条用户信息加上排名号
        for each in message:
            times += 1
            each.append(times)
        return render(request, "honor_score_range_all.html", {"message": message,
                                                              "score_type": "论文",
                                                              "username": username,
                                                              "user_type": user_type,
                                                              })
    if score_type == "patent":
        score_all = Student_honorwall.objects.all().order_by("-student_patent_score")
        for i in score_all.values("student__student_name",
                                  "student_competition_score",
                                  "student_paper_score",
                                  "student_patent_score",
                                  "student_scholarship_score",
                                  "student_experience_score",
                                  ):
            student_score = i["student_patent_score"]
            message.append([i["student__student_name"], student_score])

        times = 0
        # 给每一条用户信息加上排名号
        for each in message:
            times += 1
            each.append(times)
        return render(request, "honor_score_range_all.html", {"message": message,
                                                              "score_type": "专利",
                                                              "username": username,
                                                              "user_type": user_type,
                                                              })
    if score_type == "scholarship":
        score_all = Student_honorwall.objects.all().order_by("-student_scholarship_score")
        for i in score_all.values("student__student_name",
                                  "student_competition_score",
                                  "student_paper_score",
                                  "student_patent_score",
                                  "student_scholarship_score",
                                  "student_experience_score",
                                  ):
            student_score = i["student_scholarship_score"]
            message.append([i["student__student_name"], student_score])

        times = 0
        # 给每一条用户信息加上排名号
        for each in message:
            times += 1
            each.append(times)
        return render(request, "honor_score_range_all.html", {"message": message,
                                                              "score_type": "奖学金",
                                                              "username": username,
                                                              "user_type": user_type,
                                                              })
    if score_type == "experience":
        score_all = Student_honorwall.objects.all().order_by("-student_experience_score")
        for i in score_all.values("student__student_name",
                                  "student_competition_score",
                                  "student_paper_score",
                                  "student_patent_score",
                                  "student_scholarship_score",
                                  "student_experience_score",
                                  ):
            student_score = i["student_experience_score"]
            message.append([i["student__student_name"], student_score])

        times = 0
        # 给每一条用户信息加上排名号
        for each in message:
            times += 1
            each.append(times)
        return render(request, "honor_score_range_all.html", {"message": message,
                                                              "score_type": "社会经历",
                                                              "username": username,
                                                              "user_type": user_type,
                                                              })


def award(request, award_type, page):
    if page == "":
        page = 1
    page = int(page)
    username = request.session.get('username','')
    user_type = request.session.get('usertype', -1)
    if award_type == "competition":
        # 从老师添加的竞赛表中获取竞赛（按添加时间排序）
        competition_namelist_unsolved = [i.competition_name for i in
                                     Competition_type.objects.all().order_by("competition_id").filter(competition_class="竞赛")]
        # 从竞赛列表中去除重复元素（竞赛名称）
        competition_namelist_solved = sorted(set(competition_namelist_unsolved), key=competition_namelist_unsolved.index)
        # 建立分页器 ，8个竞赛一组
        # 选出每个竞赛
        competition_award_people_list=[]
        for each_competition in competition_namelist_solved:
            # 选出这个竞赛的获奖中人与奖的关系
            person_award = Honor_competition.objects.all().filter(competition_name=each_competition,honor_competition_is_checked=1)

            # 找出该竞赛的所有奖项设置
            competition_award_list_unsolved=[i.competition_level for i in person_award]
            # 因为有许多人会在同一个奖下，故需要去除重复的奖项名称
            competition_award_list_solved = sorted(set(competition_award_list_unsolved),
                                                 key=competition_award_list_unsolved.index)
            competition_required_list = []
            for each_award in competition_award_list_solved:
                competition_required_list.append([each_award, [i.student.student_name for i in person_award.filter(competition_level=each_award)]])
            competition_award_people_list.append([each_competition, competition_required_list])


        paginator = Paginator(competition_award_people_list, 8)
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
        # 用于前端判断字典是否为空
        blank_list = []
        return render(request, "honor_award_competition.html", {"page": page,
                                                                "contacts": contacts,
                                                                "paper_list": paper_list,
                                                                "blank_list": blank_list,
                                                                "username": username,
                                                                "user_type": user_type,
                                                                })
    if award_type == "paper":

        paper_list = Honor_paper_magazine.objects.all().order_by("honor_paper_magazine_check_time").filter(honor_paper_magazine_is_checked=1)
        # 建立分页器 ，8个竞赛一组
        paginator = Paginator(paper_list, 8)
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
        is_meeting_paper = 0
        return render(request, "honor_award_paper.html", {"page": page,
                                                          "contacts": contacts,
                                                          "paper_list": paper_list,
                                                          "is_meeting_paper": is_meeting_paper,
                                                          "username": username,
                                                          "user_type": user_type,
                                                          })
    if award_type == "meeting-paper":

        paper_list = Honor_paper_meeting.objects.all().order_by("honor_paper_meeting_check_time").filter(honor_paper_meeting_is_checked=1)
        # 建立分页器 ，8个论文一组
        paginator = Paginator(paper_list, 8)
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
        is_meeting_paper=1
        return render(request, "honor_award_paper.html", {"page": page,
                                                          "contacts": contacts,
                                                          "paper_list": paper_list,
                                                          "is_meeting_paper": is_meeting_paper,
                                                          "username": username,
                                                          "user_type": user_type,
                                                          })
    if award_type == "patent":

        paper_list = Honor_patent.objects.all().order_by("honor_patent_check_time").filter(honor_patent_is_checked=1)

        # 建立分页器 ，8个论文一组
        paginator = Paginator(paper_list, 8)
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

        return render(request, "honor_award_patent.html", {"page": page,
                                                           "contacts": contacts,
                                                           "paper_list": paper_list,
                                                           "username": username,
                                                           "user_type": user_type,
                                                           })



# 通知榜路由

def inform(request, page):
    # 当访问./inform时默认显示第一页
    if page == "":
        page = 1
    # 字符串转化为整形
    page = int(page)
    # 获取通知列单
    inform_list = Message.objects.all().order_by("-message_date")
    if page == 1:
        # 最新消息
        # 取最新的一条消息
        fast_news = inform_list[0]
        # 提取该消息内容的前150字
        fast_news_content = fast_news.message_content[:150]

    # 创建分页器实例
    paginator = Paginator(inform_list, 10)
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
    # for each in contacts:
    #     each.message_content = each.message_content.replace(" ", "&nbsp").replace("\r\n", "<br>")
    #     each.save()
    username = request.session.get("username")
    user_type = request.session.get('usertype', -1)
    if page == 1:
        return render(request, "honor_inform.html", {"page": page,
                                                     "contacts": contacts,
                                                     "paper_list": paper_list,
                                                     "fast_news": fast_news,
                                                     "fast_news_content": fast_news_content,
                                                     "username": username,
                                                     "user_type": user_type,
                                                     })
    else:
        return render(request, "honor_inform.html", {"page": page,
                                                     "contacts": contacts,
                                                     "paper_list": paper_list,
                                                     "username": username,
                                                     "user_type": user_type,
                                                     })


def inform_page(request, id):
    paper = Message.objects.get(id=id)
    content = paper.message_content.replace(" ", "&nbsp").replace("\r\n", "<br>")
    user_type = request.session.get('usertype', -1)
    username = request.session.get('username', '')
    return render(request, "honor_inform_paper.html", {"paper": paper,
                                                       "content": content,
                                                       "username": username,
                                                       "user_type": user_type,
                                                       })

def logout(request):
    response = HttpResponseRedirect('/')
    response.delete_cookie('username')
    auth.logout(request)
    return response


def student_login(request):
    if request.method == 'POST':
        # username 是Netid
        username = request.POST.get('username', '')
        password = request.POST.get('password', '')
        # 为了用户的隐私，本地用户库里面存储的是MD5简单加密后的密码
        # 首先检验本地用户库里面有无该账号

        # 期望result是从学校验证后返回的字典
        # 格式result={"pass":1,"student_id":"2160508045","name":"刘星宇",...} pass 表示验证成功(1)还是失败(0)
        result = school_validate(username, password)
        # 学校认证成功
        password = result["student_id"]
        if result["pass"] == 1:
            #添加新用户数据到本地库
            user = auth.authenticate(username=username,password=password)
            if user is not None:
                auth.login(request, user)
                request.session.set_expiry(0)
                request.session['userid'] = user.last_name  # 学号
                request.session['usertype'] = result["is_teacher"]
                request.session['username'] = result["name"]
            else:

                new_user = User.objects.create_user(username=username, password=password)
                # 把用户的学号存入user的last_name列里面！
                new_user.first_name = result["name"]
                new_user.last_name = str(result["student_id"])  #
                new_user.save()
                auth.login(request, new_user)
                request.session.set_expiry(0)
                request.session['userid'] = new_user.last_name  # 学号
                request.session['usertype'] = result["is_teacher"]
                request.session['username'] = result["name"]

            response = HttpResponseRedirect('/')
            response.set_cookie('username', result["name"], 3600)
            return response
        else:
            return render(request, 'login.html', {'error': 'input error!', })

    else:
        return render(request, 'login.html')


def school_validate(netid, password):
    if (netid == '2160508044') & (password == '123456'):
        return {"pass": 1, "student_id": "2160508045", "name": "sui ling", "is_teacher": 0, }
    if (netid == '2160508045') & (password == '123456'):
        return {"pass": 1, "student_id": "2160508045", "name": "liu xing yu", "is_teacher": 0, }
    if (netid == 'admin') & (password == 'admin'):
        return {"pass": 1, "student_id": "2160508046", "name": "tao ye", "is_teacher": 1, }
    else:
        return {"pass": 0, }


def make_paper_list(page, max_page, long):
    if (page-5 > 0) & (page+3 < max_page):

        return [i for i in range(page-5,page-5+long)]
    if (page-5 <= 0) & (page+3 < max_page):

        return [i for i in range(1, min(1+long, 1+max_page))]
    if (page - 5 <= 0) & (page + 3 >= max_page):

        return [i for i in range(1, max_page+1)]
    if (page - 5 > 0) & (page + 3 >= max_page):

        return [i for i in range(max_page+1-long, max_page+1)]
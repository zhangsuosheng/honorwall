from django.shortcuts import render
from home.models import Competition_type,Teacher,Student_honorwall,Student_message_editable,Student_message_uneditable,Honor_competition,Honor_patent,Honor_paper_magazine,Honor_paper_meeting,Honor_scholarship,Honor_experience
from django.http import HttpResponse,HttpRequest
from django.db.models import Q
from django.core.paginator import Paginator,EmptyPage,PageNotAnInteger
from datetime import datetime
# 常量数组竞赛常用名称
static_competition_name=["全国大学生电子设计竞赛","中国大学生数学建模竞赛","美国大学生数学建模竞赛","西安交通大学大学生数学建模竞赛","ACM国际大学生程序设计竞赛","全国大学生信息安全竞赛","全国大学生机械创新设计大赛",
                         "全国青少年科技创新大赛","中国机器人大赛（暨RoboCup中国公开赛）","Robocon全国大学生机器人大赛","“互联网+”全国大学生创新创业大赛","“挑战杯”全国大学生课外学术科技作品竞赛",
                         "“创青春”全国大学生创业大赛","中国大学生物理学术竞赛","全国周培源大学生力学竞赛","全国大学生节能减排社会实践与科技竞赛"]
#定义的mytable函数的排序
def dict_mytable(s):
    return s["id"]

#竞赛审核数据表的刷新
def checking_mytable_competition(request,select,page=1):
    page=int(page)
    table_id="'my_table'"
    url="'competition'"
    # select=str(select)
    # b=type(select)==str
    # a = Competition_type.objects.filter(competition_name=select)
    # return HttpResponse(str(b)+"  "+select+a[0].competition_name)
    #获取竞赛名称对应的competition_id
    page_length=10
    if select=="全部":
        try:
            co_name=Competition_type.objects.filter()
            if(len(co_name)==0):
                return HttpResponse('<h4 style="color:red">无此项数据的记录<small>你可以选择其他的选项进行访问</small></h4>')
        except Exception:
            return HttpResponse('<h4 style="color:red">无此项数据的记录<small>你可以选择其他的选项进行访问</small></h4>')
    elif select=="其他":
        try:
            co_name = Competition_type.objects.filter(~Q(competition_name__in=static_competition_name))
            if (len(co_name) == 0):
                return HttpResponse('<h4 style="color:red">无此项数据的记录<small>你可以选择其他的选项进行访问1</small></h4>')
        except Exception:
            return HttpResponse('<h4 style="color:red">无此项数据的记录<small>你可以选择其他的选项进行访问2</small></h4>')
    else:
        try:
            co_name=Competition_type.objects.filter(competition_name=select)
            if (len(co_name) == 0):
                return HttpResponse('<h4 style="color:red">无此项数据的记录<small>你可以选择其他的选项进行访问3</small></h4>')
        except Exception:
            return HttpResponse('<h4 style="color:red">无此项数据的记录<small>你可以选择其他的选项进行访问4</small></h4>')
    try:
        cos=Honor_competition.objects.filter(competition_type__in=co_name,honor_competition_is_checked=0)
        if(len(cos)==0):
            return HttpResponse('<h4 style="color:red">无此项数据的记录<small>你可以选择其他的选项进行访问5</small></h4>')
    except Exception:
        return HttpResponse('<h4 style="color:red">无此项数据的记录<small>你可以选择其他的选项进行访问6</small></h4>')
    #获取返回数据（从竞赛审核表中） 并进行分页操作
    html_head='<table class="table table-striped table-bordered table-condensed"><thead><tr class="info"><th>序号</th><th>竞赛名称</th><th>获奖级别</th><th>姓名</th><th>审核提交时间</th><th>审核</th></tr></thead><tbody>'
    html_middle=''
    html_end='</tbody></table>'
    message_all=[]
    for co in cos:
        id=co.id #提交号
        # forigen_co=co.competition_type #竞赛类型外键
        forigen_st=co.student #学生外键
        name=co.competition_name #竞赛名称
        level=co.competition_level #竞赛级别
        name_st=forigen_st.student_name #提交人
        time=str(co.honor_competition_submit_time) #提交时间
        message={"id":id,"name":name,"level":level,"name_st":name_st,"time":time}#记录数据的字典
        message_all.append(message);
    message_all=sorted(message_all,key=dict_mytable)
    #分页
    p=Paginator(message_all,page_length)
    p_length=p.num_pages

    if (p_length < 7):
        html_end += '<div id="pagin" style="text-align:center;"><ul class="pagination">'
        if not (page == 1):
            html_end += '<li id="page_up" onclick="onclick1(' + str(
                page)+","+table_id+","+ url + ')"><a  aria-label="Previous"><span aria-hidden="true">&laquo;</span></a></li>'
        for i in range(1, p_length + 1):
            if i == page:
                html_end += '<li onclick="onclick3(' + str(
                i)+","+table_id+","+url + ')" id="active" class="active"><a >' + str(i) + '</a></li>'
            else:
                html_end += '<li onclick="onclick3(' + str(
                i)+","+table_id+","+url + ')"><a >' + str(i) + '</a></li>'
        if not (page == p_length):
            html_end += '<li id="page_down" onclick="onclick2(' + str(
                page)+","+table_id+","+url + ')"><a  aria-label="Next"><span aria-hidden="true">&raquo;</span></a></li>'
        html_end += '</ul></div>'
    elif (p_length - 3 < page):
        html_end += '<div id="pagin" style="text-align:center;"><ul class="pagination"><li onclick="onclick1(' + str(
                page)+","+table_id+","+url + ')" id="page_up"><a  aria-label="Previous"><span aria-hidden="true">&laquo;</span></a></li>'
        for i in range(p_length - 6, p_length + 1):
            if i == page:
                html_end += '<li onclick="onclick3(' + str(
                i)+","+table_id+","+url + ')" id="active" class="active"><a >' + str(i) + '</a></li>'
            else:
                html_end += '<li onclick="onclick3(' + str(
                i)+","+table_id+","+url + ')"><a >' + str(i) + '</a></li>'
        if not (page == p_length):
            html_end += '<li id="page_down" onclick="onclick2(' + str(
                page)+","+table_id+","+url + ')"><a  aria-label="Next"><span aria-hidden="true">&raquo;</span></a></li>'
        html_end += '</ul></div>'
    elif (p_length - 3 >= page):
        html_end += '<div id="pagin" style="text-align:center;"><ul class="pagination">'
        if not (page == 1):
            html_end += '<li id="page_up" onclick="onclick1(' + str(
                page)+","+table_id+","+url + ')"><a aria-label="Previous"><span aria-hidden="true">&laquo;</span></a></li>'
        if page - 3 <= 0:
            min = 1
            max = 8
        else:
            min = page - 3
            max = page + 3 + 1
        for i in range(min, max):
            if i == page:
                html_end += '<li onclick="onclick3(' + str(
                i)+','+table_id+','+'"'+url+'"' + ')" id="active" class="active"><a >' + str(i) + '</a></li>'
            else:
                html_end += '<li onclick="onclick3(' + str(
                i)+","+table_id+","+url + ')"><a >' + str(i) + '</a></li>'
        if not (page == p_length):
            html_end += '<li id="page_down" onclick="onclick2(' + str(
                page)+","+table_id+","+url + ')"><a  aria-label="Next"><span aria-hidden="true">&raquo;</span></a></li>'
        html_end += '</ul></div>'
    count=0
    if p.count<=page*page_length:
        p_max=p.count
    else:
        p_max=page*page_length
    for message in range((page-1)*page_length,p_max):
        count += 1
        if count == 1:
            mess = r'<tr class="success"><th>' + str(message_all[message]["id"]) + r'</th><th>' + message_all[message]["name"] + r'</th><th>' + message_all[message]["level"] + r'</th><th>' + message_all[message]["name_st"] + r'</th><th>' + message_all[message]["time"] + r'</th><th><a href=' + './competitionid='+str(message_all[message]["id"])+ r'>审核</a></th>'
        else:
            mess = '<tr><th>' + str(message_all[message]["id"]) + '</th><th>' + message_all[message]["name"] + '</th><th>' + message_all[message]["level"] + '</th><th>' + message_all[message]["name_st"] + '</th><th>' + message_all[message]["time"] + '</th><th><a href=' + './competitionid='+str(message_all[message]["id"]) + '>审核</a></th>'
        html_middle += mess

    return HttpResponse(html_head+html_middle+html_end)

def checking_mytable_magazinepaper(request,page=1):
    page=int(page)
    table_id="'my_table_2'"
    url="'magazinepaper'"
    #获取所有的期刊论文数据

    page_length=10
    try:
        mags = Honor_paper_magazine.objects.filter(honor_paper_magazine_is_checked=0)
        if(len(mags)==0):
            return HttpResponse('<h4 style="color:red">无此项数据的记录<small>你可以选择其他的选项进行访问3</small></h4>')
    except Exception:
        return HttpResponse('<h4 style="color:red">无此项数据的记录<small>你可以选择其他的选项进行访问4</small></h4>')
    #获取返回数据（从期刊论文表审核表中） 并进行分页操作
    html_head='<table class="table table-striped table-bordered table-condensed"><thead><tr class="info"><th>序号</th><th>期刊论文名称</th><th>期刊论文级别</th><th>期刊名称</th><th>姓名</th><th>审核提交时间</th><th>审核</th></tr></thead><tbody>'
    html_middle=''
    html_end='</tbody></table>'
    message_all=[]
    for mag in mags:
        id=mag.id #提交号
        name = mag.honor_paper_magazine_papername  # 名称r
        level=mag.honor_paper_magazine_type#级别
        name_2=mag.honor_paper_magazine_magazinename #刊物名称
        forigen_st=mag.student #学生外键
        name_st=forigen_st.student_name #提交人
        time=str(mag.honor_paper_magazine_submit_time) #提交时间
        message={"id":id,"name":name,"level":level,"name_2":name_2,"name_st":name_st,"time":time}#记录数据的字典
        message_all.append(message);
    message_all=sorted(message_all,key=dict_mytable)
    #分页
    p=Paginator(message_all,page_length)
    p_length=p.num_pages

    if (p_length < 7):
        html_end += '<div id="pagin" style="text-align:center;"><ul class="pagination">'
        if not (page == 1):
            html_end += '<li id="page_up" onclick="onclick1(' + str(
                page)+","+table_id+","+ url + ')"><a  aria-label="Previous"><span aria-hidden="true">&laquo;</span></a></li>'
        for i in range(1, p_length + 1):
            if i == page:
                html_end += '<li onclick="onclick3(' + str(
                i)+","+table_id+","+url + ')" id="active" class="active"><a >' + str(i) + '</a></li>'
            else:
                html_end += '<li onclick="onclick3(' + str(
                i)+","+table_id+","+url + ')"><a >' + str(i) + '</a></li>'
        if not (page == p_length):
            html_end += '<li id="page_down" onclick="onclick2(' + str(
                page)+","+table_id+","+url + ')"><a  aria-label="Next"><span aria-hidden="true">&raquo;</span></a></li>'
        html_end += '</ul></div>'
    elif (p_length - 3 < page):
        html_end += '<div id="pagin" style="text-align:center;"><ul class="pagination"><li onclick="onclick1(' + str(
                page)+","+table_id+","+url + ')" id="page_up"><a  aria-label="Previous"><span aria-hidden="true">&laquo;</span></a></li>'
        for i in range(p_length - 6, p_length + 1):
            if i == page:
                html_end += '<li onclick="onclick3(' + str(
                i)+","+table_id+","+url + ')" id="active" class="active"><a >' + str(i) + '</a></li>'
            else:
                html_end += '<li onclick="onclick3(' + str(
                i)+","+table_id+","+url + ')"><a >' + str(i) + '</a></li>'
        if not (page == p_length):
            html_end += '<li id="page_down" onclick="onclick2(' + str(
                page)+","+table_id+","+url + ')"><a  aria-label="Next"><span aria-hidden="true">&raquo;</span></a></li>'
        html_end += '</ul></div>'
    elif (p_length - 3 >= page):
        html_end += '<div id="pagin" style="text-align:center;"><ul class="pagination">'
        if not (page == 1):
            html_end += '<li id="page_up" onclick="onclick1(' + str(
                page)+","+table_id+","+url + ')"><a aria-label="Previous"><span aria-hidden="true">&laquo;</span></a></li>'
        if page - 3 <= 0:
            min = 1
            max = 8
        else:
            min = page - 3
            max = page + 3 + 1
        for i in range(min, max):
            if i == page:
                html_end += '<li onclick="onclick3(' + str(
                i)+','+table_id+','+'"'+url+'"' + ')" id="active" class="active"><a >' + str(i) + '</a></li>'
            else:
                html_end += '<li onclick="onclick3(' + str(
                i)+","+table_id+","+url + ')"><a >' + str(i) + '</a></li>'
        if not (page == p_length):
            html_end += '<li id="page_down" onclick="onclick2(' + str(
                page)+","+table_id+","+url + ')"><a  aria-label="Next"><span aria-hidden="true">&raquo;</span></a></li>'
        html_end += '</ul></div>'

    count=0
    if p.count<=page*page_length:
        p_max=p.count
    else:
        p_max=page*page_length
    for message in range((page-1)*page_length,p_max):
        count += 1
        if count == 1:
            mess = r'<tr class="success"><th>' + str(message_all[message]["id"]) + r'</th><th>' + message_all[message]["name"] + r'</th><th>' + message_all[message]["level"] + r'</th><th>' +message_all[message]["name_2"]+r'</th><th>'+ message_all[message]["name_st"] + r'</th><th>' + message_all[message]["time"] + r'</th><th><a href=' + './magazinepaperid='+str(message_all[message]["id"])+ r'>审核</a></th>'
        else:
            mess = r'<tr><th>' + str(message_all[message]["id"]) + r'</th><th>' + message_all[message]["name"] + r'</th><th>' + message_all[message]["level"] + r'</th><th>' +message_all[message]["name_2"]+r'</th><th>'+ message_all[message]["name_st"] + r'</th><th>' + message_all[message]["time"] + r'</th><th><a href=' + './magazinepaperid='+str(message_all[message]["id"])+ r'>审核</a></th>'
        html_middle += mess

    return HttpResponse(html_head+html_middle+html_end)

def checking_mytable_meetingpaper(request,page=1):
    page = int(page)
    table_id = "'my_table_3'"
    url = "'meetingpaper'"
    # 获取所有的期刊论文数据

    page_length = 10
    try:
        mags = Honor_paper_meeting.objects.filter(honor_paper_meeting_is_checked=0)
        if (len(mags) == 0):
            return HttpResponse('<h4 style="color:red">无此项数据的记录<small>你可以选择其他的选项进行访问3</small></h4>')
    except Exception:
        return HttpResponse('<h4 style="color:red">无此项数据的记录<small>你可以选择其他的选项进行访问4</small></h4>')
    # 获取返回数据（从期刊论文表审核表中） 并进行分页操作
    html_head = '<table class="table table-striped table-bordered table-condensed"><thead><tr class="info"><th>序号</th><th>会议论文名称</th><th>会议论文级别</th><th>会议名称</th><th>姓名</th><th>审核提交时间</th><th>审核</th></tr></thead><tbody>'
    html_middle = ''
    html_end = '</tbody></table>'
    message_all = []
    for mag in mags:
        id = mag.id  # 提交号
        name = mag.honor_paper_meeting_papername  # 名称
        level = mag.honor_paper_meeting_type  # 级别
        name_2 = mag.honor_paper_meeting_meetingname  # 刊物名称
        forigen_st = mag.student  # 学生外键
        name_st = forigen_st.student_name  # 提交人
        time = str(mag.honor_paper_meeting_submit_time)  # 提交时间
        message = {"id": id, "name": name, "level": level, "name_2": name_2, "name_st": name_st,
                   "time": time}  # 记录数据的字典
        message_all.append(message);
    message_all = sorted(message_all, key=dict_mytable)
    # 分页
    p = Paginator(message_all, page_length)
    p_length = p.num_pages

    if (p_length < 7):
        html_end += '<div id="pagin" style="text-align:center;"><ul class="pagination">'
        if not (page == 1):
            html_end += '<li id="page_up" onclick="onclick1(' + str(
                page) + "," + table_id + "," + url + ')"><a  aria-label="Previous"><span aria-hidden="true">&laquo;</span></a></li>'
        for i in range(1, p_length + 1):
            if i == page:
                html_end += '<li onclick="onclick3(' + str(
                    i) + "," + table_id + "," + url + ')" id="active" class="active"><a >' + str(i) + '</a></li>'
            else:
                html_end += '<li onclick="onclick3(' + str(
                    i) + "," + table_id + "," + url + ')"><a >' + str(i) + '</a></li>'
        if not (page == p_length):
            html_end += '<li id="page_down" onclick="onclick2(' + str(
                page) + "," + table_id + "," + url + ')"><a  aria-label="Next"><span aria-hidden="true">&raquo;</span></a></li>'
        html_end += '</ul></div>'
    elif (p_length - 3 < page):
        html_end += '<div id="pagin" style="text-align:center;"><ul class="pagination"><li onclick="onclick1(' + str(
            page) + "," + table_id + "," + url + ')" id="page_up"><a  aria-label="Previous"><span aria-hidden="true">&laquo;</span></a></li>'
        for i in range(p_length - 6, p_length + 1):
            if i == page:
                html_end += '<li onclick="onclick3(' + str(
                    i) + "," + table_id + "," + url + ')" id="active" class="active"><a >' + str(i) + '</a></li>'
            else:
                html_end += '<li onclick="onclick3(' + str(
                    i) + "," + table_id + "," + url + ')"><a >' + str(i) + '</a></li>'
        if not (page == p_length):
            html_end += '<li id="page_down" onclick="onclick2(' + str(
                page) + "," + table_id + "," + url + ')"><a  aria-label="Next"><span aria-hidden="true">&raquo;</span></a></li>'
        html_end += '</ul></div>'
    elif (p_length - 3 >= page):
        html_end += '<div id="pagin" style="text-align:center;"><ul class="pagination">'
        if not (page == 1):
            html_end += '<li id="page_up" onclick="onclick1(' + str(
                page) + "," + table_id + "," + url + ')"><a aria-label="Previous"><span aria-hidden="true">&laquo;</span></a></li>'
        if page - 3 <= 0:
            min = 1
            max = 8
        else:
            min = page - 3
            max = page + 3 + 1
        for i in range(min, max):
            if i == page:
                html_end += '<li onclick="onclick3(' + str(
                    i) + ',' + table_id + ',' + '"' + url + '"' + ')" id="active" class="active"><a >' + str(
                    i) + '</a></li>'
            else:
                html_end += '<li onclick="onclick3(' + str(
                    i) + "," + table_id + "," + url + ')"><a >' + str(i) + '</a></li>'
        if not (page == p_length):
            html_end += '<li id="page_down" onclick="onclick2(' + str(
                page) + "," + table_id + "," + url + ')"><a  aria-label="Next"><span aria-hidden="true">&raquo;</span></a></li>'
        html_end += '</ul></div>'

    count = 0
    if p.count <= page * page_length:
        p_max = p.count
    else:
        p_max = page * page_length
    for message in range((page - 1) * page_length, p_max):
        count += 1
        if count == 1:
            mess = r'<tr class="success"><th>' + str(message_all[message]["id"]) + r'</th><th>' + message_all[message][
                "name"] + r'</th><th>' + message_all[message]["level"] + r'</th><th>' + message_all[message][
                       "name_2"] + r'</th><th>' + message_all[message]["name_st"] + r'</th><th>' + message_all[message][
                       "time"] + r'</th><th><a href=' + './meetingpaperid='+str(message_all[message]["id"])+ r'>审核</a></th>'
        else:
            mess = r'<tr><th>' + str(message_all[message]["id"]) + r'</th><th>' + message_all[message][
                "name"] + r'</th><th>' + message_all[message]["level"] + r'</th><th>' + message_all[message][
                       "name_2"] + r'</th><th>' + message_all[message]["name_st"] + r'</th><th>' + message_all[message][
                       "time"] + r'</th><th><a href=' + './meetingpaperid='+str(message_all[message]["id"])+ r'>审核</a></th>'
        html_middle += mess

    return HttpResponse(html_head + html_middle + html_end)

def checking_mytable_patent(request,page=1):
    page = int(page)
    table_id = "'my_table_4'"
    url = "'patent'"
    # 获取所有的期刊论文数据

    page_length = 10
    try:
        mags = Honor_patent.objects.filter(honor_patent_is_checked=0)
        if (len(mags) == 0):
            return HttpResponse('<h4 style="color:red">无此项数据的记录<small>你可以选择其他的选项进行访问3</small></h4>')
    except Exception:
        return HttpResponse('<h4 style="color:red">无此项数据的记录<small>你可以选择其他的选项进行访问4</small></h4>')
    # 获取返回数据（从期刊论文表审核表中） 并进行分页操作
    html_head = '<table class="table table-striped table-bordered table-condensed"><thead><tr class="info"><th>序号</th><th>专利名称</th><th>专利类别</th><th>专利号</th><th>姓名</th><th>审核提交时间</th><th>审核</th></tr></thead><tbody>'
    html_middle = ''
    html_end = '</tbody></table>'
    message_all = []
    for mag in mags:
        id = mag.id  # 提交号
        name = mag.honor_patent_name  # 名称
        level = mag.honor_patent_type  # 级别
        name_2 = mag.honor_paper_patent_number  # 刊物名称
        forigen_st = mag.student  # 学生外键
        name_st = forigen_st.student_name  # 提交人
        time = str(mag.honor_patent_submit_time)  # 提交时间
        message = {"id": id, "name": name, "level": level, "name_2": name_2, "name_st": name_st,
                   "time": time}  # 记录数据的字典
        message_all.append(message);
    message_all = sorted(message_all, key=dict_mytable)
    # 分页
    p = Paginator(message_all, page_length)
    p_length = p.num_pages

    if (p_length < 7):
        html_end += '<div id="pagin" style="text-align:center;"><ul class="pagination">'
        if not (page == 1):
            html_end += '<li id="page_up" onclick="onclick1(' + str(
                page) + "," + table_id + "," + url + ')"><a  aria-label="Previous"><span aria-hidden="true">&laquo;</span></a></li>'
        for i in range(1, p_length + 1):
            if i == page:
                html_end += '<li onclick="onclick3(' + str(
                    i) + "," + table_id + "," + url + ')" id="active" class="active"><a >' + str(i) + '</a></li>'
            else:
                html_end += '<li onclick="onclick3(' + str(
                    i) + "," + table_id + "," + url + ')"><a >' + str(i) + '</a></li>'
        if not (page == p_length):
            html_end += '<li id="page_down" onclick="onclick2(' + str(
                page) + "," + table_id + "," + url + ')"><a  aria-label="Next"><span aria-hidden="true">&raquo;</span></a></li>'
        html_end += '</ul></div>'
    elif (p_length - 3 < page):
        html_end += '<div id="pagin" style="text-align:center;"><ul class="pagination"><li onclick="onclick1(' + str(
            page) + "," + table_id + "," + url + ')" id="page_up"><a  aria-label="Previous"><span aria-hidden="true">&laquo;</span></a></li>'
        for i in range(p_length - 6, p_length + 1):
            if i == page:
                html_end += '<li onclick="onclick3(' + str(
                    i) + "," + table_id + "," + url + ')" id="active" class="active"><a >' + str(i) + '</a></li>'
            else:
                html_end += '<li onclick="onclick3(' + str(
                    i) + "," + table_id + "," + url + ')"><a >' + str(i) + '</a></li>'
        if not (page == p_length):
            html_end += '<li id="page_down" onclick="onclick2(' + str(
                page) + "," + table_id + "," + url + ')"><a  aria-label="Next"><span aria-hidden="true">&raquo;</span></a></li>'
        html_end += '</ul></div>'
    elif (p_length - 3 >= page):
        html_end += '<div id="pagin" style="text-align:center;"><ul class="pagination">'
        if not (page == 1):
            html_end += '<li id="page_up" onclick="onclick1(' + str(
                page) + "," + table_id + "," + url + ')"><a aria-label="Previous"><span aria-hidden="true">&laquo;</span></a></li>'
        if page - 3 <= 0:
            min = 1
            max = 8
        else:
            min = page - 3
            max = page + 3 + 1
        for i in range(min, max):
            if i == page:
                html_end += '<li onclick="onclick3(' + str(
                    i) + ',' + table_id + ',' + '"' + url + '"' + ')" id="active" class="active"><a >' + str(
                    i) + '</a></li>'
            else:
                html_end += '<li onclick="onclick3(' + str(
                    i) + "," + table_id + "," + url + ')"><a >' + str(i) + '</a></li>'
        if not (page == p_length):
            html_end += '<li id="page_down" onclick="onclick2(' + str(
                page) + "," + table_id + "," + url + ')"><a  aria-label="Next"><span aria-hidden="true">&raquo;</span></a></li>'
        html_end += '</ul></div>'

    count = 0
    if p.count <= page * page_length:
        p_max = p.count
    else:
        p_max = page * page_length
    for message in range((page - 1) * page_length, p_max):
        count += 1
        if count == 1:
            mess = r'<tr class="success"><th>' + str(message_all[message]["id"]) + r'</th><th>' + message_all[message][
                "name"] + r'</th><th>' + message_all[message]["level"] + r'</th><th>' + message_all[message][
                       "name_2"] + r'</th><th>' + message_all[message]["name_st"] + r'</th><th>' + message_all[message][
                       "time"] + r'</th><th><a href=' + './patentid='+str(message_all[message]["id"])+ r'>审核</a></th>'
        else:
            mess = r'<tr><th>' + str(message_all[message]["id"]) + r'</th><th>' + message_all[message][
                "name"] + r'</th><th>' + message_all[message]["level"] + r'</th><th>' + message_all[message][
                       "name_2"] + r'</th><th>' + message_all[message]["name_st"] + r'</th><th>' + message_all[message][
                       "time"] + r'</th><th><a href=' + './patentid='+str(message_all[message]["id"])+ r'>审核</a></th>'
        html_middle += mess

    return HttpResponse(html_head + html_middle + html_end)

def checking_mytable_prize(request,page=1):
    page = int(page)
    table_id = "'my_table_5'"
    url = "'prize'"
    # 获取所有的期刊论文数据
    page_length = 10
    try:
        mags = Honor_scholarship.objects.filter(honor_scholarship_is_checked=0)
        if (len(mags) == 0):
            return HttpResponse('<h4 style="color:red">无此项数据的记录<small>你可以选择其他的选项进行访问3</small></h4>')
    except Exception:
        return HttpResponse('<h4 style="color:red">无此项数据的记录<small>你可以选择其他的选项进行访问4</small></h4>')
    # 获取返回数据（从期刊论文表审核表中） 并进行分页操作
    html_head = '<table class="table table-striped table-bordered table-condensed"><thead><tr class="info"><th>序号</th><th>奖学金名称</th><th>获奖年度</th><th>奖学金金额</th><th>姓名</th><th>审核提交时间</th><th>审核</th></tr></thead><tbody>'
    html_middle = ''
    html_end = '</tbody></table>'
    message_all = []
    for mag in mags:
        id = mag.id  # 提交号
        name = mag.honor_scholarship_name  # 名称
        level = mag.honor_scholarship_year  # 级别
        name_2 = mag.honor_scholarship_moneyperyear  # 刊物名称
        forigen_st = mag.student  # 学生外键
        name_st = forigen_st.student_name  # 提交人
        time = str(mag.honor_scholarship_submit_time)  # 提交时间
        message = {"id": id, "name": name, "level": level, "name_2": name_2, "name_st": name_st,
                   "time": time}  # 记录数据的字典
        message_all.append(message);
    message_all = sorted(message_all, key=dict_mytable)
    # 分页
    p = Paginator(message_all, page_length)
    p_length = p.num_pages

    if (p_length < 7):
        html_end += '<div id="pagin" style="text-align:center;"><ul class="pagination">'
        if not (page == 1):
            html_end += '<li id="page_up" onclick="onclick1(' + str(
                page) + "," + table_id + "," + url + ')"><a  aria-label="Previous"><span aria-hidden="true">&laquo;</span></a></li>'
        for i in range(1, p_length + 1):
            if i == page:
                html_end += '<li onclick="onclick3(' + str(
                    i) + "," + table_id + "," + url + ')" id="active" class="active"><a >' + str(i) + '</a></li>'
            else:
                html_end += '<li onclick="onclick3(' + str(
                    i) + "," + table_id + "," + url + ')"><a >' + str(i) + '</a></li>'
        if not (page == p_length):
            html_end += '<li id="page_down" onclick="onclick2(' + str(
                page) + "," + table_id + "," + url + ')"><a  aria-label="Next"><span aria-hidden="true">&raquo;</span></a></li>'
        html_end += '</ul></div>'
    elif (p_length - 3 < page):
        html_end += '<div id="pagin" style="text-align:center;"><ul class="pagination"><li onclick="onclick1(' + str(
            page) + "," + table_id + "," + url + ')" id="page_up"><a  aria-label="Previous"><span aria-hidden="true">&laquo;</span></a></li>'
        for i in range(p_length - 6, p_length + 1):
            if i == page:
                html_end += '<li onclick="onclick3(' + str(
                    i) + "," + table_id + "," + url + ')" id="active" class="active"><a >' + str(i) + '</a></li>'
            else:
                html_end += '<li onclick="onclick3(' + str(
                    i) + "," + table_id + "," + url + ')"><a >' + str(i) + '</a></li>'
        if not (page == p_length):
            html_end += '<li id="page_down" onclick="onclick2(' + str(
                page) + "," + table_id + "," + url + ')"><a  aria-label="Next"><span aria-hidden="true">&raquo;</span></a></li>'
        html_end += '</ul></div>'
    elif (p_length - 3 >= page):
        html_end += '<div id="pagin" style="text-align:center;"><ul class="pagination">'
        if not (page == 1):
            html_end += '<li id="page_up" onclick="onclick1(' + str(
                page) + "," + table_id + "," + url + ')"><a aria-label="Previous"><span aria-hidden="true">&laquo;</span></a></li>'
        if page - 3 <= 0:
            min = 1
            max = 8
        else:
            min = page - 3
            max = page + 3 + 1
        for i in range(min, max):
            if i == page:
                html_end += '<li onclick="onclick3(' + str(
                    i) + ',' + table_id + ',' + '"' + url + '"' + ')" id="active" class="active"><a >' + str(
                    i) + '</a></li>'
            else:
                html_end += '<li onclick="onclick3(' + str(
                    i) + "," + table_id + "," + url + ')"><a >' + str(i) + '</a></li>'
        if not (page == p_length):
            html_end += '<li id="page_down" onclick="onclick2(' + str(
                page) + "," + table_id + "," + url + ')"><a  aria-label="Next"><span aria-hidden="true">&raquo;</span></a></li>'
        html_end += '</ul></div>'

    count = 0
    if p.count <= page * page_length:
        p_max = p.count
    else:
        p_max = page * page_length
    for message in range((page - 1) * page_length, p_max):
        count += 1
        if count == 1:
            mess = r'<tr class="success"><th>' + str(message_all[message]["id"]) + r'</th><th>' + message_all[message][
                "name"] + r'</th><th>' + message_all[message]["level"] + r'</th><th>' + message_all[message][
                       "name_2"] + r'</th><th>' + message_all[message]["name_st"] + r'</th><th>' + message_all[message][
                       "time"] + r'</th><th><a href=' + './prizeid='+str(message_all[message]["id"])+ r'>审核</a></th>'
        else:
            mess = r'<tr><th>' + str(message_all[message]["id"]) + r'</th><th>' + message_all[message][
                "name"] + r'</th><th>' + message_all[message]["level"] + r'</th><th>' + message_all[message][
                       "name_2"] + r'</th><th>' + message_all[message]["name_st"] + r'</th><th>' + message_all[message][
                       "time"] + r'</th><th><a href=' + './prizeid='+str(message_all[message]["id"])+ r'>审核</a></th>'
        html_middle += mess

    return HttpResponse(html_head + html_middle + html_end)

def checking_mytable_experience(request,page=1):
    page = int(page)
    table_id = "'my_table_6'"
    url = "'experience'"
    # 获取所有的社会经历数据

    page_length = 10
    try:
        mags = Honor_experience.objects.filter(honor_experience_is_checked=0)
        if (len(mags) == 0):
            return HttpResponse('<h4 style="color:red">无此项数据的记录<small>你可以选择其他的选项进行访问3</small></h4>')
    except Exception:
        return HttpResponse('<h4 style="color:red">无此项数据的记录<small>你可以选择其他的选项进行访问4</small></h4>')
    # 获取返回数据（从期刊论文表审核表中） 并进行分页操作
    html_head = '<table class="table table-striped table-bordered table-condensed"><thead><tr class="info"><th>序号</th><th>活动名称</th><th>活动单位</th><th>活动开始时间</th><th>姓名</th><th>审核提交时间</th><th>审核</th></tr></thead><tbody>'
    html_middle = ''
    html_end = '</tbody></table>'
    message_all = []
    for mag in mags:
        id = mag.id  # 提交号
        name = mag.honor_experience_name  # 名称
        level = mag.honor_experience_authority  # 级别
        name_2 = mag.honor_experience_start  # 刊物名称
        forigen_st = mag.student  # 学生外键
        name_st = forigen_st.student_name  # 提交人
        time = str(mag.honor_experience_submit_time)  # 提交时间
        message = {"id": id, "name": name, "level": level, "name_2": name_2, "name_st": name_st,
                   "time": time}  # 记录数据的字典
        message_all.append(message);
    message_all = sorted(message_all, key=dict_mytable)
    # 分页
    p = Paginator(message_all, page_length)
    p_length = p.num_pages

    if (p_length < 7):
        html_end += '<div id="pagin" style="text-align:center;"><ul class="pagination">'
        if not (page == 1):
            html_end += '<li id="page_up" onclick="onclick1(' + str(
                page) + "," + table_id + "," + url + ')"><a  aria-label="Previous"><span aria-hidden="true">&laquo;</span></a></li>'
        for i in range(1, p_length + 1):
            if i == page:
                html_end += '<li onclick="onclick3(' + str(
                    i) + "," + table_id + "," + url + ')" id="active" class="active"><a >' + str(i) + '</a></li>'
            else:
                html_end += '<li onclick="onclick3(' + str(
                    i) + "," + table_id + "," + url + ')"><a >' + str(i) + '</a></li>'
        if not (page == p_length):
            html_end += '<li id="page_down" onclick="onclick2(' + str(
                page) + "," + table_id + "," + url + ')"><a  aria-label="Next"><span aria-hidden="true">&raquo;</span></a></li>'
        html_end += '</ul></div>'
    elif (p_length - 3 < page):
        html_end += '<div id="pagin" style="text-align:center;"><ul class="pagination"><li onclick="onclick1(' + str(
            page) + "," + table_id + "," + url + ')" id="page_up"><a  aria-label="Previous"><span aria-hidden="true">&laquo;</span></a></li>'
        for i in range(p_length - 6, p_length + 1):
            if i == page:
                html_end += '<li onclick="onclick3(' + str(
                    i) + "," + table_id + "," + url + ')" id="active" class="active"><a >' + str(i) + '</a></li>'
            else:
                html_end += '<li onclick="onclick3(' + str(
                    i) + "," + table_id + "," + url + ')"><a >' + str(i) + '</a></li>'
        if not (page == p_length):
            html_end += '<li id="page_down" onclick="onclick2(' + str(
                page) + "," + table_id + "," + url + ')"><a  aria-label="Next"><span aria-hidden="true">&raquo;</span></a></li>'
        html_end += '</ul></div>'
    elif (p_length - 3 >= page):
        html_end += '<div id="pagin" style="text-align:center;"><ul class="pagination">'
        if not (page == 1):
            html_end += '<li id="page_up" onclick="onclick1(' + str(
                page) + "," + table_id + "," + url + ')"><a aria-label="Previous"><span aria-hidden="true">&laquo;</span></a></li>'
        if page - 3 <= 0:
            min = 1
            max = 8
        else:
            min = page - 3
            max = page + 3 + 1
        for i in range(min, max):
            if i == page:
                html_end += '<li onclick="onclick3(' + str(
                    i) + ',' + table_id + ',' + '"' + url + '"' + ')" id="active" class="active"><a >' + str(
                    i) + '</a></li>'
            else:
                html_end += '<li onclick="onclick3(' + str(
                    i) + "," + table_id + "," + url + ')"><a >' + str(i) + '</a></li>'
        if not (page == p_length):
            html_end += '<li id="page_down" onclick="onclick2(' + str(
                page) + "," + table_id + "," + url + ')"><a  aria-label="Next"><span aria-hidden="true">&raquo;</span></a></li>'
        html_end += '</ul></div>'

    count = 0
    if p.count <= page * page_length:
        p_max = p.count
    else:
        p_max = page * page_length
    for message in range((page - 1) * page_length, p_max):
        count += 1
        if count == 1:
            mess = r'<tr class="success"><th>' + str(message_all[message]["id"]) + r'</th><th>' + message_all[message][
                "name"] + r'</th><th>' + message_all[message]["level"] + r'</th><th>' + message_all[message][
                       "name_2"] + r'</th><th>' + message_all[message]["name_st"] + r'</th><th>' + message_all[message][
                       "time"] + r'</th><th><a href=' + './experienceid='+str(message_all[message]["id"])+ r'>审核</a></th>'
        else:
            mess = r'<tr><th>' + str(message_all[message]["id"]) + r'</th><th>' + message_all[message][
                "name"] + r'</th><th>' + message_all[message]["level"] + r'</th><th>' + message_all[message][
                       "name_2"] + r'</th><th>' + message_all[message]["name_st"] + r'</th><th>' + message_all[message][
                       "time"] + r'</th><th><a href=' + './experienceid='+str(message_all[message]["id"])+ r'>审核</a></th>'
        html_middle += mess

    return HttpResponse(html_head + html_middle + html_end)


def checking_mytable_already(request,select,page=1):
    try:
        sessionid=request.session.get('sessionid','')
        teacher=Teacher.objects.get(teacher_id=sessionid)
    except:
        return render(request,"404.html")
    page = int(page)
    table_id = "'my_table_7'"
    url = "'already'"
    page_length = 10;
    if(select=='竞赛'):
        try:
            com_list=Honor_competition.objects.filter(~Q(honor_competition_is_checked=0),teacher=teacher)
            com_listing=[]
            com_already=[]
            message_all=[]
            for com in com_list:
                if int(com.honor_competition_is_checked)==2:
                    com_listing.append(com)
                else:
                    com_already.append(com)
        except:
            return render(request,"404.html")
        html_head = '<table class="table table-striped table-bordered table-condensed"><thead><tr class="info"><th>序号</th><th>竞赛名称</th><th>获奖级别</th><th>姓名</th><th>审核时间</th><th>审核状态</th></tr></thead><tbody>'
        html_middle = ''
        html_end = '</tbody></table>'

        for co in com_already:
            id = co.id  # 提交号
            # forigen_co=co.competition_type #竞赛类型外键
            forigen_st = co.student  # 学生外键
            name = co.competition_name  # 竞赛名称
            level = co.competition_level  # 竞赛级别
            name_st = forigen_st.student_name  # 提交人
            is_checked = co.honor_competition_is_checked
            if is_checked == 1:
                is_checked = '审核通过'
            elif is_checked == 0:
                is_checked = '未审核'
            elif is_checked == -1:
                is_checked = '审核不通过'
            elif is_checked == 2:
                is_checked = '正在审核'
            time = str(co.honor_competition_check_time)  # 提交时间
            message = {"id": id, "name": name, "level": level, "name_st": name_st, "time": time,
                       'is_checked': is_checked}  # 记录数据的字典
            message_all.append(message);
        for co in com_listing:
            id = co.id  # 提交号
            # forigen_co=co.competition_type #竞赛类型外键
            forigen_st = co.student  # 学生外键
            name = co.competition_name  # 竞赛名称
            level = co.competition_level  # 竞赛级别
            name_st = forigen_st.student_name  # 提交人
            is_checked=co.honor_competition_is_checked
            if is_checked == 1:
                is_checked = '审核通过'
            elif is_checked == 0:
                is_checked = '未审核'
            elif is_checked == -1:
                is_checked = '审核不通过'
            elif is_checked == 2:
                is_checked = '正在审核'
            time = str(co.honor_competition_check_time)  # 审核时间
            message = {"id": id, "name": name, "level": level, "name_st": name_st, "time": time,'is_checked':is_checked}  # 记录数据的字典
            message_all.append(message);
        # 分页
        message_all.reverse()
        p = Paginator(message_all, page_length)
        p_length = p.num_pages

        if (p_length < 7):
            html_end += '<div id="pagin" style="text-align:center;"><ul class="pagination">'
            if not (page == 1):
                html_end += '<li id="page_up" onclick="onclick1(' + str(
                    page) + "," + table_id + "," + url + ')"><a  aria-label="Previous"><span aria-hidden="true">&laquo;</span></a></li>'
            for i in range(1, p_length + 1):
                if i == page:
                    html_end += '<li onclick="onclick3(' + str(
                        i) + "," + table_id + "," + url + ')" id="active" class="active"><a >' + str(
                        i) + '</a></li>'
                else:
                    html_end += '<li onclick="onclick3(' + str(
                        i) + "," + table_id + "," + url + ')"><a >' + str(i) + '</a></li>'
            if not (page == p_length):
                html_end += '<li id="page_down" onclick="onclick2(' + str(
                    page) + "," + table_id + "," + url + ')"><a  aria-label="Next"><span aria-hidden="true">&raquo;</span></a></li>'
            html_end += '</ul></div>'
        elif (p_length - 3 < page):
            html_end += '<div id="pagin" style="text-align:center;"><ul class="pagination"><li onclick="onclick1(' + str(
                page) + "," + table_id + "," + url + ')" id="page_up"><a  aria-label="Previous"><span aria-hidden="true">&laquo;</span></a></li>'
            for i in range(p_length - 6, p_length + 1):
                if i == page:
                    html_end += '<li onclick="onclick3(' + str(
                        i) + "," + table_id + "," + url + ')" id="active" class="active"><a >' + str(
                        i) + '</a></li>'
                else:
                    html_end += '<li onclick="onclick3(' + str(
                        i) + "," + table_id + "," + url + ')"><a >' + str(i) + '</a></li>'
            if not (page == p_length):
                html_end += '<li id="page_down" onclick="onclick2(' + str(
                    page) + "," + table_id + "," + url + ')"><a  aria-label="Next"><span aria-hidden="true">&raquo;</span></a></li>'
            html_end += '</ul></div>'
        elif (p_length - 3 >= page):
            html_end += '<div id="pagin" style="text-align:center;"><ul class="pagination">'
            if not (page == 1):
                html_end += '<li id="page_up" onclick="onclick1(' + str(
                    page) + "," + table_id + "," + url + ')"><a aria-label="Previous"><span aria-hidden="true">&laquo;</span></a></li>'
            if page - 3 <= 0:
                min = 1
                max = 8
            else:
                min = page - 3
                max = page + 3 + 1
            for i in range(min, max):
                if i == page:
                    html_end += '<li onclick="onclick3(' + str(
                        i) + ',' + table_id + ',' + '"' + url + '"' + ')" id="active" class="active"><a >' + str(
                        i) + '</a></li>'
                else:
                    html_end += '<li onclick="onclick3(' + str(
                        i) + "," + table_id + "," + url + ')"><a >' + str(i) + '</a></li>'
            if not (page == p_length):
                html_end += '<li id="page_down" onclick="onclick2(' + str(
                    page) + "," + table_id + "," + url + ')"><a  aria-label="Next"><span aria-hidden="true">&raquo;</span></a></li>'
            html_end += '</ul></div>'
        count = 0
        if p.count <= page * page_length:
            p_max = p.count
        else:
            p_max = page * page_length
        for message in range((page - 1) * page_length, p_max):
            count += 1
            if count == 1:
                mess = r'<tr class="success"><th>' + str(message_all[message]["id"]) + r'</th><th>' + \
                       message_all[message]["name"] + r'</th><th>' + message_all[message]["level"] + r'</th><th>' + \
                       message_all[message]["name_st"] + r'</th><th>' + message_all[message][
                           "time"] + r'</th><th><a href=' + './competitionid=' + str(
                    message_all[message]["id"]) +"already"+ r'>'+message_all[message]["is_checked"]+'</a></th>'
            else:
                mess = '<tr><th>' + str(message_all[message]["id"]) + '</th><th>' + message_all[message][
                    "name"] + '</th><th>' + message_all[message]["level"] + '</th><th>' + message_all[message][
                           "name_st"] + '</th><th>' + message_all[message][
                           "time"] + '</th><th><a href=' + './competitionid=' + str(
                    message_all[message]["id"]) +"already"+'>'+message_all[message]["is_checked"]+'</a></th>'
            html_middle += mess

        return HttpResponse(html_head + html_middle + html_end)
    elif(select=='期刊论文'):
        page = int(page)
        table_id = "'my_table_7'"
        url = "'already'"
        # 获取所有的期刊论文数据

        page_length = 10
        try:
            mags = Honor_paper_magazine.objects.filter(~Q(honor_paper_magazine_is_checked=0))
            if (len(mags) == 0):
                return HttpResponse('<h4 style="color:red">无此项数据的记录<small>你可以选择其他的选项进行访问3</small></h4>')
        except Exception:
            return HttpResponse('<h4 style="color:red">无此项数据的记录<small>你可以选择其他的选项进行访问4</small></h4>')
        # 获取返回数据（从期刊论文表审核表中） 并进行分页操作
        html_head = '<table class="table table-striped table-bordered table-condensed"><thead><tr class="info"><th>序号</th><th>期刊论文名称</th><th>期刊论文级别</th><th>期刊名称</th><th>姓名</th><th>审核时间</th><th>审核状态</th></tr></thead><tbody>'
        html_middle = ''
        html_end = '</tbody></table>'
        message_all = []
        message_listing=[]
        message_already=[]
        for mag in mags:
            if mag.honor_paper_meeting_is_checked==2:
                message_listing.append(mag)
            else:
                message_already.append(mag)

        for mag in message_already:
            id = mag.id  # 提交号
            name = mag.honor_paper_magazine_papername  # 名称r
            level = mag.honor_paper_magazine_type  # 级别
            name_2 = mag.honor_paper_magazine_magazinename  # 刊物名称
            forigen_st = mag.student  # 学生外键
            name_st = forigen_st.student_name  # 提交人
            time = str(mag.honor_paper_magazine_check_time)  # 提交时间
            is_checked = mag.honor_paper_magazine_is_checked
            if is_checked == 1:
                is_checked = '审核通过'
            elif is_checked == 0:
                is_checked = '未审核'
            elif is_checked == -1:
                is_checked = '审核不通过'
            elif is_checked == 2:
                is_checked = '正在审核'
            message = {"id": id, "name": name, "level": level, "name_2": name_2, "name_st": name_st,
                       "time": time,'is_checked':is_checked}  # 记录数据的字典
            message_all.append(message);
        for mag in message_listing:
            id = mag.id  # 提交号
            name = mag.honor_paper_magazine_papername  # 名称r
            level = mag.honor_paper_magazine_type  # 级别
            name_2 = mag.honor_paper_magazine_magazinename  # 刊物名称
            forigen_st = mag.student  # 学生外键
            name_st = forigen_st.student_name  # 提交人
            time = str(mag.honor_paper_magazine_check_time)  # 提交时间
            is_checked = mag.honor_paper_magazine_is_checked
            if is_checked == 1:
                is_checked = '审核通过'
            elif is_checked == 0:
                is_checked = '未审核'
            elif is_checked == -1:
                is_checked = '审核不通过'
            elif is_checked == 2:
                is_checked = '正在审核'
            message = {"id": id, "name": name, "level": level, "name_2": name_2, "name_st": name_st,
                       "time": time,'is_checked':is_checked}  # 记录数据的字典
            message_all.append(message);
        # 分页
        message_all.reverse()
        p = Paginator(message_all, page_length)
        p_length = p.num_pages

        if (p_length < 7):
            html_end += '<div id="pagin" style="text-align:center;"><ul class="pagination">'
            if not (page == 1):
                html_end += '<li id="page_up" onclick="onclick1(' + str(
                    page) + "," + table_id + "," + url + ')"><a  aria-label="Previous"><span aria-hidden="true">&laquo;</span></a></li>'
            for i in range(1, p_length + 1):
                if i == page:
                    html_end += '<li onclick="onclick3(' + str(
                        i) + "," + table_id + "," + url + ')" id="active" class="active"><a >' + str(i) + '</a></li>'
                else:
                    html_end += '<li onclick="onclick3(' + str(
                        i) + "," + table_id + "," + url + ')"><a >' + str(i) + '</a></li>'
            if not (page == p_length):
                html_end += '<li id="page_down" onclick="onclick2(' + str(
                    page) + "," + table_id + "," + url + ')"><a  aria-label="Next"><span aria-hidden="true">&raquo;</span></a></li>'
            html_end += '</ul></div>'
        elif (p_length - 3 < page):
            html_end += '<div id="pagin" style="text-align:center;"><ul class="pagination"><li onclick="onclick1(' + str(
                page) + "," + table_id + "," + url + ')" id="page_up"><a  aria-label="Previous"><span aria-hidden="true">&laquo;</span></a></li>'
            for i in range(p_length - 6, p_length + 1):
                if i == page:
                    html_end += '<li onclick="onclick3(' + str(
                        i) + "," + table_id + "," + url + ')" id="active" class="active"><a >' + str(i) + '</a></li>'
                else:
                    html_end += '<li onclick="onclick3(' + str(
                        i) + "," + table_id + "," + url + ')"><a >' + str(i) + '</a></li>'
            if not (page == p_length):
                html_end += '<li id="page_down" onclick="onclick2(' + str(
                    page) + "," + table_id + "," + url + ')"><a  aria-label="Next"><span aria-hidden="true">&raquo;</span></a></li>'
            html_end += '</ul></div>'
        elif (p_length - 3 >= page):
            html_end += '<div id="pagin" style="text-align:center;"><ul class="pagination">'
            if not (page == 1):
                html_end += '<li id="page_up" onclick="onclick1(' + str(
                    page) + "," + table_id + "," + url + ')"><a aria-label="Previous"><span aria-hidden="true">&laquo;</span></a></li>'
            if page - 3 <= 0:
                min = 1
                max = 8
            else:
                min = page - 3
                max = page + 3 + 1
            for i in range(min, max):
                if i == page:
                    html_end += '<li onclick="onclick3(' + str(
                        i) + ',' + table_id + ',' + '"' + url + '"' + ')" id="active" class="active"><a >' + str(
                        i) + '</a></li>'
                else:
                    html_end += '<li onclick="onclick3(' + str(
                        i) + "," + table_id + "," + url + ')"><a >' + str(i) + '</a></li>'
            if not (page == p_length):
                html_end += '<li id="page_down" onclick="onclick2(' + str(
                    page) + "," + table_id + "," + url + ')"><a  aria-label="Next"><span aria-hidden="true">&raquo;</span></a></li>'
            html_end += '</ul></div>'

        count = 0
        if p.count <= page * page_length:
            p_max = p.count
        else:
            p_max = page * page_length
        for message in range((page - 1) * page_length, p_max):
            count += 1
            if count == 1:
                mess = r'<tr class="success"><th>' + str(message_all[message]["id"]) + r'</th><th>' + \
                       message_all[message]["name"] + r'</th><th>' + message_all[message]["level"] + r'</th><th>' + \
                       message_all[message]["name_2"] + r'</th><th>' + message_all[message]["name_st"] + r'</th><th>' + \
                       message_all[message][
                           "time"] + r'</th><th><a href=' + './magazinepaperid=' + str(
                    message_all[message]["id"])+'already' + r'>'+message_all[message]["is_checked"]+'</a></th>'
            else:
                mess = r'<tr><th>' + str(message_all[message]["id"]) + r'</th><th>' + message_all[message][
                    "name"] + r'</th><th>' + message_all[message]["level"] + r'</th><th>' + message_all[message][
                           "name_2"] + r'</th><th>' + message_all[message]["name_st"] + r'</th><th>' + \
                       message_all[message][
                           "time"] + r'</th><th><a href=' + './magazinepaperid=' + str(
                    message_all[message]["id"])+'already' + r'>'+message_all[message]["is_checked"]+'</a></th>'
            html_middle += mess

        return HttpResponse(html_head + html_middle + html_end)
    elif(select=='会议论文'):
        page = int(page)
        table_id = "'my_table_7'"
        url = "'already'"
        # 获取所有的期刊论文数据

        page_length = 10
        try:
            mags = Honor_paper_meeting.objects.filter(~Q(honor_paper_meeting_is_checked=0))
            if (len(mags) == 0):
                return HttpResponse('<h4 style="color:red">无此项数据的记录<small>你可以选择其他的选项进行访问3</small></h4>')
        except Exception:
            return HttpResponse('<h4 style="color:red">无此项数据的记录<small>你可以选择其他的选项进行访问4</small></h4>')
        # 获取返回数据（从期刊论文表审核表中） 并进行分页操作
        html_head = '<table class="table table-striped table-bordered table-condensed"><thead><tr class="info"><th>序号</th><th>会议论文名称</th><th>会议论文级别</th><th>会议名称</th><th>姓名</th><th>审核时间</th><th>审核状态</th></tr></thead><tbody>'
        html_middle = ''
        html_end = '</tbody></table>'
        message_all = []
        message_listing = []
        message_already = []
        for mag in mags:
            if mag.honor_paper_meeting_is_checked == 2:
                message_listing.append(mag)
            else:
                message_already.append(mag)

        for mag in message_already:
            id = mag.id  # 提交号
            name = mag.honor_paper_meeting_papername  # 名称r
            level = mag.honor_paper_meeting_type  # 级别
            name_2 = mag.honor_paper_meeting_meetingname  # 刊物名称
            forigen_st = mag.student  # 学生外键
            name_st = forigen_st.student_name  # 提交人
            time = str(mag.honor_paper_meeting_check_time)  # 提交时间
            is_checked = mag.honor_paper_meeting_is_checked
            if is_checked == 1:
                is_checked = '审核通过'
            elif is_checked == 0:
                is_checked = '未审核'
            elif is_checked == -1:
                is_checked = '审核不通过'
            elif is_checked == 2:
                is_checked = '正在审核'
            message = {"id": id, "name": name, "level": level, "name_2": name_2, "name_st": name_st,
                       "time": time, 'is_checked': is_checked}  # 记录数据的字典
            message_all.append(message);
        for mag in message_listing:
            id = mag.id  # 提交号
            name = mag.honor_paper_meeting_papername  # 名称r
            level = mag.honor_paper_meeting_type  # 级别
            name_2 = mag.honor_paper_meeting_meetingname  # 刊物名称
            forigen_st = mag.student  # 学生外键
            name_st = forigen_st.student_name  # 提交人
            time = str(mag.honor_paper_meeting_check_time)  # 提交时间
            is_checked = mag.honor_paper_meeting_is_checked
            if is_checked == 1:
                is_checked = '审核通过'
            elif is_checked == 0:
                is_checked = '未审核'
            elif is_checked == -1:
                is_checked = '审核不通过'
            elif is_checked == 2:
                is_checked = '正在审核'
            message = {"id": id, "name": name, "level": level, "name_2": name_2, "name_st": name_st,
                       "time": time, 'is_checked': is_checked}  # 记录数据的字典
            message_all.append(message);
        # 分页
        message_all.reverse()
        p = Paginator(message_all, page_length)
        p_length = p.num_pages

        if (p_length < 7):
            html_end += '<div id="pagin" style="text-align:center;"><ul class="pagination">'
            if not (page == 1):
                html_end += '<li id="page_up" onclick="onclick1(' + str(
                    page) + "," + table_id + "," + url + ')"><a  aria-label="Previous"><span aria-hidden="true">&laquo;</span></a></li>'
            for i in range(1, p_length + 1):
                if i == page:
                    html_end += '<li onclick="onclick3(' + str(
                        i) + "," + table_id + "," + url + ')" id="active" class="active"><a >' + str(i) + '</a></li>'
                else:
                    html_end += '<li onclick="onclick3(' + str(
                        i) + "," + table_id + "," + url + ')"><a >' + str(i) + '</a></li>'
            if not (page == p_length):
                html_end += '<li id="page_down" onclick="onclick2(' + str(
                    page) + "," + table_id + "," + url + ')"><a  aria-label="Next"><span aria-hidden="true">&raquo;</span></a></li>'
            html_end += '</ul></div>'
        elif (p_length - 3 < page):
            html_end += '<div id="pagin" style="text-align:center;"><ul class="pagination"><li onclick="onclick1(' + str(
                page) + "," + table_id + "," + url + ')" id="page_up"><a  aria-label="Previous"><span aria-hidden="true">&laquo;</span></a></li>'
            for i in range(p_length - 6, p_length + 1):
                if i == page:
                    html_end += '<li onclick="onclick3(' + str(
                        i) + "," + table_id + "," + url + ')" id="active" class="active"><a >' + str(i) + '</a></li>'
                else:
                    html_end += '<li onclick="onclick3(' + str(
                        i) + "," + table_id + "," + url + ')"><a >' + str(i) + '</a></li>'
            if not (page == p_length):
                html_end += '<li id="page_down" onclick="onclick2(' + str(
                    page) + "," + table_id + "," + url + ')"><a  aria-label="Next"><span aria-hidden="true">&raquo;</span></a></li>'
            html_end += '</ul></div>'
        elif (p_length - 3 >= page):
            html_end += '<div id="pagin" style="text-align:center;"><ul class="pagination">'
            if not (page == 1):
                html_end += '<li id="page_up" onclick="onclick1(' + str(
                    page) + "," + table_id + "," + url + ')"><a aria-label="Previous"><span aria-hidden="true">&laquo;</span></a></li>'
            if page - 3 <= 0:
                min = 1
                max = 8
            else:
                min = page - 3
                max = page + 3 + 1
            for i in range(min, max):
                if i == page:
                    html_end += '<li onclick="onclick3(' + str(
                        i) + ',' + table_id + ',' + '"' + url + '"' + ')" id="active" class="active"><a >' + str(
                        i) + '</a></li>'
                else:
                    html_end += '<li onclick="onclick3(' + str(
                        i) + "," + table_id + "," + url + ')"><a >' + str(i) + '</a></li>'
            if not (page == p_length):
                html_end += '<li id="page_down" onclick="onclick2(' + str(
                    page) + "," + table_id + "," + url + ')"><a  aria-label="Next"><span aria-hidden="true">&raquo;</span></a></li>'
            html_end += '</ul></div>'

        count = 0
        if p.count <= page * page_length:
            p_max = p.count
        else:
            p_max = page * page_length
        for message in range((page - 1) * page_length, p_max):
            count += 1
            if count == 1:
                mess = r'<tr class="success"><th>' + str(message_all[message]["id"]) + r'</th><th>' + \
                       message_all[message]["name"] + r'</th><th>' + message_all[message]["level"] + r'</th><th>' + \
                       message_all[message]["name_2"] + r'</th><th>' + message_all[message]["name_st"] + r'</th><th>' + \
                       message_all[message][
                           "time"] + r'</th><th><a href=' + './meetingpaperid=' + str(
                    message_all[message]["id"]) + 'already' + r'>' + message_all[message]["is_checked"] + '</a></th>'
            else:
                mess = r'<tr><th>' + str(message_all[message]["id"]) + r'</th><th>' + message_all[message][
                    "name"] + r'</th><th>' + message_all[message]["level"] + r'</th><th>' + message_all[message][
                           "name_2"] + r'</th><th>' + message_all[message]["name_st"] + r'</th><th>' + \
                       message_all[message][
                           "time"] + r'</th><th><a href=' + './meetingpaperid=' + str(
                    message_all[message]["id"]) + 'already' + r'>' + message_all[message]["is_checked"] + '</a></th>'
            html_middle += mess

        return HttpResponse(html_head + html_middle + html_end)
    elif(select=='专利'):
        page = int(page)
        table_id = "'my_table_7'"
        url = "'already'"
        # 获取所有的期刊论文数据

        page_length = 10
        try:
            mags = Honor_patent.objects.filter(~Q(honor_patent_is_checked=0))
            if (len(mags) == 0):
                return HttpResponse('<h4 style="color:red">无此项数据的记录<small>你可以选择其他的选项进行访问3</small></h4>')
        except Exception:
            return HttpResponse('<h4 style="color:red">无此项数据的记录<small>你可以选择其他的选项进行访问4</small></h4>')
        # 获取返回数据（从期刊论文表审核表中） 并进行分页操作
        html_head = '<table class="table table-striped table-bordered table-condensed"><thead><tr class="info"><th>序号</th><th>专利名称</th><th>专利级别</th><th>专利号</th><th>姓名</th><th>审核时间</th><th>审核状态</th></tr></thead><tbody>'
        html_middle = ''
        html_end = '</tbody></table>'
        message_all = []
        message_listing = []
        message_already = []
        for mag in mags:
            if mag.honor_patent_is_checked == 2:
                message_listing.append(mag)
            else:
                message_already.append(mag)

        for mag in message_already:
            id = mag.id  # 提交号
            name = mag.honor_patent_name  # 名称r
            level = mag.honor_patent_type  # 级别
            name_2 = mag.honor_patent_number  # 刊物名称
            forigen_st = mag.student  # 学生外键
            name_st = forigen_st.student_name  # 提交人
            time = str(mag.honor_patent_check_time)  # 提交时间
            is_checked = mag.honor_patent_is_checked
            if is_checked == 1:
                is_checked = '审核通过'
            elif is_checked == 0:
                is_checked = '未审核'
            elif is_checked == -1:
                is_checked = '审核不通过'
            elif is_checked == 2:
                is_checked = '正在审核'
            message = {"id": id, "name": name, "level": level, "name_2": name_2, "name_st": name_st,
                       "time": time, 'is_checked': is_checked}  # 记录数据的字典
            message_all.append(message);
        for mag in message_listing:
            id = mag.id  # 提交号
            name = mag.honor_patent_name  # 名称r
            level = mag.honor_patent_type  # 级别
            name_2 = mag.honor_patent_number  # 刊物名称
            forigen_st = mag.student  # 学生外键
            name_st = forigen_st.student_name  # 提交人
            time = str(mag.honor_patent_check_time)  # 提交时间
            is_checked = mag.honor_patent_is_checked
            if is_checked == 1:
                is_checked = '审核通过'
            elif is_checked == 0:
                is_checked = '未审核'
            elif is_checked == -1:
                is_checked = '审核不通过'
            elif is_checked == 2:
                is_checked = '正在审核'
            message = {"id": id, "name": name, "level": level, "name_2": name_2, "name_st": name_st,
                       "time": time, 'is_checked': is_checked}  # 记录数据的字典
            message_all.append(message);
        # 分页
        message_all.reverse()
        p = Paginator(message_all, page_length)
        p_length = p.num_pages

        if (p_length < 7):
            html_end += '<div id="pagin" style="text-align:center;"><ul class="pagination">'
            if not (page == 1):
                html_end += '<li id="page_up" onclick="onclick1(' + str(
                    page) + "," + table_id + "," + url + ')"><a  aria-label="Previous"><span aria-hidden="true">&laquo;</span></a></li>'
            for i in range(1, p_length + 1):
                if i == page:
                    html_end += '<li onclick="onclick3(' + str(
                        i) + "," + table_id + "," + url + ')" id="active" class="active"><a >' + str(i) + '</a></li>'
                else:
                    html_end += '<li onclick="onclick3(' + str(
                        i) + "," + table_id + "," + url + ')"><a >' + str(i) + '</a></li>'
            if not (page == p_length):
                html_end += '<li id="page_down" onclick="onclick2(' + str(
                    page) + "," + table_id + "," + url + ')"><a  aria-label="Next"><span aria-hidden="true">&raquo;</span></a></li>'
            html_end += '</ul></div>'
        elif (p_length - 3 < page):
            html_end += '<div id="pagin" style="text-align:center;"><ul class="pagination"><li onclick="onclick1(' + str(
                page) + "," + table_id + "," + url + ')" id="page_up"><a  aria-label="Previous"><span aria-hidden="true">&laquo;</span></a></li>'
            for i in range(p_length - 6, p_length + 1):
                if i == page:
                    html_end += '<li onclick="onclick3(' + str(
                        i) + "," + table_id + "," + url + ')" id="active" class="active"><a >' + str(i) + '</a></li>'
                else:
                    html_end += '<li onclick="onclick3(' + str(
                        i) + "," + table_id + "," + url + ')"><a >' + str(i) + '</a></li>'
            if not (page == p_length):
                html_end += '<li id="page_down" onclick="onclick2(' + str(
                    page) + "," + table_id + "," + url + ')"><a  aria-label="Next"><span aria-hidden="true">&raquo;</span></a></li>'
            html_end += '</ul></div>'
        elif (p_length - 3 >= page):
            html_end += '<div id="pagin" style="text-align:center;"><ul class="pagination">'
            if not (page == 1):
                html_end += '<li id="page_up" onclick="onclick1(' + str(
                    page) + "," + table_id + "," + url + ')"><a aria-label="Previous"><span aria-hidden="true">&laquo;</span></a></li>'
            if page - 3 <= 0:
                min = 1
                max = 8
            else:
                min = page - 3
                max = page + 3 + 1
            for i in range(min, max):
                if i == page:
                    html_end += '<li onclick="onclick3(' + str(
                        i) + ',' + table_id + ',' + '"' + url + '"' + ')" id="active" class="active"><a >' + str(
                        i) + '</a></li>'
                else:
                    html_end += '<li onclick="onclick3(' + str(
                        i) + "," + table_id + "," + url + ')"><a >' + str(i) + '</a></li>'
            if not (page == p_length):
                html_end += '<li id="page_down" onclick="onclick2(' + str(
                    page) + "," + table_id + "," + url + ')"><a  aria-label="Next"><span aria-hidden="true">&raquo;</span></a></li>'
            html_end += '</ul></div>'

        count = 0
        if p.count <= page * page_length:
            p_max = p.count
        else:
            p_max = page * page_length
        for message in range((page - 1) * page_length, p_max):
            count += 1
            if count == 1:
                mess = r'<tr class="success"><th>' + str(message_all[message]["id"]) + r'</th><th>' + \
                       message_all[message]["name"] + r'</th><th>' + message_all[message]["level"] + r'</th><th>' + \
                       message_all[message]["name_2"] + r'</th><th>' + message_all[message]["name_st"] + r'</th><th>' + \
                       message_all[message][
                           "time"] + r'</th><th><a href=' + './patentid=' + str(
                    message_all[message]["id"]) + 'already' + r'>' + message_all[message]["is_checked"] + '</a></th>'
            else:
                mess = r'<tr><th>' + str(message_all[message]["id"]) + r'</th><th>' + message_all[message][
                    "name"] + r'</th><th>' + message_all[message]["level"] + r'</th><th>' + message_all[message][
                           "name_2"] + r'</th><th>' + message_all[message]["name_st"] + r'</th><th>' + \
                       message_all[message][
                           "time"] + r'</th><th><a href=' + './patentid=' + str(
                    message_all[message]["id"]) + 'already' + r'>' + message_all[message]["is_checked"] + '</a></th>'
            html_middle += mess

        return HttpResponse(html_head + html_middle + html_end)
    elif(select=='奖学金'):
        page = int(page)
        table_id = "'my_table_7'"
        url = "'already'"
        # 获取所有的期刊论文数据

        page_length = 10
        try:
            mags = Honor_scholarship.objects.filter(~Q(honor_scholarship_is_checked=0))
            if (len(mags) == 0):
                return HttpResponse('<h4 style="color:red">无此项数据的记录<small>你可以选择其他的选项进行访问3</small></h4>')
        except Exception:
            return HttpResponse('<h4 style="color:red">无此项数据的记录<small>你可以选择其他的选项进行访问4</small></h4>')
        # 获取返回数据（从期刊论文表审核表中） 并进行分页操作
        html_head = '<table class="table table-striped table-bordered table-condensed"><thead><tr class="info"><th>序号</th><th>奖学金名称</th><th>获奖年度</th><th>获奖金额</th><th>姓名</th><th>审核时间</th><th>审核状态</th></tr></thead><tbody>'
        html_middle = ''
        html_end = '</tbody></table>'
        message_all = []
        message_listing = []
        message_already = []
        for mag in mags:
            if mag.honor_scholarship_is_checked == 2:
                message_listing.append(mag)
            else:
                message_already.append(mag)

        for mag in message_already:
            id = mag.id  # 提交号
            name = mag.honor_scholarship_name  # 名称r
            level = mag.honor_scholarship_year  # 级别
            name_2 = mag.honor_scholarship_moneyperyear  # 刊物名称
            forigen_st = mag.student  # 学生外键
            name_st = forigen_st.student_name  # 提交人
            time = str(mag.honor_scholarship_check_time)  # 提交时间
            is_checked = mag.honor_scholarship_is_checked
            if is_checked == 1:
                is_checked = '审核通过'
            elif is_checked == 0:
                is_checked = '未审核'
            elif is_checked == -1:
                is_checked = '审核不通过'
            elif is_checked == 2:
                is_checked = '正在审核'
            message = {"id": id, "name": name, "level": level, "name_2": name_2, "name_st": name_st,
                       "time": time, 'is_checked': is_checked}  # 记录数据的字典
            message_all.append(message);
        for mag in message_listing:
            id = mag.id  # 提交号
            name = mag.honor_scholarship_name  # 名称r
            level = mag.honor_scholarship_year  # 级别
            name_2 = mag.honor_scholarship_moneyperyear  # 刊物名称
            forigen_st = mag.student  # 学生外键
            name_st = forigen_st.student_name  # 提交人
            time = str(mag.honor_scholarship_check_time)  # 提交时间
            is_checked = mag.honor_scholarship_is_checked
            if is_checked == 1:
                is_checked = '审核通过'
            elif is_checked == 0:
                is_checked = '未审核'
            elif is_checked == -1:
                is_checked = '审核不通过'
            elif is_checked == 2:
                is_checked = '正在审核'
            message = {"id": id, "name": name, "level": level, "name_2": name_2, "name_st": name_st,
                       "time": time, 'is_checked': is_checked}  # 记录数据的字典
            message_all.append(message);z
        # 分页
        message_all.reverse()
        p = Paginator(message_all, page_length)
        p_length = p.num_pages

        if (p_length < 7):
            html_end += '<div id="pagin" style="text-align:center;"><ul class="pagination">'
            if not (page == 1):
                html_end += '<li id="page_up" onclick="onclick1(' + str(
                    page) + "," + table_id + "," + url + ')"><a  aria-label="Previous"><span aria-hidden="true">&laquo;</span></a></li>'
            for i in range(1, p_length + 1):
                if i == page:
                    html_end += '<li onclick="onclick3(' + str(
                        i) + "," + table_id + "," + url + ')" id="active" class="active"><a >' + str(i) + '</a></li>'
                else:
                    html_end += '<li onclick="onclick3(' + str(
                        i) + "," + table_id + "," + url + ')"><a >' + str(i) + '</a></li>'
            if not (page == p_length):
                html_end += '<li id="page_down" onclick="onclick2(' + str(
                    page) + "," + table_id + "," + url + ')"><a  aria-label="Next"><span aria-hidden="true">&raquo;</span></a></li>'
            html_end += '</ul></div>'
        elif (p_length - 3 < page):
            html_end += '<div id="pagin" style="text-align:center;"><ul class="pagination"><li onclick="onclick1(' + str(
                page) + "," + table_id + "," + url + ')" id="page_up"><a  aria-label="Previous"><span aria-hidden="true">&laquo;</span></a></li>'
            for i in range(p_length - 6, p_length + 1):
                if i == page:
                    html_end += '<li onclick="onclick3(' + str(
                        i) + "," + table_id + "," + url + ')" id="active" class="active"><a >' + str(i) + '</a></li>'
                else:
                    html_end += '<li onclick="onclick3(' + str(
                        i) + "," + table_id + "," + url + ')"><a >' + str(i) + '</a></li>'
            if not (page == p_length):
                html_end += '<li id="page_down" onclick="onclick2(' + str(
                    page) + "," + table_id + "," + url + ')"><a  aria-label="Next"><span aria-hidden="true">&raquo;</span></a></li>'
            html_end += '</ul></div>'
        elif (p_length - 3 >= page):
            html_end += '<div id="pagin" style="text-align:center;"><ul class="pagination">'
            if not (page == 1):
                html_end += '<li id="page_up" onclick="onclick1(' + str(
                    page) + "," + table_id + "," + url + ')"><a aria-label="Previous"><span aria-hidden="true">&laquo;</span></a></li>'
            if page - 3 <= 0:
                min = 1
                max = 8
            else:
                min = page - 3
                max = page + 3 + 1
            for i in range(min, max):
                if i == page:
                    html_end += '<li onclick="onclick3(' + str(
                        i) + ',' + table_id + ',' + '"' + url + '"' + ')" id="active" class="active"><a >' + str(
                        i) + '</a></li>'
                else:
                    html_end += '<li onclick="onclick3(' + str(
                        i) + "," + table_id + "," + url + ')"><a >' + str(i) + '</a></li>'
            if not (page == p_length):
                html_end += '<li id="page_down" onclick="onclick2(' + str(
                    page) + "," + table_id + "," + url + ')"><a  aria-label="Next"><span aria-hidden="true">&raquo;</span></a></li>'
            html_end += '</ul></div>'

        count = 0
        if p.count <= page * page_length:
            p_max = p.count
        else:
            p_max = page * page_length
        for message in range((page - 1) * page_length, p_max):
            count += 1
            if count == 1:
                mess = r'<tr class="success"><th>' + str(message_all[message]["id"]) + r'</th><th>' +message_all[message]["name"] + r'</th><th>' + message_all[message]["level"] + r'</th><th>' + str(message_all[message]["name_2"]) + r'</th><th>' + message_all[message]["name_st"] + r'</th><th>' + message_all[message]["time"] + r'</th><th><a href=' + './prizeid=' + str(message_all[message]["id"]) + 'already' + r'>' + message_all[message]["is_checked"] + '</a></th>'
                html_middle += mess
            else:
                mess = r'<tr><th>' + str(message_all[message]["id"]) + r'</th><th>' + message_all[message]["name"] + r'</th><th>' + message_all[message]["level"] + r'</th><th>' + str(message_all[message]["name_2"]) + r'</th><th>' + message_all[message]["name_st"] + r'</th><th>' + message_all[message]["time"] + r'</th><th><a href=' + './prizeid=' + str(message_all[message]["id"]) + 'already' + r'>' + message_all[message]["is_checked"] + '</a></th>'
                html_middle += mess

        return HttpResponse(html_head + html_middle + html_end)
    elif(select=='社会经历'):
        page = int(page)
        table_id = "'my_table_7'"
        url = "'already'"
        # 获取所有的期刊论文数据

        page_length = 10
        try:
            mags = Honor_experience.objects.filter(~Q(honor_experience_is_checked=0))
            if (len(mags) == 0):
                return HttpResponse('<h4 style="color:red">无此项数据的记录<small>你可以选择其他的选项进行访问3</small></h4>')
        except Exception:
            return HttpResponse('<h4 style="color:red">无此项数据的记录<small>你可以选择其他的选项进行访问4</small></h4>')
        # 获取返回数据（从期刊论文表审核表中） 并进行分页操作
        html_head = '<table class="table table-striped table-bordered table-condensed"><thead><tr class="info"><th>序号</th><th>活动名称</th><th>活动单位</th><th>活动开始时间</th><th>姓名</th><th>审核时间</th><th>审核状态</th></tr></thead><tbody>'
        html_middle = ''
        html_end = '</tbody></table>'
        message_all = []
        message_listing = []
        message_already = []
        for mag in mags:
            if mag.honor_experience_is_checked == 2:
                message_listing.append(mag)
            else:
                message_already.append(mag)
        for mag in message_listing:
            id = mag.id  # 提交号
            name = mag.honor_experience_name  # 名称r
            level = mag.honor_experience_authority  # 级别
            name_2 = mag.honor_experience_start  # 刊物名称
            forigen_st = mag.student  # 学生外键
            name_st = forigen_st.student_name  # 提交人
            time = str(mag.honor_experience_check_time)  # 提交时间
            is_checked = mag.honor_experience_is_checked
            if is_checked == 1:
                is_checked = '审核通过'
            elif is_checked == 0:
                is_checked = '未审核'
            elif is_checked == -1:
                is_checked = '审核不通过'
            elif is_checked == 2:
                is_checked = '正在审核'
            message = {"id": id, "name": name, "level": level, "name_2": name_2, "name_st": name_st,
                       "time": time, 'is_checked': is_checked}  # 记录数据的字典
            message_all.append(message);
        for mag in message_already:
            id = mag.id  # 提交号
            name = mag.honor_experience_name  # 名称r
            level = mag.honor_experience_authority  # 级别
            name_2 = mag.honor_experience_start  # 刊物名称
            forigen_st = mag.student  # 学生外键
            name_st = forigen_st.student_name  # 提交人
            time = str(mag.honor_experience_check_time)  # 提交时间
            is_checked = mag.honor_experience_is_checked
            if is_checked == 1:
                is_checked = '审核通过'
            elif is_checked == 0:
                is_checked = '未审核'
            elif is_checked == -1:
                is_checked = '审核不通过'
            elif is_checked == 2:
                is_checked = '正在审核'
            message = {"id": id, "name": name, "level": level, "name_2": name_2, "name_st": name_st,
                       "time": time, 'is_checked': is_checked}  # 记录数据的字典
            message_all.append(message);
        # 分页
        message_all.reverse()
        p = Paginator(message_all, page_length)
        p_length = p.num_pages

        if (p_length < 7):
            html_end += '<div id="pagin" style="text-align:center;"><ul class="pagination">'
            if not (page == 1):
                html_end += '<li id="page_up" onclick="onclick1(' + str(
                    page) + "," + table_id + "," + url + ')"><a  aria-label="Previous"><span aria-hidden="true">&laquo;</span></a></li>'
            for i in range(1, p_length + 1):
                if i == page:
                    html_end += '<li onclick="onclick3(' + str(
                        i) + "," + table_id + "," + url + ')" id="active" class="active"><a >' + str(i) + '</a></li>'
                else:
                    html_end += '<li onclick="onclick3(' + str(
                        i) + "," + table_id + "," + url + ')"><a >' + str(i) + '</a></li>'
            if not (page == p_length):
                html_end += '<li id="page_down" onclick="onclick2(' + str(
                    page) + "," + table_id + "," + url + ')"><a  aria-label="Next"><span aria-hidden="true">&raquo;</span></a></li>'
            html_end += '</ul></div>'
        elif (p_length - 3 < page):
            html_end += '<div id="pagin" style="text-align:center;"><ul class="pagination"><li onclick="onclick1(' + str(
                page) + "," + table_id + "," + url + ')" id="page_up"><a  aria-label="Previous"><span aria-hidden="true">&laquo;</span></a></li>'
            for i in range(p_length - 6, p_length + 1):
                if i == page:
                    html_end += '<li onclick="onclick3(' + str(
                        i) + "," + table_id + "," + url + ')" id="active" class="active"><a >' + str(i) + '</a></li>'
                else:
                    html_end += '<li onclick="onclick3(' + str(
                        i) + "," + table_id + "," + url + ')"><a >' + str(i) + '</a></li>'
            if not (page == p_length):
                html_end += '<li id="page_down" onclick="onclick2(' + str(
                    page) + "," + table_id + "," + url + ')"><a  aria-label="Next"><span aria-hidden="true">&raquo;</span></a></li>'
            html_end += '</ul></div>'
        elif (p_length - 3 >= page):
            html_end += '<div id="pagin" style="text-align:center;"><ul class="pagination">'
            if not (page == 1):
                html_end += '<li id="page_up" onclick="onclick1(' + str(
                    page) + "," + table_id + "," + url + ')"><a aria-label="Previous"><span aria-hidden="true">&laquo;</span></a></li>'
            if page - 3 <= 0:
                min = 1
                max = 8
            else:
                min = page - 3
                max = page + 3 + 1
            for i in range(min, max):
                if i == page:
                    html_end += '<li onclick="onclick3(' + str(
                        i) + ',' + table_id + ',' + '"' + url + '"' + ')" id="active" class="active"><a >' + str(
                        i) + '</a></li>'
                else:
                    html_end += '<li onclick="onclick3(' + str(
                        i) + "," + table_id + "," + url + ')"><a >' + str(i) + '</a></li>'
            if not (page == p_length):
                html_end += '<li id="page_down" onclick="onclick2(' + str(
                    page) + "," + table_id + "," + url + ')"><a  aria-label="Next"><span aria-hidden="true">&raquo;</span></a></li>'
            html_end += '</ul></div>'

        count = 0
        if p.count <= page * page_length:
            p_max = p.count
        else:
            p_max = page * page_length
        for message in range((page - 1) * page_length, p_max):
            count += 1
            if count == 1:
                mess = r'<tr class="success"><th>' + str(message_all[message]["id"]) + r'</th><th>' + message_all[message]["name"] + r'</th><th>' + message_all[message]["level"] + r'</th><th>' + str(message_all[message]["name_2"]) + r'</th><th>' + message_all[message]["name_st"] + r'</th><th>' + message_all[message]["time"] + r'</th><th><a href=' + './experienceid=' + str(message_all[message]["id"]) + 'already' + r'>' + message_all[message]["is_checked"] + '</a></th>'
                html_middle += mess
            else:
                mess = r'<tr><th>' + str(message_all[message]["id"]) + r'</th><th>' + message_all[message]["name"] + r'</th><th>' + message_all[message]["level"] + r'</th><th>' + str(message_all[message]["name_2"]) + r'</th><th>' + message_all[message]["name_st"] + r'</th><th>' + message_all[message]["time"] + r'</th><th><a href=' + './experienceid=' + str(message_all[message]["id"]) + 'already' + r'>' + message_all[message]["is_checked"] + '</a></th>'
                html_middle += mess

        return HttpResponse(html_head + html_middle + html_end)
    elif(select=='全部'):
        pass


def competition_success(request,id,already):
    # return HttpResponse(request.session.get('sessionid',''))
    # return HttpResponse(already==None)
    # return HttpResponse(id)
    try:
        if request.session.get('sessionid',''):
            teacher_id=request.session.get('sessionid','')
            teacher=Teacher.objects.get(teacher_id=teacher_id)
        else:
            return render(request,"404.html")


        com=Honor_competition.objects.get(id=id)
        if request.method=="POST":
            com_point=request.POST.get('point',0)
            com.competition_point=com_point
            if com.honor_competition_is_checked!=1:
                student = com.student
                wall = Student_honorwall.objects.get(student=student)
                wall.student_competition_number+=1
                # wall.student_competition_score+=com_point
                wall.save()
        com.honor_competition_is_checked=1
        com.teacher=teacher
        com.honor_competition_check_time=datetime.now()
        com.save()

    except:
        return render(request,"404.html")
    try:
        if not already:
            message=Honor_competition.objects.filter(honor_competition_is_checked=0)[0]
        else:
            message=Honor_competition.objects.filter(~Q(honor_competition_is_checked=0),id__gt=id)[0]
    except IndexError:
        if not already:
            return render(request, "teacher_center_checking.html", {'none': 1,'competition':1})
        else:
            return render(request, "teacher_center_already.html", {'none': 1})
    is_checked=message.honor_competition_is_checked
    if is_checked==1:
        is_checked='审核通过'
    elif is_checked==0:
        is_checked='未审核'
    elif is_checked==-1:
        is_checked='审核不通过'
    elif is_checked==2:
        is_checked='正在审核'
    if not already:
        return render(request,"teacher_center_competition.html",{'message':message,'is_checked':is_checked})
    else:
        return render(request,"teacher_center_competition.html",{'message':message,'is_checked':is_checked,'already':1})
def competition_fail(request,id,already=None):
    try:
        if request.session.get('sessionid',''):
            teacher_id=request.session.get('sessionid','')
            teacher=Teacher.objects.get(teacher_id=teacher_id)
        else:
            return render(request,"404.html")
        com=Honor_competition.objects.get(id=id)
        if com.honor_competition_is_checked==1:
            student = com.student
            wall = Student_honorwall.objects.get(student=student)
            wall.student_competition_number-=1;
            # wall.student_competition_score-=com.honor_competition_point
            wall.save()
        com.teacher=teacher
        com.honor_competition_check_time=datetime.now()
        com.honor_competition_is_checked=-1
        com.save()
    except:
        return render(request,"404.html")
    try:
        if not already:
            message=Honor_competition.objects.filter(honor_competition_is_checked=0)[0]
        else:
            message = Honor_competition.objects.filter(~Q(honor_competition_is_checked=0),id__gt=id)[0]
    except IndexError:
        if not already:
            return render(request, "teacher_center_checking.html", {'none': 1,'competition':1})
        else:
            return render(request, "teacher_center_already.html", {'none': 1})
    is_checked = message.honor_competition_is_checked
    if is_checked == 1:
        is_checked = '审核通过'
    elif is_checked == 0:
        is_checked = '未审核'
    elif is_checked == -1:
        is_checked = '审核不通过'
    elif is_checked == 2:
        is_checked = '正在审核'
    if not already:
        return render(request,"teacher_center_competition.html",{'message':message,'is_checked':is_checked})
    else:
        return render(request, "teacher_center_competition.html", {'message': message, 'is_checked': is_checked,'already':1})

def competition_next(request,id,already=None):
    try:
        if request.session.get('sessionid',''):
            teacher_id=request.session.get('sessionid','')
            teacher=Teacher.objects.get(teacher_id=teacher_id)
        else:
            return render(request,"404.html")
        com=Honor_competition.objects.get(id=id)
        com.teacher=teacher
        com.honor_competition_check_time=datetime.now()
        if com.honor_competition_is_checked==2:
            com.honor_competition_is_checked=0
        com.save()
    except:
        return render(request,"404.html")
    try:
        if not already:
            message=Honor_competition.objects.filter(honor_competition_is_checked=0)[0]
        else:
            message = Honor_competition.objects.filter(~Q(honor_competition_is_checked=0),id__gt=id)[0]
        if message.honor_competition_is_checked==0:
            message.honor_competition_is_checked=2
            message.save()
    except IndexError:
        if not already:
            return render(request, "teacher_center_checking.html", {'none': 1,'competition':1})
        else:
            return render(request, "teacher_center_already.html", {'none': 1})
    is_checked = message.honor_competition_is_checked
    if is_checked == 1:
        is_checked = '审核通过'
    elif is_checked == 0:
        is_checked = '未审核'
    elif is_checked == -1:
        is_checked = '审核不通过'
    elif is_checked == 2:
        is_checked = '正在审核'
    if not already:
        return render(request, "teacher_center_competition.html", {'message': message, 'is_checked': is_checked})
    else:
        return render(request, "teacher_center_competition.html",
                      {'message': message, 'is_checked': is_checked, 'already': 1})





def experience_success(request,id,already=None):
    # return HttpResponse(request.session.get('sessionid',''))
    try:
        if request.session.get('sessionid',''):
            teacher_id=request.session.get('sessionid','')
            teacher=Teacher.objects.get(teacher_id=teacher_id)
        else:
            return render(request,"404.html")


        com=Honor_experience.objects.get(id=id)
        if request.method=="POST":
            com_point=request.POST.get('point',0)
            com.honor_experience_point=com_point
            if com.honor_experience_is_checked!=1:
                student=com.student
                wall=Student_honorwall.objects.get(student=student)
                wall.student_experience_number+=1
                # wall.student_experience_score+=com_point
                wall.save()
        com.honor_experience_is_checked=1
        com.teacher=teacher
        com.honor_experience_check_time=datetime.now()
        com.save()

    except:
        return render(request,"404.html")
    try:
        if not already:
            message=Honor_experience.objects.filter(honor_experience_is_checked=0)[0]
        else:
            message=Honor_experience.objects.filter(~Q(honor_experience_is_checked=0),id__gt=id)[0]
    except IndexError:
        if not already:
            return render(request, "teacher_center_checking.html", {'none': 1,'experience':1})
        else:
            return render(request, "teacher_center_already.html", {'none': 1})
    is_checked = message.honor_experience_is_checked
    if is_checked == 1:
        is_checked = '审核通过'
    elif is_checked == 0:
        is_checked = '未审核'
    elif is_checked == -1:
        is_checked = '审核不通过'
    elif is_checked == 2:
        is_checked = '正在审核'
    if not already:
        return render(request,"teacher_center_experience.html",{'message':message,'is_checked':is_checked})
    else:
        return render(request,"teacher_center_experience.html",{'message':message,'is_checked':is_checked,'already':1})
def experience_fail(request,id,already=None):
    try:
        if request.session.get('sessionid',''):
            teacher_id=request.session.get('sessionid','')
            teacher=Teacher.objects.get(teacher_id=teacher_id)
        else:
            return render(request,"404.html")
        com=Honor_experience.objects.get(id=id)
        if com.honor_experience_is_checked==1:
            student = com.student
            wall = Student_honorwall.objects.get(student=student)
            wall.student_experience_number -= 1;
            # wall.student_experience_score -= com.honor_experience_point
            wall.save()
        com.teacher=teacher
        com.honor_experience_check_time=datetime.now()
        com.honor_experience_is_checked=-1
        com.save()
    except:
        return render(request,"404.html")
    try:
        if not already:
            message=Honor_experience.objects.filter(honor_experience_is_checked=0)[0]
        else:
            message=Honor_experience.objects.filter(~Q(honor_experience_is_checked=0),id__gt=id)[0]
    except IndexError:
        if not already:
            return render(request, "teacher_center_checking.html", {'none': 1,'experience':1})
        else:
            return render(request,"teacher_center_already.html",{'none':1})
    is_checked = message.honor_experience_is_checked
    if is_checked == 1:
        is_checked = '审核通过'
    elif is_checked == 0:
        is_checked = '未审核'
    elif is_checked == -1:
        is_checked = '审核不通过'
    elif is_checked == 2:
        is_checked = '正在审核'
    if not already:
        return render(request,"teacher_center_experience.html",{'message':message,'is_checked':is_checked})
    else:
        return render(request,"teacher_center_experience.html",{'message':message,'is_checked':is_checked,'already':1})

def experience_next(request,id,already=None):
    try:
        if request.session.get('sessionid',''):
            teacher_id=request.session.get('sessionid','')
            teacher=Teacher.objects.get(teacher_id=teacher_id)
        else:
            return render(request,"404.html")
        com=Honor_experience.objects.get(id=id)
        com.teacher=teacher
        com.honor_experience_check_time=datetime.now()
        if com.honor_experience_is_checked==2:
            com.honor_experience_is_checked=0;
        com.save()
    except:
        return render(request,"404.html")
    try:
        if not already:
            message=Honor_experience.objects.filter(honor_experience_is_checked=0)[0]
        else:
            message=Honor_experience.objects.filter(~Q(honor_experience_is_checked=0),id__gt=id)[0]
        if message.honor_experience_is_checked==0:
            message.honor_experience_is_checked = 2
            message.save()
    except IndexError:
        if not already:
            return render(request, "teacher_center_checking.html", {'none': 1,'experience':1})
        else:
            return render(request,"teacher_center_already.html",{'none':1})
    is_checked = message.honor_experience_is_checked
    if is_checked == 1:
        is_checked = '审核通过'
    elif is_checked == 0:
        is_checked = '未审核'
    elif is_checked == -1:
        is_checked = '审核不通过'
    elif is_checked == 2:
        is_checked = '正在审核'
    if not already:
        return render(request,"teacher_center_experience.html",{'message':message,'is_checked':is_checked})
    else:
        return render(request,"teacher_center_experience.html",{'message':message,'is_checked':is_checked,'already':1})

def magazinepaper_success(request,id,already=None):
    # return HttpResponse(request.session.get('sessionid',''))
    try:
        if request.session.get('sessionid',''):
            teacher_id=request.session.get('sessionid','')
            teacher=Teacher.objects.get(teacher_id=teacher_id)
        else:
            return render(request,"404.html")


        com=Honor_paper_magazine.objects.get(id=id)

        if request.method=="POST":
            com_point=request.POST.get('point',0)
            if com.honor_paper_meeting_is_checked != 1:
                student=com.student
                wall=Student_honorwall.objects.get(student=student)
                wall.student_paper_magazine_number+=1
                # wall.student_paper_magazine_score+=com_point
                wall.save()
        com.honor_paper_magazine_is_checked=1
        com.teacher=teacher
        com.honor_paper_magazine_check_time=datetime.now()
        com.save()

    except:
        return render(request,"404.html")
    try:
        if not already:
            message=Honor_paper_magazine.objects.filter(honor_paper_magazine_is_checked=0)[0]
        else:
            message=Honor_paper_magazine.objects.filter(~Q(honor_paper_magazine_is_checked=0),id__gt=id)[0]

    except IndexError:
        if not already:
            return render(request, "teacher_center_checking.html", {'none': 1,'magazinepaper':1})
        else:
            return render(request, "teacher_center_already.html", {'none': 1})
    is_checked = message.honor_paper_magazine_is_checked
    if is_checked == 1:
        is_checked = '审核通过'
    elif is_checked == 0:
        is_checked = '未审核'
    elif is_checked == -1:
        is_checked = '审核不通过'
    elif is_checked == 2:
        is_checked = '正在审核'
    if not already:
        return render(request,"teacher_center_magazinepaper.html",{'message':message,'is_checked':is_checked})
    else:
        return render(request, "teacher_center_magazinepaper.html", {'message': message, 'is_checked': is_checked,'already':1})
def magazinepaper_fail(request,id,already=None):
    try:
        if request.session.get('sessionid',''):
            teacher_id=request.session.get('sessionid','')
            teacher=Teacher.objects.get(teacher_id=teacher_id)
        else:
            return render(request,"404.html")
        com=Honor_paper_magazine.objects.get(id=id)
        if com.honor_paper_magazine_is_checked==1:
            student = com.student
            wall = Student_honorwall.objects.get(student=student)
            wall.student_paper_magazine_number -= 1;
            # wall.student_paper_magazine_score -= com.honor_paper_magazine_point
            wall.save()
        com.teacher=teacher
        com.honor_paper_magazine_check_time=datetime.now()
        com.honor_paper_magazine_is_checked=-1
        com.save()
    except:
        return render(request,"404.html")
    try:
        if not already:
            message=Honor_paper_magazine.objects.filter(honor_paper_magazine_is_checked=0)[0]
        else:
            message = Honor_paper_magazine.objects.filter(~Q(honor_paper_magazine_is_checked=0),id__gt=id)[0]
    except IndexError:
        if not already:
            return render(request, "teacher_center_checking.html", {'none': 1,'magazinepaper':1})
        else:
            return render(request, "teacher_center_already.html", {'none': 1})
    is_checked = message.honor_paper_magazine_is_checked
    if is_checked == 1:
        is_checked = '审核通过'
    elif is_checked == 0:
        is_checked = '未审核'
    elif is_checked == -1:
        is_checked = '审核不通过'
    elif is_checked == 2:
        is_checked = '正在审核'
    if not already:
        return render(request,"teacher_center_magazinepaper.html",{'message':message,'is_checked':is_checked})
    else:
        return render(request, "teacher_center_magazinepaper.html", {'message': message, 'is_checked': is_checked,'already':already})

def magazinepaper_next(request,id,already=None):
    try:
        if request.session.get('sessionid',''):
            teacher_id=request.session.get('sessionid','')
            teacher=Teacher.objects.get(teacher_id=teacher_id)
        else:
            return render(request,"404.html")
        com=Honor_paper_magazine.objects.get(id=id)
        if com.honor_paper_magazine_is_checked==2:
            com.honor_paper_magazine_is_checked=0;
        com.teacher=teacher
        com.honor_paper_magazine_check_time=datetime.now()

        com.save()
    except:
        return render(request,"404.html")
    try:
        if not already:
            message=Honor_paper_magazine.objects.filter(honor_paper_magazine_is_checked=0)[0]
        else:
            message = Honor_paper_magazine.objects.filter(~Q(honor_paper_magazine_is_checked=0),id__gt=id)[0]
        if message.honor_paper_magazine_is_checked==0:
            message.honor_paper_magazine_is_checked = 2
            message.save()
    except IndexError:
        if not already:
            return render(request, "teacher_center_checking.html", {'none': 1,'magazinepaper':1})
        else:
            return render(request, "teacher_center_already.html", {'none': 1})
    is_checked = message.honor_paper_magazine_is_checked
    if is_checked == 1:
        is_checked = '审核通过'
    elif is_checked == 0:
        is_checked = '未审核'
    elif is_checked == -1:
        is_checked = '审核不通过'
    elif is_checked == 2:
        is_checked = '正在审核'
    if not already:
        return render(request,"teacher_center_magazinepaper.html",{'message':message,'is_checked':is_checked})
    else:
        return render(request, "teacher_center_magazinepaper.html", {'message': message, 'is_checked': is_checked,'already':already})

def meetingpaper_success(request,id,already=None):
    # return HttpResponse(request.session.get('sessionid',''))
    # return HttpResponse(id)
    try:
        if request.session.get('sessionid',''):
            teacher_id=request.session.get('sessionid','')
            teacher=Teacher.objects.get(teacher_id=teacher_id)
        else:
            return render(request,"404.html")

        com=Honor_paper_meeting.objects.get(id=id)

        if request.method=="POST":
            com_point=request.POST.get('point',0)
            com.honor_paper_meeting_point=com_point
            if com.honor_paper_meeting_is_checked != 1:
                student = com.student
                wall = Student_honorwall.objects.get(student=student)
                wall.student_paper_meeting_number += 1
                # wall.student_paper_meeting_score+=com_point
                wall.save()
        com.honor_paper_meeting_is_checked=1
        com.teacher=teacher
        com.honor_paper_meeting_check_time=datetime.now()
        com.save()

    except:
        return render(request,"404.html")
    try:
        if not already:
            message=Honor_paper_meeting.objects.filter(honor_paper_meeting_is_checked=0)[0]
        else:
            message=Honor_paper_meeting.objects.filter(~Q(honor_paper_meeting_is_checked=0),id__gt=id)[0]
    except IndexError:
        if not already:
            return render(request, "teacher_center_checking.html", {'none': 1,'meetingpaper':1})
        else:
            return render(request, "teacher_center_already.html", {'none': 1})
    is_checked = message.honor_paper_meeting_is_checked
    if is_checked == 1:
        is_checked = '审核通过'
    elif is_checked == 0:
        is_checked = '未审核'
    elif is_checked == -1:
        is_checked = '审核不通过'
    elif is_checked == 2:
        is_checked = '正在审核'
    if not already:
        return render(request,"teacher_center_meetingpaper.html",{'message':message,'is_checked':is_checked})
    else:
        return render(request, "teacher_center_meetingpaper.html", {'message': message, 'is_checked': is_checked,'already':1})
def meetingpaper_fail(request,id,already=None):
    try:
        if request.session.get('sessionid',''):
            teacher_id=request.session.get('sessionid','')
            teacher=Teacher.objects.get(teacher_id=teacher_id)
        else:
            return render(request,"404.html")
        com=Honor_paper_meeting.objects.get(id=id)
        if com.honor_paper_meeting_is_checked==1:
            student = com.student
            wall = Student_honorwall.objects.get(student=student)
            wall.student_paper_meeting_number -= 1;
            # wall.student_paper_meeting_score -= com.honor_paper_meeting_point
            wall.save()
        com.teacher=teacher
        com.honor_paper_meeting_check_time=datetime.now()
        com.honor_paper_meeting_is_checked=-1
        com.save()
    except:
        return render(request,"404.html")
    try:
        if not already:
            message=Honor_paper_meeting.objects.filter(honor_paper_meeting_is_checked=0)[0]
        else:
            message = Honor_paper_meeting.objects.filter(~Q(honor_paper_meeting_is_checked=0),id__gt=id)[0]
    except IndexError:
        if not already:
            return render(request, "teacher_center_checking.html", {'none': 1,'meetingpaper':1})
        else:
            return render(request, "teacher_center_already.html", {'none': 1})
    is_checked = message.honor_paper_meeting_is_checked
    if is_checked == 1:
        is_checked = '审核通过'
    elif is_checked == 0:
        is_checked = '未审核'
    elif is_checked == -1:
        is_checked = '审核不通过'
    elif is_checked == 2:
        is_checked = '正在审核'
    if not already:
        return render(request,"teacher_center_meetingpaper.html",{'message':message,'is_checked':is_checked})
    else:
        return render(request, "teacher_center_meetingpaper.html", {'message': message, 'is_checked': is_checked,'already':1})

def meetingpaper_next(request,id,already=None):
    try:
        if request.session.get('sessionid',''):
            teacher_id=request.session.get('sessionid','')
            teacher=Teacher.objects.get(teacher_id=teacher_id)
        else:
            return render(request,"404.html")
        com=Honor_paper_meeting.objects.get(id=id)
        if com.honor_paper_meeting_is_checked==2:
            com.honor_paper_meeting_is_checked=0
        com.teacher=teacher
        com.honor_paper_meeting_check_time=datetime.now()
        com.save()
    except:
        return render(request,"404.html")
    try:
        if not already:
            message=Honor_paper_meeting.objects.filter(honor_paper_meeting_is_checked=0)[0]
        else:
            message = Honor_paper_meeting.objects.filter(~Q(honor_paper_meeting_is_checked=0), id__gt=id)[0]
        if message.honor_paper_meeting_is_checked==0:
            message.honor_paper_meeting_is_checked = 2
            message.save()
    except IndexError:
        if not already:
            return render(request, "teacher_center_checking.html", {'none': 1,'meetingpaper':1})
        else:
            return render(request, "teacher_center_already.html", {'none': 1})
    is_checked = message.honor_paper_meeting_is_checked
    if is_checked == 1:
        is_checked = '审核通过'
    elif is_checked == 0:
        is_checked = '未审核'
    elif is_checked == -1:
        is_checked = '审核不通过'
    elif is_checked == 2:
        is_checked = '正在审核'
    return render(request,"teacher_center_meetingpaper.html",{'message':message,'is_checked':is_checked})


def patent_success(request,id,already=None):
    # return HttpResponse(request.session.get('sessionid',''))
    try:
        if request.session.get('sessionid',''):
            teacher_id=request.session.get('sessionid','')
            teacher=Teacher.objects.get(teacher_id=teacher_id)
        else:
            return render(request,"404.html")


        com=Honor_patent.objects.get(id=id)
        if request.method=="POST":
            com_point=request.POST.get('point',0)
            com.honor_patent_point=com_point
            if com.honor_patent_is_checked!=1:
                student=com.student
                wall=Student_honorwall.objects.get(student=student)
                wall.student_patent_number+=1
                # wall.student_patent_score+=com_point
                wall.save()
        com.honor_patent_is_checked=1
        com.teacher=teacher
        com.honor_patent_check_time=datetime.now()
        com.save()

    except:
        return render(request,"404.html")
    try:
        if not already:
            message=Honor_patent.objects.filter(honor_patent_is_checked=0)[0]
        else:
            message = Honor_patent.objects.filter(~Q(honor_patent_is_checked=0),id__gt=id)[0]
    except IndexError:
        if not already:
            return render(request, "teacher_center_checking.html", {'none': 1,'patent':1})
        else:
            return render(request, "teacher_center_already.html", {'none': 1})
    is_checked = message.honor_patent_is_checked
    if is_checked == 1:
        is_checked = '审核通过'
    elif is_checked == 0:
        is_checked = '未审核'
    elif is_checked == -1:
        is_checked = '审核不通过'
    elif is_checked == 2:
        is_checked = '正在审核'
    if not already:
        return render(request,"teacher_center_patent.html",{'message':message,'is_checked':is_checked})
    else:
        return render(request, "teacher_center_patent.html", {'message': message, 'is_checked': is_checked,'already':1})
def patent_fail(request,id,already=None):
    try:
        if request.session.get('sessionid',''):
            teacher_id=request.session.get('sessionid','')
            teacher=Teacher.objects.get(teacher_id=teacher_id)
        else:
            return render(request,"404.html")
        com=Honor_patent.objects.get(id=id)
        if com.honor_patent_is_checked==1:
            student = com.student
            wall = Student_honorwall.objects.get(student=student)
            wall.student_patent_number -= 1;
            # wall.student_patent_score -= com.honor_patent_point
            wall.save()
        com.teacher=teacher
        com.honor_patent_check_time=datetime.now()
        com.honor_patent_is_checked=-1
        com.save()
    except:
        return render(request,"404.html")
    try:
        if not already:
            message=Honor_patent.objects.filter(honor_patent_is_checked=0)[0]
        else:
            message=Honor_patent.objects.filter(~Q(honor_patent_is_checked=0),id__gt=id)[0]
    except IndexError:
        if not already:
            return render(request, "teacher_center_checking.html", {'none': 1,'patent':1})
        else:
            return render(request, "teacher_center_already.html", {'none': 1})
    is_checked = message.honor_patent_is_checked
    if is_checked == 1:
        is_checked = '审核通过'
    elif is_checked == 0:
        is_checked = '未审核'
    elif is_checked == -1:
        is_checked = '审核不通过'
    elif is_checked == 2:
        is_checked = '正在审核'
    if not already:
        return render(request,"teacher_center_patent.html",{'message':message,'is_checked':is_checked})
    else:
        return render(request, "teacher_center_patent.html", {'message': message, 'is_checked': is_checked,'already':1})

def patent_next(request,id,already=None):
    try:
        if request.session.get('sessionid',''):
            teacher_id=request.session.get('sessionid','')
            teacher=Teacher.objects.get(teacher_id=teacher_id)
        else:
            return render(request,"404.html")
        com=Honor_patent.objects.get(id=id)
        if com.honor_patent_is_checked==2:
            com.honor_patent_is_checked=0
        com.teacher=teacher
        com.honor_patent_check_time=datetime.now()
        com.save()
    except:
        return render(request,"404.html")
    try:
        if already:
            message=Honor_patent.objects.filter(~Q(honor_patent_is_checked=0),id__gt=id)[0]
        else:
            message = Honor_patent.objects.filter(honor_patent_is_checked=0)[0]
        message.honor_patent_is_checked = 2
        message.save()
    except IndexError:
        return render(request, "teacher_center_checking.html", {'none': 1,'patent':1})
    is_checked = message.honor_patent_is_checked
    if is_checked == 1:
        is_checked = '审核通过'
    elif is_checked == 0:
        is_checked = '未审核'
    elif is_checked == -1:
        is_checked = '审核不通过'
    elif is_checked == 2:
        is_checked = '正在审核'
    return render(request,"teacher_center_patent.html",{'message':message,'is_checked':is_checked})


def prize_success(request,id,already=None):
    # return HttpResponse(request.session.get('sessionid',''))
    try:
        if request.session.get('sessionid',''):
            teacher_id=request.session.get('sessionid','')
            teacher=Teacher.objects.get(teacher_id=teacher_id)
        else:
            return render(request,"404.html")


        com=Honor_scholarship.objects.get(id=id)
        if request.method=="POST":
            com_point=request.POST.get('point',0)
            com.honor_scholarship_point=com_point
            if com.honor_scholarship_is_checked != 1:
                student=com.student
                wall=Student_honorwall.objects.get(student=student)
                wall.student_scholarship_number+=1
                # wall.student_scholarship_score+=com_point
                wall.save()
        com.honor_scholarship_is_checked=1
        com.teacher=teacher
        com.honor_scholarship_check_time=datetime.now()
        com.save()

    except:
        return render(request,"404.html")
    try:
        if not already:
            message=Honor_scholarship.objects.filter(honor_scholarship_is_checked=0)[0]
        else:
            message = Honor_scholarship.objects.filter(~Q(honor_scholarship_is_checked=0),id__gt=id)[0]
    except IndexError:
        if not already:
            return render(request, "teacher_center_checking.html", {'none': 1,'prize':1})
        else:
            return render(request, "teacher_center_already.html", {'none': 1})
    is_checked = message.honor_scholarship_is_checked
    if is_checked == 1:
        is_checked = '审核通过'
    elif is_checked == 0:
        is_checked = '未审核'
    elif is_checked == -1:
        is_checked = '审核不通过'
    elif is_checked == 2:
        is_checked = '正在审核'
    if not already:
        return render(request,"teacher_center_prize.html",{'message':message,'is_checked':is_checked})
    else:
        return render(request, "teacher_center_prize.html", {'message': message, 'is_checked': is_checked,'already':1})
def prize_fail(request,id,already=None):
    try:
        if request.session.get('sessionid',''):
            teacher_id=request.session.get('sessionid','')
            teacher=Teacher.objects.get(teacher_id=teacher_id)
        else:
            return render(request,"404.html")
        com=Honor_scholarship.objects.get(id=id)
        if com.honor_scholarship_is_checked==1:
            student = com.student
            wall = Student_honorwall.objects.get(student=student)
            wall.student_scholarship_number -= 1;
            # wall.student_scholarship_score -= com.honor_scholarship_point
            wall.save()
        com.teacher=teacher
        com.honor_scholarship_check_time=datetime.now()
        com.honor_scholarship_is_checked=-1
        com.save()
    except:
        return render(request,"404.html")
    try:
        if not already:
            message = Honor_scholarship.objects.filter(honor_scholarship_is_checked=0)[0]
        else:
            message = Honor_scholarship.objects.filter(~Q(honor_scholarship_is_checked=0), id__gt=id)[0]
    except IndexError:
        if not already:
            return render(request, "teacher_center_checking.html", {'none': 1, 'prize': 1})
        else:
            return render(request, "teacher_center_already.html", {'none': 1})
    is_checked = message.honor_scholarship_is_checked
    if is_checked == 1:
        is_checked = '审核通过'
    elif is_checked == 0:
        is_checked = '未审核'
    elif is_checked == -1:
        is_checked = '审核不通过'
    elif is_checked == 2:
        is_checked = '正在审核'
    if not already:
        return render(request,"teacher_center_prize.html",{'message':message,'is_checked':is_checked})
    else:
        return render(request, "teacher_center_prize.html", {'message': message, 'is_checked': is_checked,'already':1})

def prize_next(request,id,already=None):
    try:
        if request.session.get('sessionid',''):
            teacher_id=request.session.get('sessionid','')
            teacher=Teacher.objects.get(teacher_id=teacher_id)
        else:
            return render(request,"404.html")
        com=Honor_scholarship.objects.get(id=id)
        if com.honor_scholarship_is_checked==2:
            com.honor_scholarship_is_checked=0
        com.teacher=teacher
        com.honor_scholarship_check_time=datetime.now()

        com.save()
    except:
        return render(request,"404.html")
    try:
        if already:
            message=Honor_scholarship.objects.filter(~Q(honor_scholarship_is_checked=0),id__gt=id)[0]
        else:
            message = Honor_scholarship.objects.filter(honor_scholarship_is_checked, id__gt=id)[0]
        if message.honor_scholarship_is_checked==0:
            message.honor_scholarship_is_checked = 2
            message.save()
    except IndexError:
        return render(request, "teacher_center_checking.html", {'none': 1,'prize':1})
    is_checked = message.honor_scholarship_is_checked
    if is_checked == 1:
        is_checked = '审核通过'
    elif is_checked == 0:
        is_checked = '未审核'
    elif is_checked == -1:
        is_checked = '审核不通过'
    elif is_checked == 2:
        is_checked = '正在审核'
    return render(request,"teacher_center_prize.html",{'message':message})
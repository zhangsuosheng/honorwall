from django.core.paginator import Paginator,EmptyPage,PageNotAnInteger
from django.contrib.auth.decorators import login_required
from django.shortcuts import render

@login_required
def myhonorwall(request,page=1):
    # if page == "":
    #     page = 1
    # page = int(page)
    # test_list = [i for i in range(1, 500)]  # 生成一个有500条数据的表
    # paginator = Paginator(test_list, 10)  # 把这个列表分割成10个为一页的分页器
    # try:
    #     # 获取指定页面的数据
    #     contacts = paginator.page(page)
    # except PageNotAnInteger:
    #     # 如果获取的页面不是整数,page取第一页
    #     page = 1
    #     contacts = paginator.page(page)
    # except EmptyPage:
    #     # 如果获取的页面超出范围，则显示最后一页
    #     page = paginator.num_pages
    #     contacts = paginator.page(page)
    #     # 根据当前所在页产生长度为10的页码，放入列表中
    # paper_list = make_paper_list(page, paginator.num_pages, 10)
    # userrelname=request.COOKIES.get('userrelname','')
    # return render(request, "my_honorwall.html", {"page": page, "contacts": contacts, "paper_list": paper_list, "userrelname":userrelname})
      return render(request,"my_honorwall.html")
#输入一个数字，生成以它为中心的一个数列
def make_paper_list(page, max_page, long):
    if (page-5 > 0) & (page+3 < max_page):
        return [i for i in range(page-5,page-5+long)]
    if (page-5 <= 0) & (page+3 < max_page):
        return [i for i in range(1, min(1+long, 1+max_page))]
    if (page - 5 <= 0) & (page + 3 >= max_page):
        return [i for i in range(1,max_page+1)]
    if (page - 5 > 0) & (page + 3 >= max_page):
        return [i for i in range(max_page+1-long, max_page+1)]

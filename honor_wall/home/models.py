from django.db import models
# Create your models here.

# 荣誉奖项表（老师添加）
class Competition_type(models.Model):
    competition_id = models.AutoField(unique=True,primary_key=True)  # 奖项编号自增
    competition_class=models.CharField(max_length=20) # 荣誉类别
    competition_name = models.CharField(max_length=30)  # 奖项名称
    competition_competition_level = models.IntegerField()  # 竞赛级别
    competition_level=models.CharField(max_length=30) #荣誉级别
    competition_point=models.IntegerField(default=0) #荣誉积分
    def __str__(self):
        pass
#教师表
class Teacher(models.Model):
    teacher_name=models.CharField(max_length=30)#教师姓名
    teacher_id=models.BigIntegerField(unique=True)#教工号
    teacher_faculty=models.CharField(max_length=20)#教师学院
    def __str__(self):
        pass
#学生基本信息表(表内信息是学生)
class Student_message_uneditable(models.Model):
    student_name=models.CharField(max_length=30)#学生姓名
    student_sex=models.BooleanField()#学生性别0女 1男
    student_id=models.BigIntegerField(unique=True)#学生学号#设置学号唯一
    student_field=models.CharField(max_length=20)#学生专业  eg:自动化
    student_classname=models.IntegerField()#学生专业班级号码  eg:62
    student_faculty=models.CharField(max_length=20)#学生学院
    student_grade=models.IntegerField()#学生年级(入学年份)
    student_state=models.BooleanField()#账号状态(正常1,冻结0)
    def __str__(self):
        pass

#学生信息表(可修改的)
class Student_message_editable(models.Model):
    Competitions=models.ManyToManyField(Competition_type)
    student=models.ForeignKey(Student_message_uneditable,to_field="student_id")#学生学号student_id 外键
    student_nickname=models.CharField(default="无",max_length=20)#学生昵称(默认为无)
    student_birthday=models.CharField(max_length=20)#学生出生日期
    student_political_state=models.CharField(max_length=20)#政治面貌(应该是勾选选项)
    student_people=models.CharField(max_length=10)#学生民族
    student_birthplace=models.CharField(max_length=20)#籍贯
    student_document_type=models.CharField(max_length=10)#证件类型
    student_document_number=models.CharField(max_length=100)#证件号码(加密密文)
    #好像因为随意自己填写身份证号可能会重复 就不设置唯一了
    # student_documentnumber.unique=True #设置证件号码是唯一的
    student_email=models.EmailField(unique=True,max_length=30)#邮箱号码#邮箱设置为唯一
    student_phone_number=models.BigIntegerField(unique=True)#手机号码#手机号码设置唯一
    student_qq_number=models.BigIntegerField(unique=True)#qq号码#QQ号码设置唯一
    #############################################################
    student_photo = models.ImageField(upload_to='student/photo/')  #学生照片
    ##****************************************************************
    student_name_conceal=models.BooleanField(default=False)#姓名是否隐藏
    student_contact_conceal=models.BooleanField(default=False)#联系方式是否隐藏
    student_sex_conceal=models.BooleanField(default=False)#性别是否隐藏

    ##################################################################
    student_address=models.CharField(max_length=100,default="未填写")
    student_sign=models.CharField(max_length=100,default="未填写")
    student_all_conceal = models.BooleanField(default=False)  # 所有信息(除了荣誉信息)是否隐藏
    student_honor_wall_conceal = models.BooleanField(default=False)  # 荣誉墙外网是否可访问
    #*******************************************************************
    def __str__(self):
        pass

#学生荣誉墙表
class Student_honorwall(models.Model):
    student=models.ForeignKey(Student_message_uneditable,to_field="student_id")#学生学号student_id外键
    #学生总积分与前端将各类积分相加即可
    student_competition_number=models.IntegerField()#学生竞赛奖项数目
    student_competition_score=models.IntegerField()#学生竞赛奖项积分 ，排名根据实时积分排序得出
    student_competition_rank=models.IntegerField(null=True)#学生竞赛排名
    student_paper_number=models.IntegerField()#学生论文数目
    student_paper_score=models.IntegerField()#学生论文积分
    student_paper_rank=models.IntegerField(null=True)#学生论文排名
    student_paper_magazine_number=models.IntegerField()#学生期刊论文数目
    student_paper_magazine_score=models.IntegerField()#学生期刊论文积分
    student_paper_magazine_rank=models.IntegerField(null=True)#学生期刊论文排名
    student_paper_meeting_number=models.IntegerField()#学生会议论文数目
    student_paper_meeting_score=models.IntegerField()#学生会议论文积分
    student_paper_meeting_rank=models.IntegerField(null=True)#学生会议论文排名
    student_patent_number=models.IntegerField()#学生专利总数
    student_patent_score=models.IntegerField()#学生专利积分
    student_patent_rank=models.IntegerField(null=True)#学生专利排名
    student_scholarship_number=models.IntegerField()#学生奖学金总数
    student_scholarship_score=models.IntegerField()#学生奖学金积分
    student_scholarship_rank=models.IntegerField(null=True)#学生奖学金排名
    student_experience_number=models.IntegerField()#学生社会经历总数
    student_experience_score=models.IntegerField()#学生社会经历积分
    student_experience_rank=models.IntegerField(null=True)#学生社会经历排名

    student_total_number=models.IntegerField(null=True)#总数
    student_total_score=models.IntegerField(null=True)#总积分
    student_total_rank=models.IntegerField(null=True)#总排名

    student_portrait=models.ImageField(upload_to='student/head/')#学生荣誉墙头像
    def __str__(self):
        pass



# 具体竞赛级别积分表
# class Competition_level_type(models.Model):
#     competition_uid = models.IntegerField()  # 该uid对应具体竞赛的某一级别奖项
#     competition = models.ForeignKey(Competition_type, to_field="competition_id")  # 奖项编号外键
#     competition_level = models.CharField(max_length=30)  # 奖项级别
#     compitition_score = models.IntegerField()  # 荣誉积分
#
#     def __str__(self):
#         pass
#
#
#             # ↑上面两张表的作用有，第一，帮助学生选择竞赛，第二，通过由老师添加奖项，和级别分数省去老师多次打分的麻烦（但学生如果选择的是其他，仍然要打分）
# 竞赛荣誉审核,提交表
class Honor_competition(models.Model):
    level = (
        (0, '~'),
        (1, '国际级'),
        (2, '国家级'),
        (3, '西北赛区级'),
        (4, '省级'),
        (5, '校级'),
        (6, '不分级'),
    )
    level_check = (
        (-1, '未通过'),
        (0, '审核中'),
        (1, '通过'),
        (2, '正在审核'),
    )
    student = models.ForeignKey(Student_message_uneditable, to_field="student_id")  # 学生学号student_id外键
    teacher = models.ForeignKey(Teacher, to_field="teacher_id",null=True)  # 审核人 外键 以审核人teacher_id为外键
    honor_competition_teacher=models.CharField(max_length=30)   #指导教师
    honor_competition_award = models.CharField(max_length=100)  # 颁奖单位
    honor_competition_message = models.CharField(max_length=800)  # 备注信息
    honor_competition_get_time = models.CharField(max_length=20)  # 荣誉获得时间(大致时间不用满足时间格式)
    honor_competition_point = models.IntegerField(default=0)  # 荣誉积分(初始值为0) 判断competition_type是否为0-"其他"，若不为0则从具体积分竞赛积分表中获取，否则由老师评分给定
    honor_competition_submit_time = models.DateTimeField(auto_now=True)  # 提交时间,直接记录提交时间
    honor_competition_check_time = models.DateTimeField(null=True)  # 审核时间(修改时间)
    honor_competition_is_checked = models.IntegerField(default=0,choices=level_check)  # 审核状态(-1未通过，0审核中，1通过,2正在审核)
    honor_competition_confirm_file = models.FileField()  # 审核材料

    competition_name = models.CharField(max_length=30)  # 奖项名称
    competition_competition_level = models.IntegerField(choices=level)  # 竞赛级别
    competition_level=models.CharField(max_length=30) #荣誉级别
    competition_point=models.IntegerField(default=0) #荣誉积分

    competition_type = models.ForeignKey(Competition_type, to_field="competition_id",null=True)  # 以具体竞赛荣誉级别的competition_id为外键、

    def __str__(self):
        pass


# 专利荣誉审核,提交表
class Honor_patent(models.Model):
    level_check = (
        (-1, '未通过'),
        (0, '审核中'),
        (1, '通过'),
        (2, '正在审核'),
    )
    student = models.ForeignKey(Student_message_uneditable, to_field="student_id")  # 学生学号student_id外键
    teacher = models.ForeignKey(Teacher, to_field="teacher_id",null=True)  # 审核人 外键 以审核人teacher_id为外键
    honor_patent_type = models.CharField(max_length=20)  # 专利类别
    honor_patent_name = models.CharField(max_length=100)  # 专利名称
    honor_patent_number = models.CharField(max_length=50)  # 专利（申请）号
    honor_patent_date_apply = models.CharField(max_length=20)  # 专利申请日期
    honor_patent_date_auth = models.CharField(max_length=20)  # 专利授权日期
    honor_patent_legalstatus = models.CharField(max_length=20)  # 专利法律状态
    honor_patent_firstman = models.BooleanField(default=True)  # 是否为第一发明人
    honor_patent_people = models.CharField(max_length=150)  # 发明人列表
    honor_patent_people_number = models.IntegerField()  # 自己在发明人中的序号
    honor_patent_point = models.IntegerField()  # 荣誉积分(初始值为0) 由老师评分给定
    honor_patent_submit_time = models.DateTimeField(auto_now=True)  # 提交时间,直接记录提交时间
    honor_patent_check_time = models.DateTimeField(null=True)  # 审核时间(修改时间)
    honor_patent_is_checked = models.IntegerField(default=0,choices=level_check)  # 审核状态(-1未通过，0审核中，1通过)
    honor_patent_confirm_file = models.FileField()  # 证明材料

    competition_type = models.ForeignKey(Competition_type,to_field="competition_id",null=True)  # 以具体竞赛荣誉级别的competition_id为外键、


    def __str__(self):
        pass


# 期刊论文荣誉审核,提交表
class Honor_paper_magazine(models.Model):
    level_check = (
        (-1, '未通过'),
        (0, '审核中'),
        (1, '通过'),
        (2, '正在审核'),
    )
    student = models.ForeignKey(Student_message_uneditable, to_field="student_id")  # 学生学号student_id外键
    teacher = models.ForeignKey(Teacher, to_field="teacher_id",null=True)  # 审核人 外键 以审核人teacher_id为外键

    honor_paper_magazine_type = models.CharField(max_length=20)  # 期刊类别
    honor_paper_magazine_magazinename = models.CharField(max_length=100)  # 刊物名称
    # !改动 长度应该增长为max_length=200
    honor_paper_magazine_papername = models.CharField(max_length=100)  # 文章名称


    honor_paper_magazine_status = models.CharField(max_length=20)  # 论文状态
    honor_paper_magazine_page_begin = models.IntegerField()  # 起始页码
    honor_paper_magazine_ISBNcode = models.CharField(max_length=100)  # ISBN码/卷期号
    honor_paper_magazine_page_number=models.CharField(max_length=50)  #卷号 页号
    honor_paper_magazine_date_publish = models.CharField(max_length=20)  # 出版日期
    honor_paper_magazine_is_firstauthor = models.BooleanField(default=False)  # 是否为通讯作者或第一作者
    honor_paper_magazine_quotetimes = models.IntegerField()  # 被引用次数
    honor_paper_magazine_impactfactors = models.IntegerField()  # 影响因子数
    # 改动max_
    honor_paper_magazine_searching = models.CharField(max_length=300)  # 检查收录情况
    honor_paper_magazine_people = models.CharField(max_length=150)  # 其他作者列表
    honor_paper_magazine_abstract = models.CharField(max_length=1000)  # 论文摘要

    honor_paper_magazine_point = models.IntegerField()  # 荣誉积分(初始值为0) 由老师评分给定
    honor_paper_magazine_submit_time = models.DateTimeField(auto_now=True)  # 提交时间,直接记录提交时间
    honor_paper_magazine_check_time = models.DateTimeField(null=True)  # 审核时间(修改时间)
    honor_paper_magazine_is_checked = models.IntegerField(default=0,choices=level_check)  # 审核状态(-1未通过，0审核中，1通过)
    honor_paper_magazine_confirm_file = models.FileField()  # 证明材料

    competition_type = models.ForeignKey(Competition_type,to_field="competition_id",null=True)  # 以具体竞赛荣誉级别的competition_id为外键、



def __str__(self):
    pass


# 会议论文荣誉审核,提交表
class Honor_paper_meeting(models.Model):
    level_check = (
        (-1, '未通过'),
        (0, '审核中'),
        (1, '通过'),
        (2, '正在审核'),
    )
    student = models.ForeignKey(Student_message_uneditable, to_field="student_id")  # 学生学号student_id外键
    teacher = models.ForeignKey(Teacher, to_field="teacher_id",null=True)  # 审核人 外键 以审核人teacher_id为外键

    honor_paper_meeting_type = models.CharField(max_length=20)  # 会议类别
    honor_paper_meeting_meetingname = models.CharField(max_length=100)  # 会议名称
    honor_paper_meeting_papername = models.CharField(max_length=100)  # 文章名称
    honor_paper_meeting_address = models.CharField(max_length=100)  # 会议地址
    honor_paper_meeting_date = models.CharField(max_length=20)  # 会议日期
    honor_paper_meeting_is_firstauthor = models.BooleanField(default=False)  # 是否为通讯作者或第一作者
    honor_paper_meeting_people = models.CharField(max_length=150)  # 其他作者列表


    honor_paper_meeting_point = models.IntegerField(default=0)  # 荣誉积分(初始值为0) 由老师评分给定
    honor_paper_meeting_submit_time = models.DateTimeField(auto_now=True)  # 提交时间,直接记录提交时间
    honor_paper_meeting_check_time = models.DateTimeField(null=True)  # 审核时间(修改时间)
    honor_paper_meeting_is_checked = models.IntegerField(default=0,choices=level_check)  # 审核状态(-1未通过，0审核中，1通过)
    honor_paper_meeting_confirm_file = models.FileField()  # 证明材料

    competition_type = models.ForeignKey(Competition_type,to_field="competition_id",null=True)  # 以具体竞赛荣誉级别的competition_id为外键、


def __str__(self):
    pass


# 奖学金荣誉审核,提交表
class Honor_scholarship(models.Model):
    level_check = (
        (-1, '未通过'),
        (0, '审核中'),
        (1, '通过'),
        (2, '正在审核'),
    )
    student = models.ForeignKey(Student_message_uneditable, to_field="student_id")  # 学生学号student_id外键
    teacher = models.ForeignKey(Teacher, to_field="teacher_id",null=True)  # 审核人 外键 以审核人teacher_id为外键
    honor_scholarship_name = models.CharField(max_length=100)  # 奖学金名称
    honor_scholarship_year = models.CharField(max_length=20)  # 获奖学年度
    honor_scholarship_moneyperyear = models.IntegerField()  # 每年多少奖学金
    honor_scholarship_authority = models.CharField(max_length=100)  # 授奖单位
    honor_scholarship_point = models.IntegerField()  # 荣誉积分(初始值为0) 由老师评分给定
    honor_scholarship_submit_time = models.DateTimeField(auto_now=True)  # 提交时间,直接记录提交时间
    honor_scholarship_check_time = models.DateTimeField(null=True)  # 审核时间(修改时间)
    honor_scholarship_is_checked = models.IntegerField(default=0,choices=level_check)  # 审核状态(-1未通过，0审核中，1通过)
    honor_scholarship_confirm_file = models.FileField()  # 证明材料

    competition_type = models.ForeignKey(Competition_type,to_field="competition_id",null=True)  # 以具体竞赛荣誉级别的competition_id为外键、


    def __str__(self):
        pass


# 社会经历荣誉审核,提交表
class Honor_experience(models.Model):
    level_check = (
        (-1, '未通过'),
        (0, '审核中'),
        (1, '通过'),
        (2, '正在审核'),
    )
    student = models.ForeignKey(Student_message_uneditable, to_field="student_id")  # 学生学号student_id外键
    teacher = models.ForeignKey(Teacher, to_field="teacher_id",null=True)  # 审核人 外键 以审核人teacher_id为外键
    honor_experience_name = models.CharField(max_length=100)  # 社会经历名称
    honor_experience_start = models.CharField(max_length=20)  # 活动开始时间
    honor_experience_end = models.CharField(max_length=20)  # 活动结束时间
    honor_experience_authority = models.CharField(max_length=100)  # 所在单位
    honor_experience_note = models.CharField(max_length=2000)  # 活动描述
    honor_experience_point = models.IntegerField()  # 荣誉积分(初始值为0) 由老师评分给定
    honor_experience_submit_time = models.DateTimeField(auto_now=True)  # 提交时间,直接记录提交时间
    honor_experience_check_time = models.DateTimeField(null=True)  # 审核时间(修改时间)
    honor_experience_is_checked = models.IntegerField(default=0,choices=level_check)  # 审核状态(-1未通过，0审核中，1通过)
    honor_experience_confirm_file = models.FileField()  # 证明材料

    competition_type = models.ForeignKey(Competition_type,to_field="competition_id",null=True)  # 以具体竞赛荣誉级别的competition_id为外键、


    def __str__(self):
        pass


# 通知表
class Message(models.Model):
    teacher = models.ForeignKey(Teacher, to_field="teacher_id")  # 发布人 外键 以发布人teacher_id为外键
    message_title = models.CharField(max_length=21)  # 文章标题
    message_type = models.IntegerField()  # 文章类别
    message_content = models.CharField(max_length=3000)  # 文章内容
    message_date = models.DateTimeField(auto_now=True)  # 文章发布日期(发布时刻/更新时刻)
    message_file = models.FileField()  # 文章附件

    def __str__(self):
        pass

#####################################################以下是张所晟后来添加的表
#推荐信申请记录
class Recommendation(models.Model):
    student = models.ForeignKey(Student_message_uneditable, to_field="student_id")#申请人学号
    company=models.CharField(max_length=100)#要申请的公司
    position=models.CharField(max_length=100)#要申请的职位
    paper=models.BooleanField(default=False)#是否需要纸质版
    date=models.DateTimeField(auto_now=True)#用户提交申请的时间
    checked=models.IntegerField(default=0)#是否已经审核通过 1审核通过 0待审核 -1审核失败
    def __str__(self):
        pass

#软链接申请记录
class Links(models.Model):
    student=models.ForeignKey(Student_message_uneditable, to_field="student_id")#申请人学号
    link=models.CharField(max_length=200)#连接
    date=models.CharField(max_length=100)#时间戳
    use_times=models.IntegerField()#该软连接的剩余使用次数
    def __str__(self):
        pass
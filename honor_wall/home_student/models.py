from django.db import models

# Create your models here.
#学生基本信息表(表内信息是学生)
class Student_message_uneditable(models.Model):
    student_name=models.CharField(max_length=30)#学生姓名
    student_sex=models.BooleanField()#学生性别0女 1男
    student_id=models.IntegerField(unique=True)#学生学号#设置学号唯一
    student_field=models.CharField(max_length=20)#学生专业  eg:自动化
    student_classname=models.CharField(max_length=10)#学生专业班级  eg:电信62
    student_faculty=models.CharField(max_length=20)#学生学院
    student_grade=models.IntegerField()#学生年级(入学年份)
    student_state=models.BooleanField()#账号状态(正常,冻结)
    def __str__(self):
        pass

#学生信息表(可修改的)
class Student_message_editable(models.Model):
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
    student_phone_number=models.IntegerField(unique=True)#手机号码#手机号码设置唯一
    student_qq_number=models.IntegerField(unique=True)#qq号码#QQ号码设置唯一
    student_photo=models.ImageField(upload_to='img')#学生照片
    student_name_conceal=models.BooleanField(default=False)#姓名是否隐藏
    student_contact_conceal=models.BooleanField(default=False)#联系方式是否隐藏
    student_sex_conceal=models.BooleanField(default=False)#性别是否隐藏
    student_all_conceal=models.BooleanField(default=False)#所有信息(除了荣誉信息)是否隐藏
    def __str__(self):
        pass

#学生荣誉墙表
class Student_honorwall(models.Model):
    student=models.ForeignKey(Student_message_uneditable,to_field="student_id")#学生学号student_id外键
    #学生总积分与前端将各类积分相加即可
    student_competition_number=models.IntegerField()#学生竞赛奖项数目
    student_competition_score=models.IntegerField()#学生竞赛奖项积分 ，排名根据实时积分排序得出
    student_paper_number=models.IntegerField()#学生论文数目
    student_paper_score=models.IntegerField()#学生论文积分
    student_paper_magazine_number=models.IntegerField()#学生期刊论文数目
    student_paper_magazine_score=models.IntegerField()#学生期刊论文积分
    student_paper_meeting_number=models.IntegerField()#学生会议论文数目
    student_paper_meeting_score=models.IntegerField()#学生会议论文积分
    student_patent_number=models.IntegerField()#学生专利总数
    student_patent_score=models.IntegerField()#学生专利积分
    student_scholarship_number=models.IntegerField()#学生奖学金总数
    student_scholarship_score=models.IntegerField()#学生奖学金积分
    student_experience_number=models.IntegerField()#学生社会经历总数
    student_experience_score=models.IntegerField()#学生社会经历积分

    student_portrait=models.ImageField()#学生荣誉墙头像
    def __str__(self):
        pass

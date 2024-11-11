from django.db import models


class BookInfo(models.Model):  # 定义一个book类，相当于定义一个数据库表
    name = models.CharField(max_length=10)  # name= 相当于设置字段名 max_length与varchar()一样


class PeopleInfo(models.Model):
    name = models.CharField(max_length=10)
    gender = models.BooleanField()  # 布尔类型(是男是女判断返回false或true)
    # 外键约束
    book = models.ForeignKey(BookInfo,)
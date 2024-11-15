from django.db import models


# Create your models here.
class BookInfo(models.Model):
    name = models.CharField(max_length=10, unique=True, verbose_name='名字')
    pub_data = models.DateField(null=True)
    readcount = models.IntegerField(default=0)
    commentcount = models.IntegerField(default=0)
    is_delete = models.BooleanField(default=False)

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'bookinfo'  # 修改表名写法
        verbose_name = '书籍管理'  # 站点管理admin


class PeopleInfo(models.Model):
    # 定义有序字典
    GENDER_CHOICE = (
        (1, 'male'),
        (2, 'female')
    )
    name = models.CharField(max_length=10, unique=True)  # 名字，unique唯一性
    gender = models.SmallIntegerField(choices=GENDER_CHOICE, default=1)  # 性别，从有序字典中选择
    description = models.CharField(max_length=100, null=True)  # 人物描述
    is_delete = models.BooleanField(default=False)  # 默认不允许删除

    book = models.ForeignKey(BookInfo, on_delete=models.CASCADE)  # 外键为ForeignKey,且删除操作为级联操作

    class Meta:
        db_table = 'peopleinfo'
        verbose_name = '人物管理'

    def __str__(self):
        return self.name

from django.http import HttpResponse
from django.shortcuts import render

from book.models import BookInfo


# Create your views here.
def index(request):
    books = BookInfo.objects.all()
    print(books)
    return HttpResponse('index')


# 实现增删改查在这里
# 复制到Shell打开
# 方法一
from book.models import BookInfo

book = BookInfo(
    name='Django',
    pub_data='2024-11-15',
    readcount=10
)

# 方法二
BookInfo.objects.create(
    name='Python开发',
    pub_data='2024-1-1',
    readcount=100
)

BookInfo.objects.create(
    name='zzx',
    pub_data='2000-1-1',
    readcount=1000
)

# 修改数据
# 方法一
book = BookInfo.objects.get(id=10)
book.name = 'zxy'
book.save()

# 方法二
BookInfo.objects.filter(id=11).update(name='wbf', pub_data='2024-11-14', readcount=1000)

BookInfo.objects.filter(id=5).update(name='qhy', pub_data='2003-8-15', readcount=100)

BookInfo.objects.filter(id=5).update(commentcount=999)

# 删除数据
# 先获取数据
# 方法一
book = BookInfo.objects.get(id=5)
book.delete()

# 方法二
BookInfo.objects.filter(id=10).delete()

# 查询数据
# BookInfo.objects.get(id=1),单条数据
# 加入异常处理
try:
    BookInfo.objects.get(id=1)
except BookInfo.DoesNotExist:
    print("查询书籍不存在")

# 查询人物
from book.models import PeopleInfo
PeopleInfo.objects.all()

# count()方法

from book.models import BookInfo
BookInfo.objects.all().count()

# 过滤查询
# 类.objects.filter(属性名_运算符=值) N个结果
# 类.objects.exclude(属性名_运算符=值) N个结果 排除剩下的
# 类.objects.get(属性名_运算符=值) 单一数据
# 查询编号为1的图书
BookInfo.objects.get(id=1)
# 查询书名包含“湖”的图书 name__contains=..
BookInfo.objects.filter(name__contains='湖')
# 查询书名以“部”结尾的图书 name__endswith=..
BookInfo.objects.filter(name__endswith='部')
# 查询书名为空的图书
BookInfo.objects.filter(name__isnull=True)
# 查询书名id为1，3，5的图书
BookInfo.objects.filter(id__in=[1, 3, 4])
# 查询编号大于3的图书
# 大于gt
# 大于等于gte
# 小于lt
# 小于等于lte
BookInfo.objects.filter(id__gt=3)
# 查询id不等于3的书籍
BookInfo.objects.exclude(id=3)
# 查询1980年发表的图书
BookInfo.objects.filter(pub_data__year=1980)
# 查询1980年1-1后发表的图书
BookInfo.objects.filter(pub_data__gte='1980-1-1')
# 查询阅读量大于等于评论的书籍
# 运用F对象查询
# 导入F对象
from django.db.models import F
BookInfo.objects.filter(readcount__gte=F('commentcount'))
# 查询评论量大于阅读量的书籍
BookInfo.objects.filter(commentcount__gte=F('readcount'))
# 并且查询，阅读量大于20，且编号小于3的图书
BookInfo.objects.filter(readcount__gt=20).filter(id__lte=3)
# 查询阅读量大于20或编号小于3的图书
from django.db.models import Q
BookInfo.objects.filter(Q(readcount__gt=20) | Q(id__lte=3))
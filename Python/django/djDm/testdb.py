from django.http import HttpResponse
from django.shortcuts import render

from TestModel.models import Test


# 数据库操作
def testdb(request):
    # 初始化
    response = []

    # 通过objects这个模型管理器的all()获得所有数据行,相当于SQL中的select * from
    list = Test.objects.all()

    # filter相当于sql中的where,可设置条件过滤条件
    # response2 = Test.objects.filter(id=1)

    # 获取单个对象
    # response3 = Test.objects.get(id=1)

    # 限制返回的数据, 相当于sql中的offset 0 limit2;
    Test.objects.order_by('name')[0:2]

    # 数据排序
    Test.objects.order_by("id")

    # 上面的方法可以连锁使用
    Test.objects.filter(name="runoob").order_by("id")

    # 输出所有数据
    for var in list:
        response.append(var)

    context = {}
    context['response'] = response
    return render(request, 'hello.html', context)


def testInsert(request):
    for i in range(10):
        test = Test(name='test%s' % str(i))
        test.save()

    return HttpResponse("<p>数据添加成功!</p>")


def insert(request):

    name = request.GET['name']

    test = Test(name=name)
    test.save()

    return HttpResponse("<p>修改成功</p>")


def update(request):
    id = 0
    name = 'old'

    if 'id' in request.GET:
        id = request.GET['id']
    if 'name' in request.GET:
        name = request.GET['name']

    test = Test.objects.get(id=id)
    test.name = name
    test.save()

    # 另一种方式
    # Test.objects.filter(id=1).update(name='new game')

    return HttpResponse("<p>修改成功</p>")

def delete(request):
    id = 0

    if 'id' in request.GET:
        id = request.GET['id']

    test = Test.objects.get(id=id)
    test.delete()

    # 另一种方式
    # Test.objects.filter(id=2).delete()

    return HttpResponse("<p>删除成功</p>")


def find(request):
    name = request.GET['name']
    list = Test.objects.filter(name__contains=name)

    context = {}
    context['response'] = list
    return render(request, 'hello.html', context)

1、项目结构
-DJANGO
    -back_app（由manage.py生成的app）
        -models.py
        -views.py（定义页面的具体功能函数）
    -DJANGO_BACK(项目主体)
        -settings.py
        -urls.py（设置链接地址和页面函数的对应关系）
    -venv（临时配置的虚拟环境；包括一些包和依赖）
    -manage.py(生成app和启动某些功能)


2、创建页面以及页面对应功能：
    在"urls.py"里配置访问地址如：path('index/'); "index/" = "www.xxx.com/index"
    在"views.py"里定义功能函数如：def index(requests): ; ###requests为默认参数
    导入"views.py"包里的"index"函数,通过"urls.py"里的path('index/',views.index)链接
    启动"python manage.py runserver"
    达成访问"www.xxx.com/index"调用"index"函数

3、views里常用返回的函数：
    HttpResponse("字符串")        #返回普通字符串
    render("request","xxx.html") #返回寻找到的模板文件，默认app-templates-xxx.html

4、DJANGO提供了ORM框架操作数据库：
    1）创建/修改/删除数据库中的表（无法创建数据库）
    models.py操作命令
        ## python manage.py makemigrations
        ## python manage.py migrate
        ## 允许为空(null=Ture,blank=Ture)

    2）操作表中的数据;增 删 改 查
        ##增  增加表里数据 class类.object.create(行名="xxx")
        ##删  删除表里数据 class类.object.filter(id=1).delete() / class类.object.all().delete()
        ##查  获取表里数据 class类.object.all() / class类.object.filter(id=1)得到Queryset类型,可以循环出来比如：
              data_list = class类.object.all()
              for obj in data_list:
                 print(obj.id,obj.name.....)
        ##改  更新表里数据 class类.object.all().update(字段=xxx) 全部更新
                         class类.object.filter(id=1).update(字段=xxx) 条件更新

----

第一步：通过pycharm生成一个DJANGO的项目文件，配置虚拟环境

第二步：调用python运行项目文件目录下的manage.py，生成一个app文件
    #python manage.py startapp 项目名

第三步：配置项目文件
    1）删除默认生成的templates文件
    2）删除settings.py里 'DIRS': [] 对于路径

第四步：注册app，在settings.py里的 INSTALLED_APPS = [
    # 项目名.包名.类名
]

第五步：配置数据库模板
    1）settings.py中配置数据库模板：
    #DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.mysql",
        "NAME": "数据库名称",
        "USER": "账号",
        "PASSWORD": "密码",
        "HOST": "127.0.0.1",
        "PORT": 3306,
    }
}
    2）models.py里加入预设的数据库表内容
    3）预设数据表内容添加到数据库，"tools"-"Run manage.py task"-
                                                          #makemigrations
                                                          #migrate

第六步：构造静态文件‘static’包括js、css、img等等

第七步：配置页面、函数、html文件
    1）urls.py
        配置路由，引入项目包导入view页面
        #from 项目名 import view
        构建路径适配view文件
        #path('depart/list/',views.depart_list)
    2)views.py
        在views.py生成路径对应的函数和功能
        #def depart_list(request):
            return rander(request,'xxx.html')
    3)templates - html文件
        创建页面文件xxx.html
        引入一系列文件
        #{% load static %}
        #<link rel="stylesheet" href="{% static 'plugins/bootstrap-5.3.0-alpha1-dist/css/bootstrap.min.css' %}">
        #<script src="{% static 'js/jquery.min.js' %}"></script>
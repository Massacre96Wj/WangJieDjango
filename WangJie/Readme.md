## 一、Django创建的工程和配置
`django-admin.exe startproject WangJie`

`cd WangJie`

`python manage.py runserver` 测试工程是否创建成功

`python manage.py startapp blog`

添加应用**blog**到settings.py的INSTALLED_APPS 

**初始化数据库命令：**

`python manage.py migrate`

**创建后台超级管理用户：**

`python manage.py createsuperuser`

**用户名：WangJie**

**密码：邮箱密码**

**访问：**http://127.0.0.1:8000/admin/** 登陆后台管理**

**更改默认的Sqlite3为MySql**

**修改settings.py:**

`DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'HOST': '127.0.0.1',
        'PORT': 3306,
        'NAME': 'djangodb',
        'USER': 'root',
        'PASSWORD': 'root',
    }
}`

**在WangJie\_init_.py输入以下代码：**

`import pymysql`

`pymysql.install_as_MySQLdb()`

**重新执行数据库命令：**

`python manage.py makemigrations`

`python manage.py migrate`

**以上是配置工程**

## 二、APP配置创建后台数据库
**为APP创建后台数据库**
利用自带的Sqlite3数据库，在blog\models.py创建表，例如创建用户表

之后继续执行：

`python manage.py makemigrations`

`python manage.py migrate`

会生成一张用户表，表名默认会在头部添加APP名，同时创建id自增主键

**1.APP的urls配置**

在APP下新建blog_urls，这样每个APP下都有自己的urls,系统url利用include加入每个APP的urls

**2.APP的templates文件（html）配置**

在系统工程下创建templates文件，修改setting.py文件

`'DIRS': [os.path.join(BASE_DIR, 'templates')],`

**3.APP的static文件（js，css）配置**

创建根目录下的static文件，同时在每个APP下的static下建立以APP名相同的文件夹 **blog/static/blog/**，放入样式JS CSS

修改setting.py: 

STATIC_URL = '/static/'

STATICFILES_DIRS = [

  os.path.join(BASE_DIR, "static"),
  
  os.path.join(BASE_DIR, "blog", "static"),
  
]

调用方式如下：

`{% static 'blog/img/firefox-logo-small.jpg' %}`

`{% static 'blog/img/name.png' %}`

STATIC_ROOT：运行manage.py collectstatic后静态文件将复制到的目录
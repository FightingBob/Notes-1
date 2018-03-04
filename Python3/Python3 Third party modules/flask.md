
> http://docs.jinkan.org/docs/flask/quickstart.html

### 快速入门
#### first flask application

```python
from flask import Flask


app = Flask(__name__)

@app.route('/')
def index():
    return 'hello word'


if __name__ == "__main__":
    app.run()
```

#### debug moudle

```python
app.run(debug=True)
```

#### route

```python
@app.route('/')
def index():
    return 'Index Page'

@app.route('/hello')
def hello():
    return 'Hello World'
```

```python
@app.route('/user/<username>')
def user(username):
    return "hello {}".format(username)
"""
hello buglan default is <class 'str'>
"""
@app.route('/use_id/<int:id>')
def user_id(id):
    return 'id is {}'.format(type(id))
"""
id is <class 'int'>
"""
@app.route('/float/<float:float_id>')
def float_id(float_id):
    return 'float_id is {}'.format(type(float_id))
"""
float_id is <class 'float'>
"""
```
| type  | description                |
| ----- | -------------------------- |
| int   | 接受整数                   |
| float | 同 int ，但是接受浮点数    |
| path  | 和默认的相似，但也接受斜线 |

"Note"

```python
@app.route('/projects/')
def projects():
    return 'The project page'

@app.route('/about')
def about():
    return 'The about page'

"""
访问 /projects 从重定向到/projects/
如果访问 /about/ 则会出现 404 not found
"""
```

#### 构建 url

```python
@app.route('/login')
def login():
    return "login page"

@app.route('/register')
def register():
    return 'register page'

@app.route('/user/<username>')
def user(username):
    return username

with app.test_request_context():
    url_for('login')
    url_for('register')
    url_for('login', next='/')
    url_for('user', username='buglan')
```

#### HTTP methods



- GET
    浏览器告知服务器：只 获取 页面上的信息并发给我。这是最常用的方法。
- HEAD
    浏览器告诉服务器：欲获取信息，但是只关心 消息头 。应用应像处理 GET 请求一样来处理它，但是不分发实际内容。在 Flask 中你完全无需 人工 干预，底层的 Werkzeug 库已经替你打点好了。
- POST
    浏览器告诉服务器：想在 URL 上 发布 新信息。并且，服务器必须确保 数据已存储且仅存储一次。这是 HTML 表单通常发送数据到服务器的方法。
- PUT
    类似 POST 但是服务器可能触发了存储过程多次，多次覆盖掉旧值。你可 能会问这有什么用，当然这是有原因的。考虑到传输中连接可能会丢失，在 这种 情况下浏览器和服务器之间的系统可能安全地第二次接收请求，而 不破坏其它东西。因为 POST 它只触发一次，所以用 POST 是不可能的。
- DELETE
    删除给定位置的信息。
- OPTIONS
    给客户端提供一个敏捷的途径来弄清这个 URL 支持哪些 HTTP 方法。 从 Flask 0.6 开始，实现了自动处理。

```python
@app.route('/methods', methods=['GET', 'HEAD', 'POST', 'PUT', 'DELETE', 'OPTIONS'])
def methods():
    if request.method == 'GET':
        return "GET method"
    
    if request.method == 'HEAD':
        # head no response
        return "HEAD method"

    if request.method == 'POST':
        return "POST method"

    if request.method == 'PUT':
        return "PUT method"

    if request.method == 'DELETE':
        return "DELETE method"

    if request.method == 'OPTIONS':
        return "OPTIONS method"
```


#### 生成html

```python
from flask import render_template
# app.py
@app.route('/render_templates')
def render():
    return render_template('flask_index.html')
"""
# 结构
# /templates/flask_index.html
# /app.py
# more jinja2 http://docs.jinkan.org/docs/jinja2/
"""
```
#### 在模板里也可以访问的函数

- request
- session
- g object
- get_flashed_messages()

```python
@app.route('/render_templates')
def render():
    session['username'] = 'buglan'
    g.name = 'buglan'
    flash('this is flash message')
    return render_template('flask_index.html')
```

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta http-equiv="X-UA-Compatible" content="ie=edge">
    <title>Document</title>
</head>
<body>
    <p>{{ request.method }}</p>
    <p>{{ session['username'] }}</p>
    <p>{{ g.name }}</p>
    <p>{{ get_flashed_messages() }}</p>
</body>
</html>
```

```
GET

buglan

buglan

['this is flash message']
```

#### 文件上传

```python
from flask import request
from werkzeug import secure_filename

@app.route('/upload', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        f = request.files['the_file']
        f.save('/var/www/uploads/' + secure_filename(f.filename))
```

#### Cookie

```python
# get Cookies
from flask import request

@app.route('/')
def index():
    username = request.cookies.get('username')
```
```python
# save Cookies
from flask import make_response

@app.route('/')
def index():
    resp = make_response(render_template(...))
    resp.set_cookie('username', 'the username')
    return resp
```
#### 重定向和错误

```python
# 重定向
from flask import  redirect, url_for

@app.route('/')
def index():
    return redirect(url_for('login'))

```

```python
# abort 抛出http error or waring
@app.route('/login')
def login():
    abort(401)
    this_is_never_executed()
```

```python
# 定制 error or waring 页面
@app.errorhandler(404)
def page_not_found(error):
    return render_template('page_not_found.html'), 404
```

#### 关于响应

Flask 把返回值转换为响应对象的逻辑是这样：

1. 如果返回的是一个合法的响应对象，它会从视图直接返回。
2. 如果返回的是一个字符串，响应对象会用字符串数据和默认参数创建。
3. 如果返回的是一个元组，且元组中的元素可以提供额外的信息。这样的元组必须是 (response, status, headers) 的形式，且至少包含一个元素。 status 值会覆盖状态代码， headers 可以是一个列表或字典，作为额外的消息标头值。
4. 如果上述条件均不满足， Flask 会假设返回值是一个合法的 WSGI 应用程序，并转换为一个请求对象。

```python
@app.errorhandler(404)
def not_found(error):
    resp = make_response(render_template('error.html'), 404)
    resp.headers['X-Something'] = 'A value'
    return resp
```

#### 会话

```python
# 使用 session 之前 设置SECRET_KEY
# app.config['SECRET_KEY] = 'sercet_key'
 from flask import Flask, session, redirect, url_for, escape, request

app = Flask(__name__)

@app.route('/')
def index():
    if 'username' in session:
        return 'Logged in as %s' % escape(session['username'])
    return 'You are not logged in'
# escape 在模板之外转义

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        session['username'] = request.form['username']
        return redirect(url_for('index'))
    return '''
        <form action="" method="post">
            <p><input type=text name=username>
            <p><input type=submit value=Login>
        </form>
    '''

@app.route('/logout')
def logout():
    # remove the username from the session if it's there
    session.pop('username', None)
    return redirect(url_for('index'))

```
### 模板

#### jinja2配置

- 所有扩展名为 .html 、 .htm 、 .xml 以及 .xhtml 的模板会开启自动转义
- 模板可以利用 {% autoescape %} 标签选择自动转义的开关。
- Flask 在 Jinja2 上下文中插入了几个全局函数和助手，另外还有一些目前默认的值

#### 标准上下文

- config
当前的配置对象 (flask.config)


- request
当前的请求对象 (flask.request)。当模版不是在活动的请求上下文中渲染时这个变量不可用。

- session
当前的会话对象 (flask.session)。当模版不是在活动的请求上下文中渲染时这个变量不可用。

- g
请求相关的全局变量 (flask.g)。当模版不是在活动的请求上下文中渲染时这个变量不可用。

- url_for()
flask.url_for() 函数

- get_flashed_messages()
flask.get_flashed_messages() 函数

### 用蓝图实现模块化的应用

#### 为什么这样设计

- 把一个应用分解为一个蓝图的集合。这对大型应用是理想的。一个项目可以实例化一个应用对象，初始化几个扩展，并注册一集合的蓝图。
- 以 URL 前缀和/或子域名，在应用上注册一个蓝图。 URL 前缀/子域名中的参数即成为这个蓝图下的所有视图函数的共同的视图参数（默认情况下）。
- 在一个应用中用不同的 URL 规则多次注册一个蓝图。
- 通过蓝图提供模板过滤器、静态文件、模板和其它功能。一个蓝图不一定要实现应用或者视图函数。
- 初始化一个 Flask 扩展时，在这些情况中注册一个蓝图。

#### 初始化蓝图

```python
# 初始化
from flask import Blueprint

api_blueprint = Blueprint('api', __name__, template_folder='templates')
# 注册

```
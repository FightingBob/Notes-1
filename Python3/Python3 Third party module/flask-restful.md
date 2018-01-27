# Install

```bash
pip install flask-restful
```

# import 

```python
from flask_restful import Rescour
```

# Initialize

```python
from flask_restful import Api
api = Api(app)
```

# Endpoints

```python
api.add_resource(Hello, '/', '/hello', '/helloword')
```


# most small Api

```python
from flask import Flask
from flask_restful import Resource, Api

app = Flask(__name__)
api = Api(app)

class Hello(Resource):
    def get(self):
        return "most small api"

api.add_resource(Hello, '/hello')


if __name__ == '__main__':
    app.run()
```

# 快速入门
## 参数解析

```
reqparser 为你解决了验证数据的功能,简化了你的工作
```

### 初始化

```python
from flask_restful import reqparser

parser = reqparser.RequestParser()
```

### 验证参数

```python
parser.add_argument('user', type=dict, help="message")
```

### 实例化

```python
args = parser.parser_args()
```

### 实例

```python
from flask import Flask
from flask_restful import Resource, Api, reqparse


app = Flask(__name__)
api = Api(app)
parser = reqparse.RequestParser()
parser.add_argument('user', type=dict, help="user must dict type")
parser.add_argument('message', type=str, help='send_message must be str')
parser.add_argument('allow_people', type=str, help='allow_people must be str')
parser.add_argument('meeting_room', type=str, help='meeting_room must be str')



class Test1(Resource):
    def post(self):
        args = parser.parse_args()
        response = {
            "user": args['user'],
            "message": args['message'],
            "allow_people": args['allow_people'],
            "meeting_room": args['meeting_room']
        }
        return response, 200

api.add_resource(Test1, '/test1')


if __name__ == "__main__":
    app.run(debug=True)
```

### method error

```
{
    "message": "The method is not allowed for the requested URL."
}
```

### no fields

```
"no this field": args['no']

 File "e:\Notes\Python3\Python3 Third party module\code\flask-restful002.py", line 23, in post
    "no this field": args['no']
KeyError: 'no'
```

### requesr type error 

```
request
{
    "user" : {
        "username": "admin"
    },
    "message": [1,2],
    "allow_people": "all",
    "meeting_room": "meet's name"
}
response
{
    "user": {
        "username": "admin"
    },
    "message": "1",
    "allow_people": "all",
    "meeting_room": "meet's name"
}

request
{
    "user" : {
        "username": "admin"
    },
    "message": {"1": "2"},
    "allow_people": "all",
    "meeting_room": "meet's name"
}
response
{
    "user": {
        "username": "admin"
    },
    "message": "{'1': '2'}",
    "allow_people": "all",
    "meeting_room": "meet's name"
}

request
{
    "user" : {
        "username": "admin"
    },
    "message": {"1": "2"},
    "allow_people": "all",
    "meeting_room": 1
}
response
{
    "user": {
        "username": "admin"
    },
    "message": "{'1': '2'}",
    "allow_people": "all",
    "meeting_room": "1"
}

request
{
    "user" : 1,
    "message": {"1": "2"},
    "allow_people": "all",
    "meeting_room": 1
}
response 400 bad request
{
    "message": {
        "user": "user must dict type"
    }
}

request
{
    "user" : {},
    "message": {"1": "2"},
    "allow_people": "all"
}

response
{
    "user": {},
    "message": "{'1': '2'}",
    "allow_people": "all",
    "meeting_room": null
}

```

```
可见能转化的尽量会转化, 不能的则 400 bad request, request data 缺少则会使用null
```

### strict=True

```
没加
request
{
    "user" : {},
    "message": {"1": "2"},
    "allow_people": "all",
    "no": "未定义"
}
response
{
    "user": {},
    "message": "{'1': '2'}",
    "allow_people": "all",
    "meeting_room": null
}
```

```
加了
request
{
    "user" : {},
    "message": {"1": "2"},
    "allow_people": "all",
    "no": "未定义"
}
response 400 bad request
{
    "message": "Unknown arguments: no"
}
```

## 数据格式化

### import

```python
from flask_restful import fields, marshal_with
```

### 实例

```python
from flask import Flask
from flask_restful import fields, marshal_with, Api, Resource
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)
api = Api(app)

resource_fields = {
    'username': fields.String,
    "password": fields.String
}

class User(db.Model):
    __tablename__ = 'user'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(25))
    password = db.Column(db.String(50))

    def __str__(self):
        return "<User {}>".format(self.username)

class Test2(Resource):
    @marshal_with(resource_fields)
    def post(self):
        users = User.query.filter_by(username='admin').all()
        print(users)
        return users

api.add_resource(Test2, '/test2')

if __name__ == '__main__':
    db.create_all()
    app.run(debug=True)
```

# 请求解析

## 基本参数

```python
from flask_restful import reqparse

parser = reqparse.RequestParser()
parser.add_argument('rate', type=int, help="Rate cannont be canverted")
parser.add_argument('name', type=str)
args = parser.parse_args()
```
- type

```
指定的类型
```

- help

```
如果你指定了 help 参数的值，在解析的时候当类型错误被触发的时候，它将会被作为错误信息给呈现出来。如果你没有指定 help 信息的话，默认行为是返回类型错误本身的信息。
```

## 必需的参数

- required

```
要求一个值传递的参数，只需要添加 required=True 来调用 add_argument()。
```

```python
parser.add_argument('name', type=str, required=True,
help="Name cannot be blank!")
```

## 多个值&列表

```
如果你要接受一个键有多个值的话，你可以传入 action='append'
```

```python
parser.add_argument('name', type=str, action='append')

# curl http://api.example.com -d "Name=bob" -d "Name=sue" -d "Name=joe"

# args = parser.parse_args()
# args['name']    # ['bob', 'sue', 'joe']
```

## 其他目标

```
如果由于某种原因，你想要以不同的名称存储你的参数一旦它被解析的时候，你可以使用 dest kwarg。
```

```python
parser.add_argument('name', type=str, dest='public_name')

args = parser.parse_args()
args['public_name']
```

## 参数位置

```
默认下，RequestParser 试着从 flask.Request.values，以及 flask.Request.json 解析值。

在 add_argument() 中使用 location 参数可以指定解析参数的位置。flask.Request 中任何变量都能被使用
```

```python
# Look only in the POST body
parser.add_argument('name', type=int, location='form')

# Look only in the querystring
parser.add_argument('PageSize', type=int, location='args')

# From the request headers
parser.add_argument('User-Agent', type=str, location='headers')

# From http cookies
parser.add_argument('session_id', type=str, location='cookies')

# From file uploads
parser.add_argument('picture', type=werkzeug.datastructures.FileStorage, location='files')
```

## 多个位置

```
通过传入一个列表到 location 中可以指定 多个 参数位置:
```

```python
parser.add_argument('text', location=['headers', 'values'])
```

## 继承解析

```
往往你会为你编写的每个资源编写不同的解析器。这样做的问题就是如果解析器具有共同的参数。不是重写，你可以编写一个包含所有共享参数的父解析器接着使用 copy() 扩充它。你也可以使用 replace_argument() 覆盖父级的任何参数，或者使用 remove_argument() 完全删除参数
```

```python
from flask.ext.restful import RequestParser

parser = RequestParser()
parser.add_argument('foo', type=int)

parser_copy = parser.copy()
parser_copy.add_argument('bar', type=int)

# parser_copy has both 'foo' and 'bar'

parser_copy.replace_argument('foo', type=str, required=True, location='json')
# 'foo' is now a required str located in json, not an int as defined
#  by original parser

parser_copy.remove_argument('foo')
# parser_copy no longer has 'foo' argument
```

## 常见问题: 解析嵌套的dict

```python
# 实例
from flask import Flask
from flask_restful import Resource, Api, reqparse

app = Flask(__name__)
api = Api(app)


class Hello(Resource):
    """
    {
        "user" : {
            "name": "buglan,
            "sex": "man"
        }
    }
    """
    def __init__(self):
        self.parser = reqparse.RequestParser()
        self.parser.add_argument('user', type=dict)
        self.parser1 = reqparse.RequestParser()
        self.parser1.add_argument('name', type=str, location=('user'))
        super(Hello, self).__init__()
    def post(self):
        args = self.parser.parse_args()
        args1 = self.parser1.parse_args(req=args)
        print(args['user'])
        print(args1['name'])
        pass

api.add_resource(Hello, '/hello')

if __name__ == "__main__":
    app.run()
```

# 输出字段

## 基本反应

```python
from flask_restful import Resource, fields, marshal_with

resource_fields = {
    'name': fields.String,
    'address': fields.String,
    'date_updated': fields.DateTime(dt_format='rfc822'),
}

class Todo(Resource):
    @marshal_with(resource_fields, envelope='resource')
    def get(self, **kwargs):
        return db_get_todo()
```

## 重命名属性

```python
fields = {
    'name': fields.String(attribute='private_name'),
    'address': fields.String,
}
```

```python
fields = {
    'name': fields.String(attribute=lambda x: x._private_name),
    'address': fields.String,
}
```

## 默认值

```python
fields = {
    'name': fields.String(default='Anonymous User'),
    'address': fields.String,
}
```

## 自定义字段&多个值

```python
class UrgentItem(fields.Raw):
    def format(self, value):
        return "Urgent" if value & 0x01 else "Normal"

class UnreadItem(fields.Raw):
    def format(self, value):
        return "Unread" if value & 0x02 else "Read"

fields = {
    'name': fields.String,
    'priority': UrgentItem(attribute='flags'),
    'status': UnreadItem(attribute='flags'),
}
```

## Url & 其它具体字段¶

```python
class RandomNumber(fields.Raw):
    def output(self, key, obj):
        return random.random()

fields = {
    'name': fields.String,
    # todo_resource is the endpoint name when you called api.add_resource()
    'uri': fields.Url('todo_resource'),
    'random': RandomNumber,
}
```

```
默认情况下，fields.Url 返回一个相对的 uri。为了生成包含协议（scheme），主机名以及端口的绝对 uri，需要在字段声明的时候传入 absolute=True。传入 scheme 关键字参数可以覆盖默认的协议（scheme）:
```

```python
fields = {
    'uri': fields.Url('todo_resource', absolute=True)
    'https_uri': fields.Url('todo_resource', absolute=True, scheme='https')
}
```

## 列表字段

```python
>>> from flask.ext.restful import fields, marshal
>>> import json
>>>
>>> resource_fields = {'name': fields.String, 'first_names': fields.List(fields.String)}
>>> data = {'name': 'Bougnazal', 'first_names' : ['Emile', 'Raoul']}
>>> json.dumps(marshal(data, resource_fields))
>>> '{"first_names": ["Emile", "Raoul"], "name": "Bougnazal"}'
```

## 复杂结构

```python
>>> from flask.ext.restful import fields, marshal
>>> import json
>>>
>>> resource_fields = {'name': fields.String}
>>> resource_fields['address'] = {}
>>> resource_fields['address']['line 1'] = fields.String(attribute='addr1')
>>> resource_fields['address']['line 2'] = fields.String(attribute='addr2')
>>> resource_fields['address']['city'] = fields.String
>>> resource_fields['address']['state'] = fields.String
>>> resource_fields['address']['zip'] = fields.String
>>> data = {'name': 'bob', 'addr1': '123 fake street', 'addr2': '', 'city': 'New York', 'state': 'NY', 'zip': '10468'}
>>> json.dumps(marshal(data, resource_fields))
'{"name": "bob", "address": {"line 1": "123 fake street", "line 2": "", "state": "NY", "zip": "10468", "city": "New York"}}'
```

# 扩张flask-restful

# 中高级用法
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
## 安装

```
pip install flask-socketio
```

## 初始化

```python
from flask import Flask
from flask_socketio import SocketIO

app = Flask(__name__)
app.config['SECRET_KEY'] = "secret key"
socketio = SocketIO(app)

if __name__ == "__main__":
    socketio.run(app)
```
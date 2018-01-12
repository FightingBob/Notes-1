### Most small flask app

```python
from flask import Flask


app = Flask(__name__)

@app.route('/')
def index():
    return 'hello word'


if __name__ == "__main__":
    app.run()
```

### application object

- class flask.Flask(import_name, static_path=None, static_url_path=None,static_folder='static', template_folder='templates', instance_path=None, instance_relative_config=False)

参数:
	
- import_name – the name of the application package
- static_url_path – can be used to specify a different path for the static files on the web. Defaults to the name of the static_folder folder.
- static_folder – the folder with static files that should be served at  static_url_path. Defaults to the 'static' folder in the root path of the application.
- template_folder – the folder that contains the templates that should be used by the application. Defaults to 'templates' folder in the root path of the application.
- instance_path – An alternative instance path for the application. By default the folder 'instance' next to the package or module is assumed to be the instance path.
- instance_relative_config – if set to True relative filenames for loading the config are assumed to be relative to the instance path instead of the application root.

function:


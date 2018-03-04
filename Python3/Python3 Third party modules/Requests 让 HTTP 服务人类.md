
## http请求
requests.request(method, url, **kwargs)
Constructs and sends a Request.

参数:
- method -- method for the new Request object.
- url -- URL for the new Request object.

```python
>>> r = requests.request('get', 'http://www.buglan.club/')
>>> r
<Response [200]>
>>> r.status_code
200
```

- params -- (optional) Dictionary or bytes to be sent in the query string for the Request.

```python
>>> r = requests.request('post', 'http://127.0.0.1:5000/api/v1.0/test1/1', params={"message": "params"})
>>> r
<Response [200]>
>>> r.text
'{\n    "message": "\\u53d1\\u9001\\u7684\\u4e0d\\u662fjson\\u6570\\u636e"\n}\n'
>>> r.json()
{'message': '发送的不是json数据'}
```

```python
>>> import requests
>>> r = requests.get('http://127.0.0.1:5000/api/v1.0/test2/', params={"name": "buglan"})
>>> r
<Response [404]>

"""
404 not found
127.0.0.1 - - [27/Dec/2017 21:37:19] "GET /api/v1.0/test2/?name=buglan HTTP/1.1" 404 -
"""
>>> r = requests.get('http://127.0.0.1:5000/api/v1.0/test2/', params="buglan")
>>> r
<Response [404]>

"""
127.0.0.1 - - [27/Dec/2017 21:40:57] "GET /api/v1.0/test2/?buglan HTTP/1.1" 404 -
"""
```

- data -- (optional) Dictionary or list of tuples [(key, value)] (will be form-encoded), bytes, or file-like object to send in the body of the Request.

```python
>>> r = requests.post('http://127.0.0.1:5000/api/v1.0/test1/1', data={"message": "发送的是formdata"})
>>> r
<Response [200]>
>>> r.text
'{\n  "message": "\\u53d1\\u9001\\u7684\\u662fformdata"\n}\n'
>>> r.json()
{'message': '发送的是formdata'}
```

- json -- (optional) json data to send in the body of the Request.

```python
>>> r = requests.request('post', 'http://127.0.0.1:5000/api/v1.0/test1/1', json={"message": "params"})
>>> r
<Response [200]>
```
- headers -- (optional) Dictionary of HTTP Headers to send with the Request.

```python
>>> url = 'https://api.github.com/some/endpoint'
>>> headers = {'user-agent': 'my-app/0.0.1'}
>>> r = requests.get(url, headers=headers)
```

- cookies -- (optional) Dict or CookieJar object to send with the Request.
- files -- (optional) Dictionary of 'name': file-like-objects (or {'name': file-tuple}) for multipart encoding upload. file-tuple can be a 2-tuple ('filename', fileobj), 3-tuple ('filename', fileobj, 'content_type') or a 4-tuple ('filename', fileobj, 'content_type', custom_headers), where 'content-type' is a string defining the content type of the given file and custom_headers a dict-like object containing additional headers to add for the file.
- auth -- (optional) Auth tuple to enable Basic/Digest/Custom HTTP Auth.
- timeout (float or tuple) -- (optional) How many seconds to wait for the server to send data before giving up, as a float, or a (connect timeout, read - timeout) tuple.

```python
>>> r = requests.get('http://127.0.0.1:5000/api/v1.0/test1/1', timeout=2)
Traceback (most recent call last):
  File "D:\python35\lib\site-packages\urllib3\connectionpool.py", line 387, in _make_request
    six.raise_from(e, None)
  File "<string>", line 2, in raise_from
  File "D:\python35\lib\site-packages\urllib3\connectionpool.py", line 383, in _make_request
    httplib_response = conn.getresponse()
  File "D:\python35\lib\http\client.py", line 1198, in getresponse
    response.begin()
  File "D:\python35\lib\http\client.py", line 297, in begin
    version, status, reason = self._read_status()
  File "D:\python35\lib\http\client.py", line 258, in _read_status
    line = str(self.fp.readline(_MAXLINE + 1), "iso-8859-1")
  File "D:\python35\lib\socket.py", line 576, in readinto
    return self._sock.recv_into(b)
socket.timeout: timed out

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "D:\python35\lib\site-packages\requests\adapters.py", line 440, in send
    timeout=timeout
  File "D:\python35\lib\site-packages\urllib3\connectionpool.py", line 639, in urlopen
    _stacktrace=sys.exc_info()[2])
  File "D:\python35\lib\site-packages\urllib3\util\retry.py", line 357, in increment
    raise six.reraise(type(error), error, _stacktrace)
  File "D:\python35\lib\site-packages\urllib3\packages\six.py", line 686, in reraise
    raise value
  File "D:\python35\lib\site-packages\urllib3\connectionpool.py", line 601, in urlopen
    chunked=chunked)
  File "D:\python35\lib\site-packages\urllib3\connectionpool.py", line 389, in _make_request
    self._raise_timeout(err=e, url=url, timeout_value=read_timeout)
  File "D:\python35\lib\site-packages\urllib3\connectionpool.py", line 309, in _raise_timeout
    raise ReadTimeoutError(self, url, "Read timed out. (read timeout=%s)" % timeout_value)
urllib3.exceptions.ReadTimeoutError: HTTPConnectionPool(host='127.0.0.1', port=5000): Read timed out. (read timeout=2)

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "<pyshell#8>", line 1, in <module>
    r = requests.get('http://127.0.0.1:5000/api/v1.0/test1/1', timeout=2)
  File "D:\python35\lib\site-packages\requests\api.py", line 72, in get
    return request('get', url, params=params, **kwargs)
  File "D:\python35\lib\site-packages\requests\api.py", line 58, in request
    return session.request(method=method, url=url, **kwargs)
  File "D:\python35\lib\site-packages\requests\sessions.py", line 508, in request
    resp = self.send(prep, **send_kwargs)
  File "D:\python35\lib\site-packages\requests\sessions.py", line 618, in send
    r = adapter.send(request, **kwargs)
  File "D:\python35\lib\site-packages\requests\adapters.py", line 521, in send
    raise ReadTimeout(e, request=request)
requests.exceptions.ReadTimeout: HTTPConnectionPool(host='127.0.0.1', port=5000): Read timed out. (read timeout=2)
```

- allow_redirects (bool) -- (optional) Boolean. Enable/disable GET/OPTIONS/POST/PUT/PATCH/DELETE/HEAD redirection. Defaults to True.
- proxies -- (optional) Dictionary mapping protocol to the URL of the proxy.
- verify -- (optional) Either a boolean, in which case it controls whether we verify the server's TLS certificate, or a string, in which case it must be a path to a CA bundle to use. Defaults to True.
- stream -- (optional) if False, the response content will be immediately downloaded.
- cert -- (optional) if String, path to ssl client cert file (.pem). If Tuple, ('cert', 'key') pair.   


requests.head(url, **kwargs)
Sends a HEAD request.

参数:	
url -- URL for the new Request object.
**kwargs -- Optional arguments that request takes.
返回:	
Response object

返回类型:	
requests.Response


requests.get(url, params=None, **kwargs)
Sends a GET request.

参数:	
url -- URL for the new Request object.
params -- (optional) Dictionary or bytes to be sent in the query string for the Request.
**kwargs -- Optional arguments that request takes.
返回:	
Response object

返回类型:	
requests.Response


requests.post(url, data=None, json=None, **kwargs)
Sends a POST request.

参数:	
url -- URL for the new Request object.
data -- (optional) Dictionary (will be form-encoded), bytes, or file-like object to send in the body of the Request.
json -- (optional) json data to send in the body of the Request.
**kwargs -- Optional arguments that request takes.
返回:	
Response object

返回类型:	
requests.Response


requests.put(url, data=None, **kwargs)
Sends a PUT request.

参数:	
url -- URL for the new Request object.
data -- (optional) Dictionary (will be form-encoded), bytes, or file-like object to send in the body of the Request.
json -- (optional) json data to send in the body of the Request.
**kwargs -- Optional arguments that request takes.
返回:	
Response object

返回类型:	
requests.Response


requests.patch(url, data=None, **kwargs)
Sends a PATCH request.

参数:	
url -- URL for the new Request object.
data -- (optional) Dictionary (will be form-encoded), bytes, or file-like object to send in the body of the Request.
json -- (optional) json data to send in the body of the Request.
**kwargs -- Optional arguments that request takes.
返回:	
Response object

返回类型:	
requests.Response


requests.delete(url, **kwargs)
Sends a DELETE request.

参数:	
url -- URL for the new Request object.
**kwargs -- Optional arguments that request takes.
返回:	
Response object

返回类型:	
requests.Response


## 异常

异常
exception requests.RequestException(*args, **kwargs)
There was an ambiguous exception that occurred while handling your request.

exception requests.ConnectionError(*args, **kwargs)
A Connection error occurred.

exception requests.HTTPError(*args, **kwargs)
An HTTP error occurred.

exception requests.URLRequired(*args, **kwargs)
A valid URL is required to make a request.

exception requests.TooManyRedirects(*args, **kwargs)
Too many redirects.

exception requests.ConnectTimeout(*args, **kwargs)
The request timed out while trying to connect to the remote server.

Requests that produced this error are safe to retry.

exception requests.ReadTimeout(*args, **kwargs)
The server did not send any data in the allotted amount of time.

exception requests.Timeout(*args, **kwargs)
The request timed out.

Catching this error will catch both ConnectTimeout and ReadTimeout errors.

## 请求会话


待续...

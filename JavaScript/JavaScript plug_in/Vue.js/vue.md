### first vue

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta http-equiv="X-UA-Compatible" content="ie=edge">
    <script src="https://cdn.bootcss.com/vue/2.4.2/vue.min.js"></script>
    <title>Document</title>
</head>
<body>
    <div id="app">
        <p>{{message}}</p>
    </div>
    <script>
        new Vue({
            el: '#app',
            data: {
                message: "hello vue.js!!!"
            }
        })
    </script>
</body>
</html>
```

### 指令绑定: v-bind

```html
<div id="app2">
    <span v-bind:title="message">sdasdasdas</span>
</div>
```

```js
var app2 = new Vue({
                el: "#app2",
                data: {
                    message: '页面加载于' + new Date().toLocaleString()
                }
            })
```

### if & for: v-if & v-for

```html
<div id="app3">
        <span v-if="seen">now i see you</span>
    </div>
    <div id="app4">
        <ol>
            <li v-for="todo in todos">{{ todo.text }}</li>
        </ol>
    </div>
```

```js
var app3 = new Vue({
            el: '#app3',
            data: {
                seen: true
            }
        }) 
var app4 = new Vue({
    el: '#app4',
    data: {
        todos: [
            {text: "study english"},
            {text: "study js"},
            {text: "study css"},
            {text: "study python"}
        ]
    }
})
```

chrome console
```shell
app3.seen = false
# now you can see it
app4.todos.push({ text: '新项目' })
# add a new item
```

### 逆转消息: v-on

```html
 <div id="app5">
        <p>{{ message }}</p>
        <button v-on:click="reverseMessage">reverse message</button>
    </div>
```

```js
var app5 = new Vue({
            el: '#app5',
            data: {
                message: 'zhi is reverse message'
            },
            methods: {
                reverseMessage: function () {
                    this.message = this.message.split('').reverse().join('')
                }
            }

        })
```

### 注册组件

```html
<ol id="app1">
        <todo-item></todo-item>
</ol>
```

```js
 Vue.component('todo-item', {
        template:  '<li>this is a todo item</li>' 
    })
    var app1 = new Vue({
        el: '#app1'
    })
    // or
    new Vue({
        el: '#app1'
    })
```

搭配用法

```html
<div id="app2">
         <ol>
            <t-item
            v-for="item in Lists"
            v-bind:todo="item"
            v-bind:key="item.id"></t-item>
         </ol>   
    </div>
```

```js
// register component
Vue.component('t-item', {
        props: ['todo'],
        template: '<li>{{ todo.text }}</li>'
    })

var app2 = new Vue({
        el: '#app2',
        data: {
            Lists: [
                {id: 0, text: '蔬菜'},
                {id: 1, text: '西红柿'},
                {id: 2, text: '武器'},
                {id: 3, text: '剑圣'},
            ]
        }

    })
```

### 生命周期图示

![vue 生命周期](./code/lifecycle.png)

### 一次性地插值: v-once

```html
 <div id="app1">
        <p>change: {{ todo }}</p>
    </div>
    <div id="app2">
        <p v-once>not change: {{ todo }}</p>
    </div>
```

```js
 var app1 = new Vue({
        el: '#app1',
        data: {
            todo: 'this is todo test'
        }
    })
    var app2 = new Vue({
        el: '#app2',
        data: {
            todo: 'this is todo test'
        }
    })
```

chrome console

```shell
app1.todo = "changed test"
"changed test"
# app1.todo change to changed test
app2.todo = "not changed text"
"not changed text"
# app2.todo not chanegd
```
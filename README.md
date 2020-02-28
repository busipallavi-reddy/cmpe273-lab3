# Lab 3

## Pre-requisites

* Install _Pipenv_

```
pip install pipenv
```

* Install _[Flask](https://palletsprojects.com/p/flask/)_

```
pipenv install flask==1.1.1
```
* Install _[Ariadne](https://ariadnegraphql.org/docs/flask-integration.html)_ for handling GraphQL schema and binding.

```
pipenv install ariadne==0.10.0
```

* Create a schema.py and add this code:

```python
TBD
```

* Create a file called _app.py_ and add this code snippet.

```python
from flask import Flask, escape, request

@app.route('/')
def hello():
    name = request.args.get("name", "World")
    return f'Hello, {escape(name)}!'
```

* Run your Hello World Flask application from a shell/terminal.

```sh
pipenv shell
$ env FLASK_APP=app.py flask run
```

* Open [this URL](http://127.0.0.1:5000/) in a web browser or run this CLI to see the output.

```
curl -i http://127.0.0.1:5000/
```

## Requirements

You will be building a RESTful class registration API in this lab.

### Domain Model

```
|-------|               |---------|
| Class |* ---------- * | Student |
|-------|               |---------|
```

### GraphQL operations to be implemented.

* Quety an existing student

_Request_

```
{
  students(id:1) {
    name
  }
}
```

_Response_

```
{
    "name" : "Bob Smith"
}
```

- Mutate a new student

```
mutation {
  create_student(name:"Pallavi") {
  	id
    name
  }
}
```

* Mutate a class

```
mutation {
  create_class(name:"CMPE273") {
  	id
    name
  }
}
```

* Query a class

```
{
classes(id:141){
    name
    students{
      id
      name
    }
  }
}
```

* Add students to a class

```
mutation{
  update_class(student_id:1, class_id: 1) {
    id
    name
    students {
      id
      name
    }
  }
}
```




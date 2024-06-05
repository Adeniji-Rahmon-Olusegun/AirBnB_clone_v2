# 0x04. AirBnB clone - Web framework

---
### What is a Web Framework?

A web framework provides a foundation for developing web applications. It takes care of common tasks like handling web requests, routing, and templating, allowing developers to focus on the application's logic and functionality.

###  A Minimal Flask Application

Here's a basic Flask application that defines a route and returns a simple message:

```python
from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello_world():
  return "Hello, World!"

if __name__ == "__main__":
  app.run(debug=True)
```

This code creates a Flask instance (`app`), defines a route (`/`) that maps to the `hello_world` function, and runs the development server.

### Routing

Routes define the URLs that trigger specific functions within your application. In Flask, you use the `@app.route` decorator to associate a URL with a function.

**Note:** This guide excludes explanations of HTTP methods (GET, POST, etc.) for brevity.

### Rendering Templates

Jinja is a powerful templating engine used with Flask. It allows you to create dynamic HTML pages by separating the page structure (HTML) from the application logic (Python).

Here's an example using a Jinja template:

**templates/index.html:**

```html
<!DOCTYPE html>
<html>
<head>
  <title>My Flask App</title>
</head>
<body>
  <h1>Hello, {{ name }}!</h1>
</body>
</html>
```

**Python code (app.py):**

```python
from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def hello():
  name = "World"
  return render_template("index.html", name=name)

# ... (rest of your application code)
```

This example defines a template (`index.html`) with a placeholder `{{ name }}`. The `render_template` function renders the template and replaces placeholders with values passed from Python (in this case, `name="World"`).

### Synopsis

This guide provides a brief introduction to Flask and Jinja. Key concepts covered include:

- Creating a Flask application
- Defining routes
- Using Jinja templates for dynamic content

###  Variables

In Flask templates, you can use variables passed from Python code using double curly braces (`{{ variable_name }}`).

###  Comments

Jinja supports comments using the `{# ... #}` syntax. Comments are ignored when rendering the template.

###  Whitespace Control

Jinja allows you to control whitespace output using tags like `{% spaceless %}` and `{% endspaceless %}`.

###  Control Structures (up to Call)

Jinja provides various control structures like `if` statements, `for` loops, and more. You can use them to conditionally render content or loop through data.

**Note:** This guide covers control structures up to "Call" for brevity. Refer to Jinja documentation for details on all supported structures.

### Flask and Jinja Resources

This guide provides a starting point for web development with Flask and Jinja. Here are some resources for further learning:

- Flask documentation: [https://flask.palletsprojects.com/](https://flask.palletsprojects.com/)
- Jinja documentation: [https://palletsprojects.com/p/](https://palletsprojects.com/p/)

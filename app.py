from flask import Flask, request
from markupsafe import escape

from webargs import fields
from webargs.flaskparser import use_args

app = Flask(__name__)


# Get Holle World route http://localhost:48000/hello
@app.route('/hello')
def hello_route():  # put application's code here
    return 'Hello world'


# Get route for named user http://localhost:48000/user/Bob/45
@app.route('/user/<username>/<int:number>')
def dynamic_route(username, number):
    return f'Hello {escape(username)}, your number is {number}.'


# Get route with arguments as http://localhost:48000/greeting?name=Bob&age=2
@app.route('/greeting')
def query_route():
    name_param = request.args.get('name')
    age_param = request.args.get('age')

    return f'Hello {name_param}, your number is {age_param}.'


# Get route with arguments as http://localhost:48000/webarg_greeting/45?name=Bob
@app.route("/webarg_greeting/<int:age>")
@use_args({"name": fields.Str()}, location="query")
def user_detail(args, age):
    return "The user page for user {age}, showing {name} posts.".format(
        age=age, name=args["name"]
    )


if __name__ == '__main__':
    app.run()

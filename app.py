from flask import Flask, escape, request
from schema import Query
from flask_graphql import GraphQLView
from graphene import Schema

view_func = GraphQLView.as_view(
    'graphql', schema=Schema(query=Query), graphiql=True)


app = Flask(__name__)
app.add_url_rule('/graphql', view_func=view_func)

@app.route('/')
def hello():
    name = request.args.get("name", "World")
    return f'Hello, {escape(name)}!'

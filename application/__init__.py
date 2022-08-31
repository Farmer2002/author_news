from flask import Flask
from flask_restx import Api
from flask import Blueprint


blueprint = Blueprint('authornews',__name__)


from application.authornews import api as authnews 


api = Api(blueprint,
            title='AuthorNews',
            version='1.0',
            description='Some Statiscal Analysis on Crypto News',
            )

api.add_namespace(authnews)
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
# from flask_marshmallow import Marshmallow
from flask_cors import CORS
import mysql
import pyotp
from flask_mail import Mail


app = Flask(__name__)

#mail_configuration
app.config['MAIL_SERVER']='smtp.gmail.com'
app.config['MAIL_PORT'] = 465
app.config['MAIL_USERNAME'] = 'rubanjhonny01@gmail.com'
app.config['MAIL_PASSWORD'] = 'rock307700'
app.config['MAIL_USE_TLS'] = False
app.config['MAIL_USE_SSL'] = True
mail = Mail(app)

#OTP configuration
otp = pyotp.TOTP('base32secret3232',interval=300)

#CORS Prevention
cors = CORS(app,resources={r"/*": {"origins": "*"}})
app.config['CORS_HEADERS'] = 'Content-Type'

#JWT Token_key
app.config['SECRET_KEY'] = 'thisissecret'

#MSSQL SERVER connection
password='Rock#306605'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS']= True
app.config['SQLALCHEMY_DATABASE_URI'] = f"mysql://ruban:{password}@localhost:3306/Sample"
db = SQLAlchemy(app)

#Marshmallow Serializer
# ma=Marshmallow(app)
# class UsersSchema(ma.Schema):
#     class Meta:
#         fields=("user_id", "user_name", "first_name","last_name","designation",
#                 "department","email_id","contact_no","location","imageURL","mediaURL","isActive",
#                 "created_on","created_by","updated_on","updated_by","reportingTo")

# users_schema = UsersSchema(many=True)
# user_schema=UsersSchema()
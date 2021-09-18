from flask import request, jsonify
import uuid
from werkzeug.security import generate_password_hash, check_password_hash
import jwt
import datetime
from waitress import serve
from flask_mail import Message
from models import Users
from basicConfig import app,db,cors,mail,otp
import json 



@app.route('/login',methods=["POST"])
def login():
    data = request.get_json(force=True)

    if not data['userName'] or not data['password']:
        return jsonify({'success':False,'message':"Input fields cant be empty"})

    logging_user = Users.query.filter_by(user_name=data['userName']).first()

    if not logging_user:
        return jsonify({'success':False,'message':"Username or Password is Incorrect"})

    if check_password_hash(logging_user.password, data['password']):
        token = jwt.encode({'user_id' : logging_user.user_id, 'exp' : datetime.datetime.utcnow() + datetime.timedelta(minutes=1440)}, app.config['SECRET_KEY'])
        return jsonify({'token' : token,'success':True,'username':data["userName"]})

    return jsonify({'success':False,'message':"Username or Password is Incorrect"})

@app.route('/signup', methods=['POST'])
def create_user():
    data =request.get_json(force=True)
    hashed_password = generate_password_hash(data['password'], method='sha256')
    new_user = Users(user_id=str(uuid.uuid4()), user_name=data['username'], password=hashed_password, first_name=data['firstname'],last_name=data['lastname'],email_id=data["email"],contact_no=data["contactno"])
    #check if user already exist
    users = Users.query.all()
    user_name=[]
    for row in users:
        user_name.append(row.user_name)
    if data["username"] in user_name:
        return (jsonify({'message':"user name already exist"}))
    db.session.add(new_user)
    db.session.commit()
    return jsonify({'message' : 'New user created!','success':True})

@app.route('/forgetPassword',methods=["POST"])
def forget_password():
    data = request.get_json(force=True)
    if not data['email']:
        return jsonify({'message':'email cannot be empty'})

    user = Users.query.filter_by(email_id=data['email']).first()

    if not user:
        return jsonify({'message':'User is not available'})
    else:
        msg = Message('Hello', sender = 'rubanjhonny01@gmail.com', recipients = [user.email_id])
        msg.body = f"Hi your OTP is {otp.now()}"
        mail.send(msg)
        return jsonify({'success':True,'message':'sent'})

@app.route('/verifyOtp',methods=["POST"])
def verify_Otp():
    data=request.get_json(force=True)
    if otp.verify(data["otp"]):
        return jsonify({'message':"Correct","success":True})
    else:
        return jsonify({'message':"invalid or expired","success":False})

@app.route('/changePassword',methods=["POST"])
def change_password():
    data=request.get_json(force=True)
    user=db.session.query(Users).filter_by(email_id=data['email']).first()
    if not user:
        return jsonify({"message":"email not found","success":False})
    newpass=generate_password_hash(data['password'], method='sha256')
    user.password=newpass
    db.session.commit()
    return ({'message':"Password updated","success":True})



if __name__ == '__main__':
    serve(app, host='0.0.0.0', port=8080)
    # app.run(debug=True)
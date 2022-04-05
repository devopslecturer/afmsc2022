"""
# ----------------------
# Created : 17-01-2022 14:26
# Licencing : (C) 2021 Dalimol Abraham, LYIT
#             Available under GNU public licence
# Description: 
# Author : Dalimol Abraham
# ----------------------
"""
from builtins import Exception

import boto3
import flask
from botocore.exceptions import ClientError
from flask import Flask, render_template, request, flash, redirect,jsonify
from sqlalchemy.dialects import mysql
from models import User

from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash

app = Flask(__name__)

db = SQLAlchemy()

def index():
   return render_template('reset_password/reset_password.html')

def reset():
     if request.method == 'POST':
        _username = request.form['email']
        # send_email(_username)
        # return "success"
        if _username  is not None:
            user = User.query.filter_by(email=_username).first()
            if user:
                 send_email(_username)
            else:
                return jsonify({"reason": "User not found", "status": "404"})
            return render_template('users/index.html')
        else:
            return jsonify({"status": "400", "reason": "Bad Request"})
def send_email(_username):
    SENDER = "Aaadms Family <shanmarsh1234@gmail.com>"
    RECIPIENT = _username
    CONFIGURATION_SET = "ConfigSet"
    AWS_REGION = "eu-west-1"
    SUBJECT = "Amazon SES Test (SDK for Python)"
    BODY_TEXT = ("Amazon SES Test (Python)\r\n"
                 "This email was sent with Amazon SES using the "
                 "AWS SDK for Python (Boto)."
                )

    # The HTML body of the email.
    BODY_HTML = """
          <h3>ADDAMS FAMILY</h3>
          <p style="font-size: 18px">A password reset for your account was requested.
            Please click the  below link to change your password.
           </p>
           <a style="font-size: 18px" href="{}/reset-password/reset_temp" target="_blank"> Change your password</a>
    
            """.format(flask.request.host)

    # The character encoding for the email.
    CHARSET = "UTF-8"

    # Create a new SES resource and specify a region.
    client = boto3.client('ses',region_name=AWS_REGION)

    # Try to send the email.
    try:
        #Provide the contents of the email.
        response = client.send_email(
            Destination={
                'ToAddresses': [
                    RECIPIENT,
                ],
            },
            Message={
                'Body': {
                    'Html': {
                        'Charset': CHARSET,
                        'Data': BODY_HTML,
                    },
                    'Text': {
                        'Charset': CHARSET,
                        'Data': BODY_TEXT,
                    },
                },
                'Subject': {
                    'Charset': CHARSET,
                    'Data': SUBJECT,
                },
            },
            Source=SENDER,
            # following line
            # ConfigurationSetName=CONFIGURATION_SET,
        )
    # Display an error if something goes wrong.
    except ClientError as e:
        print(e.response['Error']['Message'])
    else:
        print("Email sent! Message ID:"),
        print(response['MessageId'])
def reset_temp():
   return render_template('reset_password/new_password.html')
def update_password():
    try:
        _username = request.form['username']
        print(_username);
        _pwd = request.form['cnfrm-pswd']
        user = User.query.filter_by(email=_username).first()
        if user:
            user.password = _pwd
            db.session.add(user)
            db.session.commit()
            return render_template('login/index.html')
        else:
            print("User not found")
            raise Exception

    except Exception as err:
        print(err)
        return "<h1> User not found</h1>", 404

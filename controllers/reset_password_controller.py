"""
# ----------------------
# Created : 17-01-2022 14:26
# Licencing : (C) 2021 Dalimol Abraham, LYIT
#             Available under GNU public licence
# Description: 
# Author : Dalimol Abraham
# ----------------------
"""
import boto3
from botocore.exceptions import ClientError
from flask import Flask, render_template, request, flash, redirect
from sqlalchemy.dialects import mysql

from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash

app = Flask(__name__)

db = SQLAlchemy()

def index():
   return render_template('reset_password/reset_password.html')

def reset():
     if request.method == 'POST':
        _username = request.form['email']
        if _username  is not None:
            # user = User.query.filter_by(email=_username).first()
            # print(user.firstName)
            # if user:
            #     return render_template('users/index.html')
            # else:
            #     return jsonify({"reason": "User not found", "status": "404"})
            send_email(_username)
        else:
            return jsonify({"status": "400", "reason": "Bad Request"})
def send_email(_username):
    SENDER = "Sender Name <sender@example.com>"

    RECIPIENT = _username

    CONFIGURATION_SET = "ConfigSet"
    AWS_REGION = "us-west-2"
    SUBJECT = "Amazon SES Test (SDK for Python)"
    BODY_TEXT = ("Amazon SES Test (Python)\r\n"
                 "This email was sent with Amazon SES using the "
                 "AWS SDK for Python (Boto)."
                )

    # The HTML body of the email.
    BODY_HTML = """<html>
    <head></head>
    <body>
      <h1>Amazon SES Test (SDK for Python)</h1>
      <p>This email was sent with
        <a href='https://aws.amazon.com/ses/'>Amazon SES</a> using the
        <a href='https://aws.amazon.com/sdk-for-python/'>
          AWS SDK for Python (Boto)</a>.</p>
    </body>
    </html>
                """

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
            ConfigurationSetName=CONFIGURATION_SET,
        )
    # Display an error if something goes wrong.
    except ClientError as e:
        print(e.response['Error']['Message'])
    else:
        print("Email sent! Message ID:"),
        print(response['MessageId'])

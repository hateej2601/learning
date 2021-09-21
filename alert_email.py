#!/usr/bin/env python
import snowflake.connector
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import getpass

pswd = getpass.getpass('Password:')
# Gets the version
ctx = snowflake.connector.connect(
    user='hateej2601',
    password=pswd,
    account='hya96711.us-east-1',
    role = 'ACCOUNTADMIN',
    database = 'COMPUTE_WH',
    warehouse = 'DEMO_DB',
    schema = 'PUBLIC'
    )
cs = ctx.cursor()

cs.execute("use warehouse compute_wh")
emails = ['hanbn17411@st.uel.edu.vn']
result = cs.execute("call flex_db.dev.check_error(%s, %s)", ('VEHICLEDEFINITION_ERROR_STREAM', 'MT_DOC_VEHICLEDEFINITION_ERROR')).fetchone()
content = 'Dear team, \n\n' + result[0]
# connect to server
s = smtplib.SMTP(host='smtp.office365.com', port=587)
s.ehlo()
s.starttls()
s.login('hateej2601@gmail.com', 'Convitvang*1')
# email
msg = MIMEMultipart()
msg['From'] = 'hateej2601@gmail.com'
msg['To'] = emails[0]
msg['Subject'] = 'Null data in raw tables.'
msg.attach(MIMEText(content))
# send
s.send_message(msg)
print('Email sent!')

cs.close()
ctx.close()
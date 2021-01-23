import os
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail


def enviar_mail():

    message = Mail(
        from_email='tesis_lau_majo@hotmail.com',
        to_emails='padagoal012@gmail.com',
        subject='Sending with Twilio SendGrid is Fun, SUPER FUN',
        html_content='<strong>and easy to do anywhere, even with Python</strong>')

    API_KEY = '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'

    try:
        sg = SendGridAPIClient(API_KEY)
        response = sg.send(message)
        print(response.status_code)
        print(response.body)
        print(response.headers)
    except Exception as e:
        print(e)

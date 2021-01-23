import os
from sendgrid import SendGridAPIClient, sendgrid
from sendgrid.helpers.mail import Mail

API_KEY = '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'


def enviar_mail():
    message = Mail(
        from_email='tesis_lau_majo@hotmail.com',
        to_emails='padagoal012@gmail.com',
        subject='Sending with Twilio SendGrid is Fun, SUPER FUN',
        html_content='<strong>and easy to do anywhere, even with Python</strong>')

    try:
        sg = SendGridAPIClient(API_KEY)
        response = sg.send(message)
        print(response.status_code)
        print(response.body)
        print(response.headers)
    except Exception as e:
        print(e)


def enviar_mail_personalizado(ciudad,hotel,habitacion,checkin,checkout,costo,personas, receptor):
    sg = sendgrid.SendGridAPIClient(API_KEY)
    data = {
        "from": {
            "email": "tesis_lau_majo@hotmail.com"
        },
        "personalizations": [
            {
                "to": [
                    {
                        "email": receptor
                    }
                ],
                "dynamic_template_data": {
                    "ciudad": ciudad,
                    "hotel": hotel,
                    "habitacion": habitacion,
                    "checkin": checkin,
                    "checkout": checkout,
                    "costo": costo,
                    "personas": personas

                }
            }
        ],
        "template_id": "d-0e86a7b2c25544d995416ff97e776168"
    }
    print(data)
    try:
        response = sg.client.mail.send.post(request_body=data)
        print(response.status_code)
        print(response.body)
        print(response.headers)
    except Exception as e:
        print(e)





import os
from sendgrid import SendGridAPIClient, sendgrid
from sendgrid.helpers.mail import Mail

API_KEY = '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'
sg = sendgrid.SendGridAPIClient(API_KEY)


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


def enviar_mail_personalizado_hotel(ciudad,hotel,habitacion,checkin,checkout,costo,personas, receptor):
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

    try:
        response = sg.client.mail.send.post(request_body=data)
        return 'OK'
    except Exception as e:
        print(e)
        return 'NO'


def enviar_mail_personalizado_tour(reservaTour, receptor):
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
                    "tour": reservaTour.tour_selected.tour_name,
                    "fecha": reservaTour.fecha_tour_reserva.strftime('%d/%m/%Y'),
                    "ciudades": reservaTour.tour_selected.get_ciudades(),
                    "lugar": reservaTour.tour_selected.get_places_names(),
                    "costo": reservaTour.tour_cost,
                    "personas": reservaTour.cantidad_personas_tour,

                }
            }
        ],
        "template_id": "d-b8c48877c22d4bd99dc7c22b3e7624b3"
    }

    try:

        response = sg.client.mail.send.post(request_body=data)
        return response
    except Exception as e:
        print(e)
        return 'NO'


def enviar_mail_contacto(nombre,asunto,correo,mensaje):
    data = {
        "from": {
            "email": "tesis_lau_majo@hotmail.com"
        },
        "personalizations": [
            {
                "to": [
                    {
                        "email": "padagoal012@gmail.com"
                    }
                ],
                "dynamic_template_data": {
                    "nombre": nombre,
                    "asunto": asunto,
                    "correo": correo,
                    "mensaje": mensaje,
                }
            }
        ],
        "template_id": "d-5d06edfacd934e7792551a5b824d00cd"
    }

    try:

        response = sg.client.mail.send.post(request_body=data)
        return response
    except Exception as e:
        print(e)
        return 'NO'

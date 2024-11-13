from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.utils.html import strip_tags
from django.conf import settings

def send_checkout_email(user_email, order):
    print("Sending mail now")
    subject = "Order Confirmation"
    html_message = render_to_string('emails/order_confirmation.html', {'order': order})
    plain_message = strip_tags(html_message)  # Convert HTML to plain text
    from_email = settings.DEFAULT_FROM_EMAIL
    to_email = [user_email]
    send_mail(subject, plain_message, from_email, to_email, html_message=html_message)
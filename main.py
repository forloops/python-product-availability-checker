from gazpacho import get
from bs4 import BeautifulSoup
import smtplib

url = 'https://shop.flipperzero.one/'
html = get(url)
soup = BeautifulSoup(html, features="html.parser")

found = soup.select('span[data-add-to-cart-text]')


def send_email():
    gmail_user = 'edward.comarzan@gmail.com'
    gmail_password = 'biuadulrtoceyuhy'

    sent_from = gmail_user
    to = ['i74oodxa1s@pomail.net']
    subject = 'Flipper Zero In Stock!'
    body = 'Flipper Zero might be back in stock. Please check the website and good luck!'
    email_text = """\
    From: %s
    To: %s
    Subject: %s

    %s

    """ % (sent_from, ", ".join(to), subject, body)

    try:

        smtp_server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
        smtp_server.ehlo()
        smtp_server.login(gmail_user, gmail_password)
        smtp_server.sendmail(sent_from, to, email_text)
        smtp_server.close()
        print("Email sent successfully!")
    except Exception as ex:
        print("Something went wrong….", ex)


if 'Sold out' in found[0].text:
    send_email()
    print('Flipper Sold out')
else:
    print('Flipper In Stock!')

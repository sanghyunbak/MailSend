# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import argparse
import os
import smtplib
import traceback
from email import encoders
from email.header import Header
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

from termcolor import colored


def set_smtp_connection(mail_server: str, port: int, id: str, password: str):
    print(colored(f"{type(password)}", "green"))
    print(colored(f"password: {password}", "green"))
    s = smtplib.SMTP(mail_server, port)
    s.starttls()
    s.login(id, password)
    return s


def sendmail(password):
    s = set_smtp_connection(mail_server='smtp.gmail.com', port=587, id='sanghyunbak@gmail.com', password=password)
    msg = MIMEText('내용 : 본문내용 테스트입니다.')
    message = MIMEMultipart("mixed")
    message['Subject'] = Header(s='파일첨부 메일송신 테스트', charset='utf-8')
    message.set_charset('utf-8')
    message.attach(msg)

    attach_binary = MIMEBase("application", "octet-stream")

    attachment = os.path.join(os.path.abspath(os.path.dirname(__file__)), 'img.png')
    try:
        binary = open(attachment, "rb").read()
        attach_binary.set_payload(binary)
        encoders.encode_base64(attach_binary)

        filename = os.path.basename(attachment)
        attach_binary.add_header("Content-Disposition", "attachment", filename=('utf-8', '', filename))
        message.attach(attach_binary)
    except Exception as e:
        print(colored(f"{traceback.format_exc()}", "red"))
    s.sendmail("sanghyunbak@gmail.com", "sanghyunbak@gmail.com", message.as_string())
    s.quit()


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='password add')
    parser.add_argument('--password', metavar='N', type=str)
    args = parser.parse_args()
    sendmail(args.password)

# See PyCharm help at https://www.jetbrains.com/help/pycharm/

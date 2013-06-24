#!/usr/bin/env python
# -*- coding: utf-8 -*-

from getpass import getpass
from smtplib import SMTP

def connect(host=None, port=None, user=None, password=None, tls=True,
            prompt_user=None, prompt_password='password? '):

    server = SMTP(host, port)

    if tls:
        server.starttls()

    if not user and prompt_user:
        user = raw_input(prompt_user)

    if user and not password and prompt_password:
        password = getpass(prompt_password)

    if user and password:
        server.login(user, password)

    return server

def send(body, **kargs):

    if '_server' in kargs:
        server = kargs['_server']
        connected_by_me = False
    else:
        server = connect(
            **dict((k[1:], v) for k, v in kargs.items() if k.startswith('_'))
        )
        connected_by_me = True

    sendmail_kargs = {'from': '', 'to': ''}

    headers = []

    for key, value in kargs.items():

        if key.startswith('_'): continue

        key = key.rstrip('_').lower().replace('_', '-')
        if key in sendmail_kargs:
            sendmail_kargs[key] = value

        if hasattr(value, '__iter__') and not isinstance(value, str):
            value = ', '.join(value)

        headers.append('%s: %s' % (key, value))

    headers = '\r\n'.join(headers)

    server.sendmail(sendmail_kargs['from'], sendmail_kargs['to'], '%s\r\n\r\n%s' % (headers, body))

    if connected_by_me:
        server.quit()

def gsend(body, **kargs):
    kargs['_host'] = 'smtp.gmail.com:587'
    return send(body, **kargs)

if __name__ == '__main__':

    gsend(
        _user   = 'mosky.bot@gmail.com',
        from_   = '"Mosky Bot" <mosky.bot@gmail.com>',
        to      = ['"Mosky Liu" <mosky.tw@gmail.com>', '"Mosky Liu" <mosky.liu@pinkoi.com>'],
        cc      = '"Mosky Bot" <mosky.bot@gmail.com>',
        subject = 'Hello :) cc pinkoi v4',
        body    = ':D'
    )

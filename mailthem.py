#!/usr/bin/env python
# -*- coding: utf-8 -*-

from getpass import getpass
from smtplib import SMTP

def connect(host=None, port=None, user=None, password=None, tls=True, prompt_user=None, prompt_password='password? '):

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

def send(server, body, **headers_dict):

    connected_by_me = False

    if isinstance(server, basestring):
        server = connect(server)
        connected_by_me = True

    primary_kargs = {'from': None, 'to': None}

    headers = []

    for key, value in headers_dict.items():

        key = key.rstrip('_').lower().replace('_', '-')
        if key in primary_kargs:
            primary_kargs[key] = value

        if hasattr(value, '__iter__') and not isinstance(value, str):
            value = ', '.join(value)

        headers.append('%s: %s' % (key, value))

    headers = '\r\n'.join(headers)

    server.sendmail(primary_kargs['from'], primary_kargs['to'], '%s\r\n\r\n%s' % (headers, body))

    if connected_by_me:
        server.quit()


if __name__ == '__main__':

    server = connect('smtp.gmail.com:587', user='mosky.bot@gmail.com')
    server.set_debuglevel(2)

    send(
        server,
        from_   = '"Mosky Bot" <mosky.bot@gmail.com>',
        to      = '"Mosky Liu" <mosky.tw@gmail.com>',
        cc      = '"Mosky Liu" <mosky.liu@pinkoi.com>',
        subject = 'Hello :) cc pinkoi',
        body    = ':D'
    )

    server.quit()

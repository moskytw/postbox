#!/usr/bin/env python
# -*- coding: utf-8 -*-

from postbox import Gmail

with Gmail(user='mosky.bot@gmail.com') as gmail:

    gmail.send(
        from_   = 'Mosky Bot <mosky.bot@gmail.com>',
        to      = 'Mosky Liu <mosky.tw@gmail.com>',
        subject = 'Test from Postbox :) #simplest',
        body    = ':D',
    )

    gmail.send(
        from_   = 'Mosky Bot <mosky.bot@gmail.com>',
        to = [
            'Mosky Liu <mosky.tw@gmail.com>',
            'Mosky Liu <mosky.liu@pinkoi.com>',
            'Mosky Liu <mosky@ubuntu-tw.org>'
        ],
        cc = [
            'Mosky Liu <mosky.tw@gmail.com>',
            'Mosky Liu <mosky.liu@pinkoi.com>',
            'Mosky Liu <mosky@ubuntu-tw.org>'
        ],
        subject = 'Test from Postbox :) #multi-to-cc',
        body    = ':D',
    )

    gmail.send(
        from_    = 'Mosky Bot <mosky.bot@gmail.com>',
        to       = 'Mosky Liu <mosky.tw@gmail.com>',
        reply_to = 'Mosky Bot <mosky.bot+123@gmail.com>',
        subject  = 'Test from Postbox :) #reply-to',
        body     = ':D',
    )

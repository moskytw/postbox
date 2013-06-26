Postbox
=======

It makes sending mail easier. The main features:

1. It allows you specify message headers by keyword arguments.
2. Support interactive prompt for username or password.
3. Support optional `with` statement.

Installation
------------

You can install it via PyPI,

::

    sudo pip install postbox

or download it manually.

Examples
--------

It is an example which sends a mail from Python shell.

::

    >>> from postbox import Postbox, Gmail

    >>> gmail = Postbox(host='smtp.google.com:587') # or gmail = Gmail()
    username? mosky.bot@gmail.com
    password? 

    >>> gmail.send(
    ...     to = ['mosky.tw@gmail.com', 'mosky.liu@pinkoi.com'],
    ...     bcc = 'mosky@ubuntu-tw.org',
    ...     subject = 'Test from Python Shell',
    ...     body = 'It is sent by postbox. :)'
    ... )
    ... 

    >>> gmail.close()
    >>>

You can find more examples `here
<https://github.com/moskytw/postbox/tree/master/examples>`_.

Usage
-----

`Postbox`
~~~~~~~~~

The ``Postbox`` (or ``Gmail``) accepts the following keyword arguments:

1. ``host``: the hostname of your SMTP server. ex. 'smtp.google.com' or
   'smtp.google.com:587'
2. ``port``: the port number of your SMTP server.
3. ``user``: the username.
4. ``password``: the password.
5. ``tls``: use tls or not.
6. ``prompt_user``: prompt string if you don't specified ``user``.
7. ``prompt_password``: prompt string if you don't specified ``password``.
8. ``debuglevel``: the debuglevel.
9. ``dry_run``: don't send the mail out.


`postbox.send`
~~~~~~~~~~~~~~

The all keyword arguments to ``send`` will be translated into message headers,
except the ``body`` is the body of this mail. The common headers list:

1. ``to``: It it used as the `to_addrs
   <http://docs.python.org/2/library/smtplib.html#smtplib.SMTP.sendmail>`_, so
   you must to specify it.
2. ``from_``: It is used as the `from_addr
   <http://docs.python.org/2/library/smtplib.html#smtplib.SMTP.sendmail>`_. If
   you don't specify it, it takes the ``user`` from `Postbox` instance as
   default.
3. ``subject``
4. ``cc``
5. ``bcc``
6. ``reply_to``

If a value is iterable but not a string, it will be joined into a string by
comma.

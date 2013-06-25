Postbox
=======

It makes sending mail easier. The main features:

1. It allows you specify headers by keyword arguments.
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

    >>>     gmail.send(
    ...             to = ['mosky.tw@gmail.com', 'mosky.liu@pinkoi.com'],
    ...             bcc = 'mosky@ubuntu-tw.org',
    ...             subject = 'Test from Python Shell',
    ...             body = 'It used postbox to send. :)'
    ...     )
    ... 

    >>> gmail.close()
    >>>

You can find more examples `here
<https://github.com/moskytw/postbox/tree/master/examples>`_.

Documentation
-------------

The ``Postbox`` or ``Gmail`` accepts the following keyword arguments:

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

The all keyword arguments to ``send`` will be translated into headers, except
the ``body`` is the body of this mail. If you don't specify ``from_``, it takes
the username as default. The iterable but not string will be joined to a string
by comma.

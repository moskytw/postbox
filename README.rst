Postbox
=======

It makes sending mail easier. The main features:

1. It allows you specify SMTP headers by keyword arguments.
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

It is an example which sends a mail from Python Shell.

::

    >>> from postbox import Gmail

    >>> gmail = Gmail()
    username? mosky.bot@gmail.com
    password? 

    >>>     gmail.send(
    ...             to = ['mosky.tw@gmail.com', 'mosky.liu@pinkoi.com'],
    ...             bcc = 'mosky@ubuntu-tw.org',
    ...             subject = 'Test from Python Shell',
    ...             body = 'It is used postbox to send. :)'
    ...     )
    ... 

    >>> gmail.close()
    >>>

You can find more examples `here
<https://github.com/moskytw/postbox/tree/master/examples>`_.

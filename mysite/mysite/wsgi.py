"""
WSGI config for mysite project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/1.11/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "mysite.settings")

application = get_wsgi_application()

http_proxy = "172.16.2.30:8080"
https_proxy = "172.16.2.30:8080"
ftp_proxy = "172.16.2.30:8080"

proxyDict = {
		"http"	:http_proxy,
		"https"	:https_proxy,
		"ftp"	:ftp_proxy
}

os.environ["PROXIES"] = str(proxyDict)

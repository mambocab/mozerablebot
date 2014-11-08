#!/usr/bin/env python
import os

def application(environ, start_response):
    start_response('301 Redirect', [('Location', 'https://twitter.com/mozerablebot'),])
    return []

#
# Below for testing only
#
if __name__ == '__main__':
    from wsgiref.simple_server import make_server
    httpd = make_server('localhost', 8051, application)
    # Wait for a single request, serve it and quit.
    httpd.handle_request()

#!/usr/bin/env python
#-*- coding: utf-8 -*-

from wsgiref.simple_server import WSGIServer, WSGIRequestHandler
import multiprocessing.pool
import json
import traceback
import shutil
import os
import amqp
import time
from app import app
import db

import urlparse

amqp.get_amqplib_connection()
amqp.get_connection()
db.get_connections()

def application(environ, start_response):

    start_time = time.time()
    output = {}

    try:
        output = app(
            command_name=environ['PATH_INFO'].strip('/'),
            data=urlparse.parse_qs(environ['QUERY_STRING'])
        )
    except Exception as e:
        output['error'] = str(e)
        traceback.print_exc()

    start_response("200 OK", [('Content-Type', 'application/json')])
    output['time'] = '%.3f ms' % ((time.time() - start_time) * 1000)
    return [json.dumps(output, indent=2)]


class ThreadPoolWSGIServer(WSGIServer):

    def __init__(self, thread_count=None, *args, **kwargs):
        '''If 'thread_count' == None, we'll use multiprocessing.cpu_count() threads.'''
        WSGIServer.__init__(self, *args, **kwargs)
        self.thread_count = thread_count
        self.pool = multiprocessing.pool.ThreadPool(self.thread_count)

    # Inspired by SocketServer.ThreadingMixIn.
    def process_request_thread(self, request, client_address):
        try:
            self.finish_request(request, client_address)
            self.shutdown_request(request)
        except:
            self.handle_error(request, client_address)
            self.shutdown_request(request)

    def process_request(self, request, client_address):
        self.pool.apply_async(self.process_request_thread, args=(request, client_address))


def make_server(host, port, app, thread_count=None, handler_class=WSGIRequestHandler):
    httpd = ThreadPoolWSGIServer(thread_count, (host, port), handler_class)
    httpd.set_app(app)
    return httpd


print 'Starting...'
httpd = make_server('', 8080, application)
httpd.serve_forever()

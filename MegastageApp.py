#!/usr/bin/env python
import os

import tornado.httpserver
import tornado.ioloop
import tornado.web
import Settings

import ui_modules

class MainHandler(tornado.web.RequestHandler):
    def get(self, filename):
        filename = {
            '': 'index.html',
        }.get(filename, filename)

        self.render("template.html", filename=filename)


class MegastageApp(tornado.web.Application):
    def __init__(self):
        url_patterns = [
            (r"/favicon.ico", tornado.web.StaticFileHandler, {'path': Settings.STATIC_PATH}),
            (r"/(images/.*)", tornado.web.StaticFileHandler, {'path': Settings.STATIC_PATH}),
            (r"/(css/.*)", tornado.web.StaticFileHandler, {'path': Settings.STATIC_PATH}),
            (r"/(specs/.*)", tornado.web.StaticFileHandler, {'path': Settings.STATIC_PATH}),
            (r"/(megastage/.*)", tornado.web.StaticFileHandler, {'path': Settings.STATIC_PATH}),
            (r"/(.*)", MainHandler),
        ]
        settings = {
            "ui_modules": ui_modules,
            "template_path": Settings.TEMPLATE_PATH,
            "static_path": Settings.STATIC_PATH,
        }
        tornado.web.Application.__init__(self, url_patterns, **settings)


def main():
    app = MegastageApp()
    http_server = tornado.httpserver.HTTPServer(app)
    http_server.listen(8080)
    tornado.ioloop.IOLoop.instance().start()

if __name__ == "__main__":
    main()

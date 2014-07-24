import tornado
import tornado.web

class MainPage(tornado.web.UIModule):
    def render(self, filename):
        return self.render_string("module-%s" % filename)



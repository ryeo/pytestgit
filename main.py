from google.appengine.ext import webapp


class MainHandler(webapp.RequestHandler):
    def get(self):
        self.response.out.write('Hellddddddddsssddddddmmmmmmdddo world!')


app = webapp.WSGIApplication([('/', MainHandler)],
                             debug=True)


from google.appengine.ext import webapp


class MainHandler(webapp.RequestHandler):
    def get(self):
        self.response.out.write('Feature world! Master Update 1 by Team 2')


app = webapp.WSGIApplication([('/', MainHandler)],
                             debug=True)


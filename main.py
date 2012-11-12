from google.appengine.ext import webapp


class MainHandler(webapp.RequestHandler):
    def get(self):
        self.response.out.write('Feature world! Master Update 2 by Team 1')


app = webapp.WSGIApplication([('/', MainHandler)],
                             debug=True)


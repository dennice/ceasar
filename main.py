
import webapp2
import cgi


from ceasar import encrypt
form="""
<form method="post">
    <label> What text do you want to encrypt?<input name="thingy" value="%(thingy)s">
    </label>
    <br>
    <br>
    <label> How many numbers do you want to encrypt by?<input name="rot" value="%(rot)s">
    </label>
    <div style="color: red">%(error)s</div>
    <br>
    <br>
    <input type="submit" value="Submit"/>
</form>
"""

#how to validate negative numbers and 0? isinstance
def valid_rot(rot):
    if rot and rot.isdigit():
        return int(rot)
#def escape_html(s):
#    return cgi.escape(s, quote =True)


class AddThing(webapp2.RequestHandler):
    """requests to encrypt"""
    def write_form(self, error="", rot="", thingy=""):
        self.response.out.write(form % {"error": (error),
                                        "rot": (rot),
                                        "thingy":(thingy)})

    def get(self):
        self.write_form()

    def post(self):

        user_rot = self.request.get('rot')
        thingy = self.request.get('thingy')
        rot = valid_rot(user_rot)
        encrypted_word = encrypt(thingy, rot)

        if not rot:
            self.write_form("That is not a valid rotation number.", user_rot, thingy)
        else:
            self.write_form("", "", encrypted_word)




app = webapp2.WSGIApplication([
    ('/', AddThing)
], debug=True)

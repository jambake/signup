import webapp2
import re

# html boilerplate for the top of every page
page_header = """
<!DOCTYPE html>
<html>
<head>
    <title>Signup</title>
    <style type="text/css">
        .error {
            color: red;
        }
    </style>
</head>
<body>
    <h3>
        <a href="/">Signup</a>
    </h3>
"""

# html boilerplate for the bottom of every page
page_footer = """
</body>
</html>
"""

USER_RE = re.compile(r"^[a-zA-Z0-9_-]{3,20}$")
def valid_username(username):
    return username and USER_RE.match(username)

PASS_RE = re.compile(r"^.{3,20}$")
def valid_password(password):
    return password and PASS_RE.match(password)

EMAIL_RE  = re.compile(r'^[\S]+@[\S]+\.[\S]+$')
def valid_email(email):
    return not email or EMAIL_RE.match(email)


class MainHandler(webapp2.RequestHandler):

    def get(self):

        form="""
        <form method="post">
            <table style="width:50%">
                <tr>
                    <td>Username</td>
                    <td>
                        <input name="username" type="text">
                    </td>
                    <td></td>
                </tr>
                <tr>
                    <td>Password</td>
                    <td>
                        <input name="password" type="password">
                    </td>
                    <td></td>
                </tr>
                <tr>
                    <td>Verify Password</td>
                    <td>
                        <input name="verify" type="password">
                    </td>
                    <td></td>
                </tr>
                <tr>
                    <td>Email (optional)</td>
                    <td>
                        <input name="email" type="email">
                    </td>
                    <td></td>
                </tr>
            </table>
            <input type="submit">
        </form>
        """

        response = page_header + form + page_footer
        self.response.write(response)


    def post(self):

        username = self.request.get('username')
        password = self.request.get('password')
        verify = self.request.get('verify')
        email = self.request.get('email')
        error1 = ""
        error2 = ""
        error3 = ""
        error4 = ""

        if not valid_username(username):
            error1 = "That's not a valid username."

        if not valid_password(password):
            error2 = "That wasn't a valid password."

        if not password == verify:
            error3 = "Your passwords didn't match."

        if not valid_email(email):
            error4 = "That's not a valid email."

        form="""
        <form method="post">
            <table style="width:50%">
                <tr>
                    <td>Username</td>
                    <td>
                        <input name="username" type="text">
                    </td>
                    <td>%s</td>
                </tr>
                <tr>
                    <td>Password</td>
                    <td>
                        <input name="password" type="password">
                    </td>
                    <td>%s</td>
                </tr>
                <tr>
                    <td>Verify Password</td>
                    <td>
                        <input name="verify" type="password">
                    </td>
                    <td>%s</td>
                </tr>
                <tr>
                    <td>Email (optional)</td>
                    <td>
                        <input name="email" type="email">
                    </td>
                    <td>%s</td>
                </tr>
            </table>
            <input type="submit">
        </form>
        """ % (error1, error2, error3, error4)


        response = page_header + form + page_footer
        self.response.write(response)




app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)

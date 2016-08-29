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


form = """
<form method="post">
    <table>
        <tr>
            <th>Username</th>
            <td>
                <input name="username" type="text" value="{0}">
            </td>
            <td class="error">{1}</td>
        </tr>
        <tr>
            <th>Password</th>
            <td>
                <input name="password" type="password">
            </td>
            <td class="error">{2}</td>
        </tr>
        <tr>
            <th>Verify Password</th>
            <td>
                <input name="verify" type="password">
            </td>
            <td class="error">{3}</td>
        </tr>
        <tr>
            <th>Email (optional)</th>
            <td>
                <input name="email" type="email" value="{4}">
            </td>
            <td class="error">{5}</td>
        </tr>
    </table>
    <input type="submit">
</form>
"""

class MainHandler(webapp2.RequestHandler):

    def get(self):

        temp = ""
        response = page_header + form.format(temp, temp, temp, temp, temp, temp) + page_footer
        self.response.write(response)

    def post(self):
        has_error = False
        user_name = self.request.get("username")
        pass_word = self.request.get("password")
        verify_pass = self.request.get("verify")
        user_email = self.request.get("email")
        error1 = ""
        error2 = ""
        error3 = ""
        error4 = ""

        if not valid_username(user_name):
            error1 = "That's not a valid username."
            has_error = True
        if not valid_password(pass_word):
            error2 = "That wasn't a valid password."
            has_error = True
        if not pass_word == verify_pass:
            error3 = "Your passwords didn't match."
            has_error = True
        if not valid_email(user_email):
            error4 = "That's not a valid email."
            has_error = True

        if has_error:
            response = page_header + form.format(user_name, error1, error2, error3, user_email, error4) + page_footer
            self.response.write(response)
        else:
            self.redirect('/welcome?username=%s' % user_name)

class WelcomePage(webapp2.RequestHandler):

    def get(self):
        username = self.request.get("username")
        response = "Welcome, " + username + "!"
        self.response.write(response)


app = webapp2.WSGIApplication([
    ('/', MainHandler),
    ('/welcome', WelcomePage)
], debug=True)

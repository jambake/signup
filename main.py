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

class MainHandler(webapp2.RequestHandler):

    def get(self):

        form="""
        <form method="post">
            <table style="width:50%">
                <tr>
                    <td><label for="username">Username</label></td>
                    <td>
                        <input name="username" type="text" value="" required>
                    </td>
                </tr>
                <tr>
                    <td><label for="password">Password</label></td>
                    <td>
                        <input name="password" type="password" value="" required>
                    </td>
                </tr>
                <tr>
                    <td><label for="verify">Verify Password</label></td>
                    <td>
                        <input name="verify" type="password" value="" required>
                    </td>
                </tr>
                <tr>
                    <td><label for="email">Email (optional)</label></td>
                    <td>
                        <input name="email" type="email" value="">
                    </td>
                </tr>
            </table>
            <input type="submit">
        </form>
        """

        response = page_header + form + page_footer
        self.response.write(response)


    def post(self):

        def valid_username(username):
            USERNAME_RE = re.compile(r"^[a-zA-Z0-9_-]{3,20}$")
            return USERNAME_RE.match(username)

        def valid_password(verify):
            VERIFYPASS_RE = re.compile(r"^.{3,20}$")
            return VERIFYPASS_RE.match(verify)

        def valid_email(email):
            EMAIL_RE = re.compile(r"^[\S]+@[\S]+.[\S]+$")
            return EMAIL_RE.match(email)


        #                 <span class="error">That&#39;s not a valid username</span>
        #
        #                 <span class="error"></span>
        #             
        #                 <span class="error">Passwords don&#39;t match</span>
        #
        #                 <span class="error"></span>
        #
        #
        # response = page_header + form + page_footer
        # self.response.write(response)




app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)

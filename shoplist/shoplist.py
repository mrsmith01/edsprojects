import os

import jinja2
import webapp2

form_html = """
<form>
<h3>Add a Food</h3>
<input type="text" name="food">
%s
<br><br><button>Add Food</button>
</form>
"""

hidden_html = """
<input type="hidden" name="food" value="%s">
"""
item_html = "<li>%s</li>"

shoplist_html= """
<br>
<br>
<h1>Shopping List</h1>
<ul>
%s
</ul>
"""

class MainPage(webapp2.RequestHandler):
    def get(self):
        output = form_html
        output_hidden = ""

        items = self.request.get_all("food")
        if items:
            output_items = ""
            for item in items:
                output_hidden += hidden_html % item
                output_items += item_html % item

            output_shopping = shoplist_html % output_items
            output += output_shopping

        output = output % output_hidden

        self.response.out.write(output)

app = webapp2.WSGIApplication([ ('/', MainPage), ], debug=True)

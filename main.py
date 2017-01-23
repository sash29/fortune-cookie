#!/usr/bin/env python
#
# Copyright 2007 Google Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
import webapp2
import random

def getrandomFortune()
    fortunes = [ "I see much code in your future",
    "Consider eating more fortune cookies",
    "Unleash the Python onto the the Great Spider's Web...as you cut through the jungles of Java..."]

    index = random.randint(0,2)
    return fortunes[index]

class MainHandler(webapp2.RequestHandler):
    def get(self):
        header = "<h1>Fortune Cookie</h1>"
        fortune = "<strong>" + getrandomFortune() + "</strong>"
        display_fortune = "Your fortune for today : "+fortune
        fortune_para = "<p>" +display_fortune+"</p>"

        lucky_number = "<strong>" + str(random.randint(1, 100))+ "</strong>"
        display_number = "Your lucky number is : "+(lucky_number)
        number_para = "<p>" + display_number + "</p>"

        another_cookie_button = "<a href='.'><button> Another cookie pls! </button></a>"
        content = header + fortune_para + number_para + another_cookie_button
        self.response.write(content)

app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)

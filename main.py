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
import re
from controllers.SignUp import SignUpHandler
from controllers.LogIn import LogInHandler
from controllers.LogOut import LogOutHandler
from controllers.EditPage import EditPageHandler
from controllers.MainHandler import MainHandler

PAGE_RE = r'(/(?:[a-zA-Z0-9_-]+/?)*)'

app = webapp2.WSGIApplication([
    ('/signup', SignUpHandler),
    ('/login',LogInHandler),
    ('/logout',LogOutHandler),
    ('/_edit' + PAGE_RE, EditPageHandler),
    (PAGE_RE, MainHandler)
], debug=True)

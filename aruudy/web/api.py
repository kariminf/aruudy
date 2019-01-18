#!/usr/bin/env python
# -*- coding: utf-8 -*-

#  Copyright 2019 Abdelkrime Aries <kariminfo0@gmail.com>
#
#  ---- AUTHORS ----
#  2019    Abdelkrime Aries <kariminfo0@gmail.com>
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
# http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#

from flask import jsonify, Blueprint
from flask_cors import CORS

import sys, os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "../..")))

from aruudy.poetry import prosody, meter

aruudy_api = Blueprint("aruudy_api", __name__, template_folder="templates")

CORS(aruudy_api)

#headers = {
#    "Content-Type": "application/json",0
#    "charset": "utf-8"
#}

@aruudy_api.route("/info/<name>", methods=["GET", "POST"])
def info(name):
    b = meter.get_bahr(name)
    if b == None:
        return "Bahr not found", 404
    return jsonify(b), 200

@aruudy_api.route("/ls", methods=["GET", "POST"])
def bahrs_list():
    # res = {
    # "arabic": meter.arabic_names(),
    # "english": meter.english_names(),
    # "trans": meter.trans_names()
    # }
    res = meter.get_names()
    return jsonify(res), 200

def xor_in(elem, set_elem, bool):
    if bool:
        return elem in set_elem
    return elem not in set_elem

@aruudy_api.route("/shatr/<text>", methods=["GET", "POST"])
@aruudy_api.route("/shatr/<text>/<opt>", methods=["GET", "POST"])
def process_shatr(text, opt=None):
    s = prosody.process_shatr(text).to_dict(bahr=True)
    res = 200
    if not s["bahr"]:
        res = 404
    if opt:
        exclude = opt.startswith("-")
        set_keys = opt.replace("-","").split(",")
        bahr = s["bahr"]
        keys = [k for k in s.keys()]
        for key in keys:
            if xor_in(key, set_keys, exclude):
                if key == "bahr":
                    if s["bahr"]:
                        s["bahr"] = s["bahr"]["name"]
                else:
                    del s[key]
    return jsonify(s), res

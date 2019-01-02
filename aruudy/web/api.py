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

from flask import Flask, jsonify, Response

import sys, os
reload(sys)
sys.setdefaultencoding("utf8")
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "../..")))

from aruudy.poetry import bahr, meter
from aruudy.poetry.bahr import Bahr, BahrError

app = Flask(__name__)
app.config["JSON_AS_ASCII"] = False
#headers = {
#    "Content-Type": "application/json",0
#    "charset": "utf-8"
#}

@app.route("/info/<name>", methods=["GET", "POST"])
def info(name):
    b = bahr.get_bahr(name)
    if b == None:
        return "Bahr not found", 404
    return jsonify(b), 200

@app.route("/ls", methods=["GET", "POST"])
def bahrs_list():
    res = {
    "arabic": bahr.arabic_names(),
    "english": bahr.english_names(),
    "trans": bahr.trans_names()
    }
    return jsonify(res), 200

@app.route("/shatr/<text>", methods=["GET", "POST"])
def process_shatr(text):
    s = meter.process_shatr(text).to_dict(bahr=True)
    return jsonify(s), 200

if __name__ == "__main__":
    app.run(debug=True)

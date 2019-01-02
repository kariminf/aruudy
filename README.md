# Aruudy

[![Project](https://img.shields.io/badge/Project-Aruudy-0BDA51.svg?style=plastic)](http://ararud.sourceforge.net)
[![License](https://img.shields.io/badge/License-Apache_2-0BDA51.svg?style=plastic)](http://www.apache.org/licenses/LICENSE-2.0)
[![PyPI](https://img.shields.io/pypi/v/aruudy.svg?style=plastic)](https://pypi.python.org/pypi/aruudy)
[![Downloads](https://img.shields.io/pypi/dm/aruudy.svg?style=plastic)](https://pypi.org/project/aruudy/)
[![Python version](https://img.shields.io/pypi/pyversions/aruddy.svg?style=plastic)](https://pypi.org/project/aruudy/)
[![Travis](https://img.shields.io/travis/kariminf/aruudy.svg?style=plastic)](https://travis-ci.org/kariminf/aruudy)
[![Codecov](https://img.shields.io/codecov/c/github/kariminf/aruudy.svg?style=plastic)](https://codecov.io/gh/kariminf/aruudy)
[![CodeFactor](https://www.codefactor.io/repository/github/kariminf/aruudy/badge/master)](https://www.codefactor.io/repository/github/kariminf/aruudy/overview/master)
[![codebeat badge](https://codebeat.co/badges/9ea7f2f7-58cb-4df9-b4b7-33d33aee07aa)](https://codebeat.co/projects/github-com-kariminf-aruudy-master)
[![Code Climate](https://img.shields.io/codeclimate/maintainability-percentage/kariminf/aruudy.svg?style=plastic)](https://codeclimate.com/github/kariminf/aruudy/)

Aruudy is a light library for Arabic prosody (Aruud) or "Science of Poetry".

[Test here](http://ararud.sourceforge.net)

## Features

- bahr
    - Recover all meters (arabic name, english name, transliterated name)
    - Get the meters information by either its arabic or english names

- poetry
    - Information about Arabic poetery meters
    - Normalizing part (shatr) of a verse: delete tatweel, add forgotten diacretics
    - Writing the part into prosody form
    - Finding the arabic prosodic units "watad" and "sabab" based on haraka (vowel)
    - Finding the english prosodic units based on syllables
    - Detecting Arabic poetry meter

- web
    - API with flask
    - CGI (Common Gateway Interface) program


## Use

### Install

```
pip install aruudy
```

### Command line

```
aruudy -b 'أَسِرْبَ القَطا هَلْ مَنْ يُعِيْرُ جَناحَهُ'
```

### Programming

Arabic poetry meter detection

```python
#!/usr/bin/env python
# -*- coding: utf-8 -*-

from aruudy.poetry import meter

text = u'أَسِرْبَ القَطا هَلْ مَنْ يُعِيْرُ جَناحَهُ'

shatr = meter.process_shatr(text)

#original text
print("original: " + shatr.orig)

#Normalized text
print("normalized: " + shatr.norm)

#prosody form
print("prosody form: " + shatr.prosody)

# Farahidi meter for poetry
print("arabic scansion: " + shatr.ameter)

# Western-like metre
print("western scansion: " + shatr.emeter)

#get the bahr: it has aname, ename, trans, 
b = shatr.bahr


```

## Recommendations

To detect the meter, the poem's part must be fully vocalized (has diacritics).
To this end, It is recommended to use [Mishkal](https://github.com/linuxscout/mishkal)

@TODO more examples

## License
Copyright (C) 2014-2017 Abdelkrime Aries

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

[http://www.apache.org/licenses/LICENSE-2.0](http://www.apache.org/licenses/LICENSE-2.0)

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.

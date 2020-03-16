# -*- coding: utf-8 -*-
"""
Created on Mon Jun 17 14:46:03 2019

@author: Dilan Ramirez
"""

import requests
url = 'https://raw.githubusercontent.com/...'
page = requests.get(url)
print(page.text)
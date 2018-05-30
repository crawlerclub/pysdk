#!/usr/bin/env python
# -*- coding:utf-8 -*-
#
from sdk import client

api = client("ak", "sk")
url = "https://api.crawler.club/phone"
post_data = {"number": "13800138000", }
print(api.request(url, post_data))


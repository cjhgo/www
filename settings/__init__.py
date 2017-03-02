#coding: utf-8
#created at 17-3-2 14:17

import os

API_HOST = "info.local.cjhang.com"

www_env = os.getenv("API_ENV", "local")
if www_env == "production":
    from production import *

#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import hmac

message = b'hello world!'
key = b'123456'
h = hmac.new(key, message, digestmod='MD5')
print(h.hexdigest())
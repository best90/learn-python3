#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from PIL import Image

im = Image.open('test.jpg')
w, h = im.size
print('Original image size: %s x %s' % (w,h))

im.thumbnail((w//2, h//2))
print('Resize image to : %s x %s' % (w//2, h//2))
im.save('thumbnail.jpg', 'jpeg')
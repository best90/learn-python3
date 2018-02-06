#!/usr/bin/env python3
# -*- coding: utf-8 -*-

class HtmlOutput(object):
    def __init__(self):
        self.data = []

    def collect_data(self, data):
        if data in None:
            return
        self.data.append(data)

    def output_html(self):
        fp = open('output.html','w', encoding='utf-8')

        fp.write("<html>")
        fp.write("<head><meta http-equiv=\"content-type\" content=\"text/html;charset=utf-8\"></head>")
        fp.write("<body>")
        fp.write("<table>")

        for item in self.data:
            fp.write("<tr>")
            fp.write("<td>%s</td>" % item['url'])
            fp.write("<td>%s</td>" % item['title'])
            fp.write("<td>%s</td>" % item['summary'])
            fp.write("</tr>")

        fp.write("</table>")
        fp.write("</body>")
        fp.write("</html>")
        fp.close()
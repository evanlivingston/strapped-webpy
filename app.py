import web
import os
import urllib
import posixpath

urls = (
    '/(js|css|img)/(.*)', 'static',
    '/.*', 'index',
    )
app = web.application(urls, globals())

class index:
    def GET(self):
        render = web.template.render('templates/', base='layout')
        return render.index()

class static:
    def GET(self, media, file):
        try:
            f = open(media+'/'+file, 'r')
            return f.read()
        except:
            return '' # you can send an 404 error here if you want

if __name__ == "__main__":
        app.run()


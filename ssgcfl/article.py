import frontmatter as ft
from dateutil import parser
import jinja2
from datetime import datetime
import os
from markdown2 import Markdown
from slugify import slugify

class Article(object):
    def __init__(self, filename, settings):
        filename = os.path.join(settings.content, filename)
        self.filename = filename
        self.matter = ft.load(filename).to_dict()
        #print(self.file_content)
        self.title = self.matter.get('title', 'Untitled')
        #print(self.title)

        self.slug = self.matter.get('slug', slugify(self.title))
        self.url = '.'.join([self.slug, 'html'])
        if 'date' in self.matter:
            d = parser.parse(self.matter['date'])
            self.date = d.strftime('%Y-%m-%d %H:%M')
        else:
            self.date = self.get_create_time(filename)
        self.content = self.matter.get('content', '')
        self.html = Markdown().convert(self.content)
        #print("bu html")
        #print(self.html)
        self.rendered = jinja2.Template(self.html).render(article=self, settings=settings)

    def get_create_time(self, filename):
        created = datetime.fromtimestamp(os.stat(filename).st_ctime)
        return created.strftime('%Y-%m-%d %H:%M')


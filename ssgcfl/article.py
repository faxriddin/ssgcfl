import os
from dateutil import parser
from datetime import datetime
import jinja2
import frontmatter as ft
from markdown2 import Markdown
from slugify import slugify


class Article(object):
    def __init__(self, filename, settings):
        filename = os.path.join(settings.content, filename)
        self.filename = filename
        self.matter = ft.load(filename).to_dict()

        self.title = self.matter.get('title', 'Untitled')

        self.slug = self.matter.get('slug', slugify(self.title))
        self.url = '.'.join([self.slug, 'html'])
        if 'date' in self.matter:
            d = parser.parse(self.matter['date'])
            self.date = d.strftime('%Y-%m-%d %H:%M')
        else:
            self.date = self.get_create_time(filename)
        self.content = self.matter.get('content', '')
        self.html = Markdown().convert(self.content)

        self.rendered = jinja2.Template(self.html).render(article=self, settings=settings)

    def get_create_time(self, filename):
        created = datetime.fromtimestamp(os.stat(filename).st_ctime)
        return created.strftime('%Y-%m-%d %H:%M')


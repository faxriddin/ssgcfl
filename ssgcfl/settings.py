class Settings(object):
    def __init__(self, settings):
        self.templates = settings.get('templates', 'templates')
        self.content = settings.get('content', 'content')
        self.output = settings.get('output', 'output')
        self.site_name = settings.get('site_name', 'My Blog')
        self.site_author = settings.get('site_author', 'Anonymous')

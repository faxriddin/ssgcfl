"""SSGCFL

Usage:
    ssgcfl create_project <project_name>
    ssgcfl make_site [<file_settings>]

Options:
    -h --help  Show this screen.
    --version  Show version.  
"""


__author__ = 'Faxriddin Baltayev'
__version__ = '0.0.1'


from docopt import docopt
import json
import shutil
import sys
import os
from jinja2 import Environment, FileSystemLoader
from . import article as article_class
from . import settings as settings_class


SOURCE_URLS = {
    'templates':'templates',    
}


ARTICLES_SORT_REVERSE_BY_DATE = True


class Generator:
    """
        Main class that used for generating sites.


        Attributes
        ----------
        settings : Settings
            Settings object that has global settings params for creating project structure.
        files : list
            all article files that located in the "content" directory
        articles : list
            list of Article objects, where all articles loaded from content
        jinja : Environment
            jinja local environment. Used loader method and global`s variables.

        Methods
        -------
        load_articles()
            load markdown files from content to files attribute
        order_articles()
            initialize articles attribute from loaded files then sort by date their
        create_output_dir()
            creating output dir from manually using settings or default settings
        generate_index()
            generating index file from index.html template by rendering jinja template
        self.generate_articles()
    """

    def __init__(self, settings):
        self.settings = settings_class.Settings(settings)
        self.files = []
        self.articles = []
        self.jinja = Environment()
        if self.settings.templates:
            self.jinja.loader = FileSystemLoader(self.settings.templates)
        else:
            print("Fail on load templates")
            sys.exit(0)
        self.jinja.globals = dict(settings=self.settings, articles=self.articles)

    def load_articles(self):
        """
        Load markdown (.md) articles from our content directory.
        """

        for f in os.listdir(self.settings.content):
            if f.endswith(('.md', '.MD', '.markdown')):
                print(" Loaded: " + f)
                self.files.append(f)
                article = article_class.Article(f, self.settings)
                self.articles.append(article)

    def order_articles(self):
        """
        Order by date.
        """

        self.articles = sorted(self.articles, key=lambda a: a.date, reverse=ARTICLES_SORT_REVERSE_BY_DATE)

    def create_output_dir(self):
        """
        Creating site output directory. In this directory will be save all
        generated site resources.
        """

        if not os.path.exists(self.settings.output):
            os.mkdir(self.settings.output)

    def generate_index(self):
        """
        Creating the index file, and save in output.
        """

        index_tmpl = self.jinja.get_template('index.html')
        with open(os.path.join(self.settings.output, 'index.html'), 'w') as f:
            f.write(index_tmpl.render())

    def generate_articles(self):
        """
        Generate articles, save output in appropriate category or default output
        directory.
        """

        article_tmpl = self.jinja.get_template('article.html')
        for article in self.articles:
            with open(os.path.join(self.settings.output, article.url), 'w') as f:                
                f.write(article_tmpl.render(article=article))

    def generate(self):        
        self.load_articles()        
        self.order_articles()
        self.create_output_dir()        
        self.generate_index()        
        self.generate_articles()
        print ('Site successfully generated')


def create_project(location, src_path):
    """
    Create new blank site at location. Includes basic settings file, templates,
    and content directory.
    """

    if not os.path.exists(location):
        os.mkdir(location)
    
    defaults = settings_class.Settings({})
    
    if not os.path.exists(os.path.join(location, defaults.templates)):
        os.mkdir(os.path.join(location, defaults.templates))

    if not os.path.exists(os.path.join(location, defaults.content)):
        os.mkdir(os.path.join(location, defaults.content))    

    templates_path = os.path.join(os.path.dirname(__file__), SOURCE_URLS['templates'])
    templates_files = os.listdir(os.path.join(os.path.dirname(__file__), SOURCE_URLS['templates']))
    templates_destination_path = os.path.join(location, defaults.templates)

    for file_name in templates_files:
        if file_name.endswith(".html"):
            shutil.copy(os.path.join(templates_path, file_name), templates_destination_path)

    with open(os.path.join(location, 'settings.json'), 'w') as f:
        f.write(json.dumps(defaults.__dict__))

    print("Congratulation!")
    print("Project successfully created! :)")


def parse_args(arguments):
    src_path = os.path.dirname(__file__)

    if arguments['create_project']:
        if arguments['<project_name>']:
            create_project(arguments['<project_name>'], src_path)
            sys.exit(0)
        create_project('myblog', src_path)

    if arguments['make_site']:
        if arguments['<file_settings>']:
            config = open(arguments['<file_settings>'], 'r').read()
            os.chdir(os.path.dirname(arguments['<file_settings>']))
            settings = json.loads(config)
            generator = Generator(settings)
            generator.generate()
            sys.exit(0)
        config = open('settings.json', 'r').read()        
        settings = json.loads(config)        
        generator = Generator(settings)
        generator.generate()
    sys.exit(0)


def main():
    arguments = docopt(__doc__, version='SSGCFL {}'.format(__version__))
    parse_args(arguments)

if __name__ == '__main__':
    main()
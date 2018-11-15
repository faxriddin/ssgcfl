"""SSGCFL
Usage:
    ssgcfl create_project <name>
    ssgcfl make [<settings>]
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


SOURCE_URLS = {
    'templates':'templates',    
}


class Settings(object):
    def __init__(self, settings):
        self.templates = settings.get('templates', 'templates')        
        self.content = settings.get('content', 'content')
        self.output = settings.get('output', 'output')
        self.site_name = settings.get('site_name', 'My Blog')
        self.site_author = settings.get('site_author', 'Anonymous')


def create_project(location, src_path):
    """
    Create new blank site at location. Includes basic settings file, templates,
    and content directory.
    """
    if not os.path.exists(location):
        os.mkdir(location)
    
    defaults = Settings({})
    
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

    return True


def parse_args():
    """
    Parsing arguments and define commands
    """
    arguments = docopt(__doc__, version='SSGCFL {}'.format(__version__))
    src_path = os.path.dirname(__file__)

    if arguments['create_project']:
        if arguments['<name>']:
            if create_project(arguments['<name>'], src_path):
                print("Congratulation!")
                print("Project successfully created! :)")
            else:
                print("Fail on project creating! :(")
            sys.exit(0)
        create_project('myblog', src_path)


def main():
    parse_args()


if __name__ == '__main__':
    main()


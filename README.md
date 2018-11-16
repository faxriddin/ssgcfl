SSGCFL
======

SSGCFL (Static Site Generator Created For Learning) is a static site generator that can generate html files from markdown and template files.


Features
--------

* Single file
* Jinja2 templating language
* Articles support markdown formatting.

Install
-------

1. [Download](https://github.com/faxriddin/ssgcfl/tarball/master) source code from master branch
2. Extract downloaded archive file 
3. From command line go to `{extracted_dir_name}/ssgcfl`. In this folder you can see `generator.py` file.
4. Enter follow command:

    `python setup.py install`

Usage
-----
  
5. For create project (site structure) you should enter follow command:
    
    ``ssgcfl create_project project_path``
    - project_path - is path, where you want to create site folder
6. After successfully command your directory (project_path) should contain follow structure of folders and files
    - \[project_path\]
    
        - templates
            
            `article.html`
            
            `base.html`
            
            `home_page.html`
        - content
        
        `settings.json`
7. Now you can start make articles on the "content" directory. For this you should create "markdown" file with extension .md and enter the data of article by follow rule.
    Example:
    
    File: `article1.md`
    
    \---
    
    title: Article title
    
    date: 2018-11-14 10:12
    
    tags: article_tag1, article_tag2
    
    \---    
    
    Content of the article.  
8. After, you can begin to make site with command make_site in the project folder:
    
    ``ssgcfl make_site``
9. To run your site you can use integrated http-server of python:
    
    ``python -m http.server 8000 --bind 127.0.0.1``
    
    then on browser open the url <http://127.0.0.1:8000> 

Help
----
10.    ssgcfl [options] (-h|--help|--version)
    
    -h, --help       Show this message.
    --version        Show version.


Contributing
------------

If something is wrong or could be improved, let me know or submit a pull request.


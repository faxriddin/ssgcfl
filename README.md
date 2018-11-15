SSGCFL
======

SSGCFL is a static site generator that can generate html files from markdown and template files.


Features
--------

* Single file
* Jinja2 templating language
* Articles support markdown formatting.

Install
-------

`python setup.py install`

Usage
-----
1. [Download](https://github.com/faxriddin/ssgcfl/tarball/master) source code from master branch
2. Extract downloaded archive file 
3. From command line go to `{extracted_path}/ssgcfl`. In this folder you can see ssgcfl.py file.  
4. For create project (site structure) you should enter follow command:
    ``ssgcfl create_project project_path``
    - project_path - is path, where you want to create site folder
5. After successfully command your directory (project_path) should contain follow structure of folders and files
    - \[project_path\]
    
        - templates
            
            `article.html`
            
            `base.html`
            
            `home_page.html`
        - content
        
        `settings.json`
6. Now you can start make articles on the "content" directory. For this you should create "markdown" file with extension .md and enter the data of article by follow rule.
    Example:
    
    File: `article1.md`
    ```
    Title: Article title
    Meta: Article meta data.
    Date: 2018-11-14 10:12
    Tags: article_tag1, article_tag2

    Content of the article.  
    ```


Help
----
    ssgcfl [options] (-h|--help|--version)
    
    -h, --help       Show this message.
    --version        Show version.


Contributing
------------

If something is wrong or could be improved, let me know or submit a pull request.


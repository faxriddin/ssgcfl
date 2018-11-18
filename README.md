SSG
======  
SSG (Static Site Generator) is a static site generator that can generate html files from markdown and template files.


Features
--------  
* Single file
* Jinja2 templating language
* Articles support markdown formatting.

Installation
-------  
1. [Download](https://github.com/faxriddin/ssgcfl/tarball/master) source code from master branch
2. Extract downloaded archive file 
3. From command line go to `{extracted_dir_name}/ssgcfl`. In this folder you can see `generator.py` file.
4. Enter follow command:

    `python setup.py install`

Usage
-----  
1. For create project (site structure) you should enter follow command:
    
    ``ssgcfl create_project project_path``
    - project_path - is a path, where you want to create site folder
2. After successfully command your directory (project_path) should contain follow structure of folders and files
    - \[project_path\]
    
        - templates
            
            `article.html`
            
            `base.html`
            
            `home_page.html`
        - content
        
        `settings.json`
3. Now you can start make articles on the "content" directory. For this you should create "markdown" file with extension .md and enter the data of article by follow rule.
    Example:      
    File: `article1.md`  
    \---      
    title: Article title  
    date: 2018-11-14 10:12      
    tags: article_tag1, article_tag2      
    \---    
    
    Content of the article.  
4. After, you can begin to make site with command make_site in the project folder:
    
    ``ssgcfl make_site``
5. To run your site you can use integrated http-server of python:
    
    ``python -m http.server 8000 --bind 127.0.0.1``
    
    then on browser open the url <http://127.0.0.1:8000> 

Help
----  
    ssgcfl [options] (-h|--help|--version)
    
    -h, --help       Show this message.
    --version        Show version.


Contributing
------------  
If something is wrong or could be improved, let me know or submit a pull request.


Thank you very much 
-------------------  
While studying and creating the SSGSFL package, following codes was used for understanding SSG architecture. 
For this, I am grateful to these developers that developed it: 
- [Bark](https://github.com/Battleroid/bark) 
- [Pelican](https://github.com/getpelican/pelican)


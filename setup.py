from setuptools import setup, find_packages

setup(
        setup_requires=[],
        
        name='ssgcfl',
        version='0.0.1',
        url='https://github.com/faxriddin/ssgcfl',
        description='Static site generator created for learning.',
        license='MIT License',
        keywords='ssgcfl static site generator jinja blog python markdown',
        author='Fakhriddin Baltayev',
        author_email='faxriddinjon@gmail.com',
        download_url='https://github.com/faxriddin/ssgcfl/tarball/master',
        packages = find_packages(),
        install_requires=[            
            'docopt>=0.6.2',
            'jinja2>=2.10',
            'frontmatter>=0.4.4',
            'markdown2>=2.3.6',
            'python-dateutil>=2.7.5',
            'python-slugify>=0.0.1',
            ],
        entry_points={
            'console_scripts': ['ssgcfl = ssgcfl.generator:main']
            },
        platforms=['any'],
        classifiers=[
            'Programming Language :: Python',
            'Topic :: Internet',
            'Topic :: Internet :: WWW/HTTP :: Site Management',
            'Topic :: Text Processing',
            'Topic :: Text Processing :: Markup',
            'Topic :: Text Processing :: Markup :: HTML'
            ],
        include_package_data=True,
        data_files=[
            ('templates',['ssgcfl/templates/base.html','ssgcfl/templates/index.html','ssgcfl/templates/article.html'])
        ]
        )

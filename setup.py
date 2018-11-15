from setuptools import setup, find_packages

setup(
        setup_requires=[],
        include_package_data=True,
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
            'docopt>=0.6.2'
            ],
        entry_points={
            'console_scripts': ['ssgcfl = ssgcfl.ssgcfl:main']
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
        )

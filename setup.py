try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

config = {
    'description' : 'SumoPy',
    'author' : 'Hansoo Chang and Reiyuan Chiu',
    'url' : 'https://github.com/Penn-ABSKids/SumoPY',
    'download_url' : 'https://github.com/Penn-ABSKids/SumoPY/archive/master.zip',
    'author_email' : 'hansooc@sas.upenn.edu or chiurei@sas.upenn.edu',
    'version' : '0.1',
    'install_requires' : ['anaconda', 'nose'],
    'packages' : ['SumoPy'],
    'scripts' : [],
    'name' : 'SumoPy'
}

setup(**config)
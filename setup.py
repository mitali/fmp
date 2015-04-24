try:
	from setuptools import setup
except ImportError:
	from distutils.core import setup

config = {
	'description': 'Film Audio Program',
	'author': "Mitali Dargani',
	'url': 'dummy.com/fmp',
	'download_url': 'download.com/dummy/fmp',
	'author_email': 'mitalidargani@gmail.com',
	'version': '0.1',
	'install_requires': ['python 2.7.6', 'opencv'],
	'packages': ['NAME'],
	'scripts': [],
	'name': 'fmp'
}

setup(**config)

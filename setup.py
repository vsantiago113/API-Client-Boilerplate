"""
This setup.py file requires "git" because it uses "git" to find the latest tag for the project
the repo name and url.
"""

import subprocess
import os
from setuptools import setup

# Find Latest Git Tag Available
LATEST_GIT_TAG_AVAILABLE = subprocess.check_output(['git',
                                                    'describe',
                                                    '--tags']).decode('utf-8').strip()
assert '.' in LATEST_GIT_TAG_AVAILABLE

GET_ORIGIN_URL = subprocess.check_output(['git',
                                          'config',
                                          '--get',
                                          'remote.origin.url']).decode('utf-8').strip()
assert 'http' in GET_ORIGIN_URL
get_repo_name = GET_ORIGIN_URL.split('/', maxsplit=1)[-1].rstrip('.git')

assert os.path.isfile('requirements.txt')
with open('requirements.txt', 'r') as f:
    requirements = []
    for i in f.readlines():
        if i:
            requirements.append(i.rstrip())

with open('README.md', 'r', encoding='utf-8') as f:
    long_description = f.read()

setup(
    name=get_repo_name,
    packages=[get_repo_name],
    version=LATEST_GIT_TAG_AVAILABLE,
    license='MIT',
    description='A boilerplate to build API clients or wrappers.',
    long_description=long_description,
    long_description_content_type='text/markdown',
    author='Victor M Santiago',
    author_email='vsantiago113sec@gmail.com',
    url=GET_ORIGIN_URL.rstrip('.git'),
    download_url='{}/archive/{}.tar.gz'.format(GET_ORIGIN_URL.rstrip('.git'),
                                               LATEST_GIT_TAG_AVAILABLE),
    keywords=['RESTful', 'Client', 'API', 'Boilerplate'],
    python_requires='>=3.6.0',
    install_requires=requirements,
    classifiers=[  # https://pypi.org/classifiers/
        'Development Status :: 5 - Production/Stable',
        'Topic :: Internet :: WWW/HTTP',
        'License :: OSI Approved :: MIT License',
        'Intended Audience :: Developers',
        'Intended Audience :: Information Technology',
        'Intended Audience :: System Administrators',
        'Operating System :: MacOS :: MacOS X',
        'Operating System :: Microsoft :: Windows',
        'Operating System :: POSIX :: Linux',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
    ],
)

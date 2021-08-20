from setuptools import setup
import subprocess
import os

# Find Latest Git Tag Available
latest_git_tag_available = subprocess.check_output(['git', 'describe', '--tags']).decode('utf-8').strip()
assert '.' in latest_git_tag_available

get_origin_url = subprocess.check_output(['git', 'config', '--get', 'remote.origin.url']).decode('utf-8').strip()
assert 'http' in get_origin_url
get_repo_name = get_origin_url.split('/')[-1].rstrip('.git')

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
    version=latest_git_tag_available,
    license='MIT',
    description='A boilerplate to build API clients or wrappers.',
    long_description=long_description,
    long_description_content_type='text/markdown',
    author='Victor M Santiago',
    author_email='vsantiago113sec@gmail.com',
    url=get_origin_url.rstrip('.git'),
    download_url='{}/archive/{}.tar.gz'.format(get_origin_url.rstrip('.git'), latest_git_tag_available),
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

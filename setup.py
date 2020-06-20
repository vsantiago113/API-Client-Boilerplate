from setuptools import setup

with open('README.md', 'r', encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='API-Client-Boilerplate',
    packages=['API-Client-Boilerplate'],
    version='0.0.1',
    license='MIT',
    description='An API Client Boilerplate to build API Client that use RESTful in a standard way.',
    long_description=long_description,
    long_description_content_type='text/markdown',
    author='Victor M Santiago',
    author_email='vsantiago113sec@gmail.com',
    url='https://github.com/vsantiago113/API-Client-Boilerplate',
    download_url='',
    keywords=['RESTful', 'Client', 'API', 'Boilerplate'],
    python_requires='>=3.4.0',
    install_requires=[
        'requests',
        'urllib3',
    ],
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Topic :: Utilities',
        'License :: OSI Approved :: MIT License',
        'Operating System :: MacOS :: MacOS X',
        'Operating System :: Microsoft :: Windows',
        'Operating System :: POSIX :: Linux',
        'Programming Language :: Python',
        'Intended Audience :: Developers',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
    ],
)

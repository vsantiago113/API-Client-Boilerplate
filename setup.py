from distutils.core import setup

setup(
    name='API-Wrapper-Boilerplate',
    packages=['API-Wrapper-Boilerplate'],
    version='0.0.1',
    license='MIT',
    description='An API Wrapper Boilerplate to build API Wrappers that use RESTful in a standard way.',
    author='Victor M Santiago',
    author_email='vsantiago113sec@gmail.com',
    url='https://github.com/vsantiago113',
    download_url='https://github.com/vsantiago113/API-Wrapper-Boilerplate',
    keywords=['RESTful', 'Wrapper', 'API', 'Boilerplate'],
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

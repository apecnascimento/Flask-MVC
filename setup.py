"""
Flask-MVC
-------------

A friend to build flask application on mvc architecture pattern.
"""
from setuptools import setup


setup(
    name='flask-mvc',
    version='0.1',
    url='https://github.com/apecnascimento/flask-mvc',
    license='MIT',
    author='apecnascimento',
    author_email='apecnascimento@gmail.com',
    description='A friend to build flask application on mvc architecture pattern.',
    long_description=__doc__,
    py_modules=['flask_mvc'],
    # if you would be using a package instead use packages instead
    # of py_modules:
    # packages=['flask_mvc'],
    zip_safe=False,
    include_package_data=True,
    platforms='any',
    install_requires=[
        'Flask'
    ],
    classifiers=[
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
        'Topic :: Software Development :: Libraries :: Python Modules'
    ]
)
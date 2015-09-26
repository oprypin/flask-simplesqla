from distutils.core import setup

setup(
    name='Flask-SimpleSQLA',
    version='0.1-dev',
    url='http://github.com/blaxpirit/flask-simplesqla',
    license='BSD',
    author="Oleh Prypin",
    description="Extension providing basic support of SQLAlchemy in Flask applications",
    long_description=__doc__,
    packages=['flask_simplesqla'],
    platforms='any',
    install_requires=[
        'Flask>=0.8',
        'SQLAlchemy',
    ],
    classifiers=[
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ],
)

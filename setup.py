from setuptools import setup

setup(
    name = 'PyXiaomiGateway',
    packages = ['PyXiaomiGateway'],
    install_requires=['pycryptodome==3.4.5'],
    version = '0.3.2',
    description = 'a library to communicate with the Xiaomi Gateway',
    author='Daniel Høyer Iversen',

    url='https://github.com/Danielhiversen/PyXiaomiGateway/',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Environment :: Other Environment',
        'Intended Audience :: Developers',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Home Automation',
        'Topic :: Software Development :: Libraries :: Python Modules'
        ]
)

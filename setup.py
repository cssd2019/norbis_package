#setup.py
from setuptools import setup

setup(name='fizzbuzz',
      version='1.0.0',
      description='a fizzbuzz generator',
      author='C Monkey',
      author_email='c.monkey@banalab.uk',
      license='MIT',
      packages=['fizzbuzz'],
      classifiers=['Development Status :: 1.0.0',
                   'License :: MIT License',
                   'Programming Language :: Python :: 3.4'  ],      
      scripts=['bin/FizzBuzz.py',
           ],
#      install_requires=[
#          'typing',
#          'prettytable',
#          'munch'
#      ],
     )

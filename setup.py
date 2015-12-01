from setuptools import setup

setup (name = 'Project Euler',
       version      = '1.0',
       description  = 'My solutions to the Projecy Euler problem-set',
       author       = 'Michael Overy',
       author_email = 'mike.overy13@gmail.com',
       url          = 'http://www.github.com/movery/Project-Euler',
       packages     = ['src'],
       entry_points = {'console_scripts' : ['pe = src:main',]}
       )

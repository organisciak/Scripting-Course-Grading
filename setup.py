from setuptools import setup

setup(
   name='scripting_grading',
   version='1.0',
   description='Grading for my scripting class',
   author='Peter Organisciak',
   author_email='organisciak@gmail.com',
   packages=['scripting_grading'],
   install_requires=['IPython', 'nbformat'],
)
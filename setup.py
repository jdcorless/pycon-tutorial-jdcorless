from setuptools import setup

setup(name='pycon-tutorial-jdcorless',
      version='1.0',
      description='test stuff for pycon tutorial',
      py_modules=['wordcount_lib'],
      scripts=['wordcount'],
      setup_requires=[
          'pytest-runner',
      ],
      tests_require=[
          'pytest',
      ],
)

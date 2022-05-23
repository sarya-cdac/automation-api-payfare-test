from setuptools import setup, find_packages

setup(name='payfareapitest',
      version='1.0',
      description="Practice API testing",
      author='Shivani Arya',
      author_email='shivani.arya@testingxperts.com',
      url='',
      packages=find_packages(),
      zip_safe=False,
      install_requires=[

          "pytest-html==2.1.1",
          "requests-oauthlib==1.3.0",
          "allure-pytest"

      ]
      )

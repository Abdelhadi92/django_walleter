import os

from setuptools import setup, find_packages

version = '0.1'

base_dir = os.path.dirname(__file__)


setup(
      name='django_wallet',
      version=version,
      description='Django wallet',
      long_description=open(os.path.join(base_dir, "README.md")).read(),
      url='https://github.com/Abdelhadi92/django_wallet',
      classifiers=[
          'Environment :: Web Environment',
          'Framework :: Django',
          'License :: OSI Approved :: BSD License',
          'Operating System :: OS Independent',
          'Development Status :: 5 - Production/Stable',
          'Programming Language :: Python',
          'Programming Language :: Python :: 3',
          'Programming Language :: Python :: 3.4',
          'Programming Language :: Python :: 3.5',
          'Programming Language :: Python :: 3.6',
          'Programming Language :: Python :: 3.7',
      ],
      keywords='Django wallet',
      author='Abdelhadi Abu-Shamleh',
      author_email='abushamleh92@gmail.com',
      license='BSD',
      packages=find_packages(exclude=['ez_setup']),
      include_package_data=True,
      zip_safe=False,
      dependency_links=[],
      install_requires=[
          'setuptools',
          'jsonfield',
      ]
)

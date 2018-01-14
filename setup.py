import os

from setuptools import find_packages, setup
from pip.download import PipSession
from pip.req import parse_requirements

my_path = os.path.abspath(os.path.dirname(__file__))
# Get standard Requirements
requirements_path = os.path.join(my_path, 'requirements.txt')
install_requires = parse_requirements(requirements_path, session=PipSession())
install_requires = [str(ir.req) for ir in install_requires]

setup(name='ldapadmin',
      version='0.0.1',
      description='An API based backend for an ldap admin interface.',
      license='MIT',
      packages=find_packages(where='src'),
      package_dir={'': 'src'},
      namespace_packages=['ldapadmin'],
      install_requires=install_requires,
)

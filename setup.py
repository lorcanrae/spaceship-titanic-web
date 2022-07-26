from setuptools import find_packages
from setuptools import setup

with open('requirements.txt') as f:
    content = f.readlines()
requirements = [x.strip() for x in content if 'git+' not in x]

setup(name='spaceship-titanic-web',
      version="1.0",
      description="spaceship-titanic_streamlit_app",
      packages=find_packages(),
      install_requires=requirements,
      include_package_data=True)

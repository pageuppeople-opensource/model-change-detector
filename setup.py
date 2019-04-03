from setuptools import setup, find_packages

setup(name='dpo',
      version='0.1.0',
      packages=find_packages(),
      install_requires=[
          'psycopg2-binary==2.7.7',
          'SQLAlchemy==1.2.17',
          'alembic==1.0.8'
      ]
      )

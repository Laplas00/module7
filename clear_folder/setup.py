from setuptools import setup, find_namespace_packages

setup(name='clean_folder',
      version='1',
      description='Very useful code',
      url='https://github.com/Laplas00/module7/tree/main/clear_folder',
      author='Bogdan Gaidarzhy',
      author_email='flyingcircus@example.com',
      license='MIT',
      packages=find_namespace_packages(),
      entry_points={'console_scripts': ['clean-folder = clean_folder.sorting:main']})

from setuptools import setup, find_packages

long_description = 'View your directory structure - read the docs at https://www.github.com/nayakrujul/tree'

setup(
  name = 'tree-directory',
  version = '0.1',
  license='Apache',
  description = 'View your directory structure',
  author = 'Rujul Nayak',
  author_email = 'rujulnayak@outlook.com',
  url = 'https://github.com/nayakrujul/tree',
  download_url = 'https://github.com/nayakrujul/tree/archive/refs/tags/v_01.tar.gz',
  keywords = ['directory', 'structure'],
  install_requires=[
      ],
  classifiers=[
    'Development Status :: 3 - Alpha', 
    'Intended Audience :: Developers',
    'Topic :: Software Development :: Build Tools',
    'License :: OSI Approved :: MIT License',
    'Programming Language :: Python :: 3',
    'Programming Language :: Python :: 3.4',
    'Programming Language :: Python :: 3.5',
    'Programming Language :: Python :: 3.6',
    'Programming Language :: Python :: 3.7',
    'Programming Language :: Python :: 3.8',
    'Programming Language :: Python :: 3.9',
  ],
  long_description=long_description,
  long_description_content_type='text/x-rst',
  packages = find_packages(),
  entry_points = {
    'console_scripts': [
      'tree = tree.tree:tree_no_sorting',
      'tree2 = tree.tree:tree_sort_by_filename',
      'tree3 = tree.tree:tree_sort_by_extension'
    ]
  }
)

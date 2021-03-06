from distutils.core import setup
setup(
  name = 'pyCall',         
  packages = ['pyCall'],   
  version = '0.1',      
  license='MIT',        
  description = 'This librabry help to call functions and classes from other languages',   
  author = 'Jeffrey Kilelo', 
  author_email = '',      
  url = 'https://github.com/jkilelo/pyCall.git',   
  download_url = 'https://github.com/jkilelo/pyCall/archive/refs/heads/main.zip',    
  keywords = ['call java classes from python', 'call other languages from python', ],   
  install_requires=[],
  classifiers=[
    'Development Status :: 3 - Alpha',      
    'Intended Audience :: Developers',      
    'Topic :: Software Development :: Build Tools',
    'License :: OSI Approved :: MIT License',   
    'Programming Language :: Python :: 3', 
    'Programming Language :: Python :: 3.8',
    'Programming Language :: Python :: 3.9',
    'Programming Language :: Python :: 3.10',
  ],
)
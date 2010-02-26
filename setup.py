from distutils.core import setup
import pastebin

setup (
        name = 'PasteBin',
        version = pastebin.__version__,
        description= 'Simple pastebin.com API wrapper module.',
        author = '10n1z3d',
        author_email = '10n1z3d@w.cn',
        license = 'GPLv3',
        py_modules=['pastebin']
      )

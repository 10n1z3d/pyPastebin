#!/usr/bin/env python
#
# Simple pastebin.com API wrapper module.
#
# Copyright (C) 2010 10n1z3d <10n1z3d[at]w[dot]cn>
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.


import re
from urllib import quote
from urllib2 import urlopen

__version__ = '0.1'

class PasteError(Exception):
    '''Raised when the pastebin API retuns an error.'''
    def __init__(self, paste_error):
        self.paste_error = paste_error
        
    def __str__(self):
        return '<{0}>'.format(self.paste_error)

class PasteBin():
    def __init__(self):
        self._API_URL = 'http://pastebin.com/api_public.php'
        self._PARAMS = {}
        
    def __build_post_data(self):
        return '&'.join('{0}={1}'.format(k, v) for (k, v) in self._PARAMS.iteritems() if v)
                      
    def paste(self, paste_code, paste_name=None, paste_subdomain=None, 
              paste_private=False, paste_expire_date=None, paste_format='text', 
              timeout=10):
                  
        self._PARAMS['paste_code'] = quote(paste_code)
        self._PARAMS['paste_name'] = paste_name
        self._PARAMS['paste_subdomain'] = paste_subdomain
        self._PARAMS['paste_private'] = int(paste_private)
        self._PARAMS['paste_expire_date'] = paste_expire_date
        self._PARAMS['paste_format'] = paste_format
        
        post_data = self.__build_post_data()
        paste_url = urlopen(self._API_URL, post_data, timeout).read()
        
        if re.match('ERROR\:\s(.*)', paste_url): 
            raise PasteError(paste_url)
        
        return paste_url

def paste(paste_code, paste_name=None, paste_subdomain=None, 
          paste_private=False, paste_expire_date=None, paste_format='text', 
          timeout=10):
              
    pastebin = PasteBin()
    paste_url = pastebin.paste(paste_code, paste_name, paste_subdomain, 
                paste_private, paste_expire_date, paste_format, timeout)
                
    return paste_url
    
    
if __name__ == "__main__":
    # paste some python code
    source_code = """class PasteError(Exception):
    def __init__(self, paste_error):
        self.paste_error = paste_error
        
    def __str__(self):
        return '<{0}>'.format(self.paste_error)"""
    
    print paste(source_code, paste_format='python')
    
    # this will raise PasteError
    print paste('')

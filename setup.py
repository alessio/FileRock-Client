#!/usr/bin/python
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with FileRock Client. If not, see <http://www.gnu.org/licenses/>.
#

import os
import fnmatch
from glob import glob
from distutils.core import setup
from DistUtilsExtra.command.build_i18n import build_i18n
from DistUtilsExtra.command.clean_i18n import clean_i18n

APPNAME = 'filerock-client'

class clean_extra(clean_i18n):
    def run(self):
        clean_i18n.run(self)

        for path, dirs, files in os.walk('.'):
            for f in files:
                f = os.path.join(path, f)
                if f.endswith('.pyc'):
                    self.spawn(['rm', f])
            for d in dirs:
                if d == '__pycache__':
                    self.spawn(['rm', '-r', os.path.join(path,d)])

def opj(*args):
    path = os.path.join(*args)
    return os.path.normpath(path)

def get_subpackages(*packages):
    subpkgs_list = []
    for pkg in packages:
        for path, dirs, files in os.walk(pkg):
            if '__init__.py' in files:
                subpkgs_list.append(path.replace('/', '.'))
    return subpkgs_list

def get_data_files(srcdir, *wildcards, **kw):
    def walk_helper(arg, dirname, files):
        if '.git' in dirname:
            return
        names = []
        lst, wildcards = arg
        for wc in wildcards:
            wc_name = opj(dirname, wc)
            for f in files:
                filename = opj(dirname, f)

                if fnmatch.fnmatch(filename, wc_name) and not os.path.isdir(filename):
                    names.append(filename)
        if names:
            lst.append( (dirname, names ) )

    file_list = []
    recursive = kw.get('recursive', True)
    if recursive:
        os.path.walk(srcdir, walk_helper, (file_list, wildcards))
    else:
        walk_helper((file_list, wildcards),
                    srcdir,
                    [os.path.basename(f) for f in glob.glob(opj(srcdir, '*'))])
    return file_list

data_files = get_data_files('data/', '*')
packages = get_subpackages('filerockclient', 'FileRockSharedLibraries')

setup(
    name = APPNAME,
    description = 'FileRock Secure Cloud Storage',
    version = '0.4.0',
    author = "Heyware s.r.l.",
    author_email = "developers@filerock.com",
    url = 'https://www.filerock.com/',
    license = 'GPL-3',
    scripts = ['FileRock.py'],
    packages = packages,
    data_files = data_files,
    cmdclass = {
        'clean' : clean_extra,
        'build_i18n' :  build_i18n}
)

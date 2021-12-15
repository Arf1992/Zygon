import os
import subprocess as sp
import sys
from typing import Union


# find is expensive so see if it's been added to path first
def search(pathvariable: str) -> Union[str, int]:

    pathcode = {'win32': 'echo %PATH%', 'linux': 'echo $Path', 'darwin': 'echo $Path'}
    # need to research CLI commands for all possible sys.platform values and add to pathcode
    output = sp.getoutput(pathcode[sys.platform])
    position = output.find(pathvariable)
    if position == -1:
        return position
    pathbeginindex = output[:position].rfind(';')+1
    pathendindex = output.find(';', position)
    pathtoznn = output[pathbeginindex:pathendindex]
    return pathtoznn


# Find searches C for Windows and root for Mac/Linux
def find(name: str, path: str) -> Union[int, str]:
    for root, dirs, files in os.walk(path):
        if name in files:
            return os.path.join(root + os.path.sep)


def findznn():
    pathtoznn = search('Zenon')
    if pathtoznn == -1:
        if sys.platform == 'win32':
            pathtoznn = find('znn-cli.exe', 'C:\\')
        elif sys.platform in ('linux', 'darwin'):
            pathtoznn = find('znn-cli.exe', '\\')
    if not pathtoznn:
        return False
    else:
        return pathtoznn


if __name__ == '__main__':
    print(search('Zenon'))
    print(find('znn-cli.exe', 'C:\\Users\\'))

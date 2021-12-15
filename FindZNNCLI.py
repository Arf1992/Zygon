import os
import subprocess as sp
import sys
from typing import Union

#find is expensive so see if it's been added to path first
#need to research CLI commands for all possible sys.platform values and add to pathcode
def search(pathVariable: str) -> int:
    pathcode = {'win32': 'echo %PATH%', 'linux': 'echo $Path', 'darwin': 'echo $Path'}
    output = sp.getoutput(pathcode[sys.platform])
    position = output.find(pathVariable)
    if position == -1:
        return position
    pathBeginIndex = output[:position].rfind(';')+1
    pathEndIndex = output.find(';', position)
    pathToZNN = output[pathBeginIndex:pathEndIndex]
    return pathToZNN

#Find searches C for Windows and root for Mac/Linux
def find(name: str, path: str) -> Union[int, str]:
    for root, dirs, files in os.walk(path):
        if name in files:
            return os.path.join(root + os.path.sep)


def findZNN():
    pathtoZNN = search('Zenon')
    if pathtoZNN == -1:
        if sys.platform == 'win32':
            pathtoZNN = find('znn-cli.exe', 'C:\\')
        elif sys.platform in ('linux', 'darwin'):
            pathtoZNN = find('znn-cli.exe', '\\')
    if not pathtoZNN:
        return False
    else:
        return pathtoZNN

if __name__ == '__main__':
    print(search('Zenon'))
    print(find('znn-cli.exe', 'C:\\Users\\'))
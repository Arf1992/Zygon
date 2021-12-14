import os
import subprocess as sp
import sys
from typing import Union


def search(pathVariable: str) -> int:
    platform = sys.platform
    if platform == 'win32':
        command = 'echo %PATH%'
    elif platform in ('linux', 'darwin'):
        command = 'echo $Path'
    else:
        return -1
    position = sp.getoutput(command).find(pathVariable)
    return position


def find(name: str, path: str) -> Union[int, str]:
    for root, dirs, files in os.walk(path):
        if name in files:
            return os.path.join(root, name)


def findZNN():
    pathindex = search('Zenon')
    if pathindex == -1:
        if sys.platform == 'win32':
            pathindex = find('znn-cli.exe', 'C:\\')
        elif sys.platform in ('linux', 'darwin'):
            pathindex = find('znn-cli.exe', '\\')
    if pathindex in [-1, None]:
        return False
    else:
        return pathindex.replace('.exe', '')

if __name__ == '__main__':
    print(find('znn-cli.exe', 'C:\\Users\\'))
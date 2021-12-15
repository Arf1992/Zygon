import subprocess as sp
import os
import FindZNNCLI


def version():
    pathznn = FindZNNCLI.findznn()
    pathznn = pathznn.replace(os.path.sep, os.path.sep * 2)
    clireturn = sp.getoutput(pathznn + 'znn-cli version')
    return clireturn


if __name__ == '__main__':
    print(version())

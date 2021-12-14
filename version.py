import subprocess as sp
import FindZNNCLI


def versionZNN():
    pathZNN = FindZNNCLI.findZNN()
    pathZNN = pathZNN.replace('\\', '\\\\')
    cliReturn = sp.getoutput(pathZNN + ' version')
    return(cliReturn)

if __name__ == '__main__':
    print(versionZNN())
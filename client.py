import sys, getopt, random
from sys import argv
from SOAPpy import WSDL

def getGoogleAPIKey(wsdlFile):
    # Get Google API key from local secret file
    # This is needed by all calls to Google
    api_key = ""
    with open("api_key.txt", 'r') as secret:
        api_key = secret.readline().strip()
    return api_key

def getAvailableMethods(server):
    return server.methods.keys()

def printAvailableMethods(availableMethods):
    print "These are all the methods available: "
    for method in availableMethods:
        print " * " + method

def getRandomMethod(availableMethods):
    r = random.randint(0, len(availableMethods) - 1)
    return availableMethods[r]

def printRandomMethodsArgs(availableMethods):
    randomMethod = getRandomMethod(availableMethods)
    callInfo = server.methods[randomMethod]
    print "These are all the input args needed by " + randomMethod + ": "
    for arg in callInfo.inparams:
        print " * " + arg.name.ljust(15), arg.type

if __name__ == "__main__":
    # Read path to WSDL file from input argument
    wsdlFile = sys.argv[1]
    print "Input WSDL file is: " + wsdlFile

    # Start a Proxy and point to the path to WSDL file
    # Could be a URL as well as local path
    server = WSDL.Proxy(wsdlFile)

    # Get some info from available funtionality
    availableMethods = getAvailableMethods(server)
    printAvailableMethods(availableMethods)
    printRandomMethodsArgs(availableMethods)

from SOAPpy import WSDL

#Get Google API key from local secret file
api_key = ""
with open("api_key.txt", 'r') as secret:
    api_key = secret.readline().strip()

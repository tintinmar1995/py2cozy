import os
import json

if 'COZY_URL' in os.environ :
    URL = os.environ['COZY_URL']
else :
    URL = input('Please enter the address of your Cozy')
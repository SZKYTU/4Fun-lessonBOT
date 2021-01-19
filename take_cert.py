import json
from vulcan import Vulcan


with open('cert.json') as f:
    certificate = json.load(f)

client = Vulcan(certificate)

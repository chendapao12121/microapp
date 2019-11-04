# from hashlib import md5
# from microapp.settings import SECRET_KEY
#
# pwd = md5('majiananbenbi'.encode('utf-8')+SECRET_KEY.encode('utf-8')).hexdigest()
# print(pwd)
# from microapp.wsgi import *
# from apps import models
#
#
# token = '7f67fb1d-2525-4894-937f-2ede8a8b2873'
#
# obj = models.Admin.objects.all()
# print(obj)
import os

# dir_path = os.path.dirname(os.path.abspath(__file__))
dir_path = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
print(dir_path)
os.path.abspath(__file__)
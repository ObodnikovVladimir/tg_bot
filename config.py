
from outline_api import OutlineVPN
from decouple import config

api_url = ('https://178.253.22.14:47465/jIs8shWObKVm28fYOe54nQ')
cert_sha256 = ('3875619D869080B2DC0E6F7125D46E14D05B9B5B69E05DA51F158212150C6126')

from decouple import config
from outline_api import OutlineVPN

api_url = config('API_URL')
cert_sha256 = config('CERT_SHA')
client = OutlineVPN(api_url=api_url, cert_sha256=cert_sha256)
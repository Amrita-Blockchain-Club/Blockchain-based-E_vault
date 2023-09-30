import requests
from extract_details import get_response
import re


url = '__API_ENDPOINT__'
public_key = 'PUBLIC_KEY'
filename = 'FILE_ADDRESS'

with open(filename, 'rb') as file:
    response = requests.post(url, data={'public_key': public_key}, files={'file': file})

if response.status_code == 200:
    get_response(response=response.text)

else:
    print('Error:', response.status_code)



def get_response(response):
    message = re.findall(r'<p>(.*)</p>', response)[0]

    # Extract status code
    status_code = re.findall(r'Status code: (\d+)', response)[0]

    # Extract CID
    cid = re.findall(r'CID: (\w+)', response)[0]

    print(f'Message: {message}')
    print(f'Status code: {status_code}')
    print(f'CID: {cid}')
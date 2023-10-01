import requests
import re


def get_response(response):
    message = re.findall(r'<p>(.*)</p>', response)[0]

    # Extract status code
    status_code = re.findall(r'Status code: (\d+)', response)[0]

    # Extract CID
    cid = re.findall(r'CID: (\w+)', response)[0]

    print(f'Message: {message}')
    print(f'Status code: {status_code}')
    print(f'CID: {cid}')


def main():
    url = 'http://localhost:5100'
    public_key = '__PUBLIC_KEY__'
    filename = '__FILENAME__'

    with open(filename, 'rb') as file:
        response = requests.post(url, data={'public_key': public_key}, files={'file': file})

    if response.status_code == 200:
        get_response(response=response.text)

    else:
        print('Error:', response.status_code)

if __name__ == '__main__':
    main()
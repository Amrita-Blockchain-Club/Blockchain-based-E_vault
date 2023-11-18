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

def to_server():
    url = 'http://localhost:5100'
    public_key = '__Public Key__'
    filename = '__File Name__'

    with open(filename, 'rb') as file:
        response = requests.post(url, data={'public_key': public_key}, files={'file': file})

    if response.status_code == 200:
        get_response(response=response.text)
    else:
        print('Error:', response.status_code)

def main():
    url = "http://localhost:5100/upload"
    CID = "QmYaMvMeJdzMSW3hAmxgxzGLvrw5EhomfdHYBep8AYpPVg"
    filename = "file.go"

    try:
        response = requests.post(url, data={'CID': CID, 'filename': filename})

        if response.status_code == 200:
            with open(filename, 'wb') as f:
                f.write(response.content)

            print(f"File downloaded successfully to {filename}")
        else:
            print(f"Failed to download file. Status code: {response.status_code}")
            print(response.text)     
            if response.status_code == 200:
                with open(filename, 'wb') as file:
                    file.write(response.content)
                    print(f"File {filename} downloaded successfully")
            else:
                print('Error:', response.status_code)
    except Exception as e:
        print(e)



if __name__ == '__main__':
    main()
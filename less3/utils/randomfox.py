import requests

def fox():
    url = "https://randomfox.ca/floof/"
    response = requests.get(url)
    data = response.json()
    return (data.get('image'))

if __name__ == '__main__':
    fox()
import requests


if __name__ == '__main__':
    my_data = {"Name": "Vasya", "phone": 123}
    headers = {
        'Accept': 'application/json',
        'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 '
                      'Safari/537.36'
    }
    r = requests.post("https://httpbin.org/post", headers=headers, params=my_data)
    print(r.json())

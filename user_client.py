import requests
import sys



def signup():
    url = 'http://127.0.0.1:8000/user/signup'

    data = {
    'username': 'costica',
    'password': 'ak471989Aionaw',
    'confirm_password': 'ak471989Aionaw',
    'is_married': True,
    'email': 'costica@gmail.com',
    'age':27
}


    res = requests.post(url=url,data=data)

    print(res.status_code)
    print(res.url)
    print(res.text)


def signin():
    url = 'http://127.0.0.1:8000/api/user/sign_in/'

    data = {
    'username': 'costica',
    'password': 'ak471989S'
}


    res = requests.post(url=url,data=data)

    print(res.status_code)
    print(res.url)
    print(res.text)


def list_cars():
    url = 'http://127.0.0.1:8000/api/car/list_create'  

    headers = {
    "Authorization": "Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNzMyNjQ1NDIwLCJpYXQiOjE3MzI2NDE4MjAsImp0aSI6IjZmOGQzNWMzODQ1MDQ5OGZiNzgyOGYzOTIwZTkwY2U4IiwidXNlcm5hbWUiOiJjb3N0aWNhIn0.XcpwT4WClgZ7CgMeOL-NpMddfDEqqTaWQ5CUaNAbLYY"
    }

    res = requests.get(url=url, headers=headers)

    print(f'Status Code: {res.status_code}')
    print(f'Response URL: {res.url}')
    print(f'Response Text: {res.text}')
 


if __name__ == "__main__":
    if sys.argv[1] == 'signup':
        signup()

    if sys.argv[1] == 'signin':
        signin()
    if sys.argv[1] == 'list_cars':
        list_cars()

    else:
        exit(0) 


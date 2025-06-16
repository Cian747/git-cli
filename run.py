import urllib.request,json


git_url = 'https://api.github.com/users/{}/events'


def get_user_activity():
    '''
    This function will control the date it gets from the api
    '''

    print("Hello there! Welcome to your own Github CLI")
    print('Put in your github username below:')
    gu_name = input()

    get_user_data = git_url.format(gu_name)

    with urllib.request.urlopen(get_user_data) as url:
        user_data = url.read()
        get_user_response = json.loads(user_data)

        results = []

        for item in get_user_response:
            print(item.get('id'))
            print(item.get('repo'))
            print(item.get('created_at'))




if __name__ == "__main__":
    manager = get_user_activity()
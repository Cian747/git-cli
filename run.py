import urllib.request,json


git_url = 'https://api.github.com/users/{}/events'


def get_user_activity(user):
    '''
    This function will control the date it gets from the api
    '''

    print("Hello there! Welcome oto your own Github CLI")

    get_user_data = git_url.format(user)

    with urllib.request.urlopen(get_user_data) as url:
        user_data = url.read()
        get_user_response = json.loads(user_data)

        results = []

        for item in get_user_response:
            print(id = item.get('id'))
            print(repo = item.get('repo'))
            print(created_at = item.get('created_at'))




if __name__ == "__main__":
    manager = get_user_activity()
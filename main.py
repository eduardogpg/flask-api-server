import requests

url = 'http://localhost:5000/todo/api/v1.0/tasks'

if __name__ == '__main__':
    # json = {'title' : 'Finish workshop', 'description' : 'Finish workshop'}
    # response = requests.post(url, json=json)
    # if response.status_code == 200:
    #     print(response.text)

    params = {'order': True}
    response = requests.get(url, auth=('eduardo', 'password123'), params=params)
    if response.status_code == 200:
        json_response = response.json()

        for task in json_response.get('tasks', []):
            print("> " + task.get('title'))

    print(response.text)
    # json = {'title' : 'Finish workshop yes', 'description' : 'Finish workshop yes', 'done': 'true'}
    # response = requests.put(url + '/1', json=json)
    # if response.status_code == 200:
    #     print(response.text)
    #
    # response = requests.delete(url + '/3')
    # print(response.text)

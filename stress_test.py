import random

from locust import HttpUser, task


class Web(HttpUser):
    headers = None

    @task
    def get_car_list(self):
        resp = self.client.get('/car/list/', headers=self.headers)

    @task
    def get_car_sold_list(self):
        resp = self.client.get('/car/sold_list/', headers=self.headers)
        data = resp.json()
        if len(data['data']) > 1:
            resp = self.client.post('/car/buy/', headers=self.headers, json={
                'name': data['data'][random.randint(0, len(data['data'])-1)]['name'],
                'count': random.randint(1, 5),
            })
        print(resp.status_code)

    def on_start(self):
        data = {
            'username': 'saeed{}'.format(random.randint(1, 1000)),
            'password': 'myPas{}'.format(random.randint(1, 1000)),
        }
        resp = self.client.post('/authnz/register/', json=data)
        self.headers = {'Authorization': 'JWT {}'.format(resp.json()['data']['token'])}


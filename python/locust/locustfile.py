# locust --host=http://example.com

import string
import random
from locust import HttpLocust, TaskSet, task
from faker import Faker

# https://github.com/locustio/locust/issues/92
# Fix to many file open error
import resource
resource.setrlimit(resource.RLIMIT_NOFILE, (999999, 999999))

faker = Faker()

def random_string(n=10, random_type=0, prefix=''):
    letters = string.ascii_letters + string.digits
    if random_type == 1:
        letters = string.digits
    elif random_type == 2:
        letters = string.ascii_lowercase + string.digits
    elif random_type == 3:
        letters = string.ascii_uppercase + string.digits

    result = prefix + ''.join(random.choice(letters) for _ in range(n))

    return result


class MyTaskSet(TaskSet):
    def on_start(self):
        dev_id = random_string(36, 3)
        msisdn = random_string(10, 1, '+')
        # msisdn = "+1025370907"
        response = self.client.post("/register",
                         headers={"Content-Type": "application/json"},
                         json={
                             "username": faker.user_name(),
                             "password": faker.password(),
                         })

        response = response.json()
        token = response['token']
        self.client.get("/users/me",
                         headers={"Content-Type": "application/json"},
                         json={
                             "token": token
                         })

    @task(1)
    def my_task(self):
        pass

class MyLocust(HttpLocust):
    task_set = MyTaskSet
    min_wait = 100
    max_wait = 500

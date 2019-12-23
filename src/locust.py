from locust import HttpLocust, TaskSet, task

class LoginWithUniqueUsersSteps(TaskSet):
    @task
    def login(self):
        self.client.post("/login", {
            'email': 'LocustPerformanceUser1@gmail.com', 'password': '123456'
        })

class LoginWithUniqueUsersTest(HttpLocust):
    task_set = LoginWithUniqueUsersSteps
    host = "http://blazedemo.com"
    sock = None

    def __init__(self):
        super(LoginWithUniqueUsersTest, self).__init__()
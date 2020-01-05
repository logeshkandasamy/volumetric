from locust import HttpLocust, TaskSet, task

class LoginWithUniqueUsersSteps(TaskSet):
    @task
    def login(self):
#         self.client.post("/api/demo/1", {
#             'email': 'LocustPerformanceUser1@gmail.com', 'password': '123456'
#         })
        self.client.get("/api/demo/1")

class LoginWithUniqueUsersTest(HttpLocust):
    task_set = LoginWithUniqueUsersSteps
    host = "http://localhost:8080"
    sock = None

    def __init__(self):
        super(LoginWithUniqueUsersTest, self).__init__()
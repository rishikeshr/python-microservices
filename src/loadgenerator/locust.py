import time
import names
from locust import HttpUser, task, between

class QuickstartUser(HttpUser):
    wait_time = between(1, 2)

    @task
    def index_page(self):
        self.client.get("/")

    @task(3)
    def get_page(self):
        self.client.get("/")


    @task(2)
    def add_item(self):
        self.client.post("/post", {
           'name': names.get_full_name(),
           'message': " Hi from " + names.get_full_name()
        })

    @task(2)
    def add_another_item(self):
        self.client.post("/post", {
           'name': names.get_first_name(),
           'message': " Hi from " + names.get_first_name()
        })

__author__ = 'vincent'

from locust import Locust, TaskSet

def login(l):
    print 'on_start ----------------------------'
    l.client.post("/j_spring_security_check", {"username":"admin", "password":"admin"})



def index(l):
    l.client.get("/")

def profile(l):
    l.client.get("/druid")

class UserBehavior(TaskSet):
    tasks = {profile:2}

    def on_start(self):
        login(self)

class WebsiteUser(Locust):
    task_set = UserBehavior
    min_wait=5000
    max_wait=9000
    host="http://www.firsthuida.com:5001/fhdys"

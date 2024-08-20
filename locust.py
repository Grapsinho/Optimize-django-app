from locust import HttpUser, TaskSet, task, between
import random

class UserBehavior(TaskSet):
    search_terms = ["Tom Sawyer", "The Mill on the Floss", "harry", "Oliver Twist", "Moby Dick", "Pride and Prejudice"]

    @task(1)
    def load_homepage(self):
        query = random.choice(self.search_terms)
        self.client.get(f"/books/search/?q={query}")

    @task(2)
    def load_blog_posts(self):
        query = random.choice(self.search_terms)
        self.client.get(f"/books/search/?q={query}")

    @task(1)
    def load_post_details(self):
        query = random.choice(self.search_terms)
        self.client.get(f"/books/search/?q={query}")

class WebsiteUser(HttpUser):
    tasks = [UserBehavior]
    wait_time = between(1, 3)
from locust import HttpUser, task, between

class ImageClassifierUser(HttpUser):
    wait_time = between(1, 2)

    @task
    def upload_image(self):
        with open("test.jpeg", "rb") as f:
            files = {"file": ("test.jpg", f, "image/jpeg")}
            self.client.post("/predict", files=files)

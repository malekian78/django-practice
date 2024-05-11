from django.db import models
from django.urls import reverse
from accounts.models import User
class Task(models.Model):
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, null=True, blank=True
    )
    title = models.CharField(max_length=200)
    complete = models.BooleanField(default=False)
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    class Meta:
        order_with_respect_to = "user"
        
    def get_relative_api_url(self):
        return reverse("api-viewset:tasks-detail", kwargs={"pk": self.pk})

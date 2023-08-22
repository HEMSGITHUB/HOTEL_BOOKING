from django.db import models


class UserDetail(models.Model):
    # fields of the model
    name = models.CharField(max_length=200)
    email = models.CharField(max_length=200)
    checkin = models.CharField(max_length=200)
    checkout = models.CharField(max_length=200)
    last_modified = models.DateTimeField(auto_now_add=True)

    # renames the instances of the model
    # with their title name
    def __str__(self):
        return self.name

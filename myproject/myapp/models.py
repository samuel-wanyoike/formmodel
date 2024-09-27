from django.db import models

class Logger(models.Model):
    first_name = models.CharField(max_length = 200)
    last_name = models.CharField(max_length = 200)
    time_log = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.first_name
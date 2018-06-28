from django.db import models
import time

date_added = time.strftime("%Y/%m/%d")
class Add_board(models.Model):
    title = models.CharField(max_length=50)
    text = models.CharField(max_length=2000)
    author = models.CharField(max_length=50)
    date_added = models.CharField(max_length=50, default=date_added)

    def __str__(self):
        return self.title + " " + self.text + " "+self.author

from django.db import models

class User(models.Model) : 
    name = models.CharField(max_length = 20) # 유저이름

    def __str__(self) : 
        return self.name

class Project(models.Model):
    title = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')
    body = models.TextField()

    leader = models.CharField(max_length=200, null=True)
    team01 = models.CharField(max_length=200, null=True)
    team02 = models.CharField(max_length=200, null=True)
    team03 = models.CharField(max_length=200, null=True)

    def __str__(self):
        return self.title
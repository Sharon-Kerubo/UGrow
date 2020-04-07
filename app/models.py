from django.db import models

class crops(models.Model):
    name = models.CharField(max_length=250)
    area = models.CharField(max_length=250)

    def __str__(self):
        return self.name + '_' + self.area

class Registration(models.Model):
    username = forms.CharField(max_length=200)
    email = forms.CharField(max_length=200)
    password = forms.CharField(widget = forms.PasswordInput)
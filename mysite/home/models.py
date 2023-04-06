from django.db import models

# Create your models here.
class Headline(models.Model):

    def __str__(self):
        return self.headline_name

    headline_name = models.CharField(max_length=200)
    headline_desc = models.CharField(max_length=200)
    headline_content = models.CharField(max_length=1000)
    headline_image = models.CharField(max_length=1000,default="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSbdpd2opUVxL2tYnU2Z2KlayBAbtfWUUuMYvu1_YpSUg&usqp=CAU&ec=48600113")
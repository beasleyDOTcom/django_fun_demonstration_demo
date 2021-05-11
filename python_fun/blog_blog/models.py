from django.db import models

class Category(models.Model):

    category_id = models.AutoField(primary_key = True)
    name = models.CharField(max_length = 190)

    def __str__(self):
        return self.name


# Create your models here.
class Blog(models.Model):
    #it is pretty much always going to be like this...
    title = models.CharField(max_length = 90)
    first_name = models.CharField(max_length = 25)
    last_name = models.CharField(max_length = 40)
    content = models.TextField(max_length = 800)
    email_of_author = models.EmailField(max_length = 90)
    category_id = models.ForeignKey(Category, on_delete = models.CASCADE)
    

    def __str__(self):
        return self.title
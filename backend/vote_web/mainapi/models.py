from django.db import models

# Create your models here.


from django.db import models

class Item(models.Model):
    name = models.CharField(max_length=50,verbose_name="投票項目名稱")
    votes = models.IntegerField(default=0)
    def __str__(self):
        return self.name

class Vote(models.Model):
    voter_name = models.CharField(max_length=255)
    item = models.ForeignKey(Item, on_delete=models.CASCADE,null=True)
    created_at = models.DateTimeField(auto_now_add=True)
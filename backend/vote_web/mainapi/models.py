from django.db import models

# Create your models here.

# # 投票項目
# class VoteItems(models.Model):
#
#     item_name = models.CharField(max_length=50,blank=True,null=False,verbose_name="投票項目名稱")
#     mdt = models.DateTimeField(auto_now=True,verbose_name="編輯時間")
#
#     class Meta:
#         ordering = ('-mdt',)
#         verbose_name = "投票項目"
#         verbose_name_plural = verbose_name
#
#     def __str__(self):
#         return self.item_name
#
# # 投票紀錄
# class PollRecords(models.Model):
#
#     voter = models.CharField(max_length=50,blank=True,null=False,verbose_name="投票者")
#     representor = models.ForeignKey(VoteItems,on_delete=models.CASCADE, related_name='voteitems')
#     mdt = models.DateTimeField(auto_now=True,verbose_name="編輯時間")
#
#     class Meta:
#         ordering = ('-mdt',)
#         verbose_name = "投票紀錄"
#         verbose_name_plural = verbose_name
#
#     def __str__(self):
#         return self.sign_up_name

from django.db import models

class Item(models.Model):
    name = models.CharField(max_length=50,verbose_name="投票項目名稱")

    def __str__(self):
        return self.name
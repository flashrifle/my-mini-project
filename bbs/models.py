from django.db import models

# Create your models here.

class bbs(models.Model):
    title = models.CharField(max_length=200, verbose_name="제목")
    content = models.TextField(verbose_name="내용")
    writer = models.CharField(max_length=100, verbose_name="작성자")
    create_at = models.DateTimeField(auto_now_add=True, verbose_name="작성일")
    update_at = models.DateTimeField(auto_now=True, verbose_name="수정일")

    def __str__(self):
        return self.title
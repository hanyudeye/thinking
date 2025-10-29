from django.db import models
from django.urls import reverse

# Create your models here.

class Blog(models.Model):
    title = models.CharField(max_length=200)    # 博客标题  
    content = models.TextField()                # 博客内容
    created_at = models.DateTimeField(auto_now_add=True)  # 创建时间        
    updated_at = models.DateTimeField(auto_now=True)       # 更新时间
    author = models.CharField(max_length=100)   # 作者
    is_published = models.BooleanField(default=True)  # 是否发布
    tags = models.CharField(max_length=100, blank=True)  # 标签，逗号分隔
    category = models.ForeignKey('blog.Category', on_delete=models.CASCADE, related_name='blogs')

    def get_absolute_url(self):
        return reverse('blog:blog_detail', (), {'pk': self.pk})


class Category(models.Model):
    name = models.CharField(max_length=100)  # 分类名称
    description = models.TextField(blank=True)  # 分类描述

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('/blog/category/{self.pk}/')

    class Meta:
        verbose_name_plural = "Categories"  # 管理界面显示为复数形式
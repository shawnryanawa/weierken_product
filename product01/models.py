from django.db import models

# Create your models here.
#创建djangomodels表格（名称/产品SKU/分类/介绍/描述/图片数量/图片地址/Order(MOQ)/Payment/Shipping Port/Lead Time/Material/Product Size/Sample time/标签/商品链接/）
class Product(models.Model):
    name = models.CharField(max_length=200,blank=True,null=True)
    sku = models.CharField(max_length=200,blank=True,null=True)
    category = models.CharField(max_length=200,blank=True,null=True)
    description = models.TextField(blank=True,null=True)
    detail = models.TextField(blank=True,null=True)
    image_url = models.CharField(max_length=1024,blank=True,null=True)
    image_count = models.IntegerField(blank=True,null=True)
    order = models.CharField(max_length=200,blank=True,null=True)
    payment = models.CharField(max_length=200,blank=True,null=True)
    shipping_port = models.CharField(max_length=200,blank=True,null=True)
    lead_time = models.CharField(max_length=200,blank=True,null=True)
    material = models.CharField(max_length=200,blank=True,null=True)
    product_size = models.CharField(max_length=200,blank=True,null=True)
    sample_time = models.CharField(max_length=200,blank=True,null=True)
    tag = models.CharField(max_length=1024,blank=True,null=True)
    product_url = models.CharField(max_length=1024,blank=True,null=True)



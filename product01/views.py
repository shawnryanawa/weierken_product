from django.shortcuts import render
from product01 import models
# Create your views here.
def product_all(request):
    #获取数据库Product的数据
    product_list = models.Product.objects.all()
    #由于数据库中记录的图片链接为带逗号的字符串，需要先通过函数转为列表在加载
    for obj in product_list:
        obj.image_url_list = obj.image_url.split(",")
        print(obj.image_url_list)

    #传到前端页面
    return render(request, 'product_all.html',{'product_list':product_list})


def product_detail(request,product_id):
    #获取数据对象
    product_obj = models.Product.objects.get(id=product_id)
    product_obj.image_url_list = product_obj.image_url.split(",")
    #区分主图和其他图片
    main_img_url = product_obj.image_url_list[0]
    other_img_url_list = product_obj.image_url_list[1:]
    #生成对应主图和其他图片的字典
    img_dict = {
        "main_img_url":main_img_url,
        "other_img_url_list":other_img_url_list
    }


    return render(request, 'product_detail.html',{'product_obj':product_obj,'img_dict':img_dict})
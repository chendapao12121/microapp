from django.contrib import admin
from apps import models
# Register your models here.

admin.site.register(models.Admin)
admin.site.register(models.AdminToken)
admin.site.register(models.Auth)
admin.site.register(models.Role)
admin.site.register(models.Commodity)
admin.site.register(models.CommodityAttribute)
admin.site.register(models.CustomAttribute)
admin.site.register(models.CommodityDetail)
admin.site.register(models.CommodityDetailImg)
admin.site.register(models.CommodityCategory)
admin.site.register(models.CommoditySubCategory)


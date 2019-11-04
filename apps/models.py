from django.contrib.contenttypes.fields import GenericForeignKey, GenericRelation
from django.contrib.contenttypes.models import ContentType
from django.db.models import Q
from django.utils.safestring import mark_safe
from django.db import models
import hashlib


class Auth(models.Model):
    auth = models.CharField(verbose_name="权限",max_length=16,unique=True)

    def __str__(self):
        return "%s" % self.auth

    class Meta:
        verbose_name_plural = "权限"


class Role(models.Model):
    role = models.CharField(verbose_name="角色",max_length=16,unique=True)
    auth = models.OneToOneField(to=Auth)  # 拥有的权限

    def __str__(self):
        return "%s" % self.role

    class Meta:
        verbose_name_plural = "角色"


class Admin(models.Model):
    username = models.CharField(max_length=16,unique=True)
    password = models.CharField(max_length=64)
    role = models.OneToOneField(to=Role)  # 所属角色
    is_super = models.SmallIntegerField()  # 是否超级管理员，1为是

    def __str__(self):
        return "%s" % self.username

    class Meta:
        verbose_name_plural = "管理员"


class AdminToken(models.Model):
    admin = models.OneToOneField(to=Admin)
    token = models.CharField(max_length=64,unique=True)
    addtime = models.BigIntegerField()


class CommodityCategory(models.Model):
    name = models.CharField(max_length=16,unique=True)

    def __str__(self):
        return "%s" % self.name

    class Meta:
        verbose_name_plural = "商品大类"


class CommoditySubCategory(models.Model):
    category = models.ForeignKey("CommodityCategory")
    name = models.CharField(max_length=64, unique=True)

    def __str__(self):
        return "%s" % self.name

    class Meta:
        verbose_name_plural = "商品子类"


class Commodity(models.Model):
    name = models.CharField(max_length=32,unique=True)
    commodity_img = models.CharField(max_length=255,unique=True)  # 商品图片
    brief = models.TextField(verbose_name="商品简介")
    category = models.ForeignKey("CommoditySubCategory")   # 商品分类
    have_discount = models.SmallIntegerField()  # 商品是否打折，1为是
    discount = models.DecimalField(verbose_name="商品折扣",decimal_places=2,max_digits=3,default=1)  # 商品折扣，没有则为0，有多少折扣则为0.几
    price = models.PositiveIntegerField(verbose_name="商品价格")

    def __str__(self):
        return "%s" % self.name

    class Meta:
        verbose_name_plural = "商品"


class CommodityDetail(models.Model):
    commodity = models.ForeignKey("Commodity")
    detail = models.TextField(verbose_name="商品详情")

    class Meta:
        verbose_name_plural = "商品详情"


class CommodityAttribute(models.Model):
    area = models.CharField(verbose_name="产地",max_length=16)
    brand = models.CharField(verbose_name="品牌",max_length=16)
    commodity = models.ForeignKey("CommodityDetail")

    class Meta:
        verbose_name_plural = "商品属性"


class CustomAttribute(models.Model):
    name = models.CharField(verbose_name="属性名称",max_length=16)
    val = models.CharField(verbose_name="属性值",max_length=64)
    commodity = models.ForeignKey("CommodityDetail")

    class Meta:
        verbose_name_plural = "商品自定义属性"


class CommodityDetailImg(models.Model):
    img = models.CharField(verbose_name="商品详情图片",max_length=255,unique=True)
    commodity = models.ForeignKey("CommodityDetail")


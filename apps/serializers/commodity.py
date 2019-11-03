from apps import models
from rest_framework import serializers


class CommoditySerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Commodity
        depth = 2
        # fields = ['id', 'name','category', 'commodity_img', 'brief', 'price']
        fields = '__all__'


class CommodityDetailSerializer(serializers.ModelSerializer):
    name = serializers.CharField(source='commodity.name')
    img = serializers.SerializerMethodField(method_name='get_img')
    attribute = serializers.SerializerMethodField(method_name='get_default_attribute')
    customattribute = serializers.SerializerMethodField(method_name='get_custom_attribute')

    class Meta:
        model = models.CommodityDetail
        fields = ['name','detail', 'img', 'attribute', 'customattribute']

    def get_img(self, obj):
        # 获取商品的所有图片
        queryset = models.CommodityDetailImg.objects.filter(commodity=obj.id).all()
        return [{'id': row.id, 'img': row.img} for row in queryset]

    def get_default_attribute(self, obj):
        # 获取商品的所有图片
        queryset = models.CommodityAttribute.objects.filter(commodity=obj.id).all()
        return [{'id': row.id, 'area': row.area, 'brand': row.brand} for row in queryset]

    def get_custom_attribute(self, obj):
        # 获取商品的所有自定义属性
        queryset = models.CustomAttribute.objects.filter(commodity=obj.id).all()
        return [{'id': row.id, 'name': row.name, 'val': row.val} for row in queryset]

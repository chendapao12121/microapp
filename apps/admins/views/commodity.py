from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.viewsets import ViewSetMixin
from apps.serializers.commodity import *
from apps.admins.auth.auth import *
import shutil


class CommodityView(ViewSetMixin, APIView):

    def list(self, request, *args, **kwargs):
        '''
        商品列表接口
        :param request:
        :param args:
        :param kwargs:
        :return:
        '''
        ret = {
            'code': 1000,
            'data': None
        }
        try:
            queryset = models.Commodity.objects.all()
            ser = CommoditySerializer(instance=queryset, many=True)
            ret['data'] = ser.data
        except Exception as e:
            ret['code'] = 1001
            ret['error'] = '获取商品失败'

        return Response(ret)

    def retrieve(self, request, *args, **kwargs):
        '''
        商品详细接口
        :param request:
        :param args:
        :param kwargs:
        :return:
        '''
        ret = {
            'code': 1000,
            'data': None
        }
        try:
            pk = kwargs.get('pk')
            obj = models.CommodityDetail.objects.filter(commodity_id=pk).first()
            ser = CommodityDetailSerializer(instance=obj, many=False)
            ret['data'] = ser.data
        except Exception as e:
            ret['code'] = 1001
            ret['error'] = '获取商品失败'

        return Response(ret)

    def add(self, request, *args, **kwargs):
        '''添加商品接口'''
        # APIView.authentication_classes = [Auth, ]  # 认证模块
        ret = {
            'code': 1000,
            'data': None
        }
        custom_attribute_list = []
        name = request.data.get('name')
        commodity_img = request.data.get('commodity_img')
        brief = request.data.get('brief')
        category = request.data.get('category')
        have_discount = request.data.get('have_discount', 0)
        discount = request.data.get('discount', 1)
        price = request.data.get('price')
        detail = request.data.get('detail')
        area = request.data.get('area')
        brand = request.data.get('brand')
        custom_attribute = request.data.get('custom_attribute')
        commodity_detail_img = request.data.get('commodity_detail_img')

        try:
            models.Commodity.objects.create(
                name=name,
                commodity_img=commodity_img,
                brief=brief,
                category=models.CommoditySubCategory.objects.filter(name=category).first(),
                have_discount=have_discount,
                discount=discount,
                price=price
            )
            models.CommodityDetail.objects.create(
                commodity=models.Commodity.objects.filter(name=name).first(),
                detail=detail
            )
            models.CommodityAttribute.objects.create(
                area=area,
                brand=brand,
                commodity=models.CommodityDetail.objects.filter(commodity=models.Commodity.objects.filter(name=name).first()).first(),
            )
            for custom_name in custom_attribute:
                obj = models.CustomAttribute(name=custom_name, val=custom_attribute[custom_name],
                                             commodity=models.CommodityDetail.objects.filter(
                                                 commodity=models.Commodity.objects.filter(name=name).first()).first())
                custom_attribute_list.append(obj)
            models.CustomAttribute.objects.bulk_create(custom_attribute_list)
            for img_name in commodity_detail_img:
                shutil.move(commodity_detail_img[img_name], 'apps/static/commoditydetailimg')
                models.CommodityDetailImg.objects.create(
                    img='apps/static/commoditydetailimg/' + img_name,
                    commodity=models.CommodityDetail.objects.filter(
                        commodity=models.Commodity.objects.filter(name=name).first()
                    ).first()
                )
            ret["data"] = "添加成功！"
        except IOError as i:
            ret["code"] = 2002
            ret["data"] = "添加失败！"
        return Response(ret)
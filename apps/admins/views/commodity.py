from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.viewsets import ViewSetMixin
from apps.serializers.commodity import *
from apps.admins.auth.auth import *
from django.db import transaction
import os,shutil


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
        # try:
        #     with transaction.atomic():
        #         sid = transaction.savepoint()  # 设置事务回滚点
        #         models.Commodity.objects.create(
        #             name=name,
        #             commodity_img='http://118.89.54.143:8000/static/commodityimg/'.encode('utf-8')+commodity_img.split('/')[-1].encode('utf-8'),
        #             brief=brief,
        #             category=models.CommoditySubCategory.objects.filter(name=category).first(),
        #             have_discount=have_discount,
        #             discount=discount,
        #             price=price
        #         )
        #         models.CommodityDetail.objects.create(
        #             commodity=models.Commodity.objects.filter(name=name).first(),
        #             detail=detail
        #         )
        #         models.CommodityAttribute.objects.create(
        #             area=area,
        #             brand=brand,
        #             commodity=models.CommodityDetail.objects.filter(commodity=models.Commodity.objects.filter(name=name).first()).first(),
        #         )
        #         if custom_attribute:
        #             custom_attribute_list = []
        #             for custom_name in custom_attribute:
        #                 obj = models.CustomAttribute(name=custom_name, val=custom_attribute[custom_name],
        #                                              commodity=models.CommodityDetail.objects.filter(
        #                                                  commodity=models.Commodity.objects.filter(name=name).first()).first())
        #                 custom_attribute_list.append(obj)
        #             models.CustomAttribute.objects.bulk_create(custom_attribute_list)
        #         for img_name in commodity_detail_img:
        #             models.CommodityDetailImg.objects.create(
        #                 img='http://118.89.54.143:8000/static/commoditydetailimg/'.encode('utf-8')+img_name.encode('utf-8'),
        #                 commodity=models.CommodityDetail.objects.filter(
        #                     commodity=models.Commodity.objects.filter(name=name).first()
        #                 ).first()
        #             )
        #         obj = models.Commodity.objects.filter(name=name).first()
        #         if obj:
        #             try:
        for img_name in commodity_detail_img:
            print(os.getcwd()+'/apps/static/temporaryfolder/'+img_name, os.getcwd()+'/apps/static/commoditydetailimg')
        print(os.getcwd()+'/apps/static/temporaryfolder/'+commodity_img.split('/')[-1], os.getcwd()+'/apps/static/commodityimg')
                        # ret["data"] = "添加成功！"
        #             except Exception:
        #                 transaction.savepoint_rollback(sid)
        #                 ret["code"] = 2002
        #                 ret["data"] = "添加失败！文件路径出错！"
        # except Exception as e:
        #     ret["code"] = 2002
        #     ret["data"] = "添加失败！"
        return Response(ret)

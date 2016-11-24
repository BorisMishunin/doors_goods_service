# -*- coding: utf-8 -*-
from django.core.management.base import BaseCommand
import logging
import os
import requests
from doors_goods_service.models import TypesOfGoods, Goods, Properties, Values
import doors_goods_service.localsettings as settings

logger = logging.getLogger(__name__)

def add_new_door(door_name,foto,door_params):
    params = {}
    for param in door_params.split(','):
        param_name, param_value = param.split(':')
        params[param_name]=param_value

    type, created = TypesOfGoods.objects.get_or_create(name='doors')
    door = Goods.objects.create(article=door_name, name=door_name, type=type, foto=[], colors=[], info=dict(params))
    add_door_params(door, door_params)
    upload_file(door, foto)

def upload_file(product, file):
    image_data = {'type': 'marketplace',
                  'object': 'product',
                  'id': product.id
                  }
    manager = getattr(requests, 'post')
    files = {'file': open(file, 'rb')}
    resp = manager(settings.services['files_service'] + '/' + 'upload_file',
               data=image_data, files=files)
    if resp.status_code == 200:
        product.foto.append(resp.json().get('path'))
        product.save()

def add_door_params(door, door_params):
    for param in door_params.split(','):
        param_name, param_value= param.split(':')
        obj_param, created = Properties.objects.get_or_create(name=param_name)
        obj_param_value, created  = Values.objects.get_or_create(good_property=obj_param, value=param_value)

class Command(BaseCommand):
    help = ' fill doors '

    def add_arguments(self, parser):
        parser.add_argument('--path',
                            action='store',
                            dest='path',
                            type=str,
                            default='',
                            help='path to files')
        parser.add_argument('--filename',
                            action='store',
                            dest='filename',
                            type=str,
                            default='uploading_goods.txt',
                            help='data filename')

    def handle(self, *args, **options):
        try:
            import_file = options['path']
            filename = options['filename']
            with open(os.path.join(import_file, filename)) as import_data:
                for line in import_data:
                    door_name, fotos_list, door_params = line.split(';')
                    for foto in fotos_list.split(','):
                        if True:
                            add_new_door(door_name + '_' + foto, os.path.join(import_file, foto + '.jpg'), door_params)
                            print 'add good - %s' % foto
                        #except:
                        #    pass

        except Exception, e:
            print e
            logger.exception(e)



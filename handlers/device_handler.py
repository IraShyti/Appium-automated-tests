from base_handler import BaseHandler
import json
from bson.json_util import dumps
from sources.device_source import DeviceSource


class DeviceHandler(BaseHandler):
    def get(self, device_name):

        if not device_name or device_name == '/':
            device_name = None
        else:
            device_name = device_name.strip('/')

        result = None
        if not device_name:
            result = DeviceSource().get_devices()
            result = sorted(result, key=lambda x: x['device_index'], reverse=False)
        else:
            result = DeviceSource().get_device(device_name)
        self.write(dumps(result))

    def post(self, *args, **kwargs):
        payload = json.loads(self.request.body)
        platform_name = payload['platform_name']
        platform_version = payload['platform_version']
        device_name = payload['device_name']
        device_display_name = payload['display_name']
        device_index = payload['device_index']
        self.write(dumps({'result': DeviceSource().add_device(device_name, platform_name, platform_version,
                                                              device_display_name, device_index)}))

    def put(self, *args, **kwargs):
        payload = json.loads(self.request.body)
        platform_name = payload['platform_name']
        platform_version = payload['platform_version']
        device_name = payload['device_name']
        device_display_name = payload['display_name']
        device_index = payload['device_index']
        self.write(dumps({'result': DeviceSource().update_device(device_name, platform_name, platform_version,
                                                                 device_display_name, device_index)}))

    def delete(self, device_name):

        if not device_name or device_name == '/':
            device_name = None
        else:
            device_name = device_name.strip('/')
        print device_name
        self.write(dumps({'result': DeviceSource().delete_device(device_name)}))

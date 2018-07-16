from configuration import *


class DeviceSource(object):

    def get_devices(self):

        devices = list(db.devices.find({}))
        print 'aaa devices'
        return sorted(devices, key=lambda x: x['device_index'], reverse=False)

    def get_device(self, device_name):
        device = db.devices.find_one({'device_name': device_name})
        return device

    def add_device(self, device_name, platform_name, platform_version, device_display_name, device_index):

        if self.get_device(device_name):
            return {'status': 'failed', 'message': 'Existing device name'}

        device = {'device_name': device_name, 'platform_name': platform_name, 'platform_version': platform_version , 'device_display_name': device_display_name, 'device_index': device_index}
        result = db.devices.insert_one(device)

        if result.inserted_id:
            return {'status': 'success', 'message': 'Device added'}
        else:
            return {'status': 'failed', 'message': 'Device could not be added'}

    def delete_device(self, device_name):
        result = db.devices.delete_one({'device_name': device_name})

        if result.deleted_count == 1:
            return {'status': 'success', 'message': 'Device deleted'}
        else:
            return {'status': 'failed', 'message': 'Device could not be deleted'}

    def update_device(self, device_name, platform_name, platform_version, device_display_name, device_index):

        result = db.devices.update_one({'device_name': device_name}, {'$set': {'platform_name': platform_name, 'platform_version': platform_version, 'device_display_name': device_display_name, 'device_index': device_index}})

        if result.matched_count == 1:
            return {'status': 'success', 'message': 'Device updated'}
        else:
            return {'status': 'failed', 'message': 'Device could not be updated'}




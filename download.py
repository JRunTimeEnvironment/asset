#!/usr/bin/env python
# coding:utf-8

import xlwt
import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "asset.settings")
import django
django.setup()

def downloadMesterDevice():
    from switch.models import MesterDevice
    mesterdevicelist = MesterDevice.objects.all().order_by('uid')
    mesterdevicefile = xlwt.Workbook(encoding='utf-8')
    devicefile = mesterdevicefile.add_sheet(u'MesterDevice',cell_overwrite_ok=True)
    devicefile.write(0, 0, u"uid")
    devicefile.write(0, 1, u"name")
    devicefile.write(0, 2, u"sn_number")
    excel_row = 1
    for mesterdevice in mesterdevicelist:
        uid = mesterdevice.uid
        name = mesterdevice.name
        sn_number = mesterdevice.sn_number
        devicefile.write(excel_row, 0, uid)
        devicefile.write(excel_row, 1, name)
        devicefile.write(excel_row, 2, sn_number)
        excel_row += 1
    exist_file = os.path.exists('file/output_MesterDevice.xls')
    if exist_file:
        os.remove(r'file/output_MesterDevice.xls')
    mesterdevicefile.save('file/output_MesterDevice.xls')

def downloadFaultDevice():
    from switch.models import FaultDevice
    faultdevicelist = FaultDevice.objects.all()
    faultdevicefile = xlwt.Workbook(encoding='utf-8')
    devicefile = faultdevicefile.add_sheet(u'FaultDevice',cell_overwrite_ok=True)
    devicefile.write(0, 0, u"系统/硬件/数据库等")
    devicefile.write(0, 1, u"故障级别")
    devicefile.write(0, 2, u"故障描述")
    devicefile.write(0, 3, u"影响范围")
    devicefile.write(0, 4, u"解决方法")
    devicefile.write(0, 5, u"完成时间")
    devicefile.write(0, 6, u"故障日期")
    devicefile.write(0, 7, u"SN序列号")
    excel_row = 1
    for faultdevice in faultdevicelist:
        system = faultdevice.system
        failure_level = faultdevice.failure_level
        failt_description = faultdevice.failt_description
        incidence = faultdevice.incidence
        resolvent = faultdevice.resolvent
        finish_time = faultdevice.finish_time
        down_time = faultdevice.down_time
        sn_number = faultdevice.sn_number
        devicefile.write(excel_row, 0, system)
        devicefile.write(excel_row, 1, failure_level)
        devicefile.write(excel_row, 2, failt_description)
        devicefile.write(excel_row, 3, incidence)
        devicefile.write(excel_row, 4, resolvent)
        devicefile.write(excel_row, 5, finish_time)
        devicefile.write(excel_row, 6, down_time)
        devicefile.write(excel_row, 7, sn_number)
        excel_row += 1
    exist_file = os.path.exists('file/output_FaultDevice.xls')
    if exist_file:
        os.remove(r'file/output_FaultDevice.xls')
    faultdevicefile.save('file/output_FaultDevice.xls')

def downloadHostDevice():
    from switch.models import HostDevice
    hostdevicelist = HostDevice.objects.all().order_by('uid')
    hostdevicefile = xlwt.Workbook(encoding='utf-8')
    devicefile = hostdevicefile.add_sheet(u'HostDevice',cell_overwrite_ok=True)
    devicefile.write(0, 0, u"序号")
    devicefile.write(0, 1, u'状态')
    devicefile.write(0, 2, u'品牌')
    devicefile.write(0, 3, u'服务器名称')
    devicefile.write(0, 4, u'机房号')
    devicefile.write(0, 5, u'机架号')
    devicefile.write(0, 6, u'设备号')
    devicefile.write(0, 7, u'SN序列号')
    devicefile.write(0, 8, u'移动资产标签')
    devicefile.write(0, 9, u'系统名称')
    devicefile.write(0, 10, u'应用类别')
    devicefile.write(0, 11, u'设备类型')
    devicefile.write(0, 12, u'Lpar&Domain名称')
    devicefile.write(0, 13, u'zone(仅适用于oracle小型机)')
    devicefile.write(0, 14, u'主机名')
    devicefile.write(0, 15, u'系统IP')
    devicefile.write(0, 16, u'密码')
    devicefile.write(0, 17, u'网管机ip')
    devicefile.write(0, 18, u'登录方式')
    devicefile.write(0, 19, u'管理口IP')
    devicefile.write(0, 20, u'管理口密码')
    devicefile.write(0, 21, u'网卡绑定类型')
    devicefile.write(0, 22, u'网卡绑定子网卡')
    devicefile.write(0, 23, u'应用辅助IP')
    devicefile.write(0, 24, u'处理器类型')
    devicefile.write(0, 25, u'处理器主频(GHz)')
    devicefile.write(0, 26, u'处理器个数')
    devicefile.write(0, 27, u'每处理器核数')
    devicefile.write(0, 28, u'总核数/总线程数')
    devicefile.write(0, 29, u'内存')
    devicefile.write(0, 30, u'内存个数')
    devicefile.write(0, 31, u'硬盘大小*数量(IOU板数量)')
    devicefile.write(0, 32, u'OS')
    devicefile.write(0, 33, u'Kernel')
    devicefile.write(0, 34, u'硬件微码级别')
    devicefile.write(0, 35, u'系统软件数据库及版本')
    devicefile.write(0, 36, u'集群类型')
    devicefile.write(0, 37, u'集群版本')
    devicefile.write(0, 38, u'阵列型号')
    devicefile.write(0, 39, u'阵列序列号')
    devicefile.write(0, 40, u'阵列机房号')
    devicefile.write(0, 41, u'阵列机架号')
    devicefile.write(0, 42,u'阵列设备号')
    devicefile.write(0, 43, u'LUN容量及个数')
    devicefile.write(0, 44, u'总容量')
    devicefile.write(0, 45, u'阵列连接情况')
    devicefile.write(0, 46, u'连接的光纤交换机')
    devicefile.write(0, 47, u'是否为测试机')
    devicefile.write(0, 48, u'能否随时停机')
    devicefile.write(0, 49, u'厂商/应用联系人/手机号')
    devicefile.write(0, 50, u'移动负责人')
    devicefile.write(0, 51, u'所在部门')
    devicefile.write(0, 52, u'承载应用')
    devicefile.write(0, 53, u'维保类型')
    devicefile.write(0, 54, u'备注')
    excel_row = 1
    for hostdevice in hostdevicelist:
        uid = hostdevice.uid
        state = hostdevice.state
        brand = hostdevice.brand
        servername = hostdevice.servername
        computer_id = hostdevice.computer_id
        rack_number = hostdevice.rack_number
        device_bumber = hostdevice.device_bumber
        sn_number = hostdevice.sn_number
        mobile_label = hostdevice.mobile_label
        systematic_name = hostdevice.systematic_name
        application = hostdevice.application
        device_type = hostdevice.device_type
        ld_name = hostdevice.ld_name
        zone = hostdevice.zone
        huost_name = hostdevice.huost_name
        system_ip = hostdevice.system_ip
        password = hostdevice.password
        netword_id = hostdevice.netword_id
        login_mode = hostdevice.login_mode
        management_ip = hostdevice.management_ip
        management_password = hostdevice.management_password
        nic_type = hostdevice.nic_type
        card_type = hostdevice.card_type
        auxiliary = hostdevice.auxiliary
        processor_type = hostdevice.processor_type
        processor_ghz = hostdevice.processor_ghz
        processors = hostdevice.processors
        nucleus = hostdevice.nucleus
        number = hostdevice.number
        internal = hostdevice.internal
        menory = hostdevice.menory
        iou_type = hostdevice.iou_type
        os1 = hostdevice.os
        kernel = hostdevice.kernel
        hardware_level = hostdevice.hardware_level
        version = hostdevice.version
        cluster_type = hostdevice.cluster_type
        cluster_version = hostdevice.cluster_version
        array_model = hostdevice.array_model
        sequence_number = hostdevice.sequence_number
        room_number = hostdevice.room_number
        rack_nembers = hostdevice.rack_nembers
        device_number = hostdevice.device_number
        lun_number = hostdevice.lun_number
        gross = hostdevice.gross
        array_connection = hostdevice.array_connection
        optical = hostdevice.optical
        test_machine = hostdevice.test_machine
        stop = hostdevice.stop
        firm = hostdevice.firm
        mobile = hostdevice.mobile
        dept = hostdevice.dept
        bearer = hostdevice.bearer
        maintenance_type = hostdevice.maintenance_type
        remarks = hostdevice.remarks
        devicefile.write(excel_row, 0, uid)
        devicefile.write(excel_row, 1,state)
        devicefile.write(excel_row, 2,brand)
        devicefile.write(excel_row, 3,servername)
        devicefile.write(excel_row, 4,computer_id)
        devicefile.write(excel_row, 5,rack_number)
        devicefile.write(excel_row, 6,device_bumber)
        devicefile.write(excel_row, 7,sn_number)
        devicefile.write(excel_row, 8,mobile_label)
        devicefile.write(excel_row, 10,application)
        devicefile.write(excel_row, 11,device_type)
        devicefile.write(excel_row, 12,ld_name)
        devicefile.write(excel_row, 13,zone)
        devicefile.write(excel_row, 14,huost_name)
        devicefile.write(excel_row, 15,system_ip)
        devicefile.write(excel_row, 16,password)
        devicefile.write(excel_row, 17,netword_id)
        devicefile.write(excel_row, 18,login_mode)
        devicefile.write(excel_row, 19,management_ip)
        devicefile.write(excel_row, 24,processor_type)
        devicefile.write(excel_row, 25,processor_ghz)
        devicefile.write(excel_row, 26,processors)
        devicefile.write(excel_row, 27,nucleus)
        devicefile.write(excel_row, 28,number)
        devicefile.write(excel_row, 29,internal)
        devicefile.write(excel_row, 30,menory)
        devicefile.write(excel_row, 31,iou_type)
        devicefile.write(excel_row, 32,os1)
        devicefile.write(excel_row, 33,kernel)
        devicefile.write(excel_row, 34,hardware_level)
        devicefile.write(excel_row, 35,version)
        devicefile.write(excel_row, 36,cluster_type)
        devicefile.write(excel_row, 37,cluster_version)
        devicefile.write(excel_row, 38,array_model)
        devicefile.write(excel_row, 39,sequence_number)
        devicefile.write(excel_row, 40,room_number)
        devicefile.write(excel_row, 41,rack_nembers)
        devicefile.write(excel_row, 42,device_number)
        devicefile.write(excel_row, 43,lun_number)
        devicefile.write(excel_row, 44,gross)
        devicefile.write(excel_row, 45,array_connection)
        devicefile.write(excel_row, 46,optical)
        devicefile.write(excel_row, 47,test_machine)
        devicefile.write(excel_row, 48,stop)
        devicefile.write(excel_row, 49,firm)
        devicefile.write(excel_row, 50,mobile)
        devicefile.write(excel_row, 51,dept)
        devicefile.write(excel_row, 52,bearer)
        devicefile.write(excel_row, 53,maintenance_type)
        devicefile.write(excel_row, 54,remarks)
        excel_row += 1
    exist_file = os.path.exists('file/output_HostDevice.xls')
    if exist_file:
        os.remove(r'file/output_HostDevice.xls')
    hostdevicefile.save('file/output_HostDevice.xls')

def downloadNetworkDevice():
    from switch.models import NetworkDevice
    networkdevicelist = NetworkDevice.objects.all()
    networkdevicefile = xlwt.Workbook(encoding='utf-8')
    devicefile = networkdevicefile.add_sheet(u'NetworkDevice',cell_overwrite_ok=True)
    devicefile.write(0, 0, u"系统名称")
    devicefile.write(0, 1, u"品牌")
    devicefile.write(0, 2, u"设备的具体型号")
    devicefile.write(0, 3, u"序列号")
    devicefile.write(0, 4, u"名称/IP")
    devicefile.write(0, 5, u"登录密码")
    devicefile.write(0, 6, u"固件版本")
    devicefile.write(0, 7, u"登录方式")
    devicefile.write(0, 8, u"移动资产标签")
    devicefile.write(0, 9, u"设备位置")
    devicefile.write(0, 10, u"维保类型")
    excel_row = 1

    for networkdevice in networkdevicelist:
        system_name = networkdevice.system_name
        brand = networkdevice.brand
        specific_device = networkdevice.specific_device
        sn_number = networkdevice.sn_number
        ip = networkdevice.ip
        password = networkdevice.password
        version = networkdevice.version
        login = networkdevice.login
        mobile_tag = networkdevice.mobile_tag
        device_location = networkdevice.device_location
        type = networkdevice.type
        devicefile.write(excel_row,0, system_name)
        devicefile.write(excel_row,1, brand)
        devicefile.write(excel_row,2, specific_device)
        devicefile.write(excel_row,3, sn_number)
        devicefile.write(excel_row,4, ip)
        devicefile.write(excel_row,5, password)
        devicefile.write(excel_row,6, version)
        devicefile.write(excel_row,7, login)
        devicefile.write(excel_row,8, mobile_tag)
        devicefile.write(excel_row,9,  device_location)
        devicefile.write(excel_row,10, type)
        excel_row += 1
    exist_file = os.path.exists('file/output_NetworkDevice.xls')
    if exist_file:
        os.remove(r'file/output_NetworkDevice.xls')
    networkdevicefile.save('file/output_NetworkDevice.xls')

def downloadWarrantyDevice():
    from switch.models import WarrantyDevice
    warrantydevicelist = WarrantyDevice.objects.all()
    warrantydevicefile = xlwt.Workbook(encoding='utf-8')
    devicefile = warrantydevicefile.add_sheet(u'WarrantyDevice',cell_overwrite_ok=True)
    devicefile.write(0, 0, u"序号")
    devicefile.write(0, 1, u'业务系统')
    devicefile.write(0, 2, u'设备类型')
    devicefile.write(0, 3, u'品牌')
    devicefile.write(0, 4, u'设备号')
    devicefile.write(0, 5, u'设备型号')
    devicefile.write(0, 6, u'SN序列号')
    devicefile.write(0, 7, u'资产编码')
    devicefile.write(0, 8, u'IP地址')
    devicefile.write(0, 9, u'维保状态')
    devicefile.write(0, 10, u'所在城市')
    devicefile.write(0, 11, u'具体位置')
    devicefile.write(0, 12, u'楼层')
    devicefile.write(0, 13, u'机架')
    devicefile.write(0, 14, u'服务开始')
    devicefile.write(0, 15, u'服务期限')
    devicefile.write(0, 16, u'维保月份')
    devicefile.write(0, 17, u'移动负责人')
    devicefile.write(0, 18, u'服务类别')
    devicefile.write(0, 19, u'投资编码')
    devicefile.write(0, 20, u'项目名称')
    devicefile.write(0, 21, u'合同名称')
    devicefile.write(0, 22, u'采购合同编号')
    devicefile.write(0, 23, u'采购价格')
    devicefile.write(0, 24, u'维保厂商联系人')
    devicefile.write(0, 25, u'转维联系人')

    excel_row = 1
    for warrantydevice in warrantydevicelist:
        uid = warrantydevice.uid
        business = warrantydevice.business
        equi_type = warrantydevice.equi_type
        brand = warrantydevice.brand
        device_no = warrantydevice.device_no
        specific_device = warrantydevice.specific_device
        sn_number = warrantydevice.sn_number
        asset_coding = warrantydevice.asset_coding
        ip = warrantydevice.ip
        main_status = warrantydevice.main_status
        city = warrantydevice.city
        location = warrantydevice.location
        floor = warrantydevice.floor
        frame = warrantydevice.frame
        start_time = warrantydevice.start_time
        end_time = warrantydevice.end_time
        month = warrantydevice.month
        mobile_person = warrantydevice.mobile_person
        service_type = warrantydevice.service_type
        code = warrantydevice.code
        project_name = warrantydevice.project_name
        contract_title = warrantydevice.contract_title
        purchase_number = warrantydevice.purchase_number
        price = warrantydevice.price
        contacts = warrantydevice.contacts
        turn_contacts = warrantydevice.turn_contacts
        devicefile.write(excel_row, 0, uid)
        devicefile.write(excel_row, 1,business)
        devicefile.write(excel_row, 2,equi_type)
        devicefile.write(excel_row, 3,brand)
        devicefile.write(excel_row, 4,device_no)
        devicefile.write(excel_row, 5,specific_device)
        devicefile.write(excel_row, 6,sn_number)
        devicefile.write(excel_row, 7,asset_coding)
        devicefile.write(excel_row, 8,ip)
        devicefile.write(excel_row, 9,main_status)
        devicefile.write(excel_row, 10,city)
        devicefile.write(excel_row, 11,location)
        devicefile.write(excel_row, 12,floor)
        devicefile.write(excel_row, 13,frame)
        devicefile.write(excel_row, 14,start_time)
        devicefile.write(excel_row, 15,end_time)
        devicefile.write(excel_row, 16,month)
        devicefile.write(excel_row, 17,mobile_person)
        devicefile.write(excel_row, 18,service_type)
        devicefile.write(excel_row, 19,code)
        devicefile.write(excel_row, 20,project_name)
        devicefile.write(excel_row, 21,contract_title)
        devicefile.write(excel_row, 22,purchase_number)
        devicefile.write(excel_row, 23,price)
        devicefile.write(excel_row, 24,contacts)
        devicefile.write(excel_row, 25,turn_contacts)
        excel_row += 1
    exist_file = os.path.exists('file/output_WarrantyDevice.xls')
    if exist_file:
        os.remove(r'file/output_WarrantyDevice.xls')
    warrantydevicefile.save('file/output_WarrantyDevice.xls')


def downloadStorageDevice():
    from switch.models import StorageDevice
    storagedevicelist = StorageDevice.objects.all()
    storagedevicefile = xlwt.Workbook(encoding='utf-8')
    devicefile = storagedevicefile.add_sheet(u'StorageDevice', cell_overwrite_ok=True)

    devicefile.write(0, 0, u"所属系统+I10A1:I7G7A1:K7")
    devicefile.write(0, 1, u"品牌")
    devicefile.write(0, 2, u"存储型号")
    devicefile.write(0, 3, u"存储配置")
    devicefile.write(0, 4, u"lun详细配置")
    devicefile.write(0, 5, u"登入方法")
    devicefile.write(0, 6, u"帐号/密码")
    devicefile.write(0, 7, u"设备位")
    devicefile.write(0, 8, u"序列号")
    devicefile.write(0, 9, u"移动资产标签")
    devicefile.write(0, 10, u"维保类型")
    excel_row = 1
    for storagedevice in storagedevicelist:

        own_system = storagedevice.own_system
        brand = storagedevice.brand
        storage_model = storagedevice.storage_model
        configuration = storagedevice.configuration
        lun_configuration = storagedevice.lun_configuration
        login_method = storagedevice.login_method
        account_password = storagedevice.account_password
        device_bit = storagedevice.device_bit
        sn_number = storagedevice.sn_number
        mobile_tag = storagedevice.mobile_tag
        type = storagedevice.type
        devicefile.write(excel_row, 0, own_system)
        devicefile.write(excel_row, 1, brand)
        devicefile.write(excel_row, 2, storage_model)
        devicefile.write(excel_row, 3, configuration)
        devicefile.write(excel_row, 4, lun_configuration)
        devicefile.write(excel_row, 5, login_method)
        devicefile.write(excel_row, 6, account_password)
        devicefile.write(excel_row, 7, device_bit)
        devicefile.write(excel_row, 8, sn_number)
        devicefile.write(excel_row, 9, mobile_tag)
        devicefile.write(excel_row, 10, type)
        excel_row += 1

    exist_file = os.path.exists('file/output_StorageDevice.xls')
    if exist_file:
        os.remove(r'file/output_StorageDevice.xls')
    storagedevicefile.save('file/output_StorageDevice.xls')


downloadNetworkDevice()
downloadStorageDevice()
downloadWarrantyDevice()
downloadMesterDevice()
downloadFaultDevice()
downloadHostDevice()
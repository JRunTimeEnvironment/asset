# coding:utf-8
from django.db import models

# Create your models here.

class MesterDevice(models.Model):
    uid = models.IntegerField(verbose_name=u'id')
    name = models.CharField(max_length=30,verbose_name=u'名字')
    sn_number = models.CharField(max_length=100,verbose_name=u'SN序列号')

    class Meta:
        verbose_name = u'设备主键外键管理'
        verbose_name_plural = verbose_name


class HostDevice(models.Model):
    uid = models.IntegerField(verbose_name=u'序号',primary_key=True)
    state = models.CharField(max_length=100,verbose_name=u'状态')
    brand = models.CharField(max_length=100,verbose_name=u'品牌')
    servername = models.CharField(max_length=100, verbose_name=u'服务器名称')
    computer_id = models.CharField(max_length=100, verbose_name=u'机房号')
    rack_number = models.CharField(max_length=100, verbose_name=u'机架号')
    device_bumber = models.CharField(max_length=100, verbose_name=u'设备号')
    sn_id = models.ForeignKey('MesterDevice')
    sn_number = models.CharField(max_length=100, verbose_name=u'SN序列号')
    mobile_label = models.CharField(max_length=100, verbose_name=u'移动资产标签')
    systematic_name = models.CharField(max_length=100, verbose_name=u'系统名称')
    application = models.CharField(max_length=100, verbose_name=u'应用类别')
    device_type = models.CharField(max_length=100, verbose_name=u'设备类型')
    ld_name = models.CharField(max_length=100, verbose_name=u'Lpar&Domain名称')
    zone = models.CharField(max_length=100, verbose_name=u'zone(仅适用于oracle小型机)')
    huost_name = models.CharField(max_length=100, verbose_name=u'主机名')
    system_ip = models.CharField(max_length=100, verbose_name=u'系统IP')
    password = models.CharField(max_length=100, verbose_name=u'密码')
    netword_id = models.CharField(max_length=100, verbose_name=u'网管机ip')
    login_mode = models.CharField(max_length=100, verbose_name=u'登录方式')
    management_ip = models.CharField(max_length=100, verbose_name=u'管理口IP')
    management_password = models.CharField(max_length=100, verbose_name=u'管理口密码')
    nic_type = models.CharField(max_length=100, verbose_name=u'网卡绑定类型')
    card_type = models.CharField(max_length=100, verbose_name=u'网卡绑定子网卡')
    auxiliary = models.CharField(max_length=100, verbose_name=u'应用辅助IP')
    processor_type = models.CharField(max_length=100, verbose_name=u'处理器类型')
    processor_ghz = models.CharField(max_length=100, verbose_name=u'处理器主频(GHz)')
    processors = models.CharField(max_length=100, verbose_name=u'处理器个数')
    nucleus = models.CharField(max_length=100, verbose_name=u'每处理器核数')
    number = models.CharField(max_length=100, verbose_name=u'总核数/总线程数')
    internal = models.CharField(max_length=100, verbose_name=u'内存')
    menory = models.CharField(max_length=100, verbose_name=u'内存个数')
    iou_type = models.CharField(max_length=100, verbose_name=u'硬盘大小*数量(IOU板数量)')
    os = models.CharField(max_length=100, verbose_name=u'OS')
    kernel = models.CharField(max_length=100, verbose_name=u'Kernel')
    hardware_level = models.CharField(max_length=100, verbose_name=u'硬件微码级别')
    version = models.CharField(max_length=100, verbose_name=u'系统软件数据库及版本')
    cluster_type = models.CharField(max_length=100, verbose_name=u'集群类型',blank=True)
    cluster_version = models.CharField(max_length=100, verbose_name=u'集群版本',blank=True)
    array_model = models.CharField(max_length=100, verbose_name=u'阵列型号',blank=True)
    sequence_number = models.CharField(max_length=100, verbose_name=u'阵列序列号',blank=True)
    room_number = models.CharField(max_length=100, verbose_name=u'阵列机房号', blank=True)
    rack_nembers = models.CharField(max_length=100, verbose_name=u'阵列机架号', blank=True)
    device_number = models.CharField(max_length=100, verbose_name=u'阵列设备号', blank=True)
    lun_number = models.CharField(max_length=100, verbose_name=u'LUN容量及个数', blank=True)
    gross = models.CharField(max_length=100, verbose_name=u'总容量', blank=True)
    array_connection = models.CharField(max_length=100, verbose_name=u'阵列连接情况', blank=True)
    optical = models.CharField(max_length=100, verbose_name=u'连接的光纤交换机', blank=True)
    test_machine = models.CharField(max_length=100, verbose_name=u'是否为测试机', blank=True)
    stop = models.CharField(max_length=100, verbose_name=u'能否随时停机', blank=True)
    firm = models.CharField(max_length=100, verbose_name=u'厂商/应用联系人/手机号', blank=True)
    mobile = models.CharField(max_length=100, verbose_name=u'移动负责人', blank=True)
    dept = models.CharField(max_length=100, verbose_name=u'所在部门', blank=True)
    bearer = models.CharField(max_length=100, verbose_name=u'承载应用', blank=True)
    maintenance_type = models.CharField(max_length=100, verbose_name=u'维保类型', blank=True)
    remarks = models.CharField(max_length=100, verbose_name=u'备注', blank=True)

    class Meta:
        verbose_name = u'主机清单'
        verbose_name_plural = verbose_name


class FaultDevice(models.Model):
    sn_id = models.ForeignKey('MesterDevice')
    sn_number = models.CharField(max_length=100,verbose_name=u'SN序列号')
    system = models.CharField(max_length=100,verbose_name=u'系统/硬件/数据库等')
    failure_level = models.CharField(max_length=100, verbose_name=u'故障级别')
    failt_description = models.CharField(max_length=100, verbose_name=u'故障描述')
    incidence = models.CharField(max_length=100, verbose_name=u'影响范围')
    resolvent = models.CharField(max_length=100, verbose_name=u'解决方法')
    finish_time = models.CharField(max_length=100, verbose_name=u'完成时间')
    down_time = models.CharField(max_length=100, verbose_name=u'故障日期')

    class Meta:
        verbose_name = u'设备过往故障'
        verbose_name_plural = verbose_name


class NetworkDevice(models.Model):
    sn_id = models.ForeignKey('MesterDevice')
    uid = models.IntegerField(verbose_name=u'序号',primary_key=True)
    system_name = models.CharField(verbose_name=u'系统名称', max_length=32)
    brand = models.CharField(verbose_name=u'品牌', max_length=20, null=True, blank=True)
    specific_device = models.CharField(verbose_name=u'设备的具体型号', max_length=32, null=True, blank=True)
    sn_number = models.CharField(verbose_name=u'sn序列号', max_length=128)
    ip = models.CharField(verbose_name=u'名称/IP',max_length=100,)
    password = models.CharField(verbose_name=u'登录密码', max_length=32)
    version = models.CharField(verbose_name=u'固件版本', max_length=128)
    login = models.CharField(verbose_name=u'登录方式', max_length=20)
    mobile_tag = models.CharField(verbose_name=u'移动资产标签', max_length=32)
    device_location = models.CharField(verbose_name=u'设备位置', max_length=128)
    type = models.CharField(verbose_name=u'维保类型', max_length=64,null=True, blank=True)

    class Meta:
        verbose_name = u'sn交换机清单'
        verbose_name_plural = verbose_name



class WarrantyDevice(models.Model):
    sn_id = models.ForeignKey('MesterDevice')
    uid = models.IntegerField(verbose_name=u'序号',primary_key=True)
    business = models.CharField(verbose_name=u'业务系统', max_length=32, null=True, blank=True)
    equi_type = models.CharField(verbose_name=u'设备类型', max_length=32, null=True, blank=True)
    brand = models.CharField(verbose_name=u'品牌', max_length=20, null=True, blank=True)
    device_no = models.CharField(verbose_name=u'设备号', max_length=32, null=True, blank=True)
    specific_device = models.CharField(verbose_name=u'设备型号', max_length=32, null=True, blank=True)
    sn_number = models.CharField(verbose_name=u'SN序列号', max_length=128)
    asset_coding = models.CharField(verbose_name=u'资产编码', max_length=32)
    ip = models.GenericIPAddressField(verbose_name=u'IP', blank=True, null=True)
    main_status = models.CharField(verbose_name=u'维保状态', max_length=32)
    city = models.CharField(verbose_name=u'所在城市', max_length=32)
    location = models.CharField(verbose_name=u'具体位置', max_length=128)
    floor = models.CharField(verbose_name=u'楼层', max_length=20)
    frame = models.CharField(verbose_name=u'机架', max_length=20)
    start_time = models.CharField(verbose_name=u'服务开始',max_length=20)
    end_time = models.CharField(verbose_name=u'服务期限',max_length=20)
    month = models.CharField(verbose_name=u'维保月份', max_length=20)
    mobile_person = models.CharField(verbose_name=u'移动负责人', max_length=32)
    service_type = models.CharField(verbose_name=u'服务类别', max_length=20)
    code = models.CharField(verbose_name=u'投资编码', max_length=20)
    project_name = models.CharField(verbose_name=u'项目名称', max_length=128)
    contract_title = models.CharField(verbose_name=u'合同名称', max_length=256)
    purchase_number = models.CharField(verbose_name=u'采购合同编号', max_length=20)
    price = models.CharField(verbose_name=u'采购价格', max_length=20)
    contacts = models.CharField(verbose_name=u'维保厂商联系人', max_length=32)
    turn_contacts = models.CharField(verbose_name=u'转维联系人', max_length=32)

    class Meta:
        verbose_name = u'维保清单'
        verbose_name_plural = verbose_name



class StorageDevice(models.Model):
    sn_id = models.ForeignKey('MesterDevice')
    own_system = models.CharField(verbose_name=u'所属系统+I10A1:I7G7A1:K7', max_length=32, null=True, blank=True)
    brand = models.CharField(verbose_name=u'品牌', max_length=20)
    storage_model = models.CharField(verbose_name=u'存储型号', max_length=20)
    configuration = models.CharField(verbose_name=u'存储配置', max_length=256)
    lun_configuration = models.CharField(verbose_name=u'lun详细配置', max_length=20)
    login_method = models.CharField(verbose_name=u'登入方法', max_length=128)
    account_password = models.CharField(verbose_name=u'帐号/密码', max_length=32)
    device_bit = models.CharField(verbose_name=u'设备位', max_length=20)
    sn_number = models.CharField(verbose_name=u'序列号', max_length=128)
    mobile_tag = models.CharField(verbose_name=u'移动资产标签', max_length=32)
    type = models.CharField(verbose_name=u'维保类型', max_length=128)

    class Meta:
        verbose_name = u'存储设备清单'
        verbose_name_plural = verbose_name

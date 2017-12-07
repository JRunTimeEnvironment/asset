#!/usr/bin/env python
# coding:utf-8
import xlrd
import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "asset.settings")
import django
django.setup()
def xlrd_(book,sheet,all_content):
    row_ = sheet.nrows
    col_ = sheet.ncols
    for i in range(1, row_):
        row_content = []
        for j in range(col_):
            ctype = sheet.cell(i, j).ctype
            value = sheet.cell(i, j).value
            if ctype == 3:
                date = xlrd.xldate.xldate_as_datetime(value, 0)
                if date.year > 1996:
                    value = '%s/%s/%s' % (date.year, date.month, date.day)
                else:
                    value = '%s:%s:%s' % (date.hour, date.minute, date.second)
            elif ctype == 2 and value:
                if value == int(value):
                    value = int(value)
                else:
                    pass
            elif ctype == 1 and value:
                value = value.replace('\n', ' ')
            # elif ctype == 4:
            #     value = True if value == 1 else False
            else:
                value = value
            row_content.append(value)
        all_content.append(tuple(row_content))

def getFaultDevice():
    from switch.models import FaultDevice,MesterDevice
    file_name = ('file/设备过往故障.xlsx')
    book = xlrd.open_workbook(file_name)
    sheet = book.sheet_by_index(0)
    all_content = []
    xlrd_(book, sheet, all_content)
    for i in range(len(all_content)):
        sn_id= MesterDevice.objects.create(uid=MesterDevice.objects.annotate().count(), name=all_content[i][1],sn_number=all_content[i][7])

        sn_number = all_content[i][7]
        system = all_content[i][1]
        failure_level = all_content[i][2]
        failt_description = all_content[i][3]
        incidence = all_content[i][4]
        resolvent = all_content[i][5]
        finish_time = all_content[i][6]
        down_time = all_content[i][0]
        FaultDevice.objects.create(sn_id=sn_id, system=system, failure_level=failure_level, failt_description=failt_description, incidence=incidence, resolvent=resolvent, finish_time=finish_time, down_time=down_time,sn_number=sn_number)
    print("all done")

def getHostDevice():
    from switch.models import HostDevice,MesterDevice
    file_name = ('file/主机清单.xlsx')
    book = xlrd.open_workbook(file_name)
    sheet = book.sheet_by_index(0)
    all_content = []
    xlrd_(book, sheet, all_content)
    for i in range(len(all_content)):
        uid = HostDevice.objects.annotate().count()
        state = all_content[i][1]
        brand = all_content[i][2]
        servername = all_content[i][3]
        computer_id = all_content[i][4]
        rack_number = all_content[i][5]
        device_bumber = all_content[i][6]
        sn_id = MesterDevice.objects.create(uid=MesterDevice.objects.annotate().count(), name=all_content[i][9], sn_number=all_content[i][7])
        sn_number = all_content[i][7]
        mobile_label = all_content[i][8]
        systematic_name = all_content[i][9]
        application = all_content[i][10]
        device_type = all_content[i][11]
        ld_name = all_content[i][12]
        zone = all_content[i][13]
        huost_name = all_content[i][14]
        system_ip = all_content[i][15]
        password = all_content[i][16]
        netword_id = all_content[i][17]
        login_mode = all_content[i][18]
        management_ip = all_content[i][19]
        management_password = all_content[i][20]
        nic_type = all_content[i][21]
        card_type = all_content[i][22]
        auxiliary = all_content[i][23]
        processor_type = all_content[i][24]
        processor_ghz = all_content[i][25]
        processors = all_content[i][26]
        nucleus = all_content[i][27]
        number = all_content[i][28]
        internal = all_content[i][29]
        menory = all_content[i][30]
        iou_type = all_content[i][31]
        os = all_content[i][32]
        kernel = all_content[i][33]
        hardware_level = all_content[i][34]
        version = all_content[i][35]
        cluster_type = all_content[i][36]
        cluster_version = all_content[i][37]
        array_model = all_content[i][38]
        sequence_number = all_content[i][39]
        room_number = all_content[i][40]
        rack_nembers = all_content[i][41]
        device_number = all_content[i][42]
        lun_number = all_content[i][43]
        gross = all_content[i][44]
        array_connection = all_content[i][45]
        optical = all_content[i][46]
        test_machine = all_content[i][47]
        stop = all_content[i][48]
        firm = all_content[i][49]
        mobile = all_content[i][50]
        dept = all_content[i][51]
        bearer = all_content[i][52]
        maintenance_type = all_content[i][53]
        remarks = all_content[i][54]
        HostDevice.objects.create(sn_id=sn_id,uid=uid,state = state,brand =brand,servername = servername,computer_id = computer_id,rack_number = rack_number,device_bumber = device_bumber,sn_number=sn_number,mobile_label = mobile_label,systematic_name = systematic_name,application = application,device_type = device_type,ld_name = ld_name,zone = zone,huost_name = huost_name,system_ip = system_ip,password = password,netword_id = netword_id,login_mode = login_mode,management_ip = management_ip,management_password = management_password,nic_type = nic_type,card_type = card_type,auxiliary = auxiliary,processor_type = processor_type,processor_ghz = processor_ghz,processors = processors,nucleus = nucleus,number = number,internal = internal,menory = menory,iou_type = iou_type,os = os,kernel = kernel,hardware_level = hardware_level,version = version,cluster_type = cluster_type,cluster_version = cluster_version,array_model = array_model,sequence_number = sequence_number,room_number =room_number,rack_nembers = rack_nembers,device_number = device_number,lun_number = lun_number,gross = gross,array_connection = array_connection,optical = optical,test_machine = test_machine, stop = stop,firm = firm,mobile = mobile,dept = dept,bearer = bearer,maintenance_type = maintenance_type,remarks = remarks)
    print("all done")

def getNetworkDevice():
    from switch.models import NetworkDevice, MesterDevice
    file_name = ('file/san交换机清单.xlsx')
    book = xlrd.open_workbook(file_name)
    sheet = book.sheet_by_index(0)
    all_content = []
    xlrd_(book, sheet, all_content)
    for i in range(len(all_content)):
        sn_id = MesterDevice.objects.create(uid=MesterDevice.objects.annotate().count(), name=all_content[i][0],sn_number=all_content[i][3])

        uid = NetworkDevice.objects.annotate().count()
        system_name = all_content[i][0]
        brand = all_content[i][1]
        specific_device = all_content[i][2]
        sn_number = all_content[i][3]
        ip = all_content[i][4]
        password = all_content[i][5]
        version = all_content[i][6]

        login = all_content[i][7]
        mobile_tag = all_content[i][8]
        device_location = all_content[i][9]
        type = all_content[i][10]

        NetworkDevice.objects.create(sn_id=sn_id,uid=uid,system_name=system_name,brand=brand,specific_device=specific_device,sn_number=sn_number,
                                     ip=ip,password=password,version=version,login=login,mobile_tag=mobile_tag,device_location=device_location,type=type)
    print("all done")


def getStorageDevice():
    from switch.models import StorageDevice,MesterDevice
    file_name = ('file/存储设备清单.xlsx')
    book = xlrd.open_workbook(file_name)
    sheet = book.sheet_by_index(0)
    all_content = []
    xlrd_(book, sheet, all_content)
    for i in range(len(all_content)):
        # MesterDevice.objects.create(uid=MesterDevice.objects.annotate().count(), name=all_content[i][0],sn_number=all_content[i][7])
        # sn_id = MesterDevice.objects.get(sn_number=all_content[i][8])
        sn_id = MesterDevice.objects.create(uid=MesterDevice.objects.annotate().count(), name=all_content[i][0],sn_number=all_content[i][7])

        # uid = all_content[i][7]
        own_system = all_content[i][0]
        brand = all_content[i][1]
        storage_model = all_content[i][2]
        configuration = all_content[i][3]
        lun_configuration = all_content[i][4]

        login_method = all_content[i][5]
        account_password = all_content[i][6]
        device_bit = all_content[i][7]
        sn_number = all_content[i][8]

        mobile_tag = all_content[i][9]
        type = all_content[i][10]


        StorageDevice.objects.create(sn_id=sn_id, own_system=own_system, brand=brand, storage_model=storage_model,
                                     configuration=configuration, lun_configuration=lun_configuration, login_method=login_method, account_password=account_password,
                                     device_bit=device_bit,sn_number=sn_number,mobile_tag=mobile_tag,type=type)
    print("all done")

def getWarrantyDevice():
    from switch.models import WarrantyDevice,MesterDevice
    file_name = ('file/维保清单.xlsx')
    book = xlrd.open_workbook(file_name)
    sheet = book.sheet_by_index(0)
    all_content = []
    xlrd_(book, sheet, all_content)
    for i in range(len(all_content)):
        sn_id = MesterDevice.objects.create(uid=MesterDevice.objects.annotate().count(), name=all_content[i][1], sn_number=all_content[i][6])

        uid = WarrantyDevice.objects.annotate().count()
        business = all_content[i][1]
        equi_type = all_content[i][2]
        brand = all_content[i][3]
        device_no = all_content[i][4]
        specific_device = all_content[i][5]
        sn_number = all_content[i][6]
        asset_coding = all_content[i][7]
        ip = all_content[i][8]
        main_status = all_content[i][9]
        city = all_content[i][10]
        location = all_content[i][11]
        floor = all_content[i][12]
        frame = all_content[i][13]
        start_time = all_content[i][14]
        end_time = all_content[i][15]
        month = all_content[i][16]
        mobile_person = all_content[i][17]
        service_type = all_content[i][18]
        code = all_content[i][19]
        project_name = all_content[i][20]
        contract_title = all_content[i][21]
        purchase_number = all_content[i][22]
        price = all_content[i][23]
        contacts = all_content[i][24]
        turn_contacts = all_content[i][25]

        WarrantyDevice.objects.create(sn_id=sn_id,uid=uid,business = business,equi_type =equi_type,brand = brand,
                                      device_no = device_no,specific_device = specific_device,sn_number = sn_number,
                                      asset_coding=asset_coding,ip = ip,main_status = main_status,city = city,
                                      location = location,floor = floor,frame = frame,start_time = start_time,end_time = end_time,
                                      month = month,mobile_person = mobile_person,service_type = service_type,code = code,
                                      project_name = project_name,contract_title = contract_title,purchase_number = purchase_number,
                                      price = price,contacts = contacts,turn_contacts = turn_contacts)

    print("all done")


# getFaultDevice()
# getHostDevice()
# getWarrantyDevice()
# getStorageDevice()
# getNetworkDevice()



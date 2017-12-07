from django.shortcuts import render , HttpResponse
from switch.models import FaultDevice,HostDevice,MesterDevice, WarrantyDevice, StorageDevice, NetworkDevice
from download import downloadMesterDevice
from django.http import StreamingHttpResponse
import os
# Create your views here.


def index(request):
    return render(request,'base.html',{'you':u'你好，欢迎你来用神马系统'})

def dates(request):
    # FaultDeviceList = FaultDevice.objects.all()
    HostDeviceList = HostDevice.objects.all()
    # MesterDeviceList = MesterDevice.objects.all()
    return  render(request,'dates.html',{ 'HostDeviceList' :HostDeviceList})


def downloadfroms(request):
    downloadMesterDevice()
    the_file_name = 'output_MesterDevice.xls'  # 显示在弹出对话框中的默认的下载文件名
    filename = 'file/output_MesterDevice.xls'  # 要下载的文件路径
    response = StreamingHttpResponse(readFile(filename))
    response['Content-Type'] = 'application/octet-stream'
    response['Content-Disposition'] = 'attachment;filename="{0}"'.format(the_file_name)

    return response

def readFile(filename,chunk_size=512):
    with open(filename,'rb') as f:
        while True:
            c=f.read(chunk_size)
            if c:
                yield c
            else:
                break

# def datase(request):
#     FaultDeviceList = FaultDevice.objects.all()
#     HostDeviceList = HostDevice.objects.all()
#     MesterDeviceList = MesterDevice.objects.all()
#     return render(request,'datase.html',{ 'FaultDeviceList' : FaultDeviceList,'HostDeviceList' :HostDeviceList,'MesterDeviceList':MesterDeviceList})

def shebei(request):
    FaultDeviceList = FaultDevice.objects.all()
    return render(request,'shebei.html',{'FaultDeviceList' : FaultDeviceList})

def forms(request):
    MesterDeviceList = MesterDevice.objects.all()
    return render(request,'forms.html',{'MesterDeviceList':MesterDeviceList})

def warrantyDevice(request):
    WarrantyDeviceList = WarrantyDevice.objects.all()
    return render(request,'warranty.html',{'WarrantyDeviceList':WarrantyDeviceList})


def Storage(request):
    StorageDeviceList = StorageDevice.objects.all()
    return render(request,'storage.html',{'StorageDeviceList':StorageDeviceList})

def Network(request):
    NetworkDeviceList = NetworkDevice.objects.all()
    return render(request,'network.html',{'NetworkDeviceList':NetworkDeviceList})


def update(request):
    return render(request,'upload.html')

def upload_file(request):

    fafafa = request.FILES.get('fafafa')
    file_name = fafafa.name
    path_name ='file/'

    path_ = os.path.join(path_name)
    # path_file = os.listdir(path_)
    img_path = os.path.join(path_name,file_name)

    with open(img_path,'wb') as f:
        for item in fafafa.chunks():
            f.write(item)
    import time
    time.sleep(5)
    from xlrd_read import getNetworkDevice,getStorageDevice,getFaultDevice,getWarrantyDevice,getHostDevice
    if file_name.startswith("san交换机清单"):
        getNetworkDevice()
        print('san交换机清单')
    if file_name.startswith("存储设备清单"):
        getStorageDevice()
        print('存储设备清单')
    if file_name.startswith("设备过往故障"):
        getFaultDevice()
        print('设备过往故障')
    if file_name.startswith("维保清单"):
        getWarrantyDevice()
        print('维保清单')
    if file_name.startswith("主机清单"):
        getHostDevice()
        print('主机清单')

    ret = {'code': True , 'data': img_path}
    import json
    return HttpResponse(json.dumps(ret))





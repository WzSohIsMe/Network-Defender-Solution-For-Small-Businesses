from django.shortcuts import render
import socket
import platform
import nmap
# from django.http import HttpResponse
# from django.template import loader
import json

# Create your views here.
def getLocalIp():
    #Retrive Private IPV4 Address
    s = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
    try:
        s.connect(('192.255.255.255',1))
        IP = s.getsockname()[0]
    except:
        IP='127.0.0.1'
    finally:
        s.close()
    return IP

def scanOpenedPorts():
    #Scan Targeted Opened Ports
    nm = nmap.PortScanner()
    # nm.scan(getLocalIp(),'0-137') #0-65535
    with open('scannedResults.json','w') as outputFile:
        outputFile.write(json.dumps(nm.scan(getLocalIp(),'0-65535'),indent=4))

    for host in nm.all_hosts():
        # scannedPorts = {"Port":[],"State":[],"Name":[]}
        scannedResult=[]
        # print('----------------------------------------------------')
        # print('Host : %s (%s)' % (host, nm[host].hostname()))
        # print('State : %s' % nm[host].state())
        for proto in nm[host].all_protocols():
            # print('----------')
            # print('Protocol : %s' % proto)

            lport = nm[host][proto].keys()
            sorted(lport)
            for port in lport:
                # print ('port : %s\tstate : %s' % (port, nm[host][proto][port]['state']))
                scannedResult.append({"Port":port,"State":(nm[host][proto][port]['state']),"Name":(nm[host][proto][port]['name'])})   

    

    return [scannedResult,len(scannedResult)]


def home(request):
    targetedIPAddress = getLocalIp()
    deviceOS = platform.system()
    return render(request, 'home.html',{'targetedIPAddress':targetedIPAddress,'deviceOS':deviceOS})


def result(request):
    
    if request.GET.get('ScanPorts') == "":
        scannedResults = scanOpenedPorts()
        ipAddress = getLocalIp()
        deviceOS = platform.system()
        return render(request,'result.html',{"scannedResults":scannedResults[0],"numPorts":range(scannedResults[1]),'ipAddress':ipAddress,'deviceOS':deviceOS,"totalOpenFilterPorts":scannedResults[1]})    


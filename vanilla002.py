#!/bin/python3.8
import nmap3

target = '192.168.15.8'

pynmap = nmap3.NmapScanTechniques()
vanilla = pynmap.nmap_tcp_scan(target)

for _info in vanilla[target]:
    print (_info['portid'],_info['protocol'],_info['state'],_info['reason'])


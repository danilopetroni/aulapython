#!/bin/python3.8
import nmap3
import json

pynmap = nmap3.NmapScanTechniques()

target = '192.168.15.8'

vanilla = pynmap.nmap_tcp_scan(target)
vanilla_json = json.dumps(vanilla, indent = 6)

print(vanilla_json)

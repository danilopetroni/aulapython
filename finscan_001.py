#!/bin/python3.8
import nmap3
from datetime import datetime
from termcolor import colored

msg1 = colored('+','green', attrs=['blink'])
msg2 = colored('*','red', attrs=['blink'])
msg3 = colored('#','yellow', attrs=['blink'])
nmap_start = datetime.now()

target = '192.168.15.8'

pynmap = nmap3.NmapScanTechniques()
finscan = pynmap.nmap_fin_scan(target)

print('Porta:',finscan['ports']['portid'])
print('Protocolo...:',finscan['ports']['protocol'])
print('Serviço:',finscan['ports']['service']['name'])
print('Protocol:',finscan['ports']['state']['state'])



nmap_end = datetime.now()
nmap_time = nmap_end - nmap_start
print ('[' + msg3 + ']','Tempo de execução', nmap_time)

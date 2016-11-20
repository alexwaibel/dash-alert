from scapy.all import *
import requests
import time

def arp_display(pkt):
    if pkt[ARP].op == 1:
        if pkt[ARP].hwsrc == 'ac:63:be:e2:53:26':
            start=time.time()
            requests.get("http://localhost:8080/hello")
            current = time.time()
            while current- start < 60:
                current=time.time()



while True:
    print(sniff(prn=arp_display, filter="arp", store=0, count=10))

from scapy.all import *
import requests

def arp_display(pkt):
    if pkt[ARP].op == 1:
        if pkt[ARP].hwsrc == 'ac:63:be:e2:53:26':
            requests.get("http://localhost:8080/hello")


while True:
    print(sniff(prn=arp_display, filter="arp", store=0, count=10))

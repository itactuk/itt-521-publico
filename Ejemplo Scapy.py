from scapy.all import *

def imprimir(x):
    print("adda")
    return x.sprintf("{IP:%IP.src% -> %IP.dst%\n}{Raw:%Raw.load%\n}")

pkts = sniff(prn=imprimir)

import streamlit as st
from scapy.all import *

def packet_handler(packet):
    if IP in packet:
        src_ip = packet[IP].src
        dst_ip = packet[IP].dst
        protocol = packet[IP].proto
        packet_len = len(packet)
        
        st.write("Source IP:", src_ip)
        st.write("Destination IP:", dst_ip)
        st.write("Protocol:", protocol)
        st.write("Packet Length:", packet_len)
        st.write("-------------------------")

def start_sniffing(interface):
    st.write("Starting packet capture on interface", interface)
    sniff(iface=interface, prn=packet_handler)

def main():
    st.title("Network Protocol Analyzer")
    interface = st.text_input("Enter the interface to capture packets (e.g., eth0):")
    
    if st.button("Start Capture"):
        start_sniffing(interface)

if __name__ == "__main__":
    main()

import streamlit as st
import psutil
import speedtest
def get_interface_details(interface):
    try:
        addresses = psutil.net_if_addrs()
        if interface in addresses:
            ip_address = addresses[interface][0].address
            netmask = addresses[interface][0].netmask
            details = f"Interface: {interface}\nIP Address: {ip_address}\nNetmask: {netmask}"
            return details
    except:
        return interface

def get_available_interfaces():
    interfaces = []
    for interface, addresses in psutil.net_if_addrs().items():
        if interface != "lo":
            interface_details = get_interface_details(interface)
            interfaces.append(interface_details)
    return interfaces

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

def get_speed_test_results():
    st.write("Running speed test...")
    speed_test = speedtest.Speedtest()
    download_speed = speed_test.download() / 1024 / 1024
    upload_speed = speed_test.upload() / 1024 / 1024
    st.write("Download Speed:", round(download_speed, 2), "Mbps")
    st.write("Upload Speed:", round(upload_speed, 2), "Mbps")

def main():
    st.set_page_config(page_title="Network Analyzer (Protocol & Speed Test)")
    st.title("Network Analyzer (Protocol & Speed Test)")
    # Add custom CSS style for the page background
    page_bg_img = '''
    <style>
    .stApp {
        background-image: url("https://images.hdqwalls.com/download/purple-abstract-hd-4k-hk-1920x1080.jpg");
        background-size: cover;
    }
    </style>
    '''
    
    st.markdown(page_bg_img, unsafe_allow_html=True)
    interfaces = get_available_interfaces()
    if not interfaces:
        st.error("No network interfaces found.")
        return

    selected_option = st.selectbox("Select an option", ("Packet Capture", "Speed Test"))

    if selected_option == "Packet Capture":
        selected_interface = st.selectbox("Select an interface", interfaces, format_func=lambda x: x.replace('\n', ', '))

        if st.button("Start Capture"):
            interface_name = selected_interface.split('\n')[0].split(": ")[1]  # Extract the interface name from the selected option
            start_sniffing(interface_name)

    elif selected_option == "Speed Test":
        if st.button("Run Speed Test"):
            get_speed_test_results()

if __name__ == "__main__":
    main()

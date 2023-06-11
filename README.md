# Network Analyzer and Speed Test Repository

This repository contains a network analyzer and speed test application built using Python and Streamlit. The application provides two main functionalities: packet capture for network analysis and speed testing to measure the download and upload speeds of your network connection.

You can access the live demo of the application [here](https://deepankarvarma-nework-protocol-analyser-using-python-app-sjtqm7.streamlit.app/).

## Features

1. **Packet Capture**: Analyze network packets flowing through your chosen interface. View source and destination IP addresses, protocol, and packet length.
2. **Speed Test**: Measure the download and upload speeds of your network connection using Speedtest.net.

## Prerequisites

Before running the application, make sure you have the following dependencies installed:

- Streamlit: `pip install streamlit`
- Psutil: `pip install psutil`
- Speedtest-cli: `pip install speedtest-cli`

## How to Run

1. Clone this repository to your local machine: `git clone https://github.com/deepankarvarma/network-analyzer.git`
2. Install the required dependencies mentioned above.
3. Navigate to the project directory: `cd network-analyzer`
4. Run the application: `streamlit run app.py`
5. Access the application in your web browser at `http://localhost:8501`.

## Usage

Once you launch the application, you will see a web interface with two options:

1. **Packet Capture**: Select this option to capture and analyze network packets.
   - Choose an interface from the dropdown menu.
   - Click the "Start Capture" button to begin capturing packets.
   - The captured packet information will be displayed on the screen, including the source IP, destination IP, protocol, and packet length.

2. **Speed Test**: Select this option to measure your network's download and upload speeds.
   - Click the "Run Speed Test" button.
   - The application will perform a speed test using Speedtest.net and display the download and upload speeds in Mbps.


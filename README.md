# Network Security Scanner

This is a project which I have done in VCET HACKATHON. It was my problem statement which stated following things:
1. Scan automatically after sepcific time interval (In short a scheduler for some tasks).
2. Identify open ports.
3. Identify unnecessary services and eliminate if not required.
4. And any other network mapping or serurity feature which we can add

<hr>

The Network Security Scanner is a Python application designed to enhance your network security by identifying open ports on your internet-facing IP, scanning your local network for active devices and their IP addresses, and providing information about services running on those devices. This tool also enables you to schedule port scans on target IPs, manage services running on your device, and terminate unfamiliar services. Multi-threading is implemented using the PyQt5 framework to ensure efficient parallel task execution.

## Features

- **Internet IP Port Scanning:** Identify open ports on your internet-facing IP address to assess potential vulnerabilities.

- **Local Network Device Scanning:** Scan your local network to detect active devices and their corresponding IP addresses.

- **Service Information:** View a list of services running on your device, along with the ability to terminate unfamiliar services.

- **Port and Service Details:** Access detailed information about the open ports and services associated with active devices.

- **Scheduled Port Scans:** Schedule automated port scans on target IPs to periodically assess their security.

## Project Structure

The project is organized into several folders:

- **Final:** Contains the refined and production-ready code, including two sub-folders:
  - **UI:** Contains the PyQt5 UI code for the application's graphical interface.
  - **ThreadController:** Manages the creation and destruction of threads for parallel task execution.

- **Temp:** Contains trial and error code, demo scripts, and experimental code that has been refined and added to the 'Final' folder.

## Usage

1. Clone the repository to your local machine.
2. Navigate to the 'Final' folder to access the production-ready code.
3. Execute the main Python script to launch the application.
4. Use the different tabs and features to perform network security tasks:
   - **Internet IP Scan:** Identify open ports on your internet-facing IP.
   - **Local Network Scan:** Detect active devices and their IP addresses on your local network.
   - **Service Management:** View and terminate services running on your device.
   - **Scheduled Scans:** Schedule port scans on target IPs at specified intervals.

<!-- ## Screenshots

Screenshots of the application's interface and features can be found in the 'screenshots' directory within the 'Final' folder. These screenshots provide visual guidance on how to use the different features of the Network Security Scanner. -->

## Contributions

Contributions to this project are welcome. If you find any bugs, want to add new features, or have suggestions for improvement, feel free to submit issues or pull requests to the project's repository.

## Disclaimer

This application is intended for educational and informational purposes only. Use it responsibly and ensure you have proper authorization before performing any scanning or analysis on external networks or devices.

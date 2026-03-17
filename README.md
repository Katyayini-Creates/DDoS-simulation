# DDoS Attack Simulation and Analysis using Wireshark

## Overview

This project demonstrates the simulation of basic DDoS attack patterns in a controlled environment using Python. The generated network traffic is analyzed using Wireshark to study packet behavior and identify attack characteristics.

---

## Objective

* Simulate DDoS-like traffic safely on localhost
* Capture packets using Wireshark
* Analyze HTTP Flood and UDP Flood patterns

---

## Technologies Used

* Python
* Wireshark
* Npcap (Loopback Adapter)

---

## Experimental Setup

* Server hosted on **127.0.0.1 (localhost)** at **port 8080**
* Python scripts act as traffic generators
* Wireshark captures packets on loopback interface

---
## Use of Localhost in Simulation

### What is Localhost?

Localhost refers to the loopback network interface of a computer, typically represented by the IP address **127.0.0.1**. It allows a system to communicate with itself without using any external network.

---

### Why Localhost is Used

Localhost was used in this experiment for the following reasons:

* **Safety**: Prevents any unintended impact on external systems or networks.
* **Controlled Environment**: Ensures that all traffic remains within a single system.
* **Legal Compliance**: Avoids performing real attacks on live servers.
* **Ease of Testing**: Eliminates dependency on network connectivity.

---

### How Localhost is Used in This Project

In this project:

* A local HTTP server was hosted using:

  ```bash
  python -m http.server 8080
  ```

* The server listens on:

  * IP Address: **127.0.0.1**
  * Port: **8080**

* The Python scripts (HTTP and UDP flood) send traffic to:

  ```plaintext
  127.0.0.1:8080
  ```

* Wireshark captures this traffic using the **loopback adapter**, allowing real-time analysis.

---

## Attack Simulations

### 1. HTTP Flood Attack

* Sends multiple HTTP GET requests to the server
* Observed as repeated request-response cycles

### 2. UDP Flood Attack

* Sends continuous UDP packets to the target
* Observed as high-volume UDP traffic with ICMP responses

---

## Wireshark Analysis

* High packet rate observed
* Traffic spike in IO Graph
* Protocol dominance (HTTP/UDP)
* Repeated source and destination (127.0.0.1)

---

## Project Structure

```
ddos-simulation/
│── http_flood.py
│── udp_flood.py
│── requirements.txt
│── README.md
│── screenshots/
```

---

## How to Run

### Step 1: Start Server

```bash
python -m http.server 8080
```

### Step 2: Run HTTP Flood

```bash
python http_flood.py
```

### Step 3: Run UDP Flood

```bash
python udp_flood.py
```

### Step 4: Capture using Wireshark

* Select **Loopback Adapter**
* Apply filters:

  * `http`
  * `udp`

---

## Working of the System

### Overall Workflow

The system operates in three main components:

1. Traffic Generator (Python Scripts)
2. Target Server (Local HTTP Server)
3. Packet Analyzer (Wireshark)

---

### Step-by-Step Working

#### Step 1: Server Initialization

A local server is started using Python, which listens for incoming requests on port 8080.

---

#### Step 2: Traffic Generation
Two types of traffic are generated:

* **HTTP Flood**:

  * Sends repeated HTTP GET requests
  * Uses TCP protocol
  * Creates request-response cycles

* **UDP Flood**:

  * Sends continuous UDP packets
  * No connection establishment
  * Generates high packet volume

---

#### **Step 3: Packet Transmission**

* The packets are transmitted internally within the system.
* Source and destination both remain:

  ```plaintext
  127.0.0.1 → 127.0.0.1
  ```

---

#### **Step 4: Packet Capture**
Wireshark captures packets via the loopback interface and records:

* Source & destination IP
* Protocol type (HTTP, TCP, UDP, ICMP)
* Packet size and timing

---

#### **Step 5: Analysis**

Using Wireshark tools:

* **Filters** identify specific traffic (`http`, `udp`)
* **IO Graph** shows traffic spikes
* **Protocol Hierarchy** shows protocol distribution

---

#### **Step 6: Observed Behavior**

* High packet rate during both attacks
* Repeated requests in HTTP Flood
* Continuous packets in UDP Flood
* ICMP errors in UDP Flood (port unreachable)

---

### Summary of Working
The system simulates attack-like traffic in a safe, isolated environment. The generated packets mimic real DDoS attack patterns, and Wireshark provides detailed insights into network behavior, enabling effective analysis.

---


## Disclaimer

This project is for educational purposes only. All simulations are performed on localhost to avoid impacting real systems.

---

## Author

Katyayini Singh


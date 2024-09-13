# Week 1

## Introduction to the Web (00:27:11)

### Packet Switched Network

Packet-switched networks are the backbone of modern digital communication, including the internet.

**Data Segmentation**

**Packetization** When you send data over a packet-switched network, it is broken down into smaller chunks called packets. Each packet contains a portion of the data, plus metadata such as the destination address, source address, and sequence number

**Routing**

Each packet is routed independently through the network. The routing decision is made based on the packet’s destination address. The path a packet takes can vary, which means packets from the same message *might arrive out of order*.

**Network Nodes**

**Switches and Routers:** The network is made up of various nodes like routers and switches. Routers are used in wide area networks (WANs) and handle the routing of packets between different networks. Switches are used in local area networks (LANs) and facilitate communication within a network segment.
**Forwarding:** Each node examines the packet’s destination address and decides the next hop for the packet. This process continues until the packet reaches its final destination.

**Reassembly**

*Reassembly:* At the destination, packets are reassembled into the original message based on their sequence numbers. If some packets are lost or corrupted, the system can request retransmission of the affected packets.

**Error Handling and Quality of Service**

**Error Checking:** Packets include checksums or other error-detection codes to verify their integrity. If a packet is corrupted, it can be retransmitted.
**Quality of Service (QoS):** Some packet-switched networks implement QoS mechanisms to prioritize certain types of traffic (e.g., voice or video) to ensure they meet performance requirements.

**Advantages of Packet Switching**

**Efficiency:** Network resources are used more efficiently because packets can be routed along the least congested paths and network links are shared among many users.
**Robustness:** If a path becomes congested or fails, packets can be rerouted, making the network resilient to failures.
Scalability: It scales well with the number of users and the amount of data being transmitted.

**Comparison with Circuit Switching**

Packet switching contrasts with circuit switching (used in traditional telephone networks), where a dedicated communication path is established between the sender and receiver for the duration of the call. Packet switching, on the other hand, dynamically allocates resources and shares them among multiple users, making it more adaptable to varying traffic loads.

In summary, packet-switched networks break data into packets, route them independently, and reassemble them at the destination, offering efficient, flexible, and robust communication.


## Network Protocols

A network protocol is a set of rules and conventions that governs how data is transmitted, received, and processed across a network. It defines the format, timing, sequencing, and error-checking mechanisms for data exchanges between devices. In essence, network protocols ensure that different devices and applications can communicate with each other in a consistent and reliable manner.

### Key Components of a Network Protocol
1. Syntax: Defines the structure or format of the data being transmitted. This includes the arrangement of data in packets or frames, as well as headers and footers that provide metadata.
2. Semantics: Specifies the meaning of each part of the communication. It describes what actions should be taken based on the data received, such as how to handle errors or interpret commands.
3. Timing: Involves rules for when data should be sent and received. This includes synchronization of data flow, handling delays, and managing retransmissions in case of lost or corrupted packets.
4. Error Handling: Includes mechanisms for detecting and correcting errors in data transmission. This ensures data integrity and reliability.
5. State Management: Defines how the state of the connection or session is managed, including how devices keep track of ongoing interactions and transitions between different states.

Examples of Protocols TCP, IP, DECNET, HTTP, FTP, POP3, SMTP


**Importance of Network Protocols**

- **Interoperability:** Protocols enable devices from different manufacturers and with different designs to communicate effectively.
- **Reliability:** They ensure that data is transmitted accurately and that errors are handled appropriately.
- **Efficiency:** Protocols optimize the use of network resources and manage data flow to prevent congestion and bottlenecks.

### Network Layers

The **OSI model** (Open Systems Interconnection model) is a conceptual framework used to understand and standardize the functions of a telecommunication or computing system. It divides the process of network communication into seven distinct layers, each with specific responsibilities. This layered approach helps in designing and troubleshooting networks by isolating different aspects of communication.

Here’s a detailed look at each layer of the OSI model, starting from the top:

#### 1. **Application Layer (Layer 7)**
   - **Function:** The top layer where network applications and services operate. It provides network services directly to end-users or applications. This layer is responsible for network-related functions such as email, file transfers, and web browsing.
   - **Examples:** HTTP (Hypertext Transfer Protocol), FTP (File Transfer Protocol), SMTP (Simple Mail Transfer Protocol).

#### 2. **Presentation Layer (Layer 6)**
   - **Function:** Handles data translation, encryption, and compression. It ensures that the data is in a readable format for the application layer and translates data from application-level formats to network formats and vice versa.
   - **Examples:** Encryption protocols like SSL/TLS, data format conversions like JPEG, GIF, or ASCII.

#### 3. **Session Layer (Layer 5)**
   - **Function:** Manages sessions or connections between applications. It establishes, maintains, and terminates communication sessions between applications. This layer is responsible for session recovery and synchronization.
   - **Examples:** APIs for session management, NetBIOS, RPC (Remote Procedure Call).

#### 4. **Transport Layer (Layer 4)**
   - **Function:** Provides reliable or best-effort delivery of data between systems and handles error detection, correction, and flow control. It ensures complete data transfer by managing data segmentation and reassembly.
   - **Examples:** TCP (Transmission Control Protocol) for reliable connections, UDP (User Datagram Protocol) for connectionless communication.

#### 5. **Network Layer (Layer 3)**
   - **Function:** Handles routing and forwarding of data packets between devices across different networks. It is responsible for logical addressing and path selection.
   - **Examples:** IP (Internet Protocol), ICMP (Internet Control Message Protocol), routers.

#### 6. **Data Link Layer (Layer 2)**
   - **Function:** Provides node-to-node data transfer and handles error detection and correction at the physical layer. It packages data into frames and manages physical addressing (MAC addresses).
   - **Examples:** Ethernet, PPP (Point-to-Point Protocol), switches.

#### 7. **Physical Layer (Layer 1)**
   - **Function:** Deals with the physical transmission of data over a medium. It defines the hardware elements and electrical/optical signals used for data transmission.
   - **Examples:** Cables, switches, and the physical aspects of network interfaces.

##### How the OSI Model Works

- **Layer Interaction:** Data communication starts at the application layer on the sender's side, moving down the layers, where each layer adds its own headers or trailers. On the receiver's side, data moves up the layers, where headers or trailers are stripped away, and the data is processed at each layer according to its function.
  
- **Encapsulation and Decapsulation:** At each layer, data is encapsulated into a format suitable for the layer below it. On the receiving side, each layer decapsulates the data by removing the headers or trailers added by the corresponding layer on the sending side.

##### Importance of the OSI Model

1. **Standardization:** Provides a common framework and terminology for understanding and designing network protocols and systems.
2. **Troubleshooting:** Helps in isolating problems by allowing a focus on specific layers of the network communication process.
3. **Interoperability:** Promotes compatibility and interoperability between products and technologies from different vendors.

While the OSI model is a theoretical construct and the TCP/IP model is more commonly used in practical networking, the OSI model remains an essential reference for understanding network architecture and functions.

#### Inter Level Network (Internet)

The **Internet Protocol (IP)** is a fundamental protocol used for addressing and routing packets of data across networks, including the internet. It ensures that data is delivered from the source to the destination across potentially complex networks.

#### Key Points of IP:

1. **Addressing:** IP assigns unique addresses (IP addresses) to each device on a network, ensuring that data packets are sent to the correct destination.

2. **Routing:** IP determines the best path for packets to travel from the source to the destination, potentially passing through multiple intermediate devices (routers).

3. **Packetization:** IP breaks down data into packets, each of which contains a portion of the data, as well as addressing information.

4. **Version:** There are two versions of IP:
   - **IPv4 (Internet Protocol version 4):** Uses 32-bit addresses, allowing for about 4.3 billion unique addresses.
   - **IPv6 (Internet Protocol version 6):** Uses 128-bit addresses, providing a vastly larger address space to accommodate the growing number of devices.

In summary, IP is crucial for the operation of the internet, handling addressing, routing, and packetization to ensure data reaches its intended destination across diverse and interconnected networks. No matter what kind of hardware or network you use, please follow IPV6 or IPv4 to be connected into the internet

**Transmission Control Protocol (TCP)** is a core protocol in the Internet protocol suite that ensures reliable, ordered, and error-checked delivery of data between applications over a network. It establishes a connection between sender and receiver, manages data segmentation and reassembly, and handles error correction and retransmission to guarantee that data is transmitted accurately and completely.
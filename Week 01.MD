# Week 1

*Prof. Nitin Chandrachoodan*  
*Department of EE, IIT Madras*  

## Lecture 1: Introduction to the Web (00:27:11)

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


### Network Protocols

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


Brief overview of IP Addresses:

1. **Early Beginnings (1970s):**
   - **1973:** Vint Cerf and Bob Kahn introduced the concept of packet switching and the Transmission Control Protocol (TCP) as part of the ARPANET project, a precursor to the internet. They developed the idea of addressing packets of data to ensure they reached their destination.

2. **IPv4 Introduction (1981):**
   - **1981:** The Internet Engineering Task Force (IETF) standardized IPv4 in RFC 791. IPv4 uses a 32-bit address space, allowing for about 4.3 billion unique addresses. This version became the foundation for addressing on the internet.

3. **Expansion and Limitations (1990s-2000s):**
   - **1990s:** The rapid growth of the internet began to strain the IPv4 address space. Techniques like Network Address Translation (NAT) were developed to alleviate some of the pressure by allowing multiple devices to share a single public IP address.

4. **IPv6 Introduction (1998):**
   - **1998:** To address the limitations of IPv4, IPv6 was introduced. IPv6 uses a 128-bit address space, offering a virtually limitless number of unique addresses (about 340 undecillion). This upgrade aimed to accommodate the expanding number of internet-connected devices.

5. **Gradual Transition (2000s-Present):**
   - **2000s:** The transition to IPv6 has been gradual. Many networks and organizations began implementing IPv6 to future-proof their infrastructure and handle growing demand.
   - **2020s:** Adoption of IPv6 has been increasing, but IPv4 is still widely used due to its established presence and the complexity involved in switching entirely to IPv6.

**Octet** is a 8 bit byte. Infact Octet is a noun - a group of eight people or things.

The octet is used in representations of Internet Protocol computer network addresses.An IPv4 address consists of four octets, usually displayed individually as a series of decimal values ranging from 0 to 255, each separated by a full stop (dot). Using octets with all eight bits set, the representation of the highest-numbered IPv4 address is 255.255.255.255.

- IPv4 - 4 Octets
- IPv6 - 16 Octets like `2001:0db8:0000:0000:0123:4567:89ab:cdef`
- A variable-length sequence of octets, as in Abstract Syntax Notation One (ASN.1), is referred to as an octet string.

#### Domain Names (1985)

The Domain Name System (DNS) has a crucial role in the functionality of the internet, converting human-readable domain names into IP addresses. Here's a brief history of its development:

1. **Early Networking (1960s-1970s):**
   - **1960s:** Early networks like ARPANET used hosts.txt, a simple text file listing hostnames and their corresponding IP addresses. This file was manually updated and distributed to all ARPANET nodes.

2. **DNS Invention (1980s):**
   - **1983:** The Domain Name System was introduced by Paul Mockapetris and his colleagues. The system was detailed in RFC 882 and RFC 883. DNS replaced the hosts.txt file with a hierarchical and decentralized system, which made managing the growing number of hosts more scalable and efficient.

3. **DNS Structure and Delegation:**
   - The DNS hierarchy consists of several levels: root, top-level domains (TLDs), second-level domains, and subdomains. This hierarchical system allows for efficient management and resolution of domain names.
   - The root servers, which are crucial for the DNS infrastructure, were initially operated by various organizations. Over time, the number and distribution of these servers were optimized to improve reliability and speed.

4. **Domain Registration and Management (1990s):**
   - **1991:** The Internet Assigned Numbers Authority (IANA) began managing domain name registrations. The introduction of the Internet Corporation for Assigned Names and Numbers (ICANN) in 1998 formalized and expanded this role, overseeing domain name policies and operations.

5. **DNS Security (2000s-Present):**
   - **2000s:** The DNS Security Extensions (DNSSEC) were developed to protect against certain types of attacks, such as cache poisoning. DNSSEC adds cryptographic signatures to DNS data to ensure its authenticity.
   - **2010s:** The introduction of DNS over HTTPS (DoH) and DNS over TLS (DoT) aimed to enhance privacy and security by encrypting DNS queries and responses, protecting them from eavesdropping and tampering.

6. **Ongoing Developments:**
   - **2020s:** The DNS continues to evolve with advancements in security, privacy, and efficiency. Efforts to address issues like domain abuse, phishing, and the need for better global DNS performance are ongoing.
#### Hypertext (early foundation of WWW)

1. **Early Concepts (1960s):**
   - **1965:** Ted Nelson coined the term “hypertext” and introduced the idea in his work on “Xanadu,” a conceptual hypertext system that aimed to create a universal, interconnected information network. Though Xanadu was never fully realized, Nelson’s ideas influenced later developments.

2. **Theoretical Foundations (1960s-1970s):**
   - **1963:** Vannevar Bush's essay "As We May Think" proposed the concept of a “memex,” a hypothetical device that would allow users to access and link information in a non-linear way. This vision laid the groundwork for hypertext concepts.
   - **1968:** Douglas Engelbart demonstrated his NLS (oN-Line System) at the “Mother of All Demos,” showcasing concepts like hypertext linking, which were integral to future hypertext systems.

3. **Early Implementations (1980s):**
   - **1987:** The term "hypertext" gained more prominence with the publication of “Hypertext and Hypermedia” by George P. Landow. This period saw the development of early hypertext systems and applications.

4. **World Wide Web and HTML (1990s):**
   - **1991:** Tim Berners-Lee, a computer scientist at CERN, proposed the World Wide Web. His idea was to create a system for sharing and accessing information using hypertext. He developed HTML (HyperText Markup Language), HTTP (HyperText Transfer Protocol), and the first web browser, Mosaic, which made the web accessible to the public.
   - **1993:** The release of the Mosaic web browser brought hypertext to a broader audience, enabling users to navigate the web with clickable links and multimedia content.

5. **Modern Hypertext (2000s-Present):**
   - **2000s:** The development of web technologies continued with the introduction of XHTML, XML, and advanced JavaScript frameworks, which enhanced the capabilities of hypertext and interactivity on the web.
   - **2010s:** The rise of web standards like HTML5 and CSS3 further improved the functionality and design of web content. Hypertext has become more sophisticated with dynamic web applications, integrating multimedia, and interactive elements.

**CGI - Common Gateway Interface.** Basically a console program (executed by web server) that writes to STDIO and the web server retrieves the HTML output from STDIO and sends it back to the browser in the open HTTP/s socket connection.

#### Web 2.0
Web 2.0 represents a significant shift in the use and functionality of the internet, characterized by increased user interaction, collaboration, and the growth of social media.

1. **Conceptual Beginnings (1990s):**
   - **1999:** The term “Web 2.0” was coined by Darcy DiNucci in her article “Fragmented Future,” where she discussed the evolving nature of the web. However, the term gained wider recognition and definition in the early 2000s.

2. **Defining Web 2.0 (2000s):**
   - **2001:** Tim O'Reilly and Dale Dougherty of O'Reilly Media popularized the term “Web 2.0” during the first Web 2.0 Conference. They defined Web 2.0 as a new era of web development characterized by user-generated content, social networking, and the shift from static to dynamic web applications.
   - **2004:** The Web 2.0 Summit, organized by O'Reilly Media and MediaLive International, further solidified the concept. The summit highlighted the changes in how people interacted with the web, focusing on collaborative and interactive technologies.

3. **Key Technologies and Trends (2000s):**
   - **Social Media:** The rise of platforms like Facebook (2004), Twitter (2006), and YouTube (2005) transformed how users interacted online, emphasizing user-generated content and social networking.
   - **Ajax and Dynamic Content:** The development of Ajax (Asynchronous JavaScript and XML) allowed web pages to update content dynamically without requiring a full page reload, enhancing the interactivity and responsiveness of web applications.
   - **Rich User Interfaces:** Technologies like Flash and later HTML5, CSS3, and JavaScript frameworks (e.g., jQuery) enabled the creation of more engaging and interactive user experiences.

4. **Expansion and Evolution (2010s-Present):**
   - **Mobile and Responsive Design:** The proliferation of smartphones and tablets led to the adoption of responsive web design techniques to ensure websites function well across various devices.
   - **Cloud Computing and APIs:** Web 2.0 saw the rise of cloud-based services and the use of APIs (Application Programming Interfaces) to enable seamless integration and data exchange between applications.
   - **User-Centric Models:** Platforms and services increasingly focus on user-generated content, personalization, and community-driven features. Examples include platforms like Instagram, TikTok, and various collaborative tools like Slack and Trello.

5. **Beyond Web 2.0 (Current Trends):**
   - **Web 3.0 and the Decentralized Web:** While Web 2.0 marked a shift toward interactive and collaborative internet usage, discussions around Web 3.0 focus on decentralization, blockchain technology, and a more semantic web that aims to enhance data interoperability and user control.

In summary, Web 2.0 represents a transformative phase in internet history, characterized by dynamic content, social connectivity, and user participation. It laid the groundwork for the interactive, user-driven web experiences that have become central to modern online activity.

## Lecture 2: How does the Web Work (00:09:30)

### Web Server
   A web server is a software application or hardware device that delivers web pages and other content over the internet to users’ web browsers. It processes requests from clients (typically web browsers), retrieves the requested content, and sends it back to the client. Here’s a more detailed breakdown:

#### Key Functions of a Web Server:

1. **Handling HTTP Requests:**
   - The web server listens for incoming requests on port 80 (for HTTP) or port 443 (for HTTPS) from clients. When a request is received, the server processes it based on the HTTP protocol.

2. **Serving Web Content:**
   - The server fetches the requested web content, which can be static files (like HTML, CSS, and JavaScript files) or dynamic content generated by server-side scripts (such as PHP, Python, or Node.js).

3. **Response Handling:**
   - After processing the request, the web server sends back a response to the client. This response includes a status code (indicating success or failure) and the requested content.

4. **Static vs. Dynamic Content:**
   - **Static Content:** Directly served files (e.g., HTML pages, images) stored on the server.
   - **Dynamic Content:** Generated on-the-fly based on server-side processing, such as executing scripts or querying databases.
#### Examples of Web Servers:

- **Apache HTTP Server:** One of the most widely used web servers, known for its flexibility and extensive features.
- **Nginx:** Known for its high performance and efficiency, often used as a reverse proxy server as well as a web server.
- **Microsoft Internet Information Services (IIS):** A web server for Windows Server environments, integrated with other Microsoft technologies.
- **LiteSpeed:** A commercial web server known for its speed and security features.
#### Key Components of a Web Server:

1. **HTTP Server Software:** The core application that handles requests and responses. Examples include Apache, Nginx, and IIS.
2. **Server Hardware or Virtual Instance:** The physical or virtual machine where the web server software runs. This can range from a dedicated server to a cloud-based virtual machine.
3. **Configuration Files:** Files that dictate how the web server should operate, including settings for security, performance, and content handling.
#### Additional Features:

- **Security:** Web servers often include features to enhance security, such as SSL/TLS for encrypted connections, access control mechanisms, and firewall settings.
- **Logging:** Web servers typically log details about requests and errors, which is useful for monitoring, debugging, and analyzing traffic.

In essence, a web server plays a central role in the functioning of the web by delivering content to users and managing interactions between clients and servers.

#### Ports

In networking, **ports** are logical endpoints used to identify specific processes or services on a device. They work with IP addresses to direct data to the correct application or service. Here’s a concise explanation:

- **Port Numbers:** Each port is identified by a number, ranging from 0 to 65,535. Ports are categorized as:
  - **Well-Known Ports (0-1023):** Reserved for common protocols (e.g., HTTP on port 80, HTTPS on port 443).
    - In most operating systems the application has to be launched with administrator rights to listen on these ports
    - Only one application can listen on a port on a specific IP.
    - Port is a 16 bit unsigned integer. So you have $2^{16}$ or $65536$ ports
  - **Registered Ports (1024-49151):** Used by applications and services not covered by well-known ports.
  - **Dynamic/Private Ports (49152-65535):** Used for ephemeral or temporary connections.

- **Purpose:** Ports allow multiple services to run simultaneously on a single IP address by differentiating traffic intended for different applications.

- **Port Uniqueness:** Each port on a given IP address is associated with a single process or application. The port number helps the operating system direct incoming network traffic to the correct application. If two applications tried to listen on the same port, the operating system would be unable to distinguish which application should handle the incoming traffic.

- **Binding Conflicts:** When an application binds to a port, it essentially locks that port for its exclusive use. If another application attempts to bind to the same port, it will typically encounter an error indicating that the port is already in use.

**However**, multiple applications can use the same port number if they are listening on different IP addresses or if they are using different transport protocols (e.g., TCP and UDP). For example:

- **Different IP Addresses:** An application can listen on port 80 for IP address 192.168.1.1, while another application can listen on port 80 for IP address 192.168.1.2.

- **Different Protocols:** An application can listen on TCP port 80, and another application can listen on UDP port 80, as TCP and UDP are different transport protocols.
  
In essence, ports are essential for directing network traffic to the appropriate service on a device.

#### HTTP (HyperText Transfer Protocol)

**Hypertext Transfer Protocol (HTTP)** is a fundamental protocol used for transferring data over the web. It forms the basis of data communication on the World Wide Web. Here’s a concise note on HTTP:

##### Overview
- **Purpose:** HTTP is designed for transferring hypertext (web pages) and other data from a web server to a client (usually a web browser). It enables users to interact with websites and web applications by requesting resources and receiving responses.

##### How HTTP Works
1. **Request-Response Model:** HTTP operates on a client-server model where:
   - **Client:** The web browser or other client initiates a request for resources.
   - **Server:** The web server processes the request and returns the requested resource (e.g., HTML pages, images).

2. **Request Structure:**
   - **Method:** Defines the action to be performed (e.g., GET, POST, PUT, DELETE).
   - **URL:** Specifies the resource location.
   - **Headers:** Provide additional information (e.g., content type, authentication).
   - **Body:** Contains data sent to the server (e.g., form submissions).

3. **Response Structure:**
   - **Status Code:** Indicates the result of the request (e.g., 200 OK, 404 Not Found).
   - **Headers:** Provide metadata about the response (e.g., content type, length).
   - **Body:** Contains the requested resource or data (e.g., HTML content).

##### Key Versions
- **HTTP/1.0:** The original version, introduced in 1996, which established the basic framework for HTTP.
- **HTTP/1.1:** Introduced in 1999, it added features like persistent connections, chunked transfer encoding, and better caching mechanisms.
- **HTTP/2:** Published in 2015, it improves performance with features like multiplexing, header compression, and server push.
- **HTTP/3:** The latest version, built on QUIC (a transport layer protocol), aims to reduce latency and improve connection security.

##### Security
- **HTTPS:** HTTP Secure (HTTPS) is an extension of HTTP that incorporates SSL/TLS encryption to secure the data transmitted between the client and server, protecting it from eavesdropping and tampering.

##### Importance
HTTP is crucial for the functioning of the web, enabling the seamless transfer of web pages and resources. It supports the browsing experience by defining how data is formatted and transmitted, and how web servers and clients should respond to various requests.

In summary, HTTP is the backbone protocol of the web, facilitating communication between clients and servers, and enabling the dynamic and interactive experience of modern web applications.


## [Lecture 3: Simple Web Server (00:20:34)](https://youtu.be/XVqvp7ovWc0?list=PLZ2ps__7DhBZGVuyXs2l3KJtiHs0KMVE7)

```sh
while true; do 
   echo -e "HTTP/1.1 200 OK\n\n $(date)" | nc -N -l localhost 1500;
done
# Some bug here.. nc is not closing the socket after serving date..So use -N which works on ubuntu.. you can use -c on MACOSX
```

Use your browser to point to http://localhost.ai:1500/

### Typical HTTP request

```
GET /favicon.ico HTTP/1.1
Host: localhost:1500
Connection: keep-alive
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0.0.0 Safari/537.36 Edg/128.0.0.0
DNT: 1
Accept: image/avif,image/webp,image/apng,image/svg+xml,image/*,*/*;q=0.8
Referer: http://localhost:1500/
Accept-Encoding: gzip, deflate
Accept-Language: en-GB,en;q=0.9,en-US;q=0.8,en-IN;q=0.7
Cookie: _vwo_uuid=...
```

1. Host is required, as multiple port-ip bindings can happen in the same system
2. The Accept: header defines the content type the client accepts, or expects to be returned by the server. Depending on the situation this can be text/css, text/html, image/png, .. etc. - just some mime type.
3. Blank line after headers is VERY IMPORTANT!

### Acronyms

1. MIME = Multipurpose Internet Mail Extension
   1. MIMES are like `application/text`, `image/jpeg`

### HTTP/2.0

**HTTP/2** is a major revision of the HTTP protocol designed to improve web performance and efficiency. Key features include:

- **Multiplexing:** Allows multiple requests and responses to be sent simultaneously over a single connection, reducing latency and improving page load times.
- **Header Compression:** Uses HPACK to compress HTTP headers, reducing the amount of data sent and improving efficiency.
- **Binary Protocol:** Uses a binary format rather than text, which is more efficient for parsing and processing.
- **Stream Prioritization:** Enables prioritization of streams to ensure more important resources are delivered first.
- **Server Push:** Allows servers to send resources proactively to the client before they are explicitly requested, speeding up page rendering.

HTTP/2 aims to enhance web performance, reduce latency, and improve overall efficiency compared to its predecessor, HTTP/1.1.

#### HTTP/3.0

**HTTP/3** is the latest version of the HTTP protocol, designed to further enhance web performance and security. Key features include:

- **QUIC Protocol:** Built on the QUIC transport protocol, which improves connection speed and reduces latency by incorporating features like multiplexing, encryption, and congestion control at the transport layer.
- **Improved Connection Establishment:** Reduces connection setup time with 0-RTT (zero round-trip time) and faster handshakes.
- **Better Handling of Packet Loss:** QUIC's built-in mechanisms handle packet loss more efficiently, improving overall reliability and performance.

HTTP/3 aims to provide a faster, more secure browsing experience by addressing the limitations of previous versions and leveraging modern transport technologies.

## [Lecture 3: What is a Protocol (00:12:31)](https://youtu.be/gPrRv4Fh04U?list=PLZ2ps__7DhBZGVuyXs2l3KJtiHs0KMVE7)

**Protocol** is how computers are supposed to speak to each other  

### HTTP Protocol

HTTP (Hypertext Transfer Protocol) has a structured format that includes several key parts in both requests and responses. Here’s a breakdown of these parts:

#### HTTP Request

1. **Request Line:**
   - **Method:** Specifies the action to be performed (e.g., GET, POST, PUT, DELETE).
   - **URL:** Indicates the resource being requested.
   - **HTTP Version:** Shows the version of HTTP being used (e.g., HTTP/1.1).

   **Example:** `GET /index.html HTTP/1.1`

2. **Headers:**
   - **General Headers:** Apply to both request and response messages (e.g., `Cache-Control`, `Connection`).
   - **Request Headers:** Provide additional information about the request (e.g., `Accept`, `User-Agent`, `Authorization`).
   - **Example Header:** `Accept: text/html`

3. **Body (Optional):**
   - Contains data sent to the server (used in methods like POST or PUT). It’s not present in GET requests.

   **Example Body (in a POST request):**
   ```
   {
     "username": "user1",
     "password": "pass123"
   }
   ```

#### HTTP Response

1. **Status Line:**
   - **HTTP Version:** Indicates the HTTP version used (e.g., HTTP/1.1).
   - **Status Code:** A three-digit code indicating the result of the request (e.g., `200` for OK, `404` for Not Found).
   - **Reason Phrase:** A textual description of the status code (e.g., `OK`, `Not Found`).

   **Example:** `HTTP/1.1 200 OK`

2. **Headers:**
   - **General Headers:** Apply to both request and response messages (e.g., `Date`, `Server`).
   - **Response Headers:** Provide information specific to the response (e.g., `Content-Type`, `Content-Length`).
   - **Example Header:** `Content-Type: text/html`

3. **Body (Optional):**
   - Contains the data sent back to the client, such as the content of a web page, an image, or other resources.

   **Example Body (HTML content):**
   ```html
   <html>
     <head><title>Example</title></head>
     <body><h1>Hello, world!</h1></body>
   </html>
   ```

- **Requests** consist of a request line, headers, and optionally a body.
- **Responses** consist of a status line, headers, and optionally a body.


```sh
python -m http.server

Serving HTTP on 0.0.0.0 port 8000 (http://0.0.0.0:8000/) ...

# Will list the current directory
```


## [Lecture 4: Performance of a website(00:16:11)](https://youtu.be/ApKLmlILKSM?list=PLZ2ps__7DhBZGVuyXs2l3KJtiHs0KMVE7)

**Latency** to the time it takes for data to travel from its source to its destination across a network. It is typically measured in milliseconds (ms) and represents the delay experienced during this data transfer. Latency encompasses various factors, including:

1. **Propagation Delay:** The time required for a signal to travel through the physical medium (e.g., cables, fiber optics) from the sender to the receiver.

2. **Transmission Delay:** The time it takes to push all the packet's bits onto the wire or link.

3. **Processing Delay:** The time taken by network devices (like routers or switches) to process the data, including routing and switching decisions.

4. **Queueing Delay:** The time data spends waiting in queues at intermediate devices due to congestion or high traffic volumes.

Low latency is crucial for applications that require real-time interactions, such as online gaming, video conferencing, and VoIP (Voice over IP). High latency can cause noticeable delays and affect the performance of these applications.


#### Latency problems

1. Calculate the propagation delay for data traveling over a fiber optic link of 1,000 kilometers. Assume the speed of light in fiber optic cables is approximately 200,000 kilometers per second.
   - $t_{1-way} = \dfrac{10^6}{2\times10^8} = 0.005$ or 5 ms
   - One way propagation delay is 5ms

2.  
```
PING www.google.com (172.217.12.36) 56(84) bytes of data.
64 bytes from lga34s12-in-f36.1e100.net (172.217.12.36): icmp_seq=1 ttl=56 time=14.5 ms
64 bytes from lga34s12-in-f36.1e100.net (172.217.12.36): icmp_seq=2 ttl=56 time=14.2 ms
```

- Network Latency is $\dfrac{14.5 + 14.2}{2}$ ms
3. Say you have a 100 Mbps (Mb = Megabits, MB = Megabytes) and you want to get a 1KB resource.
   1. $\dfrac{100,000,000}{8} B/s = 12,500,000B/s = 12.5MB/s$
   2. Total requests per second $= \dfrac{12500KB}{1KB}$ ~~ 12,5K requests per second.
   3. But you will not get this in real life.

#### Google Analysis
1. Google website is 144KB
2. Headers is 100Bytes
3. We know from some publication that google serves 60K requests per second

- so thats $144.1KB * 6 \times 10^5 == 8.646 \times 10^{10}$ bytes of traffic.
- or 86.46 GB of data per second for the home page
- So they need a bandwidth of at-least  87GB/second
- This is not possible. So it has to scale out

#### Decimal Exponential Scales

The exponential scale, commonly used in computing and data storage, represents large quantities in a compact form using prefixes like giga, tera, peta, etc. These prefixes are based on powers of 10 or 2, depending on the context. Here's a breakdown:

### Base-10 (Decimal) System

1. **Kilobyte (KB):** **$10^3$ bytes**
2. **Megabyte (MB):** **$10^6$ bytes**
3. **Gigabyte (GB):** **$10^9$ bytes**
4. **Terabyte (TB):** **$10^{12}$ bytes**
5. **Petabyte (PB):** **$10^{15}$ bytes**
6. **Exabyte (EB):** **$10^{18}$ bytes**
7. **Zettabyte (ZB):** **$10^{21}$ bytes**
8. **Yottabyte (EB):** **$10^{24}$ bytes**
9. ~~Ab Bas~~ Saaku


## [Lecture 5 - What is an App (00:17:04)](https://youtu.be/JIoQoBFqOI8?list=PLZ2ps__7DhBZGVuyXs2l3KJtiHs0KMVE7)

An **app** (short for application) is a software program designed to perform specific tasks or functions for the user. Apps can be used on various devices, including computers, smartphones, tablets, and smartwatches.

#### Key Aspects of an App:

1. **Types:**
   - **Desktop Apps:** Installed on computers (e.g., Microsoft Word, Adobe Photoshop).
   - **Mobile Apps:** Designed for smartphones and tablets (e.g., Instagram, WhatsApp).
   - **Web Apps:** Accessed via web browsers and do not require installation (e.g., Google Docs, Slack).
   - **Hybrid Apps:** Combine elements of both web and native apps and can run on multiple platforms (e.g., Twitter).

2. **Platforms:**
   - **Operating Systems:** Apps are developed for specific operating systems like Windows, macOS, iOS, Android, or Linux.
   - **App Stores:** Mobile apps are often distributed through app stores like Apple App Store or Google Play Store.

3. **Functionality:** Apps can perform a wide range of functions, including:
   - **Productivity:** Managing tasks, calendars, and documents.
   - **Communication:** Sending messages, making calls, or video conferencing.
   - **Entertainment:** Streaming media, gaming, or reading content.
   - **Utilities:** Providing tools for specific tasks like photo editing, navigation, or health tracking.


### Computing Platforms

#### 1. **Android**

- **Tools and IDEs:**
  - **Android Studio:** Official Integrated Development Environment (IDE) for Android development.
  - **Eclipse with ADT Plugin:** Older option, less commonly used now.

- **Languages:**
  - **Java**
  - **Kotlin** (recommended for new projects)

- **Frameworks:**
  - **Jetpack Compose:** Modern UI toolkit for building native UIs.
  - **Retrofit:** For network operations.
  - **Room:** For local database management.

#### 2. **iOS**

- **Tools and IDEs:**
  - **Xcode:** Official IDE for iOS development.

- **Languages:**
  - **Swift** (recommended)
  - **Objective-C**

- **Frameworks:**
  - **UIKit:** Framework for building user interfaces.
  - **SwiftUI:** Modern framework for declarative UI.
  - **Core Data:** For data management.
  - **Combine:** For reactive programming.

#### 3. **Windows**

- **Tools and IDEs:**
  - **Visual Studio:** The primary IDE for Windows app development.

- **Languages:**
  - **C#**
  - **C++**
  - **VB.NET**

- **Frameworks:**
  - **.NET Framework:** For traditional Windows applications.
  - **.NET Core / .NET 5+**: For cross-platform applications.
  - **UWP (Universal Windows Platform):** For modern Windows apps.
  - **WinUI:** For native user interface components.

#### 4. **Web Applications**

- **Tools and IDEs:**
  - **Visual Studio Code:** Popular lightweight code editor.
  - **Sublime Text:** Versatile text editor.
  - **WebStorm:** IDE specifically for JavaScript development.

- **Languages:**
  - **HTML/CSS/JavaScript**

- **Frameworks and Libraries:**
  - **React:** JavaScript library for building user interfaces.
  - **Angular:** TypeScript-based framework for building web applications.
  - **Vue.js:** Progressive framework for building UIs.
  - **Node.js:** For server-side JavaScript.

#### 5. **Cross-Platform Mobile Development**

- **Tools and IDEs:**
  - **Visual Studio:** For Xamarin development.
  - **Android Studio:** For Flutter and Dart.

- **Frameworks and Languages:**
  - **Flutter (Dart):** Framework by Google for natively compiled applications.
  - **Xamarin (C#):** Framework for building cross-platform apps using .NET.
  - **React Native (JavaScript):** Framework for building mobile apps using React.
  - **Ionic (TypeScript/JavaScript):** Framework for building cross-platform mobile apps using web technologies.

#### 6. **Game Development**

- **Tools and IDEs:**
  - **Unity:** Popular game development engine.
  - **Unreal Engine:** Advanced game development engine.

- **Languages:**
  - **C# (Unity)**
  - **C++ (Unreal Engine)**

- **Frameworks and Libraries:**
  - **Unity:** Offers a wide range of tools and assets for game development.
  - **Unreal Engine:** Known for high-fidelity graphics and robust toolset.

#### 7. **Embedded Systems**

- **Tools and IDEs:**
  - **Arduino IDE:** For programming Arduino boards.
  - **PlatformIO:** For multiple embedded systems and boards.
  - **Eclipse with CDT:** For C/C++ development in embedded systems.

- **Languages:**
  - **C**
  - **C++**

- **Frameworks:**
  - **FreeRTOS:** Real-time operating system for embedded devices.
  - **MBED OS:** For ARM-based embedded systems.

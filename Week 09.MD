# Week 9

*Prof. Nitin Chandrachoodan*  
*Department of EE, IIT Madras*  

*Notes by Adarsh (23f2003570)*  


## [L9.1: Access Control (25:48)](https://youtu.be/g5NVn0_rl_I)

**Role-Based Access Control (RBAC)** is a security model in databases that assigns access rights based on roles rather than individual users. This simplifies permission management and ensures consistent access control across large systems. Key components include:

- **Roles**: Define a set of permissions, such as read, write, or delete.
- **Users**: Assigned one or more roles, inheriting the permissions associated with those roles.
- **Permissions**: Access rights to specific database objects, granted via roles.

RBAC promotes security by minimizing the risk of over-granting permissions and provides clear separation of duties. It also enhances auditing and compliance.

In an Relational Database Management System, security access to tables is controlled through different **access types**, which define what actions a user can perform on database tables. Common types include:

1. **SELECT**: Allows reading data from the table.
2. **INSERT**: Permits adding new rows to the table.
3. **UPDATE**: Enables modifying existing records in the table.
4. **DELETE**: Grants permission to remove rows from the table.
5. **REFERENCES**: Allows the creation of foreign keys that reference the table.
6. **ALTER**: Provides the ability to modify the table schema (e.g., adding columns).

These permissions can be granted and revoked at the user or role level, supporting fine-grained access control.


### Linux File Permissions

1. **Owner**: The user who owns the file.
2. **Group**: Users who are members of the file's group.
3. **Others**: All other users.

Permissions are represented by:
- **Read (r)**: Allows viewing the contents of the file.
- **Write (w)**: Allows modifying the file.
- **Execute (x)**: Allows running the file as a program.

Permissions are displayed in a 10-character string (e.g., `rwxr-xr--`), where:
- The first character shows if it’s a file or directory (`-` or `d`).
- The next three characters are the owner's permissions.
- The next three are for the group.
- The last three are for others.

**Changing permissions**:
- Use `chmod` to modify permissions:  
  ```bash
  chmod u+x file.txt  # Add execute permission for the owner
  chmod g-w file.txt  # Remove write permission for the group
  chmod o=r file.txt  # Give read-only permission to others
  ```

**Changing ownership**:
- Use `chown` to change the owner or group:
  ```bash
  chown user:group file.txt
  ```

  Linux file permissions can also be represented and modified using **bitwise** values. Each permission (read, write, execute) is assigned a value:

- **Read (r)** = 4
- **Write (w)** = 2
- **Execute (x)** = 1

Permissions for **owner**, **group**, and **others** are **combined using the sum of these values.** For example:
- **rw-** (read + write) = 4 + 2 = 6
- **r--** (read) = 4
- **x--** (execute) = 1

**Example**:
```bash
chmod 755 file.txt  # rwx for owner, rx for group and others
```

This sets permissions using **owner: group: others** format (e.g., `755` means `rwxr-xr-x`).


### **Discretionary Access Control (DAC)** and **Mandatory Access Control (MAC)**

- **DAC** allows the resource owner to control access permissions (e.g., files and directories). The owner can assign permissions freely, allowing others to share, modify, or transfer access.
  
- **MAC** enforces access based on system policies, not user discretion. Access is granted based on security labels or classifications (e.g., top-secret or public), and users cannot modify these settings.

In summary:
- **DAC** is flexible and user-driven.
- **MAC** is strict and system-enforced.

Here are examples of **Discretionary Access Control (DAC)** and **Mandatory Access Control (MAC)**:

#### Example
##### **Discretionary Access Control (DAC)**:
- **Unix/Linux File Permissions**: A file owner can assign read, write, or execute permissions to other users.
- **Windows NTFS Permissions**: The owner of a file can grant or deny access to others using user/group permissions.

##### **Mandatory Access Control (MAC)**:
- **SELinux (Security-Enhanced Linux)**: Access to resources is based on security labels and predefined policies. Users cannot change access permissions.
- **TrustedBSD**: Enforces access policies that cannot be altered by users, ensuring strict security controls.



### Principle of Least Privilege (PoLP)

The Principle of Least Privilege (PoLP) is a security concept that asserts that each user, program, or system component should be granted the minimum level of access or permissions necessary to perform its job or function. By limiting access to only what is necessary, PoLP minimizes the risk of accidental or intentional misuse of system resources. This principle helps reduce the attack surface and limits the potential damage in case of a security breach. It’s widely applied in areas like user roles, network permissions, and application access controls.

### Privilege Escalation

Good or bad depends...

- `su` - Switch user
- `sudo` - Switch user and Do command

**Privilege escalation** is a type of security vulnerability where an attacker gains higher privileges or permissions than originally granted. It can be divided into two types:

1. **Vertical Privilege Escalation**: The attacker gains higher-level privileges (e.g., a normal user becomes an administrator).
2. **Horizontal Privilege Escalation**: The attacker gains access to the resources or data of another user with the same privilege level.

Privilege escalation is commonly achieved through exploiting flaws in software, misconfigurations, or weak security practices. Preventing it requires applying the **principle of least privilege**, regular patching, and rigorous access control policies.


## [L9.2: Security Mechanisms](https://youtu.be/0hB9iqwJPhM)

### Security by obscurity

**Security by Obscurity** is a flawed security approach where the system’s security relies on keeping details about its design, structure, or vulnerabilities hidden from potential attackers. While it may delay attacks, it does not provide robust, long-term security because once the hidden details are discovered, the system becomes vulnerable.

#### Example:
- **Obscure Algorithm**: A custom encryption algorithm kept secret, instead of using well-established, peer-reviewed ones like AES. If the algorithm is discovered, the system is insecure.
- **Non Standard Ports**: Using ports that you think that only you know.

Security should focus on strong, transparent mechanisms, not just hiding the details.

### Security Checks

1. **Input Validation**: Ensuring data is properly sanitized to prevent injection attacks (e.g., SQL injection, XSS). Example: Validating email format or sanitizing special characters in user input.
   
2. **Authentication**: Verifying users via login credentials. Example: Using strong passwords and multi-factor authentication (MFA).

3. **Authorization**: Ensuring users can only access resources they're permitted to. Example: Role-based access control (RBAC) to restrict access to admin functionalities.

4. **Session Management**: Protecting against session hijacking. Example: Using secure cookies (`HttpOnly`, `Secure` flags).

5. **Encryption**: Encrypting data in transit (e.g., using HTTPS) and at rest to protect sensitive information. Example: SSL/TLS for secure connections.

6. **Cross-Site Request Forgery (CSRF) Protection**: Preventing unauthorized actions on behalf of an authenticated user. Example: Using anti-CSRF tokens in forms.

7. **Error Handling**: Avoiding detailed error messages that could reveal sensitive information. Example: Showing generic error messages instead of system-specific details.

8. **Security Headers**: Adding HTTP headers to enhance security. Example: `X-Content-Type-Options: nosniff` to prevent MIME-type sniffing.
9. **HBAC (Host-Based Access Control)** is a security model where access to resources is determined by the host or machine from which a user connects, rather than by the user’s identity. In HBAC, permissions are granted or denied based on the system’s attributes, such as IP address, hostname, or network segment, in addition to the user’s credentials.
10. **Login Mechanisms**
    1.  User Id, Password
    2.  Access tokens
11. **HTTP Authentication** is a mechanism used to verify the identity of a user or client accessing a web server. It involves sending credentials (username and password) via the HTTP request header. Common types of HTTP authentication include:
        1.  **Basic Authentication**: The credentials are base64 encoded and sent in the request header
        2.  **Digest Authentication**: Uses hashed credentials for better security, protecting against eavesdropping.
        3.  **Bearer Token Authentication**: Uses a token (e.g., OAuth) to authenticate users in modern web applications.

These methods ensure that only authorized users can access specific resources.

#### Example:
- A company might allow employees to access the internal database only from the company’s VPN or specific IP addresses, restricting access if the user attempts to connect from outside the allowed range.

These checks work together to reduce the risk of common attacks and ensure secure operation of the app.


### **Basic Authentication**

is a simple HTTP authentication scheme where the client sends a username and password encoded in base64 format via the `Authorization` header of an HTTP request.

#### Example:

1. The client sends a request to access a resource:
   ```
   GET /protected-resource HTTP/1.1
   Host: example.com
   Authorization: Basic dXNlcm5hbWU6cGFzc3dvcmQ=
   ```

   Here, `dXNlcm5hbWU6cGFzc3dvcmQ=` is the base64-encoded string for "username:password".

2. The server decodes the base64 string, verifies the credentials, and grants or denies access accordingly.

**Note:** Basic Authentication is less secure because the credentials are easily decoded (if intercepted), which is why it's recommended to use it over **HTTPS** only.

### **Digest Authentication**

is a more secure HTTP authentication method than Basic Authentication. It involves hashing the user's credentials with certain request-specific data (such as the URL, a nonce, and other headers), and then sending the hashed result in the `Authorization` header.

#### Example:

1. The client requests a resource and receives a **401 Unauthorized** response with a **nonce** (a unique, time-limited value).
2. The client hashes the password along with the nonce and other request information, then sends the hash back to the server.
3. The server hashes the stored password with the same data and compares the results. If they match, access is granted.

Digest Authentication protects against replay and man-in-the-middle attacks by never transmitting plain-text passwords.


### **Client Certificate Authentication**

is a method used to verify the identity of a client (user or application) through the use of digital certificates. It relies on Public Key Infrastructure (PKI), where the client presents a certificate issued by a trusted Certificate Authority (CA).

1. **Certificate Generation**: The client generates a private-public key pair and gets the public key signed by a CA, creating a digital certificate.
2. **Request**: When accessing a server, the client sends the certificate along with the request.
3. **Server Validation**: The server checks the certificate’s authenticity, ensuring it’s issued by a trusted CA and not expired or revoked.
4. **Authentication**: If valid, the server authenticates the client.

This method enhances security because it requires possession of the private key, which is not easily compromised like a password.

#### Example:
In a web app, when a client connects over HTTPS, their browser may present a client certificate. The server, after validating the certificate with the CA, grants access to protected resources.


### Request Level Security

**Request-Level Security in HTTP/HTTPS** refers to mechanisms and protocols designed to secure the communication between a client (like a web browser) and a server at the individual request level. It ensures that each request is authenticated, authorized, encrypted, and protected from various types of attacks. Request-level security typically works in conjunction with secure protocols like HTTPS, headers, and access controls, as well as various authentication and authorization methods.

#### 1. **Encryption with HTTPS**
   **HTTPS (HyperText Transfer Protocol Secure)** is the foundation of securing data at the request level. It uses SSL/TLS encryption to secure the data sent between the client and server. This prevents man-in-the-middle attacks, eavesdropping, and data tampering.

   **Example:**
   - **Before HTTPS**: If a user sends their password to a website over HTTP, it’s transmitted in plain text. Anyone who intercepts the communication can easily read the password.
   - **With HTTPS**: The same password is encrypted during transmission, and even if someone intercepts the data, they cannot read it without the decryption key.

   **How it works**: 
   - The server sends its public key to the client during the handshake.
   - The client uses the server’s public key to encrypt the request (like login credentials) before sending it.
   - The server then uses its private key to decrypt the message.
   
   **Benefits**: Protects the integrity and confidentiality of each request and response.

#### 2. **Authentication**
   Authentication ensures that the client making the request is who they claim to be. In the context of HTTP/HTTPS requests, this typically involves sending credentials or tokens that verify the identity of the client.

   **Example 1: Basic Authentication**
   - In **Basic Authentication**, the client sends a base64-encoded string in the "Authorization" header, which contains a username and password.
   - **Request**:
     ```
     GET /protected-resource HTTP/1.1
     Host: example.com
     Authorization: Basic dXNlcm5hbWU6cGFzc3dvcmQ=
     ```
     - This would represent a username `username` and password `password` in base64-encoded format.
   - **Drawback**: Basic Authentication is vulnerable to interception unless used with HTTPS since the credentials are transmitted as plain text when not encrypted.

   **Example 2: Token-based Authentication (Bearer Tokens)**
   - More secure methods like **Bearer Tokens** (used with OAuth2 or JWT) involve sending an access token in the "Authorization" header to authenticate the request.
   - **Request**:
     ```
     GET /api/user/profile HTTP/1.1
     Host: example.com
     Authorization: Bearer <access_token>
     ```

   **Benefit**: The server verifies the token, and the request proceeds only if the token is valid. Tokens can have expiration times and be scoped for certain actions, offering a more secure approach.

#### 3. **Authorization**
   Authorization ensures that the authenticated user has the necessary permissions to access the requested resource.

   **Example: Role-based Access Control (RBAC)**
   - The server might examine the user's role (e.g., admin, user, guest) to determine whether they have permission to access a certain resource.
   - **Request**: 
     ```
     GET /admin/dashboard HTTP/1.1
     Host: example.com
     Authorization: Bearer <valid_admin_token>
     ```
   - The server checks if the bearer token belongs to an administrator. If not, it returns a `403 Forbidden` response.
   
   **Example: Attribute-based Access Control (ABAC)**
   - The server can authorize access based on attributes (e.g., the time of day, the resource type, or the IP address of the client).
   - For instance, a client may only access certain resources if the request originates from an IP within a specified range.

#### 4. **CSRF Protection (Cross-Site Request Forgery)**
   **CSRF** is an attack where an attacker tricks a user into performing an action they did not intend to, using their authenticated session. Request-level security can prevent this by validating that the request was intentionally made by the user.

   **Example: CSRF Token**
   - A website that requires a user to change their password might include a unique CSRF token in the request.
   - **Request**:
     ```
     POST /change-password HTTP/1.1
     Host: example.com
     Content-Type: application/x-www-form-urlencoded
     X-CSRF-Token: <generated_csrf_token>
     ```
   - The server verifies the token in the header with the one stored in the user's session. If they don't match, the request is rejected.

#### 5. **Rate Limiting**
   **Rate limiting** restricts how often a user or client can make a request to a server. This prevents abuse, such as brute-force login attacks or DoS (Denial of Service) attacks.

   **Example:**
   - If an API is rate-limited to 100 requests per hour, any request made beyond the 100th will return a `429 Too Many Requests` status.
   - The server may include a `X-RateLimit-Limit` and `X-RateLimit-Remaining` headers in the response, indicating the maximum number of requests allowed and the number of remaining requests for that time window.

   **Request/Response Headers Example:**
   ```
   Response:
   HTTP/1.1 200 OK
   X-RateLimit-Limit: 100
   X-RateLimit-Remaining: 97
   X-RateLimit-Reset: 1603718400
   ```

#### 6. **Input Validation and Sanitization**
   Input validation is crucial to prevent **SQL injection**, **XSS (Cross-Site Scripting)**, and other types of attacks. Request-level security includes checking and sanitizing inputs to ensure malicious data doesn't compromise the system.

   **Example:**
   - A user submits a search query with `<script>alert('hack');</script>`. Without proper sanitization, this could execute a script on the website.
   - The server must sanitize the input to prevent harmful scripts from being executed.

   **Request Example (malicious):**
   ```
   GET /search?q=<script>alert('hack');</script>
   ```

   The server should remove or escape harmful tags to prevent execution.

#### 7. **HTTP Headers for Security**
   Several HTTP headers can be used to increase request-level security by instructing the browser or server to behave securely.

   **Example HTTP Security Headers:**
   - **Content-Security-Policy (CSP)**: Specifies allowed content sources to mitigate XSS attacks.
   - **Strict-Transport-Security (HSTS)**: Ensures that all communications are only made over HTTPS.
   - **X-Content-Type-Options**: Prevents browsers from interpreting files as something other than their declared MIME type (to prevent content type sniffing).
   - **X-Frame-Options**: Protects against clickjacking by controlling if a page can be embedded in a frame.

   **Example:**
   ```
   HTTP/1.1 200 OK
   Content-Security-Policy: default-src 'self'; script-src 'self' https://trusted-cdn.com;
   X-Content-Type-Options: nosniff
   ```

### Connection Keep Alive

**Connection Keep-Alive** (also known as **Persistent Connection**) in HTTP refers to the practice of keeping a TCP connection open between the client (usually a web browser) and the server, allowing multiple HTTP requests and responses to be sent over the same connection. This helps reduce the overhead of opening and closing connections for every single request, leading to better performance and faster loading times.

In older versions of HTTP (like HTTP/1.0), each HTTP request required a new connection to be established, which introduced overhead. **HTTP/1.1** introduced **Connection Keep-Alive** by default, allowing multiple requests and responses to share the same connection until it is explicitly closed.

#### 1. **How Connection Keep-Alive Works**

When using **HTTP Keep-Alive**, after an initial HTTP request/response cycle, the connection remains open, and subsequent requests can be made without the need to establish a new connection each time.

##### Steps in a typical HTTP/1.1 Keep-Alive communication:
1. **Client sends an HTTP request**.
2. **Server responds** with the requested resource and keeps the connection open, allowing the client to send further requests.
3. The **client sends additional requests** using the same open connection.
4. **Server sends additional responses** using the same connection.
5. Either the client or the server can close the connection once they are done sending data.

#### 2. **Benefits of Keep-Alive**
   - **Reduced Latency**: Eliminates the need to set up a new TCP connection for every request, which reduces round-trip time (RTT) delays.
   - **Lower CPU and Network Overhead**: Fewer TCP handshakes are needed, saving resources.
   - **Improved Performance**: Reduces time spent in connection setup and teardown, speeding up the load time for multiple resources.

#### 3. **Example of Connection Keep-Alive in HTTP/1.1**

In **HTTP/1.1**, the `Connection: keep-alive` header is included by default. However, it can also be explicitly stated by both the client and server.

##### Example 1: Request with Keep-Alive

**Client's Request (HTTP/1.1)**:
```
GET /index.html HTTP/1.1
Host: example.com
Connection: keep-alive
```
Here, the client is requesting the resource `index.html` from the server and explicitly indicating that it wants to keep the connection open for future requests (although, in HTTP/1.1, this is the default behavior).

##### Example 2: Server's Response with Keep-Alive

**Server's Response (HTTP/1.1)**:
```
HTTP/1.1 200 OK
Content-Type: text/html
Connection: keep-alive
Content-Length: 500

<!DOCTYPE html>
<html>
  <head><title>Welcome</title></head>
  <body><h1>Welcome to Example.com</h1></body>
</html>
```
In the response, the `Connection: keep-alive` header indicates that the server is willing to keep the connection open for further requests from the client.

After this, the client can send additional requests to the server using the same connection.

#### 4. **Connection Timeout**

The server or client may decide to close the connection after a certain period of inactivity. This is controlled by the `Keep-Alive` header, which specifies the maximum time the connection should be kept alive, or the maximum number of requests that can be sent over the connection before it is closed.

##### Example: Setting a Keep-Alive Timeout
```
HTTP/1.1 200 OK
Content-Type: text/html
Connection: keep-alive
Keep-Alive: timeout=15, max=100
Content-Length: 500
```

In this response:
- `timeout=15`: The connection will be kept alive for 15 seconds after the last request.
- `max=100`: Up to 100 requests can be sent over this single connection.

#### 5. **Example of a Non-Persistent (Closed) Connection in HTTP/1.0**
In **HTTP/1.0**, a connection was closed after each request-response cycle by default. A client would have to open a new connection for each resource request.

**Client’s Request (HTTP/1.0)**:
```
GET /index.html HTTP/1.0
Host: example.com
```

**Server’s Response (HTTP/1.0)**:
```
HTTP/1.0 200 OK
Content-Type: text/html
Content-Length: 500

<!DOCTYPE html>
<html>
  <head><title>Welcome</title></head>
  <body><h1>Welcome to Example.com</h1></body>
</html>
```
After the response, the connection is closed.

#### 6. **Keep-Alive and HTTP/2**
**HTTP/2** further improves on the concept of persistent connections. In **HTTP/2**, multiplexing allows multiple requests and responses to be sent over a single connection at the same time, improving efficiency even more than HTTP/1.1’s Keep-Alive.

In HTTP/2, the connection is kept open indefinitely until it is explicitly closed by either the client or the server. It doesn’t require explicit `Connection: keep-alive` headers because connections are persistent by default.

#### 7. **Performance Considerations and Optimizations**
While `Keep-Alive` improves performance by reducing connection overhead, there are scenarios where it may not always be beneficial:
- **Too many open connections**: A server may become overloaded if too many connections are kept open.
- **Resource contention**: If the server is handling multiple persistent connections, it may exhaust available resources like memory or CPU.

##### Best Practices:
- **Keep-Alive Timeout**: Set appropriate timeouts on the server to close idle connections and free up resources.
- **Connection Pooling**: On the client side, reuse connections and limit the number of simultaneous connections to the server.

#### 8. **Real-world Example: HTTP Requests for Multiple Resources**

Consider a web page that contains multiple resources, such as an image, CSS file, and JavaScript file. With Keep-Alive, these requests can all be made using the same connection.

**Step 1: Client Requests HTML Page (Keep-Alive)**
```
GET /index.html HTTP/1.1
Host: example.com
Connection: keep-alive
```

**Step 2: Server Responds with HTML**
```
HTTP/1.1 200 OK
Content-Type: text/html
Connection: keep-alive
Content-Length: 500

<!DOCTYPE html>
<html>
  <head><title>Welcome</title></head>
  <body>
    <h1>Welcome to Example.com</h1>
    <img src="/image.jpg">
    <link rel="stylesheet" href="/style.css">
    <script src="/app.js"></script>
  </body>
</html>
```

**Step 3: Client Requests Image, CSS, and JS Using Same Connection**
```
GET /image.jpg HTTP/1.1
Host: example.com
Connection: keep-alive

GET /style.css HTTP/1.1
Host: example.com
Connection: keep-alive

GET /app.js HTTP/1.1
Host: example.com
Connection: keep-alive
```

The client can now download the image, CSS, and JavaScript using the same connection, reducing the need for additional TCP handshakes.

### API Level Security

API level security is crucial for ensuring the integrity, confidentiality, and availability of data and services provided through APIs (Application Programming Interfaces). With the rise of cloud computing, mobile apps, and microservices architectures, APIs are exposed to external networks, making them potential targets for malicious actors. Therefore, securing APIs is essential to prevent unauthorized access, data breaches, and other security threats.

#### Key API Level Security Techniques and Best Practices

1. **Authentication**:
   Authentication ensures that the user or system calling the API is who they claim to be. It is the first line of defense against unauthorized access.

   **Techniques**:
   - **OAuth 2.0**: A widely used authentication standard, OAuth 2.0 allows clients to access server resources on behalf of a user without exposing their credentials. It uses access tokens to authenticate API requests.
   - **API Keys**: API keys are unique identifiers that authenticate API requests. While simple, they should be kept confidential and not exposed in public repositories or logs.
   - **JWT (JSON Web Tokens)**: JWT is often used for stateless authentication, where the server generates a token after authenticating the user. The client sends this token with subsequent requests, allowing the server to authenticate and authorize the user without storing session data.

   **Best Practices**:
   - Always use strong authentication mechanisms such as OAuth2 or JWT over basic authentication.
   - Never expose API keys in URLs or client-side code (e.g., JavaScript on web pages).
   - Regularly rotate API keys or tokens to limit the impact of potential compromises.

2. **Authorization**:
   Authorization determines whether an authenticated user or system has permission to perform a specific action or access specific resources.

   **Techniques**:
   - **Role-Based Access Control (RBAC)**: RBAC assigns permissions based on the user’s role (e.g., admin, user, guest). Each role has predefined permissions for accessing certain API endpoints.
   - **Attribute-Based Access Control (ABAC)**: ABAC grants or denies access based on attributes (e.g., user location, department, or time of day).
   - **Scopes in OAuth**: In OAuth 2.0, scopes are used to limit the level of access granted. Each scope represents a specific permission, and the access token is issued with specific scopes.
   
   **Best Practices**:
   - Always enforce least privilege, meaning users should only have access to the resources necessary for their role.
   - Define clear and concise roles and permissions for API endpoints.
   - Use OAuth scopes and RBAC to tightly control what authenticated users can do with the API.

3. **Rate Limiting and Throttling**:
   Rate limiting and throttling prevent abuse by controlling how many requests an API can handle from a client in a given period of time.

   **Techniques**:
   - **Rate Limiting**: Setting a maximum number of requests allowed within a specified time window (e.g., 100 requests per minute). This helps mitigate DDoS (Distributed Denial of Service) attacks and protects server resources.
   - **Leaky Bucket Algorithm / Token Bucket Algorithm**: These are techniques to smooth out the bursty traffic and ensure that a consistent flow of requests can be handled.
   - **Burst Handling**: Allowing brief periods of higher request volume while keeping the overall rate within limits.

   **Best Practices**:
   - Implement rate limiting on all public-facing APIs to prevent abuse.
   - Provide meaningful error messages (e.g., HTTP 429 Too Many Requests) when rate limits are exceeded.
   - Allow for some level of burst traffic but ensure it doesn't overwhelm the system.

4. **Encryption**:
   Encryption protects sensitive data in transit and at rest from unauthorized access and tampering.

   **Techniques**:
   - **TLS (Transport Layer Security)**: Always use HTTPS with TLS (formerly SSL) to encrypt API traffic between clients and servers. This ensures data privacy and integrity while transmitting over the network.
   - **Data Encryption at Rest**: Sensitive data stored on servers (such as passwords, credit card details) should be encrypted when at rest using strong encryption algorithms like AES (Advanced Encryption Standard).

   **Best Practices**:
   - Enforce TLS (HTTPS) for all API endpoints to protect data in transit.
   - Use strong encryption algorithms and keys to store sensitive data at rest.
   - Regularly rotate encryption keys and securely manage them.

5. **Input Validation**:
   Input validation ensures that data received by the API conforms to expected formats and prevents injection attacks (e.g., SQL Injection, XSS).

   **Techniques**:
   - **Whitelist Input Validation**: Accept only data that matches expected patterns or values (e.g., email addresses, phone numbers, numeric values).
   - **Sanitizing Inputs**: Sanitize inputs by removing or encoding potentially dangerous characters to prevent malicious data from entering the system.
   - **Parameterized Queries**: When interacting with databases, use parameterized queries or prepared statements to prevent SQL injection.

   **Best Practices**:
   - Validate all incoming data, even from trusted sources.
   - Apply strict input validation (e.g., regex checks) and reject malformed data.
   - Avoid directly inserting user input into SQL queries or shell commands without sanitization.

6. **Logging and Monitoring**:
   Logging and monitoring help detect, alert, and respond to suspicious activities, errors, and potential attacks.

   **Techniques**:
   - **Centralized Logging**: Use centralized logging solutions (e.g., ELK stack, Splunk) to aggregate logs from all API services and servers.
   - **API Usage Analytics**: Monitor API usage patterns to identify anomalies, such as a spike in requests from a single IP address or unusual activity on sensitive endpoints.
   - **Intrusion Detection Systems (IDS)**: Use IDS to detect malicious patterns, such as brute-force login attempts or known attack signatures.

   **Best Practices**:
   - Log all API requests and responses (including headers) in a secure manner, but avoid logging sensitive data (e.g., passwords, tokens).
   - Implement real-time alerting for abnormal activities such as excessive failed login attempts, unauthorized access, or unusual traffic spikes.
   - Ensure logs are stored securely and are tamper-proof.

7. **Cross-Origin Resource Sharing (CORS)**:
   CORS is a mechanism that allows servers to specify which domains are permitted to access their resources via HTTP requests.

   **Techniques**:
   - **CORS Headers**: Use the `Access-Control-Allow-Origin` header to specify which domains can access the API. This prevents cross-site request forgery (CSRF) attacks and data leakage between different domains.
   - **Allowing Specific HTTP Methods**: Specify allowed methods (e.g., GET, POST) through headers such as `Access-Control-Allow-Methods`.

   **Best Practices**:
   - Restrict API access to trusted domains by setting the appropriate CORS headers.
   - Only allow safe HTTP methods and avoid exposing sensitive API endpoints to unauthorized domains.
   - Regularly review and audit CORS settings to ensure they are as restrictive as possible.

8. **API Gateway Security**:
   An API Gateway is a centralized point that manages, authenticates, and routes API requests, helping with rate limiting, logging, security, and more.

   **Techniques**:
   - **API Gateway Authentication**: The API Gateway can act as the first line of defense, handling authentication (e.g., OAuth2), rate limiting, and logging before requests are forwarded to backend services.
   - **IP Whitelisting**: Limit access to the API Gateway by only allowing requests from trusted IP addresses or networks.

   **Best Practices**:
   - Use an API Gateway to centralize security measures such as authentication, logging, rate limiting, and CORS management.
   - Keep the API Gateway updated and secure, as it often becomes a critical attack surface.

9. **Security Testing and Vulnerability Scanning**:
   Regular testing and vulnerability scanning are crucial to identifying and addressing security weaknesses in APIs.

   **Techniques**:
   - **Penetration Testing**: Conduct regular penetration tests to identify vulnerabilities such as injection flaws, broken authentication, or insecure direct object references.
   - **Automated Scanning**: Use automated tools to scan APIs for common vulnerabilities like SQL injection, XSS, and insecure deserialization.

   **Best Practices**:
   - Regularly conduct security testing (both manual and automated) to identify and mitigate potential risks.
   - Stay updated on the latest API security vulnerabilities by monitoring security advisories and applying patches promptly.


## [L9.3: Sessions (15:51)](https://youtu.be/KtJtD4vMwtQ)

### Cookies

A **cookie** in the context of web technologies is a small piece of data stored on a user's device by a web browser while they are browsing a website. These cookies are used to store various information, like user preferences, login status, shopping cart items, and tracking information, which can be reused by the website during future visits or on subsequent requests. 

Cookies are fundamental to providing a personalized, dynamic web experience. They enable websites to "remember" users and their actions, facilitating things like user authentication, session management, and tracking behavior.

#### 1. **What Are Web Cookies?**

A web cookie is essentially a small text file that is sent from a web server to a browser. The browser stores the cookie and includes it in future requests made to the same domain, thus allowing the server to "remember" previous interactions or preferences.

There are two types of cookies:
- **First-party cookies**: Set by the website the user is currently visiting.
- **Third-party cookies**: Set by a domain other than the website the user is currently visiting, often used by advertisers for tracking across different websites.

#### 2. **How Cookies Work**

Here's a typical flow of how cookies work in a web environment:

1. **User visits a website**:
   - The server sends an HTTP response that includes a `Set-Cookie` header.
   - The cookie contains key-value pairs (e.g., `username=JohnDoe`) and optional metadata, such as expiration time, domain, and path.

2. **Browser stores the cookie**:
   - The browser stores the cookie in its local storage (in a special cookie store, usually associated with the domain).
   
3. **Future requests to the same server**:
   - When the user makes subsequent requests to the same website, the browser sends the cookie back to the server as part of the HTTP request (in the `Cookie` header).
   - The server uses the cookie data to customize the response for the user.

#### 3. **Cookie Components**

A cookie typically consists of the following components:

- **Name**: The name of the cookie (e.g., `session_id`).
- **Value**: The value assigned to the cookie (e.g., `123456`).
- **Domain**: The domain the cookie is valid for. It dictates which websites can access the cookie. For example, a cookie set for `example.com` will not be accessible by `otherwebsite.com`.
- **Path**: The URL path for which the cookie is valid. This limits the cookie's availability to a specific section of the website (e.g., `/account`).
- **Expires/Max-Age**: The expiration date of the cookie. Cookies with an expiration date are stored persistently. Cookies without an expiration date (session cookies) are deleted when the browser is closed.
- **Secure**: A flag that ensures the cookie is only sent over secure (HTTPS) connections.
- **HttpOnly**: A flag that prevents client-side access to the cookie via JavaScript (important for preventing certain types of cross-site scripting (XSS) attacks).
- **SameSite**: A flag that helps mitigate CSRF (Cross-Site Request Forgery) attacks by controlling when cookies are sent in cross-site requests.

#### 4. **Types of Cookies**

There are various types of cookies, categorized based on their usage and lifespan:

##### a) **Session Cookies**
- These cookies are temporary and are erased when the user closes the browser.
- They are primarily used for session management, such as remembering a user’s logged-in state during their visit.
- **Example**: The website stores a session ID to keep the user logged in while they browse.

##### b) **Persistent Cookies**
- Persistent cookies are stored on the user's device for a specified period, even after the browser is closed.
- These cookies are used to remember user preferences or login credentials across multiple sessions.
- **Example**: A website remembers the user’s language preference or theme choice.

##### c) **Secure Cookies**
- Secure cookies are only sent over HTTPS connections, ensuring that the data is encrypted during transmission.
- They are used for storing sensitive information, like session tokens or authentication details.

##### d) **HttpOnly Cookies**
- HttpOnly cookies can only be accessed by the server and cannot be accessed or modified via JavaScript. This adds an additional layer of security by preventing cross-site scripting (XSS) attacks.
- **Example**: A session cookie marked as HttpOnly stores the session token, preventing JavaScript from accessing it.

##### e) **SameSite Cookies**
- The **SameSite** attribute restricts how cookies are sent with cross-site requests. There are three possible settings:
  - `SameSite=Lax`: Cookies are sent with top-level navigations and GET requests, but not with cross-site sub-requests (e.g., images or iframes).
  - `SameSite=Strict`: Cookies are only sent with requests originating from the same site (no cross-site requests).
  - `SameSite=None`: Cookies will be sent in all contexts (cross-site and same-site) but must be marked as `Secure`.

#### 5. **Uses of Cookies**

Cookies serve many purposes, such as:

- **Session management**: Cookies are used to store session identifiers so users don’t need to log in every time they visit a website.
  - **Example**: A user logs into their bank account. After logging in, a session cookie is stored, allowing them to access other pages without re-entering credentials.
  
- **Personalization**: Cookies can store user preferences (e.g., language settings, theme choice) to provide a more customized browsing experience.
  - **Example**: A website remembers that a user prefers a dark mode theme.
  
- **Tracking and analytics**: Cookies are often used to track user activity on a website or across different websites to build a profile, which helps with targeted advertising and analytics.
  - **Example**: Google Analytics uses cookies to track how users interact with a website, collecting data on page views, sessions, and geographic location.
  
- **Targeted advertising**: Third-party cookies are used by advertisers to track users' browsing behavior across different websites. This allows advertisers to serve personalized ads to users based on their interests.
  - **Example**: A user visits an online store for running shoes, and then later sees ads for running shoes on other websites they visit.

#### 6. **Cookie Security and Privacy Concerns**

While cookies offer convenience, they can also pose security and privacy risks:

##### a) **Tracking and Privacy**
Cookies, particularly third-party cookies, can be used to track users across multiple sites, leading to privacy concerns. This tracking can be used for advertising or analytics without the user’s explicit consent.

##### b) **Cross-Site Scripting (XSS)**
If a website is vulnerable to XSS attacks, an attacker could steal cookies, particularly session cookies, if they are not marked as `HttpOnly`. This could lead to session hijacking.

##### c) **Cross-Site Request Forgery (CSRF)**
Without proper cookie handling (like the `SameSite` attribute), an attacker could trick a user into making an unwanted request to a website where they are logged in, potentially carrying out actions on their behalf.

##### d) **Cookie Theft**
If cookies are not properly secured (e.g., if the `Secure` flag is not set for sensitive cookies), they could be intercepted by attackers over unencrypted HTTP connections.

#### 7. **Managing Cookies: Consent and Regulations**

In many regions, regulations such as the **General Data Protection Regulation (GDPR)** in the European Union require websites to obtain user consent before storing cookies, especially third-party cookies used for advertising and tracking. 

- Websites must inform users about the cookies they use and provide options for the user to manage or disable cookies.
- The **Cookie Consent Banner** is a common approach to comply with privacy laws, allowing users to choose which types of cookies they accept.

**Example Cookie Consent Banner:**
```
We use cookies to improve your experience. By continuing to browse this site, you agree to our use of cookies. 
[Accept] [Settings] [Learn More]
```

#### 8. **Example of Setting and Using Cookies**

##### Setting a Cookie in HTTP Response:
```
Set-Cookie: username=JohnDoe; Max-Age=3600; Path=/; Secure; HttpOnly; SameSite=Strict
```
This sets a cookie named `username` with the value `JohnDoe`, which expires in 1 hour, is only sent over secure (HTTPS) connections, is inaccessible via JavaScript, and is restricted to the same site.

##### Sending a Cookie in HTTP Request:
```
Cookie: username=JohnDoe; session_id=abcd1234
```
The browser sends the `username` and `session_id` cookies with each subsequent request to the same server.

### Cookies in Flask

In Flask, cookies are used to store small pieces of data on the client-side, typically in the user's browser, that can be sent along with each subsequent request to the server. Cookies in Flask are most commonly used for session management (e.g., keeping track of whether a user is logged in) or storing user preferences (e.g., theme settings).

#### Working with Cookies in Flask

Flask provides built-in support for working with cookies through the `request` and `make_response` objects. Here's an overview of how to use cookies in Flask with examples.

#### 1. **Setting a Cookie in Flask**

To set a cookie in Flask, we use the `response.set_cookie()` method, which attaches a cookie to the HTTP response.

##### Example: Setting a Cookie

```python
from flask import Flask, make_response

app = Flask(__name__)

@app.route('/set_cookie')
def set_cookie():
    # Create the response object
    response = make_response("Cookie has been set!")
    
    # Set a cookie named 'username' with value 'JohnDoe' for 30 days
    response.set_cookie('username', 'JohnDoe', max_age=30*24*60*60)
    
    return response

if __name__ == "__main__":
    app.run(debug=True)
```

**Explanation**:
- `response.set_cookie('username', 'JohnDoe')` sets a cookie named `username` with a value of `JohnDoe`.
- `max_age=30*24*60*60` specifies the expiration time of the cookie in seconds (30 days in this case).

When a user visits the `/set_cookie` route, Flask sends an HTTP response that includes the `Set-Cookie` header, which is stored in the browser as a cookie.

#### 2. **Reading a Cookie in Flask**

To read a cookie in Flask, you can access the cookies sent with the request using `request.cookies`. This is a dictionary-like object, and you can retrieve the cookie value using the cookie name.

##### Example: Reading a Cookie

```python
from flask import Flask, request

app = Flask(__name__)

@app.route('/get_cookie')
def get_cookie():
    # Get the cookie value from the request
    username = request.cookies.get('username')
    
    if username:
        return f"Hello, {username}!"
    else:
        return "No username cookie found!"

if __name__ == "__main__":
    app.run(debug=True)
```

**Explanation**:
- `request.cookies.get('username')` retrieves the value of the `username` cookie if it exists. If the cookie is not found, it returns `None`.
- If the `username` cookie is set, the server will respond with "Hello, JohnDoe!", otherwise, it will say "No username cookie found!".

#### 3. **Deleting a Cookie in Flask**

To delete a cookie in Flask, you can use the `response.delete_cookie()` method. This will remove the cookie from the client's browser.

##### Example: Deleting a Cookie

```python
from flask import Flask, make_response

app = Flask(__name__)

@app.route('/delete_cookie')
def delete_cookie():
    # Create the response object
    response = make_response("Cookie has been deleted!")
    
    # Delete the 'username' cookie
    response.delete_cookie('username')
    
    return response

if __name__ == "__main__":
    app.run(debug=True)
```

**Explanation**:
- `response.delete_cookie('username')` removes the cookie named `username` from the browser.
- After calling this route, if the user revisits, the `username` cookie will no longer be present.

#### 4. **Using Secure and HttpOnly Cookies**

Flask also allows you to set cookies with security attributes like `Secure` and `HttpOnly`. These attributes provide additional layers of security:
- **`Secure`**: Ensures that the cookie is only sent over HTTPS connections.
- **`HttpOnly`**: Prevents JavaScript from accessing the cookie, which helps prevent XSS attacks.

##### Example: Setting Secure and HttpOnly Cookies

```python
from flask import Flask, make_response

app = Flask(__name__)

@app.route('/set_secure_cookie')
def set_secure_cookie():
    response = make_response("Secure and HttpOnly Cookie set!")
    
    # Set a secure cookie that is HttpOnly
    response.set_cookie('username', 'JohnDoe', max_age=30*24*60*60, secure=True, httponly=True)
    
    return response

if __name__ == "__main__":
    app.run(debug=True)
```

**Explanation**:
- `secure=True` ensures the cookie is only sent over HTTPS connections.
- `httponly=True` makes the cookie inaccessible to JavaScript, providing better protection against client-side scripting attacks.

#### 5. **Using Flask’s Session to Store Data in Cookies**

Flask also provides a `session` object, which is essentially a special type of cookie that automatically encrypts its data. It’s useful for storing session-specific data like user authentication state, preferences, etc.

To use sessions in Flask, you need to configure a secret key that will be used to sign session cookies and ensure their integrity.

##### Example: Using Flask Sessions

```python
from flask import Flask, session, redirect, url_for, request

app = Flask(__name__)
app.secret_key = 'your_secret_key_here'  # Secret key for signing the session cookie

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        # Store the username in the session
        session['username'] = request.form['username']
        return redirect(url_for('profile'))
    return '''
        <form method="post">
            Username: <input type="text" name="username">
            <input type="submit" value="Login">
        </form>
    '''

@app.route('/profile')
def profile():
    if 'username' in session:
        username = session['username']
        return f"Hello, {username}!"
    return redirect(url_for('login'))

if __name__ == "__main__":
    app.run(debug=True)
```

**Explanation**:
- The `session` object is used to store user-specific data (in this case, the `username`).
- `app.secret_key` is necessary to encrypt the session data and ensure its integrity.
- When the user logs in, their `username` is saved in the session and can be accessed on subsequent requests.
- The session data is automatically stored in a secure cookie, and Flask handles encryption and signing behind the scenes.

#### 6. **Cookie Expiration**

You can set an expiration time for a cookie by using the `max_age` or `expires` parameter when creating a cookie. The `max_age` parameter specifies the lifespan of the cookie in seconds, whereas `expires` specifies a specific expiration date.

##### Example: Setting Expiration Time for Cookies

```python
from flask import Flask, make_response
from datetime import datetime, timedelta

app = Flask(__name__)

@app.route('/set_expiring_cookie')
def set_expiring_cookie():
    # Create the response object
    response = make_response("Cookie with expiration time has been set!")
    
    # Set a cookie with an expiration time
    expires = datetime.utcnow() + timedelta(days=5)  # Cookie expires in 5 days
    response.set_cookie('username', 'JohnDoe', expires=expires)
    
    return response

if __name__ == "__main__":
    app.run(debug=True)
```

**Explanation**:
- `expires=datetime.utcnow() + timedelta(days=5)` sets the expiration date of the cookie to 5 days from the current time.
- After 5 days, the cookie will automatically be deleted.


**Use Redis to store sessions!**


```py
from flask import Flask, render_template, redirect, url_for, request, session
from flask_login import LoginManager, UserMixin, login_user, login_required, logout_user, current_user

app = Flask(__name__)

# Secret key for session management (make sure to change it in a real app)
app.secret_key = 'your_secret_key_here'

# Setup Flask-Login
login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = "login"  # Redirect to this view if not logged in

# In-memory user store (replace with a database in production)
users = {"testuser": {"password": "testpassword"}}

# User class for Flask-Login
class User(UserMixin):
    def __init__(self, username):
        self.id = username

    @staticmethod
    def get(user_id):
        # You can implement a database lookup here
        if user_id in users:
            return User(user_id)
        return None

# Load user from session
@login_manager.user_loader
def load_user(user_id):
    return User.get(user_id)

# Route for login page
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        # Check if user exists and password is correct
        if username in users and users[username]['password'] == password:
            user = User(username)
            login_user(user)
            return redirect(url_for('profile'))  # Redirect to profile after login
        else:
            return "Invalid credentials", 401

    return '''
        <form method="POST">
            Username: <input type="text" name="username"><br>
            Password: <input type="password" name="password"><br>
            <input type="submit" value="Login">
        </form>
    '''

# Route for user profile (protected by login_required)
@app.route('/profile')
@login_required  # Only accessible if the user is logged in
def profile():
    return f"Hello, {current_user.id}! Welcome to your profile."

# Route for logout
@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('login'))

if __name__ == "__main__":
    app.run(debug=True)
```
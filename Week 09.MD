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



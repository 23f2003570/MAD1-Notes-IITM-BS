# Week 6

*Prof. Nitin Chandrachoodan*  
*Department of EE, IIT Madras*  

*Notes by Adarsh (23f2003570)*  


## [L6.1: API Design (23:41)](https://youtu.be/FE5tva_o7ew)

### REST
#### 1. **REST (Representational State Transfer)**
   - **Definition**: REST is an architectural style for designing networked applications. It uses HTTP as the communication protocol and emphasizes stateless interactions between client and server.
   - **In Python**: Python libraries like **Flask**, **Django**, or **FastAPI** are commonly used to build RESTful APIs. A REST API exposes endpoints (URLs) for different operations like `GET`, `POST`, `PUT`, and `DELETE` to interact with resources (e.g., databases or services).

#### 2. **API (Application Programming Interface)**
   - **Definition**: An API is a set of rules and protocols that allows different software systems to communicate with each other. In the case of web APIs, they define how a client (e.g., a web browser or mobile app) can request data from a server and how the server should respond.
   - **In Python**: Python can be used to develop both RESTful APIs (using frameworks like Flask, Django, or FastAPI) and interact with APIs by sending HTTP requests (using libraries like **requests** or **http.client**).

#### 3. **Swagger**
   - **Definition**: Swagger (now known as **OpenAPI**) is a framework for describing, documenting, and testing RESTful APIs. It provides a specification and tools for auto-generating API documentation and client libraries.
   - **In Python**: Swagger can be integrated into Python web applications for API documentation and testing. Tools like **Flask-RESTPlus**, **FastAPI**, and **Django Rest Framework** support auto-generating Swagger documentation based on Python code. FastAPI, for example, automatically generates a Swagger UI for the API, making it easy to explore and interact with the API endpoints.

#### Example in Python (using FastAPI):
```python
from fastapi import FastAPI

app = FastAPI()

@app.get("/items/{item_id}")
def read_item(item_id: int, q: str = None):
    return {"item_id": item_id, "q": q}

# The API will automatically generate a Swagger UI at /docs
```

### Origins of REST

Roy Fielding's **REST (Representational State Transfer)** is an architectural style defined in his doctoral dissertation in 2000. It has become a foundational concept in designing scalable and maintainable web services. Here are the key points that define **REST**:

#### 1. **Statelessness**
   - Each interaction between the client and server must be independent. The server does not store any client context between requests.
   - All necessary information for the request (e.g., authentication, session state) must be included in each HTTP request.
   - This simplifies server design since there is no need to maintain or manage state on the server side.

#### 2. **Client-Server Architecture**
   - REST promotes a separation of concerns between the client and the server.
   - The client is responsible for the user interface and user experience, while the server handles data storage and processing.
   - This separation allows both to evolve independently.

#### 3. **Uniform Interface**
   - REST APIs should have a consistent, standardized interface (e.g., using standard HTTP methods like `GET`, `POST`, `PUT`, `DELETE`).
   - This simplifies interactions between different systems and enables the API to be easily understood and consumed by developers.
   - REST also encourages the use of clear and descriptive URIs (Uniform Resource Identifiers) to identify resources.

#### 4. **Resource-Based**
   - In REST, everything is considered a **resource** (e.g., a user, an order, or a document).
   - Resources are represented in different formats (e.g., JSON, XML), and the client can interact with them via their URIs.
   - The state of a resource is transferred between client and server during interactions, typically through representations (e.g., a JSON object representing a user).

#### 5. **Representation of Resources**
   - Clients interact with resources by exchanging **representations** (such as JSON or XML), not directly with the resources themselves.
   - For example, when requesting a resource like a user, the client receives a JSON object representing the user’s data, and changes are made by sending a modified representation back to the server.

#### 6. **Stateless Communication**
   - All communication between the client and server is stateless, meaning each request must be self-contained. The server does not retain any information about previous requests.
   - Every request must contain all the information necessary to understand and process the request, such as authentication tokens or query parameters.

#### 7. **Cacheability**
   - Responses from the server must explicitly define whether they are cacheable or not.
   - If a response is cacheable, it can be stored by the client or intermediary servers, reducing the need for repetitive requests and improving performance.

#### 8. **Layered System**
   - A REST architecture can have multiple layers, and each layer has a specific function.
   - The client doesn't need to know whether it's communicating with the end server or an intermediary server, such as a cache or load balancer. This abstraction supports scalability and modularity.

#### 9. **Code on Demand (Optional)**
   - REST allows servers to send executable code (e.g., JavaScript) to the client when needed. This is an optional constraint and not commonly used.
   - It enables the client to temporarily extend its functionality through the code provided by the server.

#### 10. **Scalability and Performance**
   - REST's stateless nature and caching make it highly scalable.
   - Its simple, standardized protocols (mainly HTTP) make it easy to scale services horizontally and handle a large number of concurrent requests.

#### 11. **Layered System**
   - REST allows an architecture to be composed of multiple layers, where each layer (such as security layers, load balancers, or caching servers) performs specific functions.
   - These layers are invisible to the client, which interacts only with the server interface.


## [L6.2: REST (20:42)](https://youtu.be/JG6K1y87EX8)


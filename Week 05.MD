# Week 5

*Prof. Nitin Chandrachoodan*  
*Department of EE, IIT Madras*  

*Notes by Adarsh (23f2003570)*  


## [L5.1: MVC Origins 18:46](https://youtu.be/hW0w6YqeDpU)

MVC - Model View Controller.


- Model Updates View
- Controller Manipulates Model
- User Uses Controller to change the view
- View is seen by user.
- User centric
  - No connection between user and DB
  - Trygve Reenskaug, Xerox PARC

### MVC with Flask vs ASP.NET Core MVC

Both Flask and ASP.NET Core MVC follow the Model-View-Controller (MVC) design pattern for web development.

MVC separates an application into three parts:

* **Model:** Represents the data of the application, including its structure and logic. It handles data access (e.g., database interaction) and business logic.
* **View:** Presents the user interface (UI) of the application. It uses templates to dynamically generate HTML based on data received from the controller.
* **Controller:** Handles user requests (routes). It interacts with the model to retrieve data and sends it to the view for presentation.


#### MVC in Flask

Flask is a lightweight Python framework. While it doesn't strictly enforce an MVC structure, you can implement it for better organization. Here's how it works:

* **Model:** Often implemented using libraries like SQLAlchemy for database access. You create Python classes representing your data structure.
* **View:** Uses Jinja2 templating engine to generate HTML based on data passed by the controller. You define templates with HTML and Jinja2 directives to dynamically insert data.
* **Controller:** Flask uses decorators (e.g., `@app.route`) to map URLs to functions. These functions handle user requests, interact with the model, and pass data to the view template for rendering.

**Key Points:**

* Flask is **flexible**. You can implement MVC loosely or tightly depending on your project needs.
* Flask offers **minimal structure**, requiring more manual configuration compared to ASP.NET Core MVC.

#### MVC in ASP.NET Core MVC

ASP.NET Core MVC is a full-fledged web framework built by Microsoft. It enforces a stricter MVC structure and provides built-in features for each layer.

* **Model:** Similar to Flask, you use C# classes or Entity Framework Core for data access.
* **View:** Uses Razor Pages or MVC Views for UI generation. Razor provides syntax for embedding C# code within HTML templates.
* **Controller:** Similar to Flask, controllers handle user requests, interact with the model, and pass data to the view. ASP.NET Core includes built-in features like model binding and routing.

**Key Points:**

* ASP.NET Core MVC provides a **structured** environment with clear separation of concerns.
* Offers features like **dependency injection** and built-in functionalities for routing and model binding.

#### Comparison

| Feature        | Flask                                      | ASP.NET Core MVC                               |
|----------------|--------------------------------------------|-------------------------------------------------|
| Language       | Python                                      | C#, F#, VB.NET (primarily C#)                  |
| MVC Structure   | Flexible implementation                     | Strict enforcement                              |
| Complexity      | Lightweight, minimal configuration         | More complex with built-in features             |
| Community      | Large and active Python community            | Large and active .NET community                |
| Platform        | Cross-platform (Windows, Linux, macOS)     | Primarily Windows (cross-platform via .NET Core) |
| View Engine    | Jinja2                                       | Razor Pages or MVC Views                       |
| Data Access     | Requires additional libraries                  | Entity Framework Core (built-in)                 |
| Routing         | Manual configuration with decorators          | Built-in routing feature                         |
| Dependency Injection | Requires manual implementation (optional) | Built-in dependency injection framework           |


#### Choosing the Right Framework

* **Choose Flask if:**
    * You need a lightweight and flexible framework.
    * You prioritize rapid development and ease of use.
    * Your project is in Python and you prefer a smaller codebase.
* **Choose ASP.NET Core MVC if:**
    * You need a full-fledged framework with built-in features.
    * You value a structured development environment.
    * Your project is in C# and you want features like dependency injection and strong typing.
    * You primarily develop for Windows (or use .NET Core for cross-platform).

### AQ 5.1

- A user uses ______ to manipulate the ______ that updates the ______ which the user sees.
  - ~~controller, model, view~~ `Struck through to help develop your reasoning`
- Which of the following is/are the area of benefit(s) in MVC architecture?
  - Ability to provide multiple views ~~Yes: Same Data Instance, Multiple Views~~
  - SOC-Separation of concerns ~~Users cannot influence the Model without validation~~
  - Easier to debug. ~~If we know View, We know Controller Path~~

![Mediator Approach](imgs/02-mediator-pattern.png)

  - controller will update the view as per the inputs given by the use
  - The view will determine how the processed data will be displayed to the user.
  - User uses the controller which is able to manipulate the model.

- MVC Properties
  - The model defines what data the app should contain.
  - The controller contains the logic that updates the model. Model is the underlying data structure
  - The view should define how the data is presented to the user and receive the data to display from the models
  - controller updates the view directly in response to input from the users of the app.

- ________ stores the data, ________shows data to the user, and the ________ which takes care of the action.
  - ~~Model, view, controller~~

## [L5.2: Requests and Responses (14.42)](https://youtu.be/K7IJ3n6lPsE)

### Requests and Responses

1. **Definition**: A request is an object that encapsulates the information sent by a client (usually a web browser) to a server, asking for some resource or action.

2. **Components of a Request**:
   - **HTTP Method**: Indicates the type of action to be performed. Common methods include:
     - `GET`: Retrieve data.
     - `POST`: Submit data to be processed.
     - `PUT`: Update existing resources.
     - `DELETE`: Remove resources.
   - **URL**: The endpoint indicating the resource or action. It may include path parameters and query parameters.
   - **Headers**: Additional information about the request (e.g., content type, authorization tokens).
   - **Body**: Data sent with the request, typically used in `POST` or `PUT` requests, often in JSON or form-data format.

3. **Controller Role**:
   - **Routing**: Controllers are often responsible for handling specific routes based on the request method and URL.
   - **Validation**: Controllers may validate request data before processing.
   - **Processing**: Controllers execute the necessary logic to handle the request, interacting with models or services as needed.

#### Responses

1. **Definition**: A response is the data sent back from the server to the client after processing a request. It indicates the outcome of the requested operation.

2. **Components of a Response**:
   - **Status Code**: A numerical code representing the outcome of the request (e.g., `200 OK`, `404 Not Found`, `500 Internal Server Error`).
   - **Headers**: Metadata about the response, such as content type and caching information.
   - **Body**: The actual data being sent back, which can be HTML, JSON, XML, or other formats, depending on the request and the API design.

3. **Controller Role**:
   - **Formatting**: Controllers often format the response data based on the client's needs (e.g., converting data to JSON).
   - **Error Handling**: Controllers manage errors by returning appropriate status codes and messages.
   - **Data Representation**: Controllers may use view models or serializers to structure the response data.

#### Interaction Between Requests and Responses

- **Lifecycle**: The interaction begins when a client makes a request to a server. The server’s routing mechanism directs the request to the appropriate controller action, which processes the request and generates a response. Finally, the server sends the response back to the client.
- **Statelessness**: HTTP is a stateless protocol, meaning each request is independent. Controllers must manage state across requests using mechanisms like sessions or tokens.
- **RESTful Principles**: In RESTful architectures, requests and responses are designed to operate on resources, using standard HTTP methods, URIs, and status codes to indicate outcomes clearly.

#### Best Practices

1. **Consistent Structure**: Maintain a consistent structure for requests and responses, making it easier for clients to interact with the API.
2. **Error Handling**: Implement comprehensive error handling to return meaningful error responses with appropriate status codes.
3. **Validation**: Always validate incoming request data to prevent issues and improve security.
4. **Documentation**: Provide clear API documentation, detailing request formats, expected responses, and possible error codes.

## [L5.3: CRUD (10:58)](https://youtu.be/cHbdUv5nwyY)

### Overview of CRUD in Flask

1. **Create**: Add new records to the database.
2. **Read**: Retrieve existing records from the database.
3. **Update**: Modify existing records in the database.
4. **Delete**: Remove records from the database.

#### Setting Up Flask for CRUD

1. **Install Flask and Required Libraries**:
   - You need Flask and a database toolkit like SQLAlchemy. Install them using pip:
     ```bash
     pip install Flask Flask-SQLAlchemy
     ```

2. **Basic Flask Application Structure**:
   - Create a basic Flask application with a simple folder structure.
   - Example: 
     ```
     /my_flask_app
     ├── app.py
     └── models.py
     ```

3. **Configuration**:
   - Set up your Flask application and configure the database connection in `app.py`:

     ```python
     from flask import Flask
     from flask_sqlalchemy import SQLAlchemy

     app = Flask(__name__)
     app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db'
     db = SQLAlchemy(app)
     ```

#### Defining the Model

In `models.py`, define a model that represents your data. For example, a simple `Item` model:

```python
from app import db

class Item(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    description = db.Column(db.String(200))

    def __repr__(self):
        return f"<Item {self.name}>"
```

#### Implementing CRUD Operations

##### 1. Create

To create a new record, you can use a route that handles POST requests. Here’s an example:

```python
from flask import request, jsonify

@app.route('/items', methods=['POST'])
def create_item():
    data = request.get_json()
    new_item = Item(name=data['name'], description=data['description'])
    db.session.add(new_item)
    db.session.commit()
    return jsonify({'message': 'Item created!', 'item': {'id': new_item.id, 'name': new_item.name}}), 201
```

##### 2. Read

To read records, you can create routes for fetching all items or a specific item:

```python
@app.route('/items', methods=['GET'])
def get_items():
    items = Item.query.all()
    return jsonify([{'id': item.id, 'name': item.name, 'description': item.description} for item in items])

@app.route('/items/<int:item_id>', methods=['GET'])
def get_item(item_id):
    item = Item.query.get_or_404(item_id)
    return jsonify({'id': item.id, 'name': item.name, 'description': item.description})
```

##### 3. Update

To update an existing record, create a route that handles PUT requests:

```python
@app.route('/items/<int:item_id>', methods=['PUT'])
def update_item(item_id):
    item = Item.query.get_or_404(item_id)
    data = request.get_json()
    item.name = data.get('name', item.name)
    item.description = data.get('description', item.description)
    db.session.commit()
    return jsonify({'message': 'Item updated!', 'item': {'id': item.id, 'name': item.name}})
```

##### 4. Delete

To delete a record, create a route that handles DELETE requests:

```python
@app.route('/items/<int:item_id>', methods=['DELETE'])
def delete_item(item_id):
    item = Item.query.get_or_404(item_id)
    db.session.delete(item)
    db.session.commit()
    return jsonify({'message': 'Item deleted!'})
```

#### Running the Application

- Make sure to create the database before running the application. You can do this by executing:
  ```python
  from app import db
  db.create_all()
  ```

- Finally, run your Flask application:
  ```bash
  if __name__ == '__main__':
      app.run(debug=True)
  ```

#### Testing CRUD Operations

You can test your CRUD endpoints using tools like Postman, curl, or directly through a front-end application:

- **Create**: Send a POST request to `/items` with a JSON body like:
  ```json
  {
    "name": "Sample Item",
    "description": "This is a sample item."
  }
  ```

- **Read**: Send GET requests to `/items` or `/items/{id}`.

- **Update**: Send a PUT request to `/items/{id}` with updated JSON data.

- **Delete**: Send a DELETE request to `/items/{id}`.



### API Notes, Python

#### Overview of APIs in Python

1. **Definition**: An API defines a set of rules and conventions for how different software components should interact. In web development, APIs allow clients (like web browsers or mobile apps) to request and manipulate resources on a server.

2. **Types of APIs**:
   - **RESTful APIs**: Follow REST (Representational State Transfer) principles, using standard HTTP methods (GET, POST, PUT, DELETE).
   - **GraphQL APIs**: Allow clients to request only the data they need, using a single endpoint.
   - **SOAP APIs**: Use XML-based messaging protocols, although less common in modern web applications.

3. **Frameworks for Building APIs in Python**:
   - **Flask**: A micro-framework that can be easily extended to build RESTful APIs.
   - **Django REST Framework**: A powerful toolkit for building Web APIs in Django applications.
   - **FastAPI**: A modern framework for building APIs with Python 3.7+ based on standard Python type hints, known for its speed.

#### Building a Simple RESTful API in Flask

1. **Install Flask**:
   ```bash
   pip install Flask
   ```

2. **Basic API Structure**:
   Create a file named `app.py`.

   ```python
   from flask import Flask, jsonify, request

   app = Flask(__name__)

   items = []

   @app.route('/items', methods=['GET'])
   def get_items():
       return jsonify(items)

   @app.route('/items', methods=['POST'])
   def create_item():
       data = request.get_json()
       items.append(data)
       return jsonify(data), 201

   if __name__ == '__main__':
       app.run(debug=True)
   ```

##### Testing the API

You can test this API using tools like Postman or curl.

- **Get all items**: `GET /items`
- **Create an item**: `POST /items` with a JSON body, e.g.:
  ```json
  {
      "name": "Sample Item",
      "description": "This is a sample item."
  }
  ```

##### Best Practices for API Design

1. **Use RESTful Principles**:
   - Use standard HTTP methods: `GET` for retrieval, `POST` for creation, `PUT` for updates, and `DELETE` for deletion.
   - Use proper status codes to indicate the result of API calls (e.g., `200 OK`, `201 Created`, `404 Not Found`, `500 Internal Server Error`).

2. **Consistent URL Structure**:
   - Use clear and meaningful resource names in URLs (e.g., `/items`, `/users`).
   - Follow a consistent naming convention, such as plural nouns for resources.

3. **Version Your API**:
   - Include a version number in the URL (e.g., `/v1/items`) to manage changes over time without breaking existing clients.

4. **Use JSON for Data Exchange**:
   - JSON is widely used and supported across platforms. Ensure your API can send and receive JSON formatted data.

5. **Authentication and Authorization**:
   - Implement proper security measures, such as OAuth2, API keys, or JWT (JSON Web Tokens), to protect sensitive endpoints.

6. **Rate Limiting**:
   - Implement rate limiting to prevent abuse and ensure fair usage of your API.

7. **Error Handling**:
   - Provide meaningful error messages in the response body, including error codes and descriptions. Standardize your error responses.

   ```json
   {
       "error": {
           "code": "NotFound",
           "message": "The requested item was not found."
       }
   }
   ```

8. **Documentation**:
   - Document your API using tools like Swagger/OpenAPI, Postman, or similar platforms to provide clear guidance to developers using your API.

9. **Test Your API**:
   - Use automated testing frameworks like `pytest` or `unittest` to ensure your API functions correctly and consistently.

10. **Performance Optimization**:
   - Implement caching strategies (e.g., using Redis or Memcached) for frequently accessed data to reduce load times and server strain.
   - Optimize database queries to minimize response time.
  


### Presentation Filters

The **Presentation Filter** is a design pattern often used in software architecture, particularly in the context of Model-View-Controller (MVC) and similar patterns. It helps to separate the presentation layer from the business logic, focusing on how data is presented to the user.

#### Overview of Presentation Filter

1. **Definition**: The Presentation Filter is a layer or component that transforms data from the model into a format suitable for the view, allowing for a cleaner separation between how data is structured and how it is displayed.

2. **Purpose**: Its main role is to take raw data from the model and apply formatting, filtering, or transformation to prepare it for presentation. This can include:
   - Formatting dates and numbers.
   - Filtering or aggregating data.
   - Adding or removing properties from the data that the view will use.

3. **Context in MVC**:
   - In the MVC architecture, the **Model** represents the data and business logic, the **View** is responsible for displaying the data, and the **Controller** manages the flow of data between the model and the view.
   - The Presentation Filter acts as an intermediary between the model and the view, ensuring that the view receives data in a suitable format.

#### Implementation of Presentation Filter

Suppose you have a web application that displays a list of products, and each product has a price that needs to be formatted (e.g., displaying it as currency) before showing it to the user.

1. **Model**: Represents the product data.
   ```python
   class Product:
       def __init__(self, name, price):
           self.name = name
           self.price = price  # Raw price as a float
   ```

2. **Presentation Filter**: Transforms the model data into a presentable format.
   ```python
   class ProductPresentationFilter:
       @staticmethod
       def format_product(product):
           return {
               'name': product.name,
               'price': f"${product.price:.2f}"  # Format price as currency
           }
   ```

3. **Controller**: Handles the request and response cycle, using the filter to prepare data for the view.
   ```python
   from flask import Flask, jsonify

   app = Flask(__name__)

   products = [Product("Widget", 19.99), Product("Gadget", 25.50)]

   @app.route('/products', methods=['GET'])
   def get_products():
       filtered_products = [ProductPresentationFilter.format_product(product) for product in products]
       return jsonify(filtered_products)
   ```

4. **View**: Receives the formatted data for rendering.
   - In a web context, this could be an HTML template that uses the formatted data to display products in a user-friendly way.

#### Benefits of Using a Presentation Filter

1. **Separation of Concerns**: By isolating the presentation logic, you keep your business logic clean and maintainable. Changes to how data is displayed do not affect how it is processed.

2. **Reusability**: The presentation filter can be reused across different views or components that require similar data formatting, reducing code duplication.

3. **Testability**: By separating data formatting from business logic, you can independently test your presentation filter, ensuring that the data is formatted correctly without needing to involve the model or view.

4. **Flexibility**: If you need to change how data is presented (e.g., switching from USD to EUR), you only need to update the presentation filter without modifying the underlying data structure.

## [L5.4: Group Actions by Controller (15:15)](https://youtu.be/boQZMoN0TAQ)

### Actions and Controllers
#### Controllers

1. **Definition**: 
   - A controller is a central component of the MVC architecture that handles user requests, interacts with the model, and determines the appropriate response.
   
2. **Responsibilities**:
   - **Routing Requests**: Receives HTTP requests from clients and routes them to the appropriate actions based on the request method (GET, POST, etc.) and the URL path.
   - **Business Logic**: Encapsulates the business logic of the application. It often calls methods on the model to retrieve or manipulate data.
   - **Response Handling**: Prepares and sends the response back to the client, which may include rendering a view or returning JSON data.
   - **Middleware Integration**: Can work with middleware for cross-cutting concerns like authentication, logging, and error handling.

3. **Example in Flask**:
   ```python
   from flask import Flask, request, jsonify

   app = Flask(__name__)

   @app.route('/items', methods=['GET'])
   def get_items():
       # Logic to retrieve items from the model
       return jsonify({'items': []})

   @app.route('/items', methods=['POST'])
   def create_item():
       # Logic to create a new item
       data = request.get_json()
       return jsonify({'message': 'Item created!', 'item': data}), 201
   ```

#### Actions

1. **Definition**: 
   - Actions are specific methods or functions defined within a controller that handle particular tasks or user interactions. They represent the various operations that can be performed in response to user requests.

2. **Responsibilities**:
   - **Perform Specific Operations**: Each action typically corresponds to a specific operation, such as creating, reading, updating, or deleting resources.
   - **Handle Input and Output**: Actions process user input, often validating it, and prepare the output to be returned to the client.
   - **Coordinate with Models**: Actions frequently call model methods to perform business logic related to their specific task.

3. **Example in Flask**:
   ```python
   @app.route('/items/<int:item_id>', methods=['GET'])
   def get_item(item_id):
       # Action to retrieve a specific item by ID
       return jsonify({'item_id': item_id, 'name': 'Sample Item'})

   @app.route('/items/<int:item_id>', methods=['PUT'])
   def update_item(item_id):
       # Action to update an existing item
       data = request.get_json()
       return jsonify({'message': 'Item updated!', 'item_id': item_id})
   ```

#### Key Differences Between Actions and Controllers

1. **Scope**:
   - **Controller**: Represents a broader entity that can encompass multiple actions. It is responsible for routing and managing the overall flow of requests.
   - **Actions**: Are specific functions or methods within a controller that execute particular tasks based on user requests.

2. **Functionality**:
   - **Controller**: May include logic for handling requests, interacting with multiple models, and determining which action to call.
   - **Actions**: Contain the detailed logic for specific operations, such as data validation, processing, and generating responses.

3. **Organization**:
   - Controllers often serve as a namespace for organizing related actions. For instance, you might have a `UserController` with actions like `create_user`, `get_user`, and `delete_user`.

#### Example of a Controller with Actions

In a larger application, you might structure your code like this:

```python
class ItemController:
    @staticmethod
    @app.route('/items', methods=['GET'])
    def get_items():
        # Action logic
        return jsonify({'items': []})

    @staticmethod
    @app.route('/items', methods=['POST'])
    def create_item():
        # Action logic
        data = request.get_json()
        return jsonify({'message': 'Item created!', 'item': data}), 201

    @staticmethod
    @app.route('/items/<int:item_id>', methods=['GET'])
    def get_item(item_id):
        # Action logic
        return jsonify({'item_id': item_id, 'name': 'Sample Item'})

    @staticmethod
    @app.route('/items/<int:item_id>', methods=['PUT'])
    def update_item(item_id):
        # Action logic
        data = request.get_json()
        return jsonify({'message': 'Item updated!', 'item_id': item_id})
```

### URN's URI, URL

In computer networking, **URN**, **URI**, and **URL** are important concepts that deal with identifying resources on the internet.

#### 1. URI (Uniform Resource Identifier)

- **Definition**: A URI is a string of characters that uniquely identifies a resource on the internet, either by location, name, or both.
  
- **Components**: A URI can be further classified into two types:
  - **URL (Uniform Resource Locator)**: Specifies the location of a resource and how to access it.
  - **URN (Uniform Resource Name)**: Specifies a resource by name in a particular namespace but does not indicate its location.

- **Syntax**: A typical URI has the following structure:
  ```
  scheme:[//authority]path[?query][#fragment]
  ```

- **Example**: 
  - `http://example.com/page` is a URL.
  - `urn:isbn:0451450523` is a URN.

#### 2. URL (Uniform Resource Locator)

- **Definition**: A URL is a specific type of URI that provides the means to access a resource on the internet. It specifies the resource's location and the protocol to be used for accessing it (such as HTTP, FTP, etc.).

- **Components**:
  - **Scheme**: Indicates the protocol used (e.g., `http`, `https`, `ftp`).
  - **Host**: The domain name or IP address of the server (e.g., `example.com`).
  - **Path**: The specific location of the resource on the server (e.g., `/page`).
  - **Query**: Optional parameters that can be sent to the server (e.g., `?id=123`).
  - **Fragment**: An optional identifier for a specific part of the resource (e.g., `#section1`).

- **Example**: 
  - `https://www.example.com/path/to/resource?query=example#fragment`
    - **Scheme**: `https`
    - **Host**: `www.example.com`
    - **Path**: `/path/to/resource`
    - **Query**: `query=example`
    - **Fragment**: `#fragment`

#### 3. URN (Uniform Resource Name)

- **Definition**: A URN is a specific type of URI that identifies a resource by name in a particular namespace. It does not provide information on how to access the resource or its location.

- **Purpose**: URNs are intended to serve as persistent, location-independent resource identifiers. They are often used for objects that need to be uniquely identified regardless of their location.

- **Syntax**: A URN typically follows the pattern:
  ```
  urn:<namespace identifier>:<namespace-specific string>
  ```

- **Example**: 
  - `urn:isbn:0451450523` identifies a book by its ISBN number.

#### Recap URN, URI, URL

- **URI**: A broad category that encompasses both URLs and URNs. It is a general identifier for any resource.
  
- **URL**: A specific type of URI that includes the means to access a resource and its location. All URLs are URIs, but not all URIs are URLs.

- **URN**: A type of URI that names a resource without indicating where it can be found or how to access it. It focuses on the identity of the resource.


## [L5.5: Routes and Controllers (20:11)](https://youtu.be/co28E0Go_VA)

### Stateless

Statelessness in HTTP means that each request from a client to a server is treated as an independent transaction, without any stored context from previous requests. This design simplifies server management, as the server does not need to retain information about users between requests.

#### Example:

1. **Basic Request:**
   - A client (like a web browser) sends a request to a server for a webpage. The server processes this request and sends back the webpage. Each time the client requests a different page, it must include all necessary information (like cookies or authentication tokens) because the server doesn’t remember past requests.

2. **Login Example:**
   - When a user logs in, they send their credentials to the server. The server validates the credentials and may send back a session token. On subsequent requests, the client must include this token to maintain the user’s authenticated state. The server doesn’t remember who the user is; it only verifies the token with each request.

In stateless communication, each request is self-contained, promoting scalability and simplifying server architecture, but requiring that clients manage their session state through tokens or cookies.

### Components of Flask App

A Flask app consists of several key components that work together to create a web application. Here’s a brief overview of these components:

#### 1. **Flask Object**
   - The core of a Flask app is the Flask object, typically instantiated like this:
     ```python
     from flask import Flask
     app = Flask(__name__)
     ```

#### 2. **Routes**
   - Routes are used to define the URL patterns that your app responds to. Each route is linked to a function (view function) that handles the request.
     ```python
     @app.route('/')
     def home():
         return 'Hello, Flask!'
     ```

     The "/" is a *decorator*

#### 3. **View Functions**
   - View functions are Python functions that return responses to HTTP requests. They can return strings, HTML, or other types of responses.
     ```python
     @app.route('/about')
     def about():
         return '<h1>About Page</h1>'
     ```

#### 4. **Templates**
   - Flask uses the Jinja2 templating engine to render HTML. Templates allow you to separate the presentation layer from your application logic.
     ```html
     <!-- templates/index.html -->
     <h1>{{ title }}</h1>
     ```

#### 5. **Static Files**
   - Static files (like CSS, JavaScript, and images) are stored in a `static` directory. You can serve these files directly to clients.
     ```html
     <link rel="stylesheet" href="{{ url_for('static', filename='style.css') }}">
     ```

#### 6. **Request and Response Objects**
   - Flask provides `request` and `response` objects to handle incoming data and send responses.
     ```python
     from flask import request
     
     @app.route('/submit', methods=['POST'])
     def submit():
         data = request.form['input_name']
         return f'You submitted: {data}'
     ```

#### 7. **Configuration**
   - Flask apps can be configured through environment variables or a configuration file. This is where you set parameters like database URLs, debug mode, and secret keys.
     ```python
     app.config['DEBUG'] = True
     ```

#### 8. **Extensions**
   - Flask supports many extensions that add functionality, like database integration (Flask-SQLAlchemy), form handling (Flask-WTF), and authentication (Flask-Login).

#### Example Structure:
Here's a simple structure of a Flask app:

```
/my_flask_app
    /static
        style.css
    /templates
        index.html
    app.py
```

### Routing Decorators in Flask


#### 1. **`@app.route()`**
This is the most commonly used decorator. It maps a URL to a function.

**Example:**
```python
@app.route('/')
def home():
    return 'Welcome to the Home Page!'
```

#### 2. **HTTP Method-Specific Decorators**
Flask provides specific decorators for handling different HTTP methods. Here are the most commonly used:

##### a. **`@app.get()`**
Used for handling GET requests.

**Example:**
```python
@app.get('/items')
def get_items():
    return ['item1', 'item2', 'item3']
```

##### b. **`@app.post()`**
Used for handling POST requests.

**Example:**
```python
@app.post('/submit')
def submit_data():
    return 'Data submitted successfully!'
```

##### c. **`@app.put()`**
Used for handling PUT requests.

**Example:**
```python
@app.put('/update/<int:item_id>')
def update_item(item_id):
    return f'Item {item_id} updated successfully!'
```

##### d. **`@app.delete()`**
Used for handling DELETE requests.

**Example:**
```python
@app.delete('/delete/<int:item_id>')
def delete_item(item_id):
    return f'Item {item_id} deleted successfully!'
```

#### 3. **Dynamic Routes**
Flask allows you to define dynamic parts in your routes using angle brackets.

**Example:**
```python
@app.route('/user/<username>')
def show_user(username):
    return f'User: {username}'
```

#### 4. **Route with Multiple Methods**
You can specify multiple HTTP methods that a single route can handle.

**Example:**
```python
@app.route('/item', methods=['GET', 'POST'])
def handle_item():
    if request.method == 'POST':
        return 'Item created!'
    else:
        return 'Retrieve item!'
```

#### 5. **Route with Default Values**
You can provide default values for dynamic segments.

**Example:**
```python
@app.route('/greet/<name>', defaults={'name': 'Guest'})
def greet(name):
    return f'Hello, {name}!'
```

#### 6. **Route with Regular Expressions**
You can also use regular expressions to define more complex routes.

**Example:**
```python
import re

@app.route('/regex/<regex("[a-z]{3}"):shortname>')
def regex_route(shortname):
    return f'Valid shortname: {shortname}'
```


### MVC and Flask - The debate

Flask is often **not** strictly classified as an MVC (Model-View-Controller) framework, primarily because it doesn't enforce the MVC pattern as strictly as some other frameworks do.

#### 1. **Flexibility**
Flask is designed to be lightweight and flexible. While you can implement MVC in a Flask app, the framework doesn't impose a specific structure. Developers have the freedom to organize their code as they see fit, which can lead to different architectural styles.

#### 2. **Absence of Formal Components**
In traditional MVC frameworks:
- **Model**: Manages the data and business logic.
- **View**: Handles the presentation layer.
- **Controller**: Manages user input and interactions.

Flask combines some of these roles:
- The **view** functions in Flask often handle both the controller and the view logic, processing requests and returning responses directly. 
- Flask uses Jinja2 templates for rendering views, but the separation between controller and view is less rigid compared to MVC frameworks like Ruby on Rails or Django.

#### 3. **Customizable Architecture**
Flask encourages a modular architecture, allowing developers to define their structure. You can have different folders for templates, static files, and models, but it's not enforced, leading to various interpretations of how to implement MVC.

#### 4. **Emphasis on Simplicity**
Flask's simplicity and minimalism mean that it focuses more on the essentials of web development rather than adhering to a strict design pattern. This makes it easy to get started, but it also means that developers might not implement MVC in a conventional way.

#### Example:
In a Flask application, you might see code that blends views and controllers:

```python
from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/item/<int:item_id>', methods=['GET', 'POST'])
def item(item_id):
    if request.method == 'POST':
        # Handle form submission (acting as controller)
        return 'Item updated'
    else:
        # Render template (acting as view)
        return render_template('item.html', item_id=item_id)
```

In this example, the `item` function acts as both the controller (handling the request) and the view (returning a rendered template).

While you can implement MVC principles in Flask, the framework's design philosophy promotes flexibility and simplicity over strict adherence to any particular architectural pattern. This allows developers to choose their preferred approach, making Flask suitable for a wide range of applications.


### WSGI

WSGI, or Web Server Gateway Interface, is a specification for a universal interface between web servers and Python web applications or frameworks. It acts as a bridge that allows a web server to communicate with web applications, facilitating the development and deployment of web applications in Python.

#### Key Concepts of WSGI

1. **Specification**
   - WSGI is defined in PEP 333 and later versions. It specifies how a web server should communicate with a Python web application and vice versa.

2. **Two Parts**
   - **Server/Gateway**: This part is responsible for receiving HTTP requests and passing them to the application.
   - **Application**: This is the Python callable (usually a function or a class) that processes the request and returns a response.

#### WSGI Application Structure

A WSGI application must be a callable (like a function or a class with a `__call__` method) that accepts two arguments:

- **environ**: A dictionary containing all the request information (HTTP headers, request method, etc.).
- **start_response**: A callback function that starts the HTTP response.

**Example of a Simple WSGI Application:**
```python
def simple_app(environ, start_response):
    status = '200 OK'  # HTTP status
    headers = [('Content-Type', 'text/plain')]
    start_response(status, headers)

    return [b'Hello, WSGI!']  # Response body must be bytes
```

#### How WSGI Works

1. **Request Handling**: When a request comes in, the WSGI server calls the WSGI application with the `environ` dictionary and the `start_response` function.
2. **Response Generation**: The application processes the request and generates a response, which is sent back through the `start_response` function and returned as an iterable (usually a list of byte strings).

#### WSGI Servers

Several servers implement the WSGI specification, allowing you to run WSGI applications. Some popular ones include:

- **Gunicorn**: A Python WSGI HTTP server for UNIX.
- **uWSGI**: A versatile server that can serve WSGI applications and also supports various other protocols.
- **Flask's built-in server**: While not suitable for production, it serves WSGI applications for development purposes.

#### WSGI Middleware

WSGI middleware is a layer that can be added between the server and the application. Middleware can process requests and responses, allowing for functionality like session management, authentication, logging, and more.

**Example of Middleware:**
```python
def simple_middleware(app):
    def wrapped_app(environ, start_response):
        # Do something before the request
        print("Before request")
        
        # Call the actual WSGI app
        response = app(environ, start_response)

        # Do something after the request
        print("After request")
        
        return response
    
    return wrapped_app
```

WSGI provides a standardized interface for web servers and Python applications, promoting compatibility and flexibility in web development. It enables developers to build portable web applications that can run on any WSGI-compliant server, facilitating the deployment and scaling of Python web applications.


| Library/Toolkit | Description                                         |
|------------------|-----------------------------------------------------|
| **Gunicorn**     | A lightweight WSGI server for UNIX, simple and efficient. |
| **uWSGI**        | A versatile application server that supports multiple protocols, highly configurable. |
| **Waitress**     | A pure Python WSGI server known for simplicity and ease of use. |
| **Daphne**       | Supports HTTP, HTTP2, and WebSocket protocols, primarily for ASGI but can serve WSGI apps. |
| **CherryPy**     | An object-oriented web framework with its own WSGI server. |
| **Mod_wsgi**     | An Apache module that allows hosting Python WSGI applications in Apache. |
| **Falcon**       | A high-performance framework for building REST APIs, with WSGI compatibility. |
| **Pyramid**      | A flexible and modular web framework that can run on any WSGI server. |
| **Zope**         | An application server and web framework with WSGI support. |
| **Tornado**      | A web framework and asynchronous networking library, can act as a WSGI server. |
| **Bjoern**       | A lightweight and high-performance WSGI server. |
| **Twisted**      | An event-driven networking engine that can serve WSGI applications. |
| **Werkzeug**     | A comprehensive WSGI toolkit that provides utilities for building WSGI applications, including a built-in development server. |

#### Werkzeug Overview
- **Description**: Werkzeug is not only a WSGI server but also a toolkit that provides utilities for creating and handling WSGI applications. It includes a development server, routing, request and response objects, and various utilities for building web applications.
- **Usage**: It's often used as the foundation for frameworks like Flask, making it an essential part of the WSGI landscape.

### SQL Alchemy relations

SQLAlchemy supports several types of relationships that define how tables in a database interact with one another. Understanding these relationships is crucial for designing a well-structured database schema. Here are the main types of relationships supported by SQLAlchemy, along with examples:

#### 1. **One-to-Many Relationship**
In a one-to-many relationship, one record in a parent table can be associated with multiple records in a child table.

**Example:**
Consider a `User` table and a `Post` table, where one user can have multiple posts.

```python
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class User(Base):
    __tablename__ = 'users'
    
    id = Column(Integer, primary_key=True)
    name = Column(String)
    
    posts = relationship("Post", back_populates="user")

class Post(Base):
    __tablename__ = 'posts'
    
    id = Column(Integer, primary_key=True)
    title = Column(String)
    user_id = Column(Integer, ForeignKey('users.id'))
    
    user = relationship("User", back_populates="posts")
```

#### 2. **Many-to-One Relationship**
This is the inverse of a one-to-many relationship. Many records in a child table can relate to one record in a parent table.

**Example:**
Using the same `Post` and `User` example, each post is related to one user.

```python
# See above example; the relationship in the Post class shows many posts can relate to one user.
```

#### 3. **Many-to-Many Relationship**
In a many-to-many relationship, multiple records in one table can relate to multiple records in another table. This is typically managed through an association table.

**Example:**
Consider a `Student` table and a `Course` table, where students can enroll in multiple courses, and courses can have multiple students.

```python
from sqlalchemy import Table

enrollment = Table('enrollment', Base.metadata,
    Column('student_id', Integer, ForeignKey('students.id')),
    Column('course_id', Integer, ForeignKey('courses.id'))
)

class Student(Base):
    __tablename__ = 'students'
    
    id = Column(Integer, primary_key=True)
    name = Column(String)
    courses = relationship("Course", secondary=enrollment, back_populates="students")

class Course(Base):
    __tablename__ = 'courses'
    
    id = Column(Integer, primary_key=True)
    title = Column(String)
    students = relationship("Student", secondary=enrollment, back_populates="courses")
```

#### 4. **One-to-One Relationship**
In a one-to-one relationship, one record in a table is associated with one record in another table. This can be implemented by using a unique foreign key constraint.

**Example:**
Consider a `User` table and a `Profile` table where each user has exactly one profile.

```python
class Profile(Base):
    __tablename__ = 'profiles'
    
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('users.id'), unique=True)
    bio = Column(String)
    
    user = relationship("User", back_populates="profile")

User.profile = relationship("Profile", uselist=False, back_populates="user")
```

#### Summary of Relationships
| Relationship Type | Description                                      |
|-------------------|--------------------------------------------------|
| One-to-Many       | One record in the parent can have multiple child records. |
| Many-to-One       | Many records in the child relate to one parent record. |
| Many-to-Many      | Many records in one table relate to many records in another table, using an association table. |
| One-to-One        | One record in one table relates to exactly one record in another table. |


### Connecting to DataBase

SQLAlchemy connects to a database engine using a connection string that specifies the database type, user credentials, host, and database name. This connection string is used to create an engine, which serves as the starting point for any SQLAlchemy application.

#### Steps to Connect to a Database Engine with SQLAlchemy

1. **Install SQLAlchemy**
   First, ensure that you have SQLAlchemy installed. You can also install the database driver for your specific database (e.g., psycopg2 for PostgreSQL, pymysql for MySQL).

   ```bash
   pip install SQLAlchemy
   pip install psycopg2  # For PostgreSQL
   pip install pymysql    # For MySQL
   ```

2. **Import Necessary Components**
   You need to import the `create_engine` function from SQLAlchemy.

   ```python
   from sqlalchemy import create_engine
   ```

3. **Create the Database Engine**
   Use the `create_engine()` function with the appropriate connection string to establish a connection to the database.

   **Example Connection Strings:**
   - **PostgreSQL**: 
     ```python
     engine = create_engine('postgresql://user:password@localhost/mydatabase')
     ```
   - **MySQL**:
     ```python
     engine = create_engine('mysql+pymysql://user:password@localhost/mydatabase')
     ```
   - **SQLite**:
     ```python
     engine = create_engine('sqlite:///mydatabase.db')
     ```

4. **Using the Engine to Connect**
   After creating the engine, you can use it to connect to the database and execute queries. Here’s a simple example demonstrating this.

#### Full Example: Connecting to a SQLite Database

```python
from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# Define the base class for declarative models
Base = declarative_base()

# Define a sample model
class User(Base):
    __tablename__ = 'users'
    
    id = Column(Integer, primary_key=True)
    name = Column(String)
    
    def __repr__(self):
        return f"<User(name='{self.name}')>"

# Create a SQLite database engine
engine = create_engine('sqlite:///mydatabase.db', echo=True)

# Create all tables in the database (if they don't exist)
Base.metadata.create_all(engine)

# Create a new session
Session = sessionmaker(bind=engine)
session = Session()

# Add a new user to the database
new_user = User(name='John Doe')
session.add(new_user)
session.commit()

# Query the database
for user in session.query(User).all():
    print(user)

# Close the session
session.close()
```

#### Explanation of the Example

1. **Creating the Engine**: 
   The `create_engine` function establishes a connection to a SQLite database called `mydatabase.db`. The `echo=True` flag enables logging of all SQL statements.

2. **Defining a Model**: 
   The `User` class defines a model that represents the `users` table.

3. **Creating the Tables**: 
   `Base.metadata.create_all(engine)` creates the tables defined in the model if they don't already exist in the database.

4. **Creating a Session**: 
   A session is created using `sessionmaker`, which provides a workspace for database operations.

5. **Adding and Committing Data**: 
   A new user is added to the session and committed to the database.

6. **Querying Data**: 
   The application queries the `User` table and prints each user.

7. **Closing the Session**: 
   It’s good practice to close the session after operations are completed.

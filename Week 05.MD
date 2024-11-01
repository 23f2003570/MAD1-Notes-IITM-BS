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


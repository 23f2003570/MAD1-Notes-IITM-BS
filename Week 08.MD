# Week 8

*Prof. Nitin Chandrachoodan*  
*Department of EE, IIT Madras*  

*Notes by Adarsh (23f2003570)*  


## [L 8.1]()

### **Key Concepts of Asynchronous Web Front-ends:**

1. **Asynchronous Programming**:  
   In traditional (synchronous) web applications, requests to the server, such as fetching data, are processed one at a time. This means the user has to wait until the server sends back a response before they can interact with the application again. Asynchronous programming allows requests to be handled "in the background" without blocking the user interface, enabling the user to interact with the page while other tasks are ongoing.

2. **Event Loop**:  
   At the heart of asynchronous programming is the **event loop**, which manages and schedules tasks. When an asynchronous task (e.g., an HTTP request) is initiated, the event loop does not wait for the task to complete. Instead, it continues processing other tasks. When the asynchronous task finishes, it triggers an event that is handled by a callback function.

3. **Promises**:  
   Promises are objects representing the eventual completion (or failure) of an asynchronous operation. They provide a cleaner way to handle asynchronous operations by allowing you to chain `.then()` methods or use `async`/`await` syntax for more readable code.

4. **Callback Functions**:  
   These are functions that are passed as arguments to other functions and executed after the completion of an asynchronous operation. While callbacks are a fundamental part of asynchronous programming, they can lead to "callback hell" (deeply nested callbacks), which is why promises and `async/await` syntax are preferred in modern JavaScript.

5. **AJAX (Asynchronous JavaScript and XML)**:  
   AJAX is a technique used in web development that allows web pages to fetch and send data to the server asynchronously, without reloading the entire page. It uses technologies like **XMLHttpRequest** or the more modern **Fetch API**.

6. **Fetch API**:  
   The Fetch API is a modern JavaScript API for making HTTP requests asynchronously. It returns a **Promise** and provides a more powerful and flexible interface for handling responses than older technologies like `XMLHttpRequest`.

#### **Advantages of Asynchronous Web Frontends:**

1. **Improved User Experience (UX)**:  
   Asynchronous frontends make the application feel faster and more responsive. For example, a page can update with new content or allow users to interact with elements while waiting for data from the server.

2. **Non-blocking UI**:  
   Asynchronous operations, like fetching data or submitting forms, do not freeze the interface. Users can continue interacting with other parts of the page (scrolling, clicking, etc.) while background tasks complete.

3. **Better Performance**:  
   Asynchronous operations can improve the performance of web applications by making better use of the user's resources. They allow tasks like fetching data or making API calls to occur without blocking the rendering of the page, leading to smoother experiences.

4. **Parallel Requests**:  
   Asynchronous web frontends enable multiple requests to be made in parallel. For example, you can fetch several resources (like images, data, etc.) at the same time, rather than waiting for one request to complete before initiating the next.

5. **Reduced Latency**:  
   By loading parts of a webpage asynchronously, the content can be shown faster. The browser does not need to wait for all resources (images, scripts, data) to load before rendering the page.

#### **Common Techniques for Asynchronous Web Frontends:**

1. **AJAX (Asynchronous JavaScript and XML)**:
   - **XMLHttpRequest (XHR)**: Traditional way of making asynchronous requests in JavaScript.
   - **Fetch API**: Modern approach to AJAX for making HTTP requests. It returns Promises, which simplifies the handling of asynchronous operations.

2. **`async`/`await` Syntax**:
   This allows asynchronous code to be written in a more synchronous-looking manner, making it easier to read and maintain.

   ```javascript
   async function fetchData() {
     try {
       let response = await fetch('https://api.example.com/data');
       let data = await response.json();
       console.log(data);
     } catch (error) {
       console.error('Error fetching data:', error);
     }
   }
   ```

3. **Web Workers**:
   Web Workers allow you to run JavaScript code in the background on a separate thread, independent of the main browser thread. This is useful for offloading computationally intensive tasks (like data processing) to prevent blocking the UI.

4. **Promises**:
   Promises are used to handle asynchronous operations in a more manageable way than callbacks. Promises allow you to chain `.then()` calls or use `async`/`await` for more readable asynchronous code.

   ```javascript
   // Using Promises with Fetch API
   fetch('https://api.example.com/data')
     .then(response => response.json())
     .then(data => console.log(data))
     .catch(error => console.error('Error:', error));
   ```

5. **React, Vue, and Angular**:
   These modern JavaScript frameworks/libraries are designed with asynchronous programming in mind. They make it easy to build reactive UIs where components are updated asynchronously, based on state or data changes.

   - **React**: React provides hooks like `useEffect` to handle asynchronous tasks (e.g., fetching data) and update components accordingly.
   - **Vue**: Vue provides mechanisms like `async` lifecycle hooks and reactive data handling that makes dealing with asynchronous operations easier.
   - **Angular**: Angular has built-in support for asynchronous operations using `RxJS` for handling streams of data asynchronously.

#### **Asynchronous Workflow in Web Frontends:**

1. **Initial Page Load**:  
   When a user loads a page, only the essential HTML, CSS, and JavaScript are loaded initially. The web page makes asynchronous requests for additional data, images, or resources.

2. **Making Asynchronous API Calls**:  
   Web frontends often need to make API calls to fetch data for displaying in the UI. This is done asynchronously using **AJAX**, **Fetch API**, or **Axios**.

3. **Rendering Content**:  
   Once the data is fetched, the frontend updates the DOM to render the new data. This might be a partial update (such as adding a new comment to a list) or a full page update (like loading a new set of results in a search).

4. **User Interaction**:  
   Asynchronous operations enable users to interact with the page without waiting for a long-running task to finish. For example, users can type in a search box while the app fetches suggestions or can continue browsing while images load in the background.

5. **Event Handling**:  
   User actions like clicks or form submissions can trigger asynchronous operations such as fetching data or posting updates. These events are handled without blocking the UI.

#### **Examples of Asynchronous Web Frontends:**

##### **Example 1: Fetching Data from an API with `fetch`**
```javascript
async function loadPosts() {
  const response = await fetch('https://jsonplaceholder.typicode.com/posts');
  const posts = await response.json();
  const postsContainer = document.getElementById('posts');
  
  posts.forEach(post => {
    const postElement = document.createElement('div');
    postElement.textContent = post.title;
    postsContainer.appendChild(postElement);
  });
}
loadPosts();
```

##### **Example 2: Using `async`/`await` for Smooth Data Fetching**
```javascript
async function getUserData(userId) {
  try {
    let response = await fetch(`https://api.example.com/users/${userId}`);
    let data = await response.json();
    document.getElementById('user-name').textContent = data.name;
  } catch (error) {
    console.error('Error fetching user data:', error);
  }
}
```

##### **Example 3: AJAX Request with jQuery**
```javascript
$.ajax({
  url: 'https://jsonplaceholder.typicode.com/posts',
  type: 'GET',
  success: function(data) {
    console.log(data);
  },
  error: function(error) {
    console.error('Error:', error);
  }
});
```

#### **Best Practices for Asynchronous Web Frontends:**

1. **Handle Errors Gracefully**:
   Always include error handling in asynchronous requests (using `try/catch` with `async/await` or `.catch()` with Promises) to manage failed API calls or unexpected conditions.

2. **Loading Indicators**:
   Provide users with feedback (like a loading spinner) while data is being fetched asynchronously, so they know something is happening in the background.

3. **Caching**:
   Implement caching strategies (e.g., using `localStorage` or service workers) to reduce redundant network requests and improve load times for frequent actions.

4. **Optimistic UI**:
   For actions like form submissions or data updates, show an immediate update to the UI, even before the backend confirms the success, for a snappier experience (e.g., showing a new comment without waiting for the server to respond).

5. **Avoid Blocking the UI**:
   Avoid long-running tasks or synchronous blocking code that can freeze the UI. Offload heavy operations to Web Workers or use **debouncing**/**throttling** to manage user inputs.


## [L8.3: Browser/Client operations]()

#### Notes on Cookies

The **lifecycle of cookies** refers to the series of stages a cookie goes through, from creation to expiration or deletion, as it interacts with a user's web browser. A cookie is a small piece of data that is sent from a server and stored on the user's device to remember information about the user's interaction with the website. Here's a breakdown of the typical cookie lifecycle:

#### 1. **Cookie Creation**
   - **Set by the server or JavaScript**: A cookie is created either by the server when it sends a `Set-Cookie` header in the HTTP response or through JavaScript running in the browser. The server might set cookies to track user sessions, preferences, authentication tokens, etc.
   - **Attributes**: A cookie can have various attributes that define its behavior:
     - **Name**: The name of the cookie.
     - **Value**: The data the cookie holds (such as a user ID or session ID).
     - **Domain**: The domain that can access the cookie. By default, this is the domain that set the cookie, but it can be scoped to subdomains.
     - **Path**: Specifies the URL path where the cookie is accessible. By default, it's available to all paths on the domain.
     - **Expires/Max-Age**: The expiration time of the cookie. If not set, it is a session cookie, which expires when the browser is closed.
     - **Secure**: Indicates the cookie should only be sent over HTTPS.
     - **HttpOnly**: Prevents access to the cookie from JavaScript, increasing security against XSS (Cross-Site Scripting) attacks.
     - **SameSite**: Restricts how cookies are sent with cross-site requests to prevent CSRF (Cross-Site Request Forgery) attacks. Can have values like `Strict`, `Lax`, or `None`.

#### 2. **Cookie Storage**
   - Once created, cookies are stored by the browser in a specific location (usually within the browser's cookie storage).
   - Each subsequent HTTP request to the server includes cookies associated with the domain, sent in the `Cookie` header, allowing the server to recognize returning users, maintain sessions, and store user preferences.

#### 3. **Cookie Usage**
   - **Session cookies**: These are temporary cookies stored only for the duration of the session (while the browser is open). Once the browser is closed, session cookies are deleted.
   - **Persistent cookies**: These cookies remain on the user's device until they either expire (based on the `Expires` or `Max-Age` attribute) or the user manually deletes them.
   - **Third-party cookies**: These cookies are set by domains other than the one the user is currently visiting. For example, cookies set by advertisers for tracking purposes across different websites.
   - **Cookie management by browsers**: Modern browsers allow users to manage cookies, including blocking or deleting specific cookies or all cookies, as well as controlling third-party cookies.

#### 4. **Cookie Expiration**
   - **Expiration date**: If a cookie is a **persistent cookie**, it will have an expiration date specified using the `Expires` or `Max-Age` attribute. When that date is reached, the cookie is automatically deleted.
   - **Session cookies**: These cookies do not have an expiration date. They exist only for the duration of the session, i.e., as long as the browser is open. When the user closes the browser, session cookies are automatically deleted.

#### 5. **Cookie Deletion**
   - **Automatic deletion**: When the cookie's expiration date has passed or when the session ends (for session cookies), the browser automatically deletes the cookie from its storage.
   - **Manual deletion**: Users can delete cookies through their browser settings. In addition, web developers can delete cookies by setting the cookie's expiration date to a past date using JavaScript (e.g., `document.cookie = "cookieName=; expires=Thu, 01 Jan 1970 00:00:00 UTC;"`).
   - **Programmatic deletion**: Websites or applications can also delete cookies by modifying or overwriting them through JavaScript, usually by setting the cookie’s expiration date to a time in the past.

#### 6. **Cookie Renewal (Recreation)**
   - When a cookie is deleted or expired, it can be recreated by the server or by JavaScript during subsequent requests or actions from the user. For example, when a user logs back in to a website, a new session cookie may be set, or when a user revisits a site, cookies may be re-set to remember preferences or settings.

#### Summary of the Cookie Lifecycle:

1. **Creation**: Cookie is created by the server or JavaScript and sent to the browser.
2. **Storage**: The cookie is stored by the browser, associated with a specific domain.
3. **Usage**: Cookies are sent with requests to the server, providing useful information such as session IDs, user preferences, or tracking data.
4. **Expiration**: The cookie expires either when the session ends or when the expiration time is reached.
5. **Deletion**: The cookie is deleted either automatically (when it expires or the session ends) or manually by the user or developer.
6. **Renewal**: The cookie may be recreated during subsequent user activity, continuing the lifecycle.

Cookies are essential for many web features, like user authentication and tracking preferences, but they also raise privacy concerns, especially when it comes to third-party cookies used for tracking across websites. Therefore, privacy laws such as the **GDPR** (General Data Protection Regulation) and **CCPA** (California Consumer Privacy Act) require websites to provide clear disclosures and obtain consent before setting certain types of cookies.


## [L8.4: Client side computations and Security Implications(17:21)](https://youtu.be/drX5zQtoRZE)

### Client Validation

1. **Built-in form validation**: HTML5 attributes like `required`, `type="email"` automatically validate input.  
   Example: `<input type="email" required>`

2. **Validating against a regular expression**: Use the `pattern` attribute to enforce a custom regex.  
   Example: `<input pattern="\d{3}-\d{2}-\d{4}" required>`

3. **Constraining length, value**: Use `minlength`, `maxlength`, `min`, `max`.  
   Example: `<input minlength="5" maxlength="10" required>`

4. **The Constraint Validation API**: Use `checkValidity()` to check if a form is valid.  
   Example: `form.checkValidity()`

5. **Customized error message**: Set a custom message with `setCustomValidity()`.  
   Example: `input.setCustomValidity("Invalid entry.")`

6. **Extending built-in validation**: Add custom validation logic with JavaScript.  
   Example: `if (input.value.length < 5) { input.setCustomValidity("Too short!"); }`

7. **Custom Validation**
   1. Setting the `novalidate` attribute on the form stops the form from showing its own error message bubbles, and allows us to instead display the custom error messages in the DOM in some manner of our own choosing.
   2. However, this doesn't disable support for the constraint validation API nor the application of CSS pseudo-classes like :valid, etc.
   3. That means that even though the browser doesn't automatically check the validity of the form before sending its data, you can still do it yourself and style the form accordingly.
   4. `<form novalidate>`
   5. See [Week09/01-custom-validation-messages.html](Extra/Work/Code/Week09/01-custom-validation-messages.html)
   
### CAPTCHA

**CAPTCHA (Completely Automated Public Turing test to tell Computers and Humans Apart)** is a security measure used to verify if a user is human or a bot. It prevents automated abuse of websites.

**Notes**
1. With the help of CAPTCHA, we can easily differentiate between real humans and bots.
2. Ticketing systems like railway tatkal also use CAPTCHA to limit frauds from writing scripts and from purchasing large number of tickets before anyone else does.
3. Some CAPTCHA types may be difficult to understand for some users which sometimes leads to frustration among them.

#### Implementation:
- **Google reCAPTCHA**: Simple integration using JavaScript API.
- **Custom CAPTCHA**: Generate images with distorted text or math problems and validate responses on the server.

#### Best Practices:
1. **Avoid Overuse**: Implement CAPTCHA only where necessary (e.g., login, registration).
2. **Accessibility**: Ensure CAPTCHA is accessible to screen readers and offers alternatives like audio.
3. **Performance**: Optimize CAPTCHA loading time to minimize user friction.
4. **Easy for Humans, Hard for Bots**: Balance complexity—make it hard for bots but not too difficult for users.


### Crypto Mining

Crypto-mining in HTML/JS generally works by running complex mathematical algorithms (like Proof of Work) using a user's CPU to mine cryptocurrencies. The mining process involves solving cryptographic puzzles, which helps validate transactions on a blockchain. In a mining script, JavaScript performs computations, utilizing the browser’s resources.

However, it’s important to note that unauthorized or hidden crypto-mining scripts (often referred to as "cryptojacking") can harm devices and are unethical.

For educational purposes, you could study how mining algorithms like SHA-256 or Ethash work in blockchain networks.

### Sandboxing

**Sandboxing** in JavaScript refers to executing code in a restricted environment to prevent it from accessing sensitive resources or interacting with the rest of the system. This isolates potentially harmful code (e.g., in a browser) from damaging the user's data or compromising security. In the context of web browsers, JavaScript runs within a "sandbox" that prevents it from accessing local files, modifying system settings, or interacting with other tabs.

- A sandbox environment is a secure area that a JavaScipt engine has access to.
- A sandbox cannot access any local storage file outside of it.

Common uses of sandboxing include:
- **Web Workers**: Isolate background tasks.
- **iframes with `sandbox` attribute**: Limit actions inside embedded content.

### Distributed Denial of Service

**DDoS (Distributed Denial-of-Service)** is an attack where multiple systems flood a target with traffic, overwhelming its resources and making it unavailable to legitimate users. These attacks can be disruptive, impacting websites and services.

**Best practices to prevent DDoS**:
1. **Rate Limiting**: Control the number of requests a user can make in a certain time period.
2. **Traffic Filtering**: Use firewalls and intrusion prevention systems to filter malicious traffic.
3. **Load Balancing**: Distribute traffic across multiple servers to handle large spikes.
4. **Cloud-based DDoS protection**: Use services like Cloudflare or AWS Shield for extra defense.
5. **Monitoring and Alerts**: Continuously monitor traffic to detect unusual spikes.

### Access to Resources

JavaScript can access local resources like **storage** (LocalStorage, SessionStorage), **sensors** (geolocation, accelerometer), and **files** (File API) with the proper permissions.

#### Examples:
1. **LocalStorage**: 
   ```javascript
   localStorage.setItem('name', 'John');
   let name = localStorage.getItem('name');
   console.log(name);  // Outputs: John
   ```

2. **Geolocation** (Accessing device's location):
   ```javascript
   navigator.geolocation.getCurrentPosition(function(position) {
       console.log(position.coords.latitude, position.coords.longitude);
   });
   ```

3. **File Access** (Reading user-selected files):
   ```javascript
   let fileInput = document.querySelector('input[type="file"]');
   fileInput.addEventListener('change', function(event) {
       let file = event.target.files[0];
       let reader = new FileReader();
       reader.onload = function(e) {
           console.log(e.target.result);  // Displays file content
       };
       reader.readAsText(file);
   });
   ```

These APIs are subject to user consent or browser security policies.

1. **Storage**: LocalStorage, SessionStorage, IndexedDB
2. **Sensors**: Geolocation, DeviceOrientation, DeviceMotion
3. **Camera and Microphone**: `navigator.mediaDevices.getUserMedia()`
4. **Network**: Network Information API
5. **Battery**: Battery Status API
6. **File System**: File API (for reading user files)
7. **Clipboard**: Clipboard API
8. **Notifications**: Push Notifications API
9. **Vibration**: Vibration API

These features often require user consent, and some may be restricted in certain browsers or contexts.

### HTML5 Input types

1. **email** – Validates an email address.
2. **url** – Validates a URL.
3. **tel** – Validates a telephone number.
4. **number** – Validates numeric input.
5. **range** – Validates a range of numbers.
6. **date** – Validates a date input.
7. **time** – Validates a time input.
8. **datetime-local** – Validates a local date and time.
9. **month** – Validates a month and year.
10. **week** – Validates a week and year.
11. **search** – Validates a search term.


## [Screencast 8.1: Introduction to Indexing(08:16)](https://youtu.be/s4aUyLhHS50)

A **database index** is a data structure that improves the speed of data retrieval operations on a database table. It works similarly to an index in a book, allowing the database to quickly locate rows based on a specific column (or combination of columns). Indexes are particularly useful for speeding up search queries, but they can slow down insertions, updates, and deletions because the index needs to be updated as well. Common types of indexes include B-trees and hash indexes.

In Flask-SQLAlchemy, you can create indices by using the `index` argument within the column definition or by creating them explicitly through the `Index` class.

#### Example of creating an index on a column:
```python
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(120), unique=True, index=True)  # Index created here
```

#### Creating a multi-column index:
```python
from sqlalchemy import Index

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(120), unique=True)
    username = db.Column(db.String(80))

    __table_args__ = (Index('ix_email_username', 'email', 'username'),)
```

### QUERY PLANS

```sql
EXPLAIN QUERY PLAN SELECT * FROM users WHERE email = 'example@example.com';
```

One can also set the CLI into automatic EXPLAIN QUERY PLAN mode using the ".eqp on" command:
`sqlite> .eqp on`

#### Full Table scan
```sql
sqlite> EXPLAIN QUERY PLAN SELECT a, b FROM t1 WHERE a=1;
QUERY PLAN
`--SCAN t1
```

#### Using Index (Non Covering)

```sql
sqlite> CREATE INDEX i1 ON t1(a);
sqlite> EXPLAIN QUERY PLAN SELECT a, b FROM t1 WHERE a=1;
QUERY PLAN
`--SEARCH t1 USING INDEX i1 (a=?)
```

#### Using Index (Covering Index)
```sql
sqlite> CREATE INDEX i2 ON t1(a, b);
sqlite> EXPLAIN QUERY PLAN SELECT a, b FROM t1 WHERE a=1; 
QUERY PLAN
`--SEARCH t1 USING COVERING INDEX i2 (a=?)
```

### Where

If the WHERE clause of a query contains an OR expression, then SQLite might use the "OR by union" strategy (also known as the OR optimization). In this case there will be single top-level record for the search, with two sub-records, one for each index:

```sql
sqlite> CREATE INDEX i3 ON t1(b);
sqlite> EXPLAIN QUERY PLAN SELECT * FROM t1 WHERE a=1 OR b=2;
QUERY PLAN
`--MULTI-INDEX OR
   |--SEARCH t1 USING COVERING INDEX i2 (a=?)
   `--SEARCH t1 USING INDEX i3 (b=?)
```

Query Plans provides a detailed report of how SQLite will execute the query

- **Use of Indexes**: Ideally, the query should use an index for efficiency.
- **Table Scans**: If it’s scanning the entire table, consider adding an index on the relevant columns.
- **Joins**: Check if joins are optimized, using indexes or efficient algorithms.

### Covered Index

A **Covered Index** refers to an index that contains all the columns required to satisfy a query, meaning SQLite can retrieve the data directly from the index without accessing the table itself. This improves performance because reading from an index is faster than accessing the table's rows.

For example, if a query only needs to retrieve columns that are part of the index, SQLite can return the data from the index, avoiding an additional lookup in the table. This is often used for queries with `SELECT` statements that filter and return specific indexed columns.

```SQL
CREATE TABLE users (
    id INTEGER PRIMARY KEY,
    name TEXT,
    email TEXT
);
CREATE INDEX idx_email_name ON users (email, name);
SELECT email, name FROM users WHERE email = 'example@example.com';
```

### Full Text Search

To support **Full Text Search (FTS)** in Flask-SQLAlchemy with SQLite, you need to create a virtual table using SQLite's **FTS** extension

#### Step 1: Enable FTS5 in SQLite
SQLite provides FTS3/FTS5 for full-text indexing. In Flask-SQLAlchemy, you can use `SQLAlchemy`'s support for virtual tables.

#### Example Implementation:

1. **Define a Model with FTS5**:
```python
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class FTSUser(db.Model):
    __tablename__ = 'fts_user'
    __searchable__ = ['name', 'email']  # Columns to be indexed

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    email = db.Column(db.String(100))

    __table_args__ = (
        db.Index('idx_full_text', 'name', 'email'),
        {'sqlite_autoincrement': True}
    )
```

2. **Perform a Full-Text Search**:
```python
result = db.session.execute(
    "SELECT * FROM fts_user WHERE fts_user MATCH :search_query",
    {"search_query": "example@example.com"}
).fetchall()
```


3. 
```python
ArticleSearch.query.filter(ArticleSearch.content.op('MATCH')(q)).all()
```

### Virtual Table

A **virtual table** in SQLite is a table-like structure that doesn’t directly store data in the usual way. Instead, it acts as an interface to data stored outside SQLite or in special forms, like full-text search indexes. Virtual tables are implemented using SQLite’s virtual table mechanisms (e.g., FTS, RTree, or custom virtual tables), allowing flexible interaction with different data sources or specialized functionality. They can be queried like regular tables but offer more advanced features, such as full-text indexing or custom search capabilities.



### Tokenizers

SQLite FTS5 provides several tokenizers, each with different behaviors:

1. **Simple Tokenizer** (`simple`): Splits text based on whitespace and punctuation.
2. **Unicode Tokenizer** (`unicode61`): A Unicode-aware tokenizer.
3. **ICU Tokenizer** (`icu`): Uses the ICU library for more complex language-specific tokenization.
4. **Spellfix Tokenizer** (`spellfix1`): Supports spell-checking features.
5. **Custom Tokenizer** (`custom`): Allows creating user-defined tokenizers.

Each tokenizer has specific use cases depending on the type of text data you're indexing. You can select the tokenizer during table creation in FTS5.


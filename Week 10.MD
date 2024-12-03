# Week 10

*Prof. Nitin Chandrachoodan*  
*Department of EE, IIT Madras*  

*Notes by Adarsh (23f2003570)*  


## [L 10.1: Application testing (28:28)](https://youtu.be/fgWIn388NyQ)

### PyTest
Pytest is a powerful testing framework for Python that makes it easy to write simple and scalable test cases. It is widely used because of its simplicity, flexibility, and rich feature set.

#### 1. **Installation**

To get started with Pytest, you need to install it. You can install it using `pip`:

```bash
pip install pytest
```

Once installed, you can use the `pytest` command in the terminal to run tests.

#### 2. **Writing Test Functions**

A test in Pytest is simply a Python function prefixed with `test_`. Pytest automatically discovers test functions by searching for functions whose names start with `test_`. These test functions contain assertions to check whether the code behaves as expected.

##### Example:

```python
def test_addition():
    assert 1 + 1 == 2

def test_subtraction():
    assert 3 - 2 == 1
```

In this example, there are two simple tests that check basic arithmetic.

#### 3. **Running Tests**

To run tests, simply navigate to the directory containing your test files and run the following command:

```bash
pytest
```

Pytest will automatically discover tests and execute them. It will output a summary, showing which tests passed or failed.

- Tests should be in files named `test_*.py` or `*_test.py`, so Pytest can find them.
- By default, Pytest will search for all files that match `test_*.py` in the current directory and its subdirectories.

#### 4. **Assertions**

Pytest uses standard Python `assert` statements to check test conditions. If the expression after `assert` evaluates to `True`, the test passes. If it evaluates to `False`, the test fails.

Example:

```python
def test_multiply():
    assert 2 * 2 == 4  # Pass
    assert 2 * 2 == 5  # Fail
```

Pytest will provide helpful error messages for failed assertions.

#### 5. **Test Fixtures**

Fixtures in Pytest are used to set up a known state for tests. They are useful for sharing setup code across multiple tests, such as creating temporary files, database connections, or mock objects.

Fixtures are defined using the `@pytest.fixture` decorator and can be injected into tests as parameters.

##### Example:

```python
import pytest

@pytest.fixture
def setup_data():
    return {"key": "value"}

def test_dict(setup_data):
    assert setup_data["key"] == "value"
```

In this example, `setup_data` is a fixture that provides a dictionary to the test function.

#### 6. **Test Discovery and Test Organization**

Pytest automatically discovers tests based on file and function naming conventions:

- Test files should be named `test_*.py` or `*_test.py`.
- Test functions should be named `test_*`.

You can organize tests into directories and subdirectories, and Pytest will recursively discover all tests.

#### 7. **Running Specific Tests**

You can run specific tests by specifying the file or even the specific test function:

- Run tests from a specific file:

    ```bash
    pytest test_example.py
    ```

- Run a specific test function within a file:

    ```bash
    pytest test_example.py::test_addition
    ```

#### 8. **Markers and Tags**

Pytest allows you to mark tests with tags or markers, which can help categorize and selectively run tests.

##### Example:

```python
import pytest

@pytest.mark.slow
def test_long_running():
    assert True

@pytest.mark.regression
def test_regression():
    assert True
```

You can run tests with specific markers using the `-m` option:

```bash
pytest -m "slow"
```

#### 9. **Parametrized Tests**

Pytest supports parametrized tests, which allows you to run the same test with different input values.

##### Example:

```python
import pytest

@pytest.mark.parametrize("input, expected", [(1, 2), (2, 4), (3, 6)])
def test_multiply(input, expected):
    assert input * 2 == expected
```

In this example, `test_multiply` will run three times, each with different input values.

#### 10. **Test Output and Reporting**

Pytest provides different output formats and options for reporting test results.

- **Verbose output**:

    ```bash
    pytest -v
    ```

- **Show only failed tests**:

    ```bash
    pytest -q --tb=short
    ```

- **HTML reporting** (requires `pytest-html` plugin):

    ```bash
    pytest --html=report.html
    ```

#### 11. **Mocking and Patching**

For unit testing, you often need to mock objects or functions. Pytest integrates well with the `unittest.mock` module, which allows you to replace parts of your system under test with mock objects.

##### Example:

```python
from unittest.mock import MagicMock

def test_mocking():
    mock = MagicMock(return_value=42)
    assert mock() == 42
```

#### 12. **Plugins**

Pytest has a rich ecosystem of plugins that extend its functionality. Some popular ones include:

- **pytest-django** for testing Django applications.
- **pytest-cov** for measuring test coverage.
- **pytest-xdist** for running tests in parallel.
- **pytest-mock** for easier mocking in tests.

You can install plugins via `pip` and use them in your tests.

#### 13. **Handling Expected Failures**

Sometimes you may know a test is going to fail, but you still want to run it (e.g., for feature testing or planned bug tracking). Pytest provides the `@pytest.mark.xfail` marker to mark such tests.

##### Example:

```python
@pytest.mark.xfail
def test_known_bug():
    assert 1 + 1 == 3
```

If the test fails, Pytest will report it as expected, and it won’t count against your test score.

#### 14. **Test Suites and Test Coverage**

Pytest integrates well with coverage tools to measure how much of your code is covered by tests. You can run tests with coverage using:

```bash
pytest --cov=your_module
```

This will generate a report showing which parts of the code were tested and which were not.


### Static and Dynamic Testing

In the context of software testing, **Static Testing** and **Dynamic Testing** refer to different approaches to identify bugs or issues in a codebase. Both are crucial for ensuring the correctness, quality, and performance of your software. Here’s an explanation of each in the context of Python development:

#### **Static Testing**

**Static Testing** refers to the process of analyzing the code **without executing it**. This type of testing checks the code for potential errors, vulnerabilities, or deviations from best practices purely based on its structure and syntax. Static testing tools typically perform code analysis or review at the level of syntax, style, and structure, without running the actual program.

##### Key Features:
- **No execution of code**: Static testing involves reviewing the source code, configuration files, or documentation.
- **Focuses on code structure**: It checks for syntax errors, compliance with coding standards, and logical flaws that could lead to issues later.
- **Earlier defect detection**: Static testing can detect defects before the code is even run (for example, syntax errors or unreachable code).
- **Automated tools**: Tools that perform static analysis can automatically scan your code and flag potential problems.

##### Examples of Static Testing in Python:
1. **Code Review**:
   - Developers manually review the code for logic, structure, and clarity.
   - Ensures adherence to coding standards and best practices.

2. **Static Code Analysis**:
   - Tools that check Python code for potential issues, inefficiencies, or bad practices.
   - Examples:
     - **`pylint`**: A popular Python static code analysis tool that checks for errors, coding standards, and code smells.
     - **`flake8`**: A tool that checks for compliance with PEP8, Python’s style guide.
     - **`mypy`**: A tool that performs static type checking on Python code (if using type annotations).
   
   Example command using `pylint`:
   ```bash
   pylint your_script.py
   ```
   This would output any issues related to syntax, logic, or coding standards.

3. **Type Checking**:
   - Python is dynamically typed, but you can still perform static type checking using type annotations in Python 3. This helps to identify potential type mismatches before runtime.
   - **`mypy`** is often used for this purpose. For example:
   ```python
   def greet(name: str) -> str:
       return "Hello, " + name
   ```
   You can run `mypy` to check type correctness:
   ```bash
   mypy your_script.py
   ```

##### Advantages of Static Testing:
- **Faster feedback**: It catches simple errors like syntax problems or undefined variables before running the code.
- **Does not require execution**: Saves time by catching mistakes without running the program.
- **Helps maintain code quality**: Enforces consistency with coding standards and guidelines.

#### Disadvantages:
- **Limited scope**: It can't detect logical errors that occur during runtime (e.g., division by zero, incorrect logic).
- **Requires manual configuration**: Static analysis tools need to be integrated into the development workflow.
  
#### **Dynamic Testing**

**Dynamic Testing** refers to the process of testing a program by actually executing it. In dynamic testing, you run the program with various inputs and observe its behavior to ensure that it behaves as expected. It helps identify runtime errors, performance issues, and functional problems that only become apparent when the code is executed.

##### Key Features:
- **Code execution**: Dynamic testing involves running the code with different input values and checking the output or side effects.
- **Focus on behavior**: It verifies that the program performs as expected under various conditions.
- **Runtime errors**: Dynamic testing is effective for identifying issues like memory leaks, unhandled exceptions, or incorrect results when the program is running.

##### Examples of Dynamic Testing in Python:
1. **Unit Testing**:
   - Writing test functions that execute small units of code (like individual functions or methods) to verify correctness.
   - Commonly done using frameworks like **`pytest`**, **`unittest`**, or **`nose`**.
   
   Example using `pytest`:
   ```python
   def add(a, b):
       return a + b

   def test_add():
       assert add(1, 2) == 3
       assert add(-1, 1) == 0
   ```

   To run the test:
   ```bash
   pytest test_file.py
   ```

2. **Integration Testing**:
   - Testing how various components of the system work together.
   - For example, testing a web application by making actual HTTP requests to ensure that the server responds as expected.

3. **System Testing**:
   - Testing the entire system as a whole, running it in a production-like environment to ensure that it behaves as expected when all components are integrated.

4. **Performance Testing**:
   - Running tests to measure how well your application performs under load, e.g., testing response times or throughput.
   - Tools like **`locust`** or **`pytest-benchmark`** can be used for performance testing in Python.

##### Advantages of Dynamic Testing:
- **Real-world validation**: It verifies that the system works correctly with real input and in real conditions.
- **Catches runtime issues**: Detects errors that only show up during execution, such as crashes, memory leaks, and unexpected behavior.
- **User-oriented**: Simulates the user experience, ensuring the application works as users would expect.

##### Disadvantages:
- **Time-consuming**: Requires actual execution of code, which may be slower than static analysis, especially for large test suites.
- **Limited coverage**: Testing may not cover all code paths unless comprehensive test cases are written. Some edge cases or conditions might be missed.
- **Environment dependency**: Tests may be influenced by the environment (e.g., database, network conditions) in which they are executed.


#### Static vs Dynamic Testing

| Aspect                 | **Static Testing**                                  | **Dynamic Testing**                                  |
|------------------------|------------------------------------------------------|------------------------------------------------------|
| **Execution**           | No execution (code review, analysis tools)          | Execution of code with different inputs and conditions|
| **Focus**               | Code structure, syntax, type checking, code quality | Behavior of the system during execution             |
| **Purpose**             | Detect early issues like syntax errors, violations of coding standards | Detect runtime issues like bugs, performance problems |
| **Tools**               | `pylint`, `flake8`, `mypy`, linters, code analyzers | `pytest`, `unittest`, performance testing tools      |
| **Use case**            | Checking for errors in code structure, adherence to standards | Verifying that the program works as expected under real conditions |
| **Feedback**            | Provides early feedback during development         | Provides feedback after running the code with test cases |

### Whitebox and Blackbox Testing

**White-box testing** and **Black-box testing** are two fundamental approaches to software testing, each focusing on different aspects of the system being tested. Both techniques can be applied in Python testing, but they approach the process from different angles:

#### **White-box Testing**

**White-box testing** (also called **clear-box**, **glass-box**, or **structural testing**) is a testing methodology where the tester has access to the internal workings of the application. The focus of white-box testing is to verify the implementation and behavior of the code itself, typically testing the internal logic, data flow, and control structures.

In white-box testing, you **write test cases based on the internal logic** and structure of the code. You know how the code is designed and can directly manipulate or examine specific parts of it to ensure they function as expected.

##### Key Features of White-box Testing:
- **Access to source code**: Testers have full access to the internal logic and implementation of the application.
- **Test internal structures**: White-box tests examine code paths, loops, functions, conditions, and the internal data flow.
- **Focus on code coverage**: White-box testing is concerned with achieving high code coverage (e.g., covering as many branches and paths as possible).
- **Manual and automated testing**: Tests can be written manually or generated automatically based on the source code.

##### Types of White-box Testing:
- **Unit Testing**: Testing individual components or functions of the application.
- **Code Coverage Analysis**: Ensuring that all code paths are executed through tests.
- **Path Testing**: Testing all possible execution paths through the code.
- **Branch Testing**: Ensuring that every possible decision (branch) in the code is tested.
- **Loop Testing**: Checking the loops to ensure they execute correctly under different conditions.

##### Example of White-box Testing in Python:

Let’s say you have a Python function `calculate_discount` that determines a discount based on the total price:

```python
def calculate_discount(total_amount):
    if total_amount > 100:
        return total_amount * 0.1  # 10% discount for amounts > 100
    elif total_amount > 50:
        return total_amount * 0.05  # 5% discount for amounts > 50
    else:
        return 0  # No discount
```

In white-box testing, you would write tests to cover all possible execution paths (e.g., total_amount > 100, total_amount > 50, and the else condition).

Using **pytest** for unit testing this function:

```python
import pytest
from your_module import calculate_discount

def test_calculate_discount():
    assert calculate_discount(150) == 15  # 150 * 0.1 = 15
    assert calculate_discount(75) == 3.75  # 75 * 0.05 = 3.75
    assert calculate_discount(30) == 0  # No discount for 30
```

In this case, **white-box testing** ensures that all the branches of the `if-elif-else` logic are tested, checking if the correct discount is applied for various amounts.

##### Advantages of White-box Testing:
- **Thorough coverage**: It can ensure all code paths, branches, and internal functions are tested.
- **Early defect detection**: Detects issues with logic, control flow, and internal structure early in the development cycle.
- **Improves code quality**: By focusing on internal structures, it encourages developers to write clean, efficient, and error-free code.

##### Disadvantages:
- **Requires knowledge of the code**: Testers need to understand the internal structure, which might not always be possible for non-developers or external testers.
- **Time-consuming**: Creating detailed white-box tests for complex systems can be very time-consuming.
- **Limited focus**: It doesn’t ensure the system works as expected from an end-user perspective (as it’s concerned with the code itself).

---

#### **Black-box Testing**

**Black-box testing** is a testing methodology where the tester does **not** have access to the internal workings of the application. The focus is on testing the functionality of the application by providing inputs and examining the outputs, without any knowledge of the underlying code structure.

In black-box testing, you only care about whether the software works as expected from the user’s perspective, not how the system achieves those results. It is primarily concerned with **functional** testing.

##### Key Features of Black-box Testing:
- **No knowledge of the code**: Testers do not need to understand the internal structure or logic of the code.
- **Focus on functionality**: Black-box testing evaluates whether the software performs the correct functions in various conditions.
- **User-centric**: Tests are based on the user’s experience, focusing on inputs, outputs, and interactions with the software.
- **High-level testing**: It's used for functional, system, acceptance, and integration testing.

##### Types of Black-box Testing:
- **Functional Testing**: Ensures that the system works according to functional requirements.
- **Regression Testing**: Ensures that new changes do not break existing functionality.
- **System Testing**: Tests the entire system’s functionality to ensure all components work together.
- **Acceptance Testing**: Determines if the software meets the business requirements and is ready for release.
- **Integration Testing**: Verifies that various parts of the system work together as expected.

##### Example of Black-box Testing in Python:

For the same `calculate_discount` function, black-box testing would focus on verifying that the function returns the correct discount value based on various inputs. Here, you would not need to know the implementation details — just the expected behavior.

Example using **pytest**:

```python
import pytest
from your_module import calculate_discount

def test_calculate_discount():
    # Test normal cases
    assert calculate_discount(150) == 15  # 150 * 0.1 = 15
    assert calculate_discount(75) == 3.75  # 75 * 0.05 = 3.75
    assert calculate_discount(30) == 0  # No discount for 30

    # Test edge cases
    assert calculate_discount(100) == 10  # 100 * 0.1 = 10
    assert calculate_discount(50) == 2.5  # 50 * 0.05 = 2.5

    # Test negative or invalid input
    assert calculate_discount(-10) == 0  # No discount for negative amount
```

Here, **black-box testing** does not require knowledge of how the discount is calculated, but only checks that the system produces the correct results for various inputs.

##### Advantages of Black-box Testing:
- **End-user perspective**: It helps verify whether the application behaves as expected from the user’s perspective, focusing on requirements and specifications.
- **No need for technical knowledge**: Testers do not need to understand the code, so it’s ideal for non-developers or external testers.
- **Helps identify functional flaws**: It ensures that the system behaves correctly under a wide range of conditions.

##### Disadvantages:
- **Limited coverage**: Without knowing the internal logic, it’s difficult to ensure comprehensive test coverage.
- **Cannot detect implementation flaws**: Black-box testing won’t identify issues like inefficiencies in the code or problems with algorithms, as it focuses purely on functionality.
- **Test cases can miss edge cases**: It's harder to identify edge cases or unexpected conditions that might not be immediately obvious from the external specification.

---

#### **White-box vs Black-box Testing**

| Aspect                   | **White-box Testing**                                      | **Black-box Testing**                                      |
|--------------------------|------------------------------------------------------------|------------------------------------------------------------|
| **Access to Code**        | Full access to the source code                            | No access to the source code                               |
| **Focus**                 | Internal logic, data flow, code paths, and structure       | Functionality, user interface, and overall behavior        |
| **Test Design**           | Based on code structure (e.g., logic, loops, functions)    | Based on requirements, functionality, and user scenarios   |
| **Testers' Knowledge**    | Tester needs to know the internal code                    | Tester does not need to know the internal code             |
| **Type of Tests**         | Unit tests, path tests, code coverage, branch testing      | Functional testing, system testing, acceptance testing     |
| **Scope**                 | Tests individual components or code units                 | Tests the entire system or software behavior               |
| **Advantages**            | Can achieve high code coverage and detect internal issues | Focuses on user experience and functionality               |
| **Disadvantages**         | Requires technical knowledge, time-consuming               | Limited coverage, doesn’t detect internal implementation flaws |


### Grey Box Testing

Grey box testing is a software testing approach that combines elements of both white box testing (which involves testing with knowledge of the internal code and architecture) and black box testing (which focuses on testing the application from an external user perspective, without knowledge of the internal workings). In grey box testing, testers have partial knowledge of the internal structure of the system, such as access to certain design documents, database schemas, or APIs, but not full access to the source code. This approach allows testers to design more effective test cases by leveraging both the internal logic and the expected behavior from an end-user perspective, helping to identify vulnerabilities, functionality issues, and integration flaws that might not be detected by purely black or white box methods.


### Regression Testing

Regression testing is the process of re-testing a software application after changes, such as enhancements, bug fixes, or new feature additions, to ensure that existing functionality remains unaffected. The goal is to detect any unintended side effects or regressions in the software caused by modifications to the code. Best practices for regression testing include maintaining a comprehensive and up-to-date test suite, automating repetitive test cases to ensure faster and more reliable execution, prioritizing tests based on risk and critical functionality, and running the regression tests frequently, especially after every significant change or update. Additionally, it's important to perform regression testing across different environments and platforms to ensure consistent performance and behavior. Regularly reviewing and refining the test cases, removing redundant tests, and focusing on areas of frequent change can help make the regression testing process more efficient and effective.

1. **Maintain an Up-to-Date Test Suite**: Ensure your regression test suite is regularly updated to reflect the latest features, fixes, and changes in the software.

2. **Automate Repetitive Tests**: Automate frequently executed regression tests to speed up the process and reduce the risk of human error.

3. **Prioritize Critical Tests**: Focus on testing core functionality, high-risk areas, and features that are frequently changed or have a history of issues.

4. **Perform Tests Frequently**: Run regression tests after each code change or update to detect issues early and avoid the accumulation of defects.

5. **Use a Version Control System**: Track and manage test cases, test scripts, and test results through version control to maintain consistency and transparency.

6. **Run Tests Across Multiple Environments**: Perform regression tests in different browsers, operating systems, and devices to ensure consistent behavior across platforms.

7. **Refine Test Cases Regularly**: Review and refine your test cases to remove redundant tests, keep them relevant, and ensure coverage is adequate.

8. **Keep Track of Defects**: Document and analyze defects found during regression testing to ensure they are addressed and prevent recurrence in future releases.

9. **Limit Test Scope Where Possible**: Focus testing on areas impacted by recent changes while balancing the need for comprehensive coverage with testing efficiency.

10. **Continuous Integration**: Integrate regression tests into the CI/CD pipeline so tests are executed automatically as part of the build process, allowing for quicker feedback.

### Code Coverage

Code coverage is a software testing metric used to measure the extent to which the source code of a program is exercised by a set of test cases. It helps assess the effectiveness of tests by identifying which parts of the code have been tested and which remain untested. Code coverage is typically expressed as a percentage, representing the proportion of code lines, branches, paths, or conditions that have been executed during testing. High code coverage suggests that the code has been thoroughly tested, but it does not guarantee the absence of defects. Different types of code coverage, such as line coverage, branch coverage, and path coverage, provide varying levels of insight into how well the code is being tested. While code coverage is a useful metric, it should be used alongside other testing practices to ensure comprehensive software quality.

1. Function Coverage
2. Branch Coverage
3. Condition Coverage
4. 
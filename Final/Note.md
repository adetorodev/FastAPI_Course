## What Are Dependencies?
Definition: Dependencies in FastAPI are functions or classes that provide shared functionality to endpoints. They allow the separation of concerns by injecting logic, data, or services into your route handlers.

Purpose:

Code Reusability: Common logic can be reused across endpoints.
Decoupling: Helps keep routes focused on business logic by delegating auxiliary concerns (e.g., authentication, database access).
Testability: Dependencies make mocking and testing easier.
Examples of Common Dependencies:

Authentication and authorization logic.
Database connections.
Data validation or transformation services.
Caching layers.
How FastAPI Handles Dependencies: FastAPI resolves dependencies automatically by analyzing the parameters of your functions. These dependencies are declared using Python’s type hints.

Key Features of Simple Dependencies
Simplicity: A dependency is just a callable that FastAPI automatically resolves.
Reusability: Define logic once and reuse it across multiple endpoints.
Flexibility: Dependencies can accept query parameters, path parameters, or even other dependencies.
Error Handling: You can raise exceptions or perform validation within dependencies.
Composability: Combine multiple dependencies to build complex, modular functionality.

Injecting Dependencies in FastAPI
Dependency injection is the process by which FastAPI automatically resolves and injects the return value of a dependency into your endpoint function or another dependency. Injecting dependencies allows you to decouple your code, making it more modular, reusable, and testable.

How Dependency Injection Works
FastAPI’s dependency injection system is based on Python's type hints. You specify dependencies in function arguments using Depends, and FastAPI handles:

Calling the dependency: FastAPI automatically executes the dependency function or class.
Injecting the result: The return value is injected into the endpoint or other dependencies.

Using Classes as Dependencies in FastAPI
In FastAPI, you can use classes as dependencies to encapsulate logic, manage state, and organize code. This is especially useful when you have complex logic or need to perform multiple related operations within a dependency.

When using a class as a dependency, FastAPI expects the class to implement a __call__ method. This method is invoked whenever the dependency is resolved, and its return value is injected where the dependency is used.

Advantages of Using Classes as Dependencies
State Management: Classes can store and manage state between different operations.
Reusability: Encapsulated logic in a class can be reused across multiple endpoints or other dependencies.
Modularity: Classes help organize code logically and improve readability.
Dependency Chaining: Classes can depend on other dependencies, just like functions.

Managing Dependencies with Scopes (Lifespans) in FastAPI
In FastAPI, you can control the lifecycle of dependencies using scopes, which determine how long a dependency will live. Scopes allow you to manage resources like database connections, authentication tokens, or other shared objects efficiently by defining when they are created and when they are destroyed.
What Are Scopes?
A scope in FastAPI defines the lifespan of a dependency. For instance:
Request scope: The dependency is created at the start of an HTTP request and destroyed at the end.
Application scope: The dependency persists for the entire application lifecycle, from startup to shutdown.
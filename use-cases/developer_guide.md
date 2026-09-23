# Developer Guide: User Registration API

Welcome to the team! If you're looking to get users signed up and into our ecosystem, you're in the right place. This guide will walk you through everything you need to know to successfully integrate with our user registration endpoint. 

Whether you're building a sleek frontend interface or testing backend workflows, we'll keep things clear, simple, and practical. Let's dive in!

---

## 1. Authentication

The good news? **No authentication is required** to register a new user account! 

Because this endpoint (`POST /api/users/register`) is the entry point for brand-new visitors, it is completely public. You don't need to pass any API keys, Bearer tokens, or session cookies in your headers to make this request work. 

---

## 2. Properly Formatting Requests

To make sure our server accepts your data, your request needs to follow a few specific rules:

* **HTTP Method:** `POST`
* **Endpoint URL:** `http://localhost:5000/api/users/register` (update the base URL depending on your environment).
* **Headers:** You must include a `Content-Type` header set to `application/json`.
* **Request Body:** Must be a valid JSON object containing three required fields:
  * `username` (string): The unique name the user wants to go by.
  * `email` (string): A valid email address (we'll automatically convert this to lowercase for you!).
  * `password` (string): A secure password that **must be at least 8 characters long**.

---

## 3. Handling and Interpreting Responses

When things go right, our API will reward your request with a status code of **`201 Created`**. 

Here is what a successful response looks like:

```json
{
  "message": "User registered successfully",
  "user": {
    "id": 42,
    "username": "janedoe",
    "email": "janedoe@example.com",
    "created_at": "2026-09-23T10:30:00.000000",
    "role": "user"
  }
}
```

* **`message`**: A friendly confirmation string letting you know the registration worked.
* **`user`**: An object containing the newly created user's profile info (notice we safely omit the password hash!). You can use the `id` field to establish session state or redirect your user.

---

## 4. Dealing with Common Errors

Even the best-laid plans encounter typos or duplicate entries. When something goes wrong, our API responds with clear error codes and descriptive messages so you know exactly how to fix it.

| Status Code | Error Type | Why It Happens | How to Fix It |
| :--- | :--- | :--- | :--- |
| **400 Bad Request** | `Missing required field` | You forgot to include `username`, `email`, or `password`. | Double-check your payload to ensure all three keys are present. |
| **400 Bad Request** | `Invalid email` | The email address format is missing an `@` symbol or domain. | Validate user input on the frontend to match a standard email format. |
| **400 Bad Request** | `Weak password` | The password provided is shorter than 8 characters. | Prompt your user to choose a longer, more secure password. |
| **409 Conflict** | `Username taken` or `Email exists` | Someone else is already using that username or email address. | Let the user know the credential is taken and invite them to pick another or log in. |
| **500 Internal Server Error** | `Server error` | Something unexpected broke on our end or during database writes. | Log the error, retry after a moment, or reach out to backend support. |

Example error response body:
```json
{
  "error": "Weak password",
  "message": "Password must be at least 8 characters long"
}
```

---

## 5. Example Code (Python)

Here is a quick, ready-to-run snippet using the popular `requests` library to show you how to register a user programmatically in Python:

```python
import requests
import json

# Define the API endpoint
url = "http://localhost:5000/api/users/register"

# Set up the required headers
headers = {
    "Content-Type": "application/json"
}

# Construct the payload
payload = {
    "username": "codeninja",
    "email": "ninja@example.com",
    "password": "SuperSecretPassword123"
}

try:
    # Make the POST request
    response = requests.post(url, headers=headers, data=json.dumps(payload))

    # Check if registration was successful
    if response.status_code == 201:
        data = response.json()
        print("Success! User created:")
        print(f"User ID: {data['user']['id']}")
        print(f"Username: {data['user']['username']}")
    else:
        # Handle known API errors gracefully
        error_data = response.json()
        print(f"Registration failed [{response.status_code}] - {error_data.get('error')}: {error_data.get('message')}")

except requests.exceptions.RequestException as e:
    print(f"An error occurred while connecting to the server: {e}")
```

---

## Wrapping Up
You're all set to start integrating! If you run into any edge cases or have questions about error handling, feel free to drop a message in our developer chat channel. Happy coding!
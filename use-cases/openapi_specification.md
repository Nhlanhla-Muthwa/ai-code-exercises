openapi: 3.0.3
info:
  title: User Management API
  description: API documentation for user registration and account creation.
  version: 1.0.0
servers:
  - url: http://localhost:5000/api
    description: Local development server
paths:
  /users/register:
    post:
      summary: Register a new user
      description: Creates a new user account, validates input data, hashes the password, and sends a confirmation email.
      operationId: registerUser
      requestBody:
        required: true
        content:
          application/json:
            schema:
              type: object
              required:
                - username
                - email
                - password
              properties:
                username:
                  type: string
                  example: johndoe
                  description: The unique username chosen by the user.
                email:
                  type: string
                  format: email
                  example: johndoe@example.com
                  description: A valid, unique email address.
                password:
                  type: string
                  format: password
                  minLength: 8
                  example: SecurePassword123
                  description: User password (must be at least 8 characters long).
      responses:
        '201':
          description: User registered successfully
          content:
            application/json:
              schema:
                type: object
                properties:
                  message:
                    type: string
                    example: User registered successfully
                  user:
                    type: object
                    properties:
                      id:
                        type: integer
                        example: 1
                      username:
                        type: string
                        example: johndoe
                      email:
                        type: string
                        example: johndoe@example.com
                      created_at:
                        type: string
                        format: date-time
                        example: '2026-09-23T10:30:00.000000'
                      role:
                        type: string
                        example: user
        '400':
          description: Bad Request - Missing required fields, invalid email format, or weak password.
          content:
            application/json:
              schema:
                type: object
                properties:
                  error:
                    type: string
                    example: Weak password
                  message:
                    type: string
                    example: Password must be at least 8 characters long
        '409':
          description: Conflict - Username or email already exists in the system.
          content:
            application/json:
              schema:
                type: object
                properties:
                  error:
                    type: string
                    example: Username taken
                  message:
                    type: string
                    example: Username is already in use
        '500':
          description: Internal Server Error - Failed to register user due to server or database issues.
          content:
            application/json:
              schema:
                type: object
                properties:
                  error:
                    type: string
                    example: Server error
                  message:
                    type: string
                    example: Failed to register user
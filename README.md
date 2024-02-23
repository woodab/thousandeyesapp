# ThousandEyes API Integration Application

This application is a simple Python script that interacts with the ThousandEyes API to retrieve a list of all tests configured in a ThousandEyes account. The application is containerized using Docker, which allows it to be easily deployed and run in any environment that supports Docker.

## Application Structure

The application consists of a single Python script (`app.py`) and a Dockerfile for building the Docker image. The Python script uses the `requests` library to make HTTP requests to the ThousandEyes API. The API token and endpoint are stored in environment variables for security.

## How to Use

To use this application, you need to have Docker installed on your machine. Then, you can build the Docker image and run a container with the following commands:
First, clone the repository to your machine
Replace `<your-api-token>` with your actual API token and verify the value set for `<your-api-endpoint>` is the correct endpoint.

```bash
# Build the Docker image
docker build -t thousandeyes-api .

# Run a container

docker run --rm thousandeyes-app  
```

## Scan with Trivy
```bash
# Scan the Docker image
trivy image thousandeyes-api 
```
Trivy scans are located in the /scans directory

## Security Considerations

This application follows several best practices for security:

- Sensitive information (API token and endpoint) is stored in environment variables, not in the code.
- The Docker image is built from a lightweight Python base image to reduce the attack surface.
- The Dockerfile only includes the necessary files and dependencies in the Docker image.

However, this is a simple application and there are many additional security measures that could be implemented in a production application, such as input validation and sanitization, use of a non-root user in the Dockerfile, and setting up a CI/CD pipeline for automatic testing and deployment.

## Future Improvements

This application could be extended in several ways:

- Implement error handling for the API requests.
- Add more features, such as the ability to create, update, or delete tests.
- Improve the output formatting for easier reading.
- Add unit tests and integration tests.
- Set up a CI/CD pipeline for automatic testing and deployment.

## Conclusion

This application demonstrates how to interact with the ThousandEyes API using Python and how to containerize a Python application with Docker. It follows best practices for security and can be easily extended with more features.

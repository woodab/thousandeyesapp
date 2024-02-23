# Use a lightweight Python base image
FROM python:3.10-slim

# Set the working directory in the container to /app
WORKDIR /app

# Copy the requirements.txt file to the container
COPY requirements.txt ./

# Install the Python dependencies specified in requirements.txt
# The --no-cache-dir option is used to keep the image size small
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application's source code to the container
COPY . .

# Set the command that will be run when the container starts
# In this case, it runs the app.py script with Python
CMD ["python", "./app.py"]
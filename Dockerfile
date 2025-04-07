FROM python:3.9

# Set the working directory
WORKDIR /app

COPY . /app

# Expose the port the app runs on, must be same port as 
# defined in webserver.py 
EXPOSE 12000

# Define the command to run the app
CMD ["python", "webserver.py"]


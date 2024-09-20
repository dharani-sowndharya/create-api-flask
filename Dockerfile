FROM python:3.11-alpine

# Allows to see the output directly on terminal without buffer
ENV PYTHONUNBUFFERED 1 

# Set the working directory
WORKDIR /route

# Copy only the requirements file first to leverage Docker caching
COPY requirements.txt .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the entire application code
COPY . .

# Expose the port your application will run on
EXPOSE 8080

# Specify the command to run on container start
CMD ["python", "route.py"]
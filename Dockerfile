# Use the official Python image
FROM python:3.11.4

# Set the working directory inside the container
ENV DockerHOME=/webapp  

# set work directory  
RUN mkdir -p $DockerHOME  

# where your code lives  
WORKDIR $DockerHOME  

ENV ACTIONS_ALLOW_USE_UNSECURE_NODE_VERSION=true

# Copy the rest of the application files to the container's working directory
COPY . $DockerHOME

# install dependencies  
#RUN pip install --upgrade pip 
RUN pip install --upgrade pip setuptools wheel
# Install required Python packages
#RUN pip install -r requirements.txt --default-timeout=100 future

# Instala los requerimientos
RUN pip install -r requirements.txt


# Expose the port that Streamlit will run on
EXPOSE 8501

# Command to run your Streamlit application
CMD ["streamlit", "run", "app.py"]
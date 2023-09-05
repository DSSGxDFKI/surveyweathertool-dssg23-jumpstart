######### NOTES FOR MODIFICATIONS
### Resources for docker and streamlit
# Docker Cheatsheet 1 - https://kapeli.com/cheat_sheets/Dockerfile.docset/Contents/Resources/Documents/index 
# Docker Cheatsheet 2 - https://dockerlabs.collabnix.com/docker/cheatsheet/
# Streamlit with Docker - https://docs.streamlit.io/knowledge-base/tutorials/deploy/docker
# Hot-reload of python code inside container using volumes - https://stackoverflow.com/questions/70155930/how-to-update-source-code-without-rebuilding-image-each-time
# 
### Run the master python scripts (something like main.py) when the container launches
# Uncomment or adapt when ready
# CMD ["python", "./src/survey/main.py"]
# CMD ["python", "./src/weather/main.py"]
# CMD ["python", "./src/dashboard/main.py"]

# Base Image
FROM python:3.10

# Run these commands to fix fiona install issue and some basic unix utilities
RUN apt-get update && \
    apt-get install -y gdal-bin libgdal-dev g++ && \
    apt-get install -y tree nano vim make build-essential curl git

# Create folder for source code and make it working directory
RUN mkdir -p /app

WORKDIR /app

# Install the python requirements
COPY Docker-requirements.txt .
RUN pip install -r Docker-requirements.txt

# Streamlit dahboard run
EXPOSE 8501
HEALTHCHECK CMD curl --fail http://localhost:8501/_stcore/health
### In future might have dashboard on public git repo.
### Once streamlit has MVP going expose to user in popup website
ENTRYPOINT ["streamlit", "run", "surveyweathertool/Home.py", "--server.port=8501", "--server.address=0.0.0.0"]

# By running the Docker container, the pipeline gets triggered
# ENTRYPOINT [ "bash" ]
### NOTE: For development purposes inside docker container on server, 
### it is beneficial to uncomment the dashboard or pipeline above and
### simply entrypoint into bash  
# CMD ["python3", "pipeline.py"]
# CMD ["bash"]
# init a base image (Alpine is small Linux distro)
FROM Python 3.9.5 -alpine
# define the present working directory
WORKDIR /Dog_breed_Bounding_box
# copy the contents into the working dir
ADD . /Dog_breed_Bounding_box
# run pip to install the dependencies of the flask app
RUN pip install -r requirements.txt
# define the command to start the container
CMD ["python","app.py"]
# Working against AWS with Python3 using boto3

The repository creates a Docker container with python3, boto3 and AWS credentials.

## Use Case

The use case is to Docker container to manipulate object and services in AWS using Python3 and Amazon SDK library *boto3*.

## Prerequisities

It is assumed you have created a user in AWS IAM and have access to the credentials.csv file with access key and secret key.

It is also assumed the user has access to the S3 buckets. That is something one controls in the AWS IAM service.

### AWS credentials

Use file *credentials.template* in docker/aws folder to set up credentials. Rename the file to *credentials* since Docker will try to copy a file with that name to the image. Check the file itself for more details.

The library boto3 uses *~/.aws/credentials* to authenticate and authorize.

### Pip requirements file

The file *docker/requirements.txt* holds a list of python packages pip should install inside the image. One package per line is the format.

### Variables in DockerFile

Check the DockerFile to change any arguments used to create the image.

## Create Docker container

### Build image

The following command builds an image *boto3-image*

```bash
docker build . --tag=boto3-image
```

### Run container

Run the container using the image created in the previous command. Check the option *-v* to fix the mapping. In the *DockerFile*, there is a variable *VOLUME* which points to the mapped folder in the Docker (in this case VOLUME=/local-git), change it if you want to avoid python errors like *missing module logic*.

```bash
docker run -itd --rm --name boto3 --hostname boto3 -v C:\marko\GitHub\boto3:/local-git boto3-image
```

### Step into container

Step into the created container

```bash
docker exec -it boto3 bash
```

## About the container

The container uses latest centOS, installs python3-pip library in order to install *virtualenv* using pip3.

It also creates a user of your choice (default is centos) which is used to run the python scripts.

Virtual environment with Python 3.6 is created and the path to the binaries in the virtual environment's folder is added to the $PATH. With that, running command *python* will use Python3.6 or whichever Python version is installed in the virtual environment.

### Example

In folder *logic* here is a Python example package and file which use library *boto3* to list all buckets in the AWS S3.

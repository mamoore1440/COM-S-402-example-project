# API (backend)
This is a sample API with Python, Flask, and Dockerk

## Running the API
It is recommended you run the API with Docker. However, you can additionally run the API with Python virutalenv.

### Docker
#### Build the image
```bash
$ docker build -t tag_name .
```

#### Run the image
```bash
$ docker run -p 3000:3000 -t tag_name
```

Learn more about docker [here](https://www.docker.com).

### Python virtualenv
With python3.8 installed

#### Setup virtualenv
```bash
# Install virtualenv
$ python -m pip install virtualenv

# Create a virtualenv folder
$ python -m virtualenv venv

# Activate the virtualenv (on windows this will be different)
$ source ./venv/bin/activate

# Install dependencies (within virtualenv)
$ pip install -r requirements.txt
```

#### Run the app
```bash
$ python app.py
```

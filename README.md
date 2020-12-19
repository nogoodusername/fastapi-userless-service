# fastapi-userless-service

This is an example package. Generated using [gh:cookiecutter-fastapi-template](https://github.com/nogoodusername/cookiecutter-fastapi-template)

---

## Directory Structure
```
fastapi-userless-service
├── app                     # Application folder Project
│   ├── api                 # API package
│   │   ├── sample_module   # Sample Module
│   │   └── views.py        # File for storing endpoints of API Package
│   ├── core                # Keep your configs here
│   │   └── settings.py     # Environment settings file
│   ├── DockerfileStag      # Dockerfile for staging environment
│   ├── DockerfileProd      # Dockerfile for production environment
│   ├── main.py             # Main file where FastAPI is initialised
│   ├── requirements        # Python requirements folder
│   │   ├── base.py         # Base requirements file (common for all environments)
│   │   ├── development.py  # Development environment requirements file
│   │   ├── production.py   # Production environment requirements file
│   │   └── staging.py      # Staging environment requirements file
│   ├── tests               # Project specific pytests
│   │   └── test_sample.py  # Sample test file
├── build                   # Build scripts for staging and production
├── tests                   # Test scripts for postman
├── LICENSE                 # LICENSE FILE
└── Makefile                # Makefile to setup project
```
---

## FastAPI Project

### Local Setup
```sh
make init
```

### Run Locally
```sh
make runserver
```

### Run tests
```sh
make runtests
```

### Check out Makefile for more commands or try
```sh
make help
```

---

## Authors
fastapi-userless-service was written by [Kshitij Nagvekar](mailto:ksnagvekar@gmail.com).

# booksnake-web

A react-based front-end for [Booksnake](https://github.com/j6k4m8/booksnake), with a Flask backend.

<img width="1292" alt="image" src="https://user-images.githubusercontent.com/693511/107521411-836ee180-6b80-11eb-99b1-d22c51afbcf7.png">

## Installation

Install dependencies with:

```shell
pip3 install -r ./requirements.txt
```

## Usage

Run the server with:

```shell
python3 ./main.py
```

This will serve the application on port 5000 on localhost:

http://localhost:5000/

The homepage of the application accesses the server without page reload via direct calls to the `/api/` URLs served by Flask.

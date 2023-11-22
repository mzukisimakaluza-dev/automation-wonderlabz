# Windows 10/11

## 1. Install virtualenv

This assumes you already have python installed on your computer, if not please do:

```$ pip install virtualenv```

## 2. Create a python environment

Now create a virtual environment named ```.venv```, this will be a folder where all python packages will be installed:

```$ python -m virtualenv .venv```

Now activate the environment like this:

```$ source .venv/Scripts/activate```

## 3. Install the required packages

Now install the required packages, which are in the ```requirements.txt``` file:

```$ pip install -r requirements.txt```

## 4. Running the test

To run the ```main.py``` script all you need to do is:

```$ python main.py```

This will lauch a chrome window and do all the tests for you.


Happy Testing!

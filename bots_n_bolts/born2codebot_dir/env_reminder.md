To create a virtual environment, go to your project’s directory and run venv. If you are using Python 2, replace venv with virtualenv in the below commands.

$ python3 -m venv env //This will create an env dir

Before you can start installing or using packages in your virtual environment you’ll need to activate it. Activating a virtual environment will put the virtual environment-specific python and pip executables into your shell’s PATH.

$ source env/bin/activate

You can confirm you’re in the virtual environment by checking the location of your Python interpreter, it should point to the env directory.

$ which python
.../env/bin/python

If you want to switch projects or otherwise leave your virtual environment, simply run:

$ deactivate

If you want to re-enter the virtual environment just follow the same instructions above about activating a virtual environment.
There’s no need to re-create the virtual environment.

It’s recommended to specify explicit dependency versions in your requirements.txt file. 
To easily update this file, you can use the pip freeze command in your active virtual environment:

$ pip freeze > requirements.txt

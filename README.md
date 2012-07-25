ARENA-FLASK
===========

An example flask app using arena as data source. Integrates ArenaPy.

SETUP
===========
This is how I recommend doing it.

1.  Create an environment directory (we'll put the virtual env dir and the project dir in here, I like to keep my env dirs out of the project dir)

    mkdir ~/chosen/path/arena-flask-env

2.  Create a virtual environment for the project*:
    
        cd ~/chosen/path/arena-flask-env
        virtualenv env

    *http://pypi.python.org/pypi/virtualenv, if you don't have virtualenv, install it with pip
        
        pip install virtualenv
    
    if you don't have pip, install it with setuptools
        
        sudo easy_install pip

3.  Activate env
        
        source ./env/bin/activate

3.  Download and install arena-flask: 
        
        git clone git://github.com/jnhasty/arena-flask.git

    arena-flask-env directory should now have 'env' dir and 'arena-flask' dir

4.  CD into project and install requirements 
        
        cd ~/chosen/path/arena-flask-env/arena-flask
        pip install -r requirements.txt

5.  Run the app and start building!
        
        python app.py

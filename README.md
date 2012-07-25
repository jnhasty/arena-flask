ARENA-FLASK
===========

An example flask app using arena as data source. Integrates ArenaPy.


SETUP
===========
This is how I recommend doing it.

1.  Create an enviroment directory (we'll put the virtual env dir and the project dir in here, I like to keep my env dirs out of the project dir)
        mkdir ~/chosen/path/arena-flask-env

2.  Create a virtual environment for the project (http://pypi.python.org/pypi/virtualenv):
        cd ~/chosen/path/arena-flask-env
        virtualenv env

3.  Activate env
        source ./env/bin/activate

3.  Download and install arena-flask: 
        git clone git://github.com/jnhasty/arena-flask.git

    arena-flask-env direcotry should now have 'env' dir and 'arena-flask' dir

4.  CD into project and install requirements 
        cd ~/chosen/path/arena-flask-env/arena-flask
        pip install -R requirements.txt

5.  Run the app and start building!
        python app.py

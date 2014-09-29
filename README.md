Assets manager
===

An admin web frontend for managing the [assets-server](/canonicalltd/assets-server).

Setting the server location
---

You'll need to have an instance of the [assets-server](/canonicalltd/assets-server) running for this manager to pair with. By default, the manager will look for the server at <http://localhost:8012>. You can change this in two ways.

By changing the default in `settings.py`:

``` python
# assets_server/settings.py

DEFAULT_SERVER_URL = 'https://assets.example.com'
```

Or by setting the `WEBSERVICE_URL` environment variable:

``` bash
# Start the development server with an environment variable

$ WEBSERVICE_URL='https://assets.example.com' make develop
```

Local development
---

Once you've setup the server credentials, here how to get the manager working locally:

### System packages

``` bash
sudo apt-get install python-dev python-pip
sudo pip install vex
```

### Python environment

You need to setup your python environment, which you can either do manually
if you know how (from `requirements/dev.txt`) or use the make target:

``` bash
$ make setup  # Sets up a new environment in the `env` folder
```

### Run the development server

``` bash
$ make develop  # Starts the dev server on port 8011
````

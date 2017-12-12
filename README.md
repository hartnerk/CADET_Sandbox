#### CADET Front End Developer Guide ####
Python 3.4, Django 1.11

A guide to help developers install and run the front end of CADET.

## I. Set Up: Project Installation 

1. Installation: Cloning the Project  
- clone the project repo, cd into root directory  
- make sure you use virtualenv    

```bash
git clone ssh://git@web4.jhuep.com:2222/diffusion/CADET/cadet.git  
cd cadet/src/front-end
```

# A. Virtual Environment (optional, but highly recommended)

A. General virtualenv 
```bash 
# run virtualenv with python3, you can name your environment whatever. This
# example, we call it *cadetenv*.
python -m venv cadetenv   
```  
If running virtual env command gives you an error, you might either have 
anaconda installed, which you need to follow[this setup:]
(https://uoa-eresearch
.github.io/eresearch-cookbook/recipe/2014/11/20/conda/).

Mac and Ubuntu users might also run into installation error if pyenv is
broken, then add this modifier to the same command:

```bash
python -m venv cadetenv --without-pip 
```

### B. With Anaconda
If not using virtualenv and has anaconda installation use this:
```bash   
conda create -n my-dev python=3.4
source activate my-dev
```

The set up will automatically add pip and django packages.  
Skip Step II: Django Installation.

## II. Set Up: Django Installation  

```bash
# upgrade pip
pip install --upgrade pip

# install django 
pip install django~=1.10.0 

# activate virtualenv  
source cadetenv/bin/activate  

# upgrade django
sudo pip install django --upgrade 
```

### III. Activate Django App

```bash
#install dependencies
pip install -r requirements.txt

# migrate database, default is sqlite
python manage.py migrate 

# Run this when you first begin
python manage.py migrate --run-syncdb

# run server
python manage.py runserver

# run to ensure that results URL is working
127.0.0.1:8000/results/test

# website homepage
127.0.0.1:8000/dashboard

#### Common Issues in the Installation Steps  

**Make sure you're using python +3.0**  

You need these libraries installed in order to run our Django Cadet:  
```
# notice we install with pip3 not pip
pip3 install djangorestframework

# node for setting up node modules
sudo apt-get install npm

# d3 library
pip3 install django-nvd3

# JSONField libary
pip3 install jsonfield

# Polling library
pip3 install polling

```

### IV. Front-End Development Set Up

This section is for future front-end developers who wishes to modify the HTML,
CSS, and JS of the project.

We are using Gulp as a taskrunner to autocompile JS and CSS assets.  Two files
Gulpfile.js and package.json lists all dependencies and configuration.  In
order to set up gulp to your local environment, you must have node.js set up.
Run these commands:

```bash
# node will search for package.json file and install dependencies
npm init
# this command finds the Gulpfile.js and run all tasks there, mostly it tells 
# gulp to compile and minify all js and sass files in teh assets directory
gulp

```








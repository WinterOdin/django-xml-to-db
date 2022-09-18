## PyPi packages info to Django 
The point of this task was to get RSS channel info once every 24h, parse it and display data in a user-friendly manner.

#### How it's working 
Firstly we get the data from the RSS feed then we are parsing it, doing additional requests to get the data then converting it to pandas df which can be easily saved to our DB. Everything is repeated every 24 h

Data is available in two formats:
 - HTML table with pagination done in JS
 - under /API/package with custom pagination class 

The task is done in a way to cover most of my skills so we are using: 
 - forms 
 - models 
 - serializers
 - filters 
 - rest framework 
 - swagger 
 - task schedulers 
 - js
 - HTML
 - CSS

(this approach is redundant it only serves to show the use cases)

### How to run it 
Create virtualenv and install requirements.txt
```
virtualenv env 
env/Scripts/activate
pip install -r requirements.txt
```
then run 
```
python manage.py makemigrations 
python manage.py migrate
python manage.py runserver
```
Your app will be running on localhost 

### Additional info 

Admin panel is turned off via 
```
ADMIN_ENABLED = False
```
variable, if you wanna turn it on just change False to True. For more robust solution create 
.env file declare variable there and then 
```
ADMIN_ENABLED = str(os.environ.get('ADMIN_ENABLED'))
```
### Other approaches 
In my approach, I pretty much scrape and do JSON requests to PyPI servers.
The downside to this is a hard limit on the number of requests that PyPI allows. This looks something like this 
```
Job "BackgroundWorker.update_db (trigger: interval[1 day, 0:00:00], next run at: 2022-09-19 13:08:26 CEST)" raised an exception
```
To omit drawbacks use google big query.
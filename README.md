# ge_be
API that allows web app to build messaging application.  Built with Python and Django Rest Framework.

## REQUIREMENTS
```
Python === 3.9.13
PostgreSQL
```
#### If you do not have Python installed you can download it from:  
https://www.python.org/downloads/  
#### If you do not have PostgreSQL installed you can download it from:  
https://www.postgresql.org/download/  

On Mac follow instructions from:  
https://postgresapp.com/ 

On Windows follow instuctions from:  
https://www.postgresql.org/docs/14/tutorial-install.html

#### On Mac you can use brew to install
```
brew install postgresql
brew upgrade postgresql
sudo pip install psycopg2
```
Then in virtual environment run:
```
env LDFLAGS='-L/usr/local/lib -L/usr/local/opt/openssl/lib -L/usr/local/opt/readline/lib' pip install psycopg2==2.8.4
```



## GET STARTED

1. Clone the repository
```
git clone https://github.com/slentell/ge_be.git
```
2. Setup a virtual environment

```
python -m venv venv
OR 
python3 -m venv venv
```
3. Activate virtual environment
```
source venv/bin/activate
```
4. Install dependencies
```
pip install -r requirements.txt
```
5. Create the database
```
createdb be_messages
python manage.py makemigrations
python manage.py migrate
OR
python3 manage.py makemigrations
python manage.py migrate
```
5. Load data
```
python manage.py loaddata messages.json
OR 
python3 manage.py loaddata messages.json
```
6. Start server
```
python manage.py runserver
OR
python3 manage.py runserver
```

## TESTING
ctrl-c to stop server
```
python manage.py test
or 
python3 manage.py test
```
#### Expected Outcome::
<img width="635" alt="Screen Shot 2022-09-14 at 12 19 21 PM" src="https://user-images.githubusercontent.com/78772769/190208656-e3ca8e6a-6278-4a50-b001-af3ac903c83a.png">

### Test Coverage Report

<img width="545" alt="Screen Shot 2022-09-13 at 11 48 49 PM" src="https://user-images.githubusercontent.com/78772769/190207698-898065b0-634a-4b5f-a3e3-98e793add90e.png">

## START AND INVOKE
Start server
```
python manage.py runserver
OR
python3 manage.py runserver
```
### In a terminal ::

Sending a message from one user to another:
```
curl -d '{"user_author":1, "user_recipient":2, "message":"this is a test message"}' -H "Content-Type: application/json" -X POST http://localhost:8000/api/messages/
```
Recent messages from all senders from the last 30 days limited to 100 messages:
```
curl -v http://localhost:8000/api/messages/
```
Recent messages for a recipient from a specific sender for the last 30 days limited to 100 messages:
```
curl -v http://localhost:8000/api/messages/2/1/
```












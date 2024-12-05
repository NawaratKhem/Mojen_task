Clone the project and then run with following command

python app.py

There are three routes;

1. /ping
   No authentication, always return 200 status code with empty body.
   
3. /test-auth
   Authenticate with the api key.
   Upon valid api key, 200 status code with empty body will be returned.
   401 status code with {"error": "unauthorized"} otherwise
   
4. /test-auth-response
   Upon valid api key, 200 status code with {"message": "hello world"} body will be returned.
   401 status code with {"error": "unauthorized"} otherwise

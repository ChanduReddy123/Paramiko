# Paramiko
## This module is for executing the linux commands over the remote linux machines via SSH
* Clone this repo or download the package.zip 
* Extract the file and edit the lambda_function.py file as required and zip it back
* Upload the same to AWS lambda function 
* you are good to go.

### Issues I've faced 
* `pip install paramiko -t . ` will install the paramiko modules in your present working directory. 
* The modules I've downloaded in Windows didn't work but it worked with linux
* Lambda function with python 3.7 as Runtime isn't working as expected changing it to 3.6 executed my code with ease.



Using the paramiko module with AWS lambda function 



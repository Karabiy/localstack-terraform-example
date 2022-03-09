# First make sure you've started docker compose. In order to start it you can use 
```shell
sudo docker-compose up -d 
```
# Now you need to create infra 
In order to create it, first you need to download provider binary locally.
https://learn.hashicorp.com/tutorials/terraform/install-cli - cli installation   
Make sure you've terraform installed. 
```shell
terraform init
```
That's the moment of win - you need to run terraform plan in order to check on which resources will be created 
```shell
terraform plan
```
As you've seen, the base resource which would be created is dynamodb, now you can test its usage with simple python script included here
```shell
python3 app-example.py
```

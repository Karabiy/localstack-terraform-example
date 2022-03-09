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


# Useful links
- dynamodb, lambda, kinesis: https://dev.to/mrwormhole/localstack-with-terraform-and-docker-for-running-aws-locally-3a6d   
- s3: https://stackoverflow.com/questions/59307312/localstack-create-s3-bucket-locally-with-terraform-doesnt-have-a-name
- sqs: https://github.com/farhad-taran/Terraform-Localstack/blob/master/main.tf
- sqs, sns, iam & others small: https://github.com/jupitercl/aws-localstack-terraform-sns-sqs-lambda/tree/master/terraform
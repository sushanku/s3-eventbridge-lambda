# Description
This repo is for learning aws eventbridge. I have made a scenario where one can upload archive(zip and tar) file in s3 bucket(bucket-1). This uploaded events wil be triggered by eventbridge and triggers the lambda function. Lambda function will then unarchive the archive file in bucket-2

## This Repository contains two folders. 
**Terraform**: This folder contains the terraform code that does following things:
* Creates Two S3 bucket, one for uploading .zip and .archive file and other bucket for extracting those uploaded archived files (check s3.tf file and change the bucket name because s3 buckets are region specific and will not allow the creation of same bucket name)
* Extracting to next bucket(bucket where extracted files are stored) is done by lambda function. 
* Lambda function get's triggered whenever there is new upload in s3 bucket(bucket where archive is stored)
* All the necessary iam roles for lambda function and eventbridge is provided

**Lambda** - This folder contains the lambda function code to unarchive the archived files from source bucket(this is identified by the eventbridge event itself) to destination bucket

## How to use the repo
Use git clone to clone the repository and make changes
    - `terraform/base` this directory contains all the resources to be created for this eventbridge task
    - Enter `cd terraform/env` to enter into the terraform main.tf directory 
    - Execute `terraform init` to initialize the terraform provider
    - Execute `terraform plan` to create a plan of the resources that are going to change or get created
    - Finally,`terraform apply` to apply this plan and get those resources created in AWS account

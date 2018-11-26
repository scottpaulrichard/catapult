# Catapult

DevOps Coding Test
Goal
Develop an AWS S3 storage analysis tool. Deploy this application in a docker container and have this hosted on an externally accessible website.
Prerequisites
You will need an AWS account. Create one if you don't own one already. You can use free-tier resources for this test.
The Task
The tool is a simple utility that is rendered on a webpage that returns information over all S3 buckets in an Amazon account.
Your tool must work on Linux, OSX and Windows.
It must be easy to install and use.
Ideally, your tool won't require installation of any other tools / libraries / frameworks to work.
Your solution should return results within seconds
Set of application and containerization:
Deploy the above utility with data rendered in a simple web page in a docker container.
Be publicly accessible.
Run Nginx or IIS inside a docker container
Automate the server setup using Terraform.
Use a configuration management tool (such as Puppet, Chef or Ansible) to bootstrap the server. Document what is happening in your definition files
Make it Cloud provider agnostic - i.e. can we repeat this in Azure or Google Cloud Platform

The utility/web page must return the following information
Bucket name
Creation date (of the bucket)
Number of files
Total size of files
Last modified date (most recent file of a bucket)
And the most important of all, how much does it cost

catapult.tf
-------
Terraform file that will stand up the machine and configure the thing to be accessible by whoever puts there name in it. Configure your AWS access code in the file ./terraform.tfvars:

    # Your secrets
    aws_access_key = "your_aws_access_key"
    aws_secret_key = "your_aws_secret_key"
    key_name = "your_username"
    private_key_path = "path_to_your_private_key"


Run the following command in the base directory of catapult to see the plan for what will be done:

    terraform plan

use the following command to apply the plan:

    terraform apply

catapultPythonApp
-------
this is where the app lives.

for a built image:

docker pull scottpaulrichard/catapult

Ansible bootstraps docker on remote machine

# Catapult

catapult.tf
-------
Terraform file that will stand up the machine and configure the thing to be accessible by whoever puts there name in it. Configure your AWS access code in the file ./terraform.tfvars:

    # Your secrets
    aws_access_key = "your_aws_access_key"
    aws_secret_key = "your_aws_secret_key"
    key_name = "your_username"
    private_key_path = "path_to_your_private_key"


Run the following command in the base directory of vent to see the plan for what will be done:

    terraform plan

use the following command to apply the plan:

    terraform apply

catapultPythonApp
-------
this is where the app lives.

for a built image:

docker pull scottpaulrichard/catapult

Ansible bootstraps docker on remote machine 

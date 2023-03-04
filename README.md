# Python Boto3
This is **NOT** an official library, this is my own personal code that I used to learn the AWS Boto3 Python library for automating tasks on AWS. I cannot garrentee that all of this code will work forever or in general. The official documentation is [here](https://boto3.amazonaws.com/v1/documentation/api/latest/index.html). **AWS CLI IS A MUST FOR AWS BOTO3**. The code is also setup in a way where all requests are passed through as functions. For example
```python
def start_ec2_instances(*args):
    """Instance IDs to Start"""

    for x in args:
        try:
            response = ec2.start_instances(
                InstanceIds=[
                    x,
                ],
                DryRun=True
            )
            print(response)
        except botocore.exceptions.ClientError:
            print(f'EC2 Instance {x}: cannot be found!')

start_ec2_instances(instance_id1, instance_id2, ect)
```
With that out of the way I hope this helps you on your journey to mastering Boto3!
## Module Setup
Boto3 can just be obtained by pip, its pretty easy to install. A lot of people get tripped up by most scripts not requiring AWS Access keys to use. AWS Boto3 needs to be setup with your credentials before you use it without a key specified in a script. Below will show you how.

### Install AWS CLI
To install boto3, were just going to use pip.
```bash
pip3 install boto3
```

| OS        | Install                                                                                                                  | Where To Execute |
|-----------|--------------------------------------------------------------------------------------------------------------------------|------------------|
| Linux x86 | curl "https://awscli.amazonaws.com/awscli-exe-linux-x86_64.zip" -o "awscliv2.zip" unzip awscliv2.zip sudo ./aws/install  | Terminal         |
| Linux ARM | curl "https://awscli.amazonaws.com/awscli-exe-linux-aarch64.zip" -o "awscliv2.zip" unzip awscliv2.zip sudo ./aws/install | Terminal         |
| Windows   | msiexec.exe /i https://awscli.amazonaws.com/AWSCLIV2.msi && msiexec.exe /i https://awscli.amazonaws.com/AWSCLIV2.msi /qn | Powershell       |
| Mac       | https://awscli.amazonaws.com/AWSCLIV2.pkg                                                                                | Use GUI          |

### Verify install and setup credentials

For checking if the install was done correctly
```bash
aws --version
```

To set your credentials you are going to need your AWS Access Key and your private key. Next your going to want to open the file that they are contained in and paste them into the following prompt. DO NOT GIVE THESE KEYS OUT TO ANYONE! USE IN AWS CLI ONLY. 

```bash
aws configure
```
^ This command will get you setup and guide you through the credential process.

## Now What?
AWS Boto3 is a little weird in the sense that it uses system varibles if you dont specify an access key. So all of the scripts on this repository you can just run and the change will be made on aws. Be weary of this and always stop/delete unneeded services. 

# Feel Free to do whatever you want with any of this code <3.
## Enjoy it, fork it, fuck it up.
### Report any issues with code to issues tab!

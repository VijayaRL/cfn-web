## README

### Project Overview
AWS CloudFormation Template: VPC, ALB, EC2
Overview
This project uses AWS CloudFormation to setup and manages various AWS resources including Virtual Private Cloud (VPC), an Application Load Balancer (ALB), and an EC2 instance serving as a web server.

###  Pre-Requisites:
1. **Create S3 bucket**: Refer to the https://docs.aws.amazon.com/AmazonS3/latest/userguide/GetStartedWithS3.html and follow step 1 to create the S3 bucket and step 2 to upload python script regions3.py file as S3 object. makesure to update the bucket name in cfn-ec2.yml at line number 23
2. **AWS Region**: Make sure you are in eu-east-1 (ireland) region.
3. **Create KeyPair**: Create an EC2 KeyPair https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/create-key-pairs.html#having-ec2-create-your-key-pair. This is to connect to EC2 via ssh.
4. **Configure AWS CLI**: Set up your AWS CLI with credentials that have necessary permissions for creating and managing the AWS resources.

###  Parameters
InstanceType: EC2 instance type to be launched.
AllowedIPAddress: IP address (CIDR format) allowed to access the web server.
EC2KeyPair: Existing EC2 KeyPair for SSH access.
S3ObjectPath: S3 bucket and Python script path.
VPCCIDR: CIDR block for the VPC.
PublicSubnetA and PublicSubnetB: CIDR blocks for public subnets in different availability zones.
Resources
1. VPC (Virtual Private Cloud)
Creates a VPC with specified CIDR block for subnets and the VPC.
2. Subnets (PubSubnetZoneA and PubSubnetZoneB)
Defines two public subnets in different availability zones.
Associates them with the VPC.
3. Internet Gateway
Creates an internet gateway and associates it with the VPC.
4. Routing
Defines a route table and associates it with the public subnets.
Routes traffic through the internet gateway.
5. Security Groups (EC2SecurityGroup and ELBSecurityGroup)
Defines security groups for EC2 instances and the ALB.
Specifies inbound rules for SSH and HTTP in EC2 Security Group and HTTP in ALB Security Group
6. IAM Role and Instance Profileb (Adjust if needed)
Creates an IAM role and instance profile for the EC2 instance.
Grants necessary permissions for SSM, S3, EC2, and describe tags.
7. EC2 Instance (AmazonLinuxInstance)
Launches an EC2 instance using Amazon Linux 2.
Installs and configures Apache, installs Python dependencies, and executes a Python script from S3.
Sends a CloudFormation signal upon successful initialization.
8. Elastic Load Balancer (ALB)
Creates an Application Load Balancer with specified subnets and security group.
Defines an ALB listener forwarding traffic to the EC2 Target Group.
9. EC2 Target Group (EC2TargetGroup)
Creates an Elastic Load Balancer target group.
Specifies health check settings and associates it with the EC2 instance.
10. Elastic IP (EIP)
Associates an Elastic IP address with the EC2 instance.

### Outputs:
VPC ID
ALB hostname - You use tho access the website.
EC2 instance ID
EC2 Target Group
ALB ID
SSH access command

### Usage Guide
Deploying the CloudFormation template can be done in 2 ways using the AWS Management Console or AWS CLI.
**AWS Console**:
   - a. Login to AWS Account
   - b. Navigate to CloudFormation Page
   - c. Click on 'Stacks' --> Select 'With New Resource(Standard) from 'Create Stack'
   - d. Choose 'Template Ready' and 'Upload a Template File' options and provide the 'cfn-ec2.yml' cloudformation file from local system -> click Next
   - e. Specify the stack details by giving stack name, parameters(AllowedIP Addresses), select ec2 keypair from dropdown and click Next
   - f. Click Next in 'Configure stack options' page
   - g. Click 'tick/check box' option at the bottom of the Review stack page and click next
   - h. Monitor the CloudFormation stack creation progress in the 'Events' tab.
   - i. Access output page by clicking on 'ALBHostName' url value provided in the outputs tab.

**AWS Cli**:

**Enhancements**:
Implement CICD via github to deploy the template in AWS.
Implement pre-commit hooks to check yml and python errors


# Example 402 Project
This is an example COM S 402 (Senior Design) project. The project comprises of a static frontend built with [React](https://reactjs.org/) and a backend API made with [Flask](https://flask.palletsprojects.com/en/2.2.x/) (Python).

#### Purpose
I made this to show and walk through at a lecture I will be giving on Cloud (specifically [AWS](https://aws.amazon.com)).


### Considerations
Again, this is an example. Ideally students can use parts of this codebase as a reference while building out their cloud architecture. \
With this in mind, there are some immediate notes and things to consider about this example.

#### Serverless
If you are creating a traditional API/backend. I'd consider building a [serverless](https://youtu.be/W_VV2Fx32_Y) API instead. Essentially, this eliminates the need to have and manage a VM.

#### Need a Database?
If you need a database, look into [AWS RDS](https://aws.amazon.com/rds/). Using RDS will allow you to keep your RDS separate from the EC2 instance, which is arguably a better practice.

##### NoSQL
If you have very simple relationships, or even none at all, then NoSQL is a good choice for your project. If that's the case, consider using [DynamoDB](https://aws.amazon.com/dynamodb).

#### Docker
Docker is wonderful, however it's use is a little off in this example. \
What's missing from this example is the use of a [Docker Registry](https://docs.docker.com/registry/). I would recommend using [Docker Hub](https://docs.docker.com/docker-hub/).

#### One or Many stacks?
I would advocate against having a frontend and a backend stack for a project like this. Instead, a single stack will be much easier to manage.


## Connecting Repository to AWS
If you still need to grant the repository access to deploy resources inside your AWS account, follow these steps.

### 1. Create an IAM Role
In your AWS Account, create a new IAM Role with the permissions you deem necessary. The role must include permissions to create/update/delete resources in the following services.

  - [Cloudformation](https://aws.amazon.com/cloudformation/)
  - [CloudFront](https://aws.amazon.com/cloudfront/)
  - [S3](https://aws.amazon.com/s3/)
  - [EC2](https://aws.amazon.com/ec2/)
  - [Systems Manager (SSM)](https://aws.amazon.com/systems-manager/)

**Note:** It is best practice to follow the [least-Privilege Principle](https://g.co/kgs/Erp38S)

### 2. Configure OpenID to connect AWS and GitHub Actions
Refer to GitHub's docs for [Configuring OpenID Connect in AWS](https://docs.github.com/en/actions/deployment/security-hardening-your-deployments/configuring-openid-connect-in-amazon-web-services) for guidance.

### 3. Add essential secrets to your GitHub repository.

Add the following secrets via **Repository settings** > **Secrets** > **Actions**.

  - `IAM_ROLE_ARN` containing your IAM Role ARN from step 1.


---
Once steps 1-3 are complete, your repository should have the access it needs to deploy resources into your AWS account.

# Example 402 Project
This is an example COM S 402 (Senior Design) project. The project comprises of a static frontend built with React and a backend API made with Flask (Python).

The purpose of this is for a lecture I am giving on Cloud (specifically AWS) to a COM S 402 class.


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


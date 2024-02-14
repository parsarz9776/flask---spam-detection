Spam Detection Flask App

![spam](https://github.com/parsarz9776/flask---spam-detection/assets/105837987/eab88716-b938-4e65-8ced-38d0a92f3878)


This project implements a simple web application using Flask for spam detection. 
The application uses a pre-trained Naive Bayes model to classify input text as either "Spam" or "Ham" (non-spam). 

To create and run a docker container, type these commands in the same place as the Dockerfile

```
docker build -t app_name .
docker run -p 127.0.0.1:5000:5000 app_name
```

To deploy it using AWS elasticbeanstalk follow the steps below. There might be different options now, select the default choices

```
eb init

Select a default region
1) us-east-1 : US East (N. Virginia)
2) us-west-1 : US West (N. California)
3) us-west-2 : US West (Oregon)
4) eu-west-1 : EU (Ireland)
5) eu-central-1 : EU (Frankfurt)
6) ap-south-1 : Asia Pacific (Mumbai)
7) ap-southeast-1 : Asia Pacific (Singapore)
8) ap-southeast-2 : Asia Pacific (Sydney)
9) ap-northeast-1 : Asia Pacific (Tokyo)
10) ap-northeast-2 : Asia Pacific (Seoul)
11) sa-east-1 : South America (Sao Paulo)
12) cn-north-1 : China (Beijing)
13) us-east-2 : US East (Ohio)
14) ca-central-1 : Canada (Central)
15) eu-west-2 : EU (London)
(default is 3): 3

Select an application to use
1) [ Create new Application ]
(default is 1): 1

Enter Application Name
(default is "Elastic-Beanstalk-Docker-Flask"): YOUR_APP
Application YOUR_APP has been created.

It appears you are using Docker. Is this correct?
(Y/n): Y

Select a platform version.
1) Docker 17.06.2-ce
2) Docker 17.03.2-ce
3) Docker 1.12.6
4) Docker 1.11.2
5) Docker 1.9.1
6) Docker 1.7.1
7) Docker 1.6.2
8) Docker 1.5.0
(default is 1): 1
Note: Elastic Beanstalk now supports AWS CodeCommit; a fully-managed source control service. To learn more, see Docs: https://aws.amazon.com/codecommit/
Do you wish to continue with CodeCommit? (y/N) (default is n): n
Do you want to set up SSH for your instances?
(Y/n): Y

Select a keypair.
1) [ Create new KeyPair ]
(default is 1): 1

eb create name_you_environment_here

```

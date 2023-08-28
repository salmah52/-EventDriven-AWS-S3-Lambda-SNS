# EventDriven-AWS-S3-Lambda-SNS
# Building an Event Driven Architecture Using AWS S3, Lambda, and SNS Services

## Introduction

In a world where data flows seamlessly and decisions are made in real-time, event-driven architectures have emerged as a game-changer. This project delves into creating an event-driven architecture utilizing AWS services such as S3, Lambda, and SNS. Explore how cloud services can orchestrate dynamic processes, expanding both your technical prowess and understanding.

## Objective

The goal of the project is to establish a robust event-driven architecture that responds intelligently to data changes in an AWS S3 bucket. By leveraging AWS Lambda functions and SNS notifications, this project enables timely processing and distribution of relevant data updates to downstream systems.

## Key Components

1. **AWS S3 Bucket**: Serving as the event source, the S3 bucket stores data files that trigger the event-driven workflow upon new additions.
2. **AWS Lambda Functions**: Design tailored Lambda functions to execute specific actions based on incoming events, like processing, transforming, and analyzing data as per business logic.
3. **Distinguishing Files and Folders**: Learn how to differentiate between file and folder uploads using the object key in the S3 event.
4. **AWS SNS (Simple Notification Service)**: Acting as the glue, SNS facilitates seamless communication between Lambda functions and downstream systems. Lambda functions publish notifications to SNS topics upon events.

## Workflow

1. **Event Trigger**: New data files in the S3 bucket trigger the architecture, initiating the workflow.
2. **Lambda Functions in Action**: Tailored Lambda functions process the incoming data. Tasks such as data validation, transformation, and enrichment are achieved through these functions.
3. **SNS Notifications**: After processing, Lambda functions publish notifications to SNS topics. This begins the distribution of processed data to subscribing systems, facilitating real-time updates.

## Installation and Usage

1. **Prerequisites**: Ensure you have an AWS account, AWS CLI, and Python 3.7+ installed.
2. **Installation**: Clone this repository and install required Python libraries using `pip install -r requirements.txt`.
3. **Configuration**: Configure your S3 bucket, IAM roles, Lambda functions, and SNS topics as described in the project documentation.
4. **Deploy**: Deploy the Lambda functions using the AWS Management Console, AWS CLI, or other preferred methods.
5. **Testing**: Upload files and folders to the S3 bucket and monitor SNS topics for notifications.

## Project Structure

- `lambda_function.py`: Contains the AWS Lambda function code responsible for processing S3 events and sending notifications.
- `example_test_event.json`: Provides an example test event for simulating S3 events in the Lambda console.

## License

This project is licensed under the MIT License. Feel free to fork and modify it to suit your needs.

## Acknowledgments

A sincere thank you to AWS for their comprehensive documentation and services that empower projects like this.

## Contact

For questions, suggestions, or contributions, please reach out via [email](mailto:youremail@example.com) or GitHub.

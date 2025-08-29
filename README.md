# AWS Serverless Image Classification Project

This repository contains all the code and assets for a serverless machine learning (ML) pipeline deployed on **AWS**. The project demonstrates an end-to-end workflow to automatically detect what kind of vehicle Scones Unlimited's delivery drivers have, in order to route them to the correct loading bay and orders.

---

## Repository Structure

The project is organized to be clear and easy to follow.

* `image-classification-pipeline.ipynb`: The main **Jupyter Notebook** file that serves as a project report. It details the data preparation, model training, and deployment steps. It also includes the visualization code.
* `lambda_functions/`: This directory holds the code for the three Lambda functions used in the serverless workflow:
    * `classifier.py`
    * `filterInferences.py`
    * `serializeImageData.py`
* `state-machine-definition.json`: This file contains the JSON definition of the AWS Step Functions workflow.
* `screenshots/`: This folder contains all the visual documentation for the project.
    * `lambda/`: Screenshots of the AWS Lambda function configurations.
    * `step-functions/`: Screenshots of the Step Functions workflow.
    * `sns-error.png`: A screenshot documenting the SNS error encountered during implementation.

---

## Project Overview

The core of this project is a three-step serverless pipeline orchestrated by **AWS Step Functions**. This workflow automates the process of taking an image, classifying it with an ML model, and applying business logic.

1.  **Data Ingestion**: Images are stored in an S3 bucket.
2.  **Serverless Workflow**: An AWS Step Functions state machine orchestrates three AWS Lambda functions:
    * `serializeImageData`: Encodes an image from S3 into a Base64 string.
    * `classifier`: Sends the encoded image to a deployed **SageMaker** endpoint for classification.
    * `filterInferences`: Filters the model's predictions based on a predefined confidence threshold.
3.  **Model Monitoring**: **SageMaker Model Monitor** captures inference data, allowing for visualizations that track model performance and confidence scores over time.
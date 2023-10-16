# README file for Computer Vision Internship Project by Aravind Sridharan

## Contact Aravind: aravind.14may93@gmail.com, +91 96770 80857

## Description
This is the read-me file for the computer vision Internship project done by Aravind Sridharan in association with Physics Wallah.

## Basic Project Workflow overview

### Module #1: Data Ingestion and transformation in AWS SageMaker

Step #1: Selection of appropriate dataset for disease detection

Step #2: Dataset ingestion from https://www.kaggle.com/datasets/paultimothymooney/chest-xray-pneumonia directly in AWS SageMaker

Step #3: Data resizing to 224x224 format and convertion to grayscale in AWS SageMaker

Step #4: Split dataset into ‘train’ and ‘test’

Step #5: Upload ‘train.lst’ and ‘test.lst’ to S3

### Module #2: Model Training and Evaluation in AWS SageMaker

Step #1: Import .lst files from S3 bucket

Step #2: Setup the image classification model with parameters

Step #3: Setup the training and hyperparameter tuning job

Step #4: Run training jobs

Step #5: Evaluate models and choose the best one for deployment

### Module #3: Model Deployment

Step #1: Create and activate endpoint of best model

Step #2: Create a lambda function to access the endpoint

Step #3: Create an API to interact with the endpoint and test this API using Postman

Step #4: Create a flask webapp to build a front-end for the deployed model

## Basic execution overview

Step #1: Execute the SageMaker notebook inside AWS to complete Modules 1 and 2 completely.

Step #2: After execution of the notebook, the endpoint should be ensured that it is active.

Step #3: Create Lambda function using the code given in the "BACKEND FILES" folder.

Step #4: Create API Gateway to package this lambda function.

Step #5: Execute the front end python code to deploy the flask webapp that hosts the API.

Step #6: Open http://127.0.0.1:2000/home link in web browser.

Step #7: Upload chest x-ray images to see prediction results

Step #8: Delete the endpoint after using the application to avoid unnecessary SageMaker costs.
# AWS Rekognition Image Labeling with Python

This project demonstrates how to build a simple image labeling system using Amazon Rekognition. It walks through setting up an S3 bucket, uploading images, configuring the AWS CLI, writing a Python script to detect image labels, and visualizing them with bounding boxes.

# Total Cost Estimate
For a basic setup with a few images, this project typically costs ₹0–₹500 (~$0–$6/month). In most cases, it remains completely free under the AWS Free Tier, which includes up to 1,000 image analyses per month and limited S3 storage. Since the tools used are free, you’ll only incur costs if usage exceeds free limits.

# Project Overview

Amazon Rekognition is a powerful AWS service that uses deep learning to analyze images and videos. In this project, we:

Store images in Amazon S3

Interact with AWS services via the AWS CLI

Use boto3 to communicate with Rekognition

Automatically detect labels and draw bounding boxes on objects in an image

## Step 1: Create an Amazon S3 Bucket

First, create an S3 bucket to store your images:

Sign in to the AWS Management Console.

Navigate to Amazon S3 and click Create bucket.

Enter a unique bucket name and choose a region.

Finish the setup by clicking Create bucket.

This bucket will serve as the storage location for the images you want to analyze.

## Step 2: Upload Images to Your Bucket

With the bucket created:

Upload the images from your local machine to S3.

You can upload multiple images for the labeling system to analyze and learn from.

## Step 3: Install and Configure AWS CLI

Install the The AWS Command Line Interface (CLI) allows us to interact with AWS services directly from the terminal.

Check if the installation was successful:

aws --version

## Step 4: Build the Python Script

Install Required Libraries

Make sure the necessary Python libraries are installed:

pip install boto3 matplotlib pillow

Write the Python Script

Create a file called label_detector.py and add the code in the label_detector.py file.

## Step 5: Run the Python Script

In your terminal, navigate to the directory containing the script and run:

python label_detector.py

The output will include:

A list of up to 10 labels detected in the image

Confidence scores for each label

A visualization of the image with red bounding boxes around detected objects

## Final Output

The program outputs something like:

Detected labels for sample.jpg:

Label: Dog
Confidence: 99.23

Label: Pet
Confidence: 97.88

Label: Animal
Confidence: 96.11
...
Total Labels Detected: 10

And a pop-up window will display the image with bounding boxes and labels annotated.

## Challenges Encountered

While the project was highly successful and demonstrated the strong capabilities of Amazon Rekognition, a few challenges highlighted areas for improvement. At times, the model misclassified objects or assigned inaccurate labels — for instance, confusing genders in group photos, detecting people where none were present, or overlooking smaller but important objects in complex scenes. These issues reveal that although Rekognition is powerful, its pre-trained models are not perfect and can benefit from further fine-tuning, domain-specific training, or additional contextual data to boost accuracy and reliability.

Despite these minor limitations, the project was an exciting exploration of how machine learning and cloud-based AI can analyze and interpret images at scale. It provided valuable insights into real-world applications of computer vision and is highly recommended for anyone interested in AI-driven image processing.


## Future Enhancements

Add support for local image uploads without S3

Automate the upload and labeling pipeline

Deploy the system as a web application

📜 License

This project is licensed under the MIT License – feel free to use, modify, and share.


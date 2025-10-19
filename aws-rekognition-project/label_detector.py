import boto3
import matplotlib.pyplot as plt
import matplotlib.patches as patches
from PIL import Image
from io import BytesIO

def detect_labels(photo, bucket):
    # Create a Rekognition client
    client = boto3.client('rekognition')

    # Detect labels in the image
    response = client.detect_labels(
        Image={'S3Object': {'Bucket': bucket, 'Name': photo}},
        MaxLabels=10
    )

    # Print detected labels and confidence scores
    print('Detected labels for:', photo)
    for label in response['Labels']:
        print("Label:", label['Name'])
        print("Confidence:", round(label['Confidence'], 2))
        print()

    # Load the image from S3
    s3 = boto3.resource('s3')
    obj = s3.Object(bucket, photo)
    img_data = obj.get()['Body'].read()
    img = Image.open(BytesIO(img_data))

    # Show the image and draw bounding boxes
    plt.imshow(img)
    ax = plt.gca()
    for label in response['Labels']:
        for instance in label.get('Instances', []):
            bbox = instance['BoundingBox']
            left = bbox['Left'] * img.width
            top = bbox['Top'] * img.height
            width = bbox['Width'] * img.width
            height = bbox['Height'] * img.height

            rect = patches.Rectangle(
                (left, top), width, height,
                linewidth=1, edgecolor='r', facecolor='none'
            )
            ax.add_patch(rect)

            label_text = f"{label['Name']} ({round(label['Confidence'], 2)}%)"
            plt.text(left, top - 2, label_text, color='r', fontsize=8,
                     bbox=dict(facecolor='white', alpha=0.7))

    plt.show()
    return len(response['Labels'])

def main():
    # S3 image name and bucket name
    photo = 'helicopter.jpg'  #replace with object name
    bucket = 'image-recognition-151025' #replace with bucket name

    label_count = detect_labels(photo, bucket)
    print("Total labels detected:", label_count)

if __name__ == "__main__":
    main()

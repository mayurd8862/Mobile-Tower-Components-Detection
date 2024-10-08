from ultralytics import YOLO
import cv2

# Load the trained model
model = YOLO('./runs/detect/train/weights/last.pt')  # Path to your trained model

# Load an image
img_path = 'image.png'  # Replace with your image path

img = cv2.imread(img_path)

# Run detection
results = model(img)

# Draw bounding boxes on the image
annotated_img = results[0].plot()

# Display the image with bounding boxes
cv2.imshow('Detected Image', annotated_img)

# Wait for a key press and close the window
cv2.waitKey(0)
cv2.destroyAllWindows()

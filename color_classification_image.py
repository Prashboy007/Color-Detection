import cv2
from color_recognition_api import color_histogram_feature_extraction
from color_recognition_api import knn_classifier
import os.path
import sys

try:
    source_image = cv2.imread(sys.argv[1])

except:
    source_image = cv2.imread('testit2.png')
prediction = 'n.a.'

PATH = './training.data'

if os.path.isfile(PATH) and os.access(PATH, os.R_OK):
    print('training data is ready, classifier is loading...')
else:
    print('training data is being created...')
    open('training.data', 'w')
    color_histogram_feature_extraction.training()
    print('training data is ready, classifier is loading...')

color_histogram_feature_extraction.color_histogram_of_test_image(source_image)
prediction, test_data_list = knn_classifier.main('training.data', 'test.data')
print('Detected color is:', prediction, "testing data is ", test_data_list)
rgb_string = ', '.join(str(val) for val in test_data_list)

text = f"Prediction: {prediction}  RGB: {rgb_string}"  # f-string for formatted text

cv2.putText(
    source_image,
    text,
    (15, 45),
    cv2.FONT_HERSHEY_PLAIN,
    1,
    200,
)

cv2.imshow('color classifier', source_image)
cv2.waitKey(0)

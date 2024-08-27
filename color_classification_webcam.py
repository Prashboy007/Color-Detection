import cv2
from color_recognition_api import color_histogram_feature_extraction
from color_recognition_api import knn_classifier
import os
import os.path

cap = cv2.VideoCapture(0)
(ret, frame) = cap.read()
prediction = 'n.a.'

PATH = './training.data'

if os.path.isfile(PATH) and os.access(PATH, os.R_OK):
    print ('training data is ready, classifier is loading...')
else:
    print ('training data is being created...')
    open('training.data', 'w')
    color_histogram_feature_extraction.training()
    print ('training data is ready, classifier is loading...')

try:
    while True:
        (ret, frame) = cap.read()

        cv2.putText(
            frame,
            'Prediction: ' + str(prediction),
            (15, 45),
            cv2.FONT_HERSHEY_PLAIN,
            3,
            (200, 0, 0),
        )

        cv2.imshow('color classifier', frame)

        color_histogram_feature_extraction.color_histogram_of_test_image(frame)

        prediction = knn_classifier.main('training.data', 'test.data')
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

except KeyboardInterrupt:
    print("Keyboard Interrupt detected. Exiting gracefully.")

cap.release()
cv2.destroyAllWindows()

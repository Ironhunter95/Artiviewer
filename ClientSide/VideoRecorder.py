import cv2
import threading
import time
from keras.models import load_model
from keras.preprocessing.image import img_to_array
import numpy as np

class VideoRecorder():

    # Video class based on openCV
    def __init__(self):

        self.open = True
        self.device_index = 0
        self.fps = 30  # fps should be the minimum constant rate at which the camera can
        self.fourcc = "MJPG"  # capture images (with no decrease in speed over time; testing is required)
        self.frameSize = (640, 480)  # video formats and sizes also depend and vary according to the camera used
        self.video_filename = "temp_video.avi"
        self.video_cap = cv2.VideoCapture(self.device_index)
        self.video_writer = cv2.VideoWriter_fourcc(*self.fourcc)
        self.video_out = cv2.VideoWriter(self.video_filename, self.video_writer, self.fps, self.frameSize)
        self.frame_counts = 1
        self.start_time = time.time()

    # Video starts being recorded
    def record(self):

        #		counter = 1
        timer_start = time.time()
        timer_current = 0
        face_classifier = cv2.CascadeClassifier('./Emotion Recognition/frontFaceDetection.xml')
        classifier = load_model('Emotion Recognition/emotionDetection.h5')

        class_labels = ['Angry', 'Happy', 'Neutral', 'Sad', 'Surprise']

        while (self.open == True):
            ret, video_frame = self.video_cap.read()
            if (ret == True):
                labels = []
                self.video_out.write(video_frame)
                #					print str(counter) + " " + str(self.frame_counts) + " frames written " + str(timer_current)
                self.frame_counts += 1
                #					counter += 1
                #					timer_current = time.time() - timer_start
                time.sleep(0.03)

                # Uncomment the following three lines to make the video to be
                # displayed to screen while recording

                gray = cv2.cvtColor(video_frame, cv2.COLOR_BGR2GRAY)
                faces = face_classifier.detectMultiScale(gray, 1.3, 5)

                for (x, y, w, h) in faces:
                    cv2.rectangle(video_frame, (x, y), (x + w, y + h), (255, 0, 0), 2)
                    roi_gray = gray[y:y + h, x:x + w]
                    roi_gray = cv2.resize(roi_gray, (48, 48), interpolation=cv2.INTER_AREA)

                    if np.sum([roi_gray]) != 0:
                        roi = roi_gray.astype('float') / 255.0
                        roi = img_to_array(roi)
                        roi = np.expand_dims(roi, axis=0)

                        # make a prediction on the ROI, then lookup the class

                        preds = classifier.predict(roi)[0]
                        label = class_labels[preds.argmax()]
                        label_position = (x, y)
                        cv2.putText(video_frame, label, label_position, cv2.FONT_HERSHEY_SIMPLEX, 2, (0, 255, 0), 3)
                    else:
                        cv2.putText(video_frame, 'No Face Found', (20, 60), cv2.FONT_HERSHEY_SIMPLEX, 2, (0, 255, 0), 3)
                cv2.imshow('Interview Webcam', video_frame)
                cv2.waitKey(1)
            else:
                break

            # 0.16 delay -> 6 fps
            #

    # Finishes the video recording therefore the thread too
    def stop(self):

        if self.open == True:

            self.open = False
            self.video_out.release()
            self.video_cap.release()
            cv2.destroyAllWindows()

        else:
            pass

    # Launches the video recording function using a thread
    def start(self):
        video_thread = threading.Thread(target=self.record)
        video_thread.start()


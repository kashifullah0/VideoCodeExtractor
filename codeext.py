import os
import cv2
import pytesseract
from PIL import Image
import tempfil  e

class CodeExtractor:

    def __init__(self, uploaded_file):
        with tempfile.NamedTemporaryFile(delete=False, suffix=".mp4") as tmp:
            tmp.write(uploaded_file.read())
            self.video_path = tmp.name

        if not os.path.exists("frames"):
            os.mkdir("frames")

        self.text_output = []
        self.extract_frames()
        self.save_text()

    def extract_frames(self):
        cap = cv2.VideoCapture(self.video_path)
        frame_count = 0

        while True:
            ret, frame = cap.read()
            if not ret:
                break

            if frame_count % 30 == 0:
                gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
                frame_filename = f"frames/frame_{frame_count}.jpg"
                cv2.imwrite(frame_filename, gray)
                text = pytesseract.image_to_string(Image.open(frame_filename))
                self.text_output.append(f"--- Frame {frame_count} ---\n{text.strip()}")

            frame_count += 1
        cap.release()

    def save_text(self):
        with open("extracted_text.txt", "w") as f:
            f.write("\n".join(self.text_output))
    
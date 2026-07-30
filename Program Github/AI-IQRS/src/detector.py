from ultralytics import YOLO

from config import (
    MODEL_PATH,
    CONFIDENCE,
    IMAGE_SIZE
)


class Detector:

    def __init__(self):

        print("===================================")
        print(" Loading YOLO Model...")
        print("===================================")

        self.model = YOLO(str(MODEL_PATH))

        print("Model Loaded Successfully\n")

    def detect(self, frame):

        results = self.model.predict(
            source=frame,
            conf=CONFIDENCE,
            imgsz=IMAGE_SIZE,
            verbose=False
        )

        result = results[0]

        annotated_frame = result.plot()

        detected_components = []

        if result.boxes is not None:

            for box in result.boxes:

                class_id = int(box.cls[0])

                component_name = self.model.names[class_id]

                detected_components.append(component_name)

        return annotated_frame, detected_components
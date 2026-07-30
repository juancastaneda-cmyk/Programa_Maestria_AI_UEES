import cv2
import time

from camera import Camera
from detector import Detector
from rules_engine import RulesEngine
from gui import InspectionGUI


def main():

    # ---------------------------------------
    # Initialize Modules
    # ---------------------------------------

    camera = Camera()
    detector = Detector()
    rules = RulesEngine()
    gui = InspectionGUI()

    print("\n===================================")
    print(" AI-IQRS Inspection System")
    print("===================================")
    print("SPACE = Inspect Tray")
    print("ESC   = Exit")
    print("===================================\n")

    # ---------------------------------------
    # Initial GUI State
    # ---------------------------------------

    inspection = {
        "PASS": None,
        "Detected": {},
        "Missing": [],
        "Extra": []
    }

    while True:

        frame = camera.read()

        if frame is None:
            print("Camera Error")
            break

        # YOLO Detection
        annotated_frame, components = detector.detect(frame)

        # Build GUI
        screen = gui.draw(annotated_frame, inspection)

        cv2.imshow("AI-IQRS Inspection System", screen)

        key = cv2.waitKey(1) & 0xFF

        # ---------------------------------------
        # SPACE = Inspect
        # ---------------------------------------

        if key == 32:

            print("\nInspecting Tray...")

            start = time.time()

            inspection = rules.inspect(components)

            elapsed = time.time() - start

            if inspection["PASS"]:

                print("\nPASS")

            else:

                print("\nFAIL")

                if inspection["Missing"]:

                    print("\nMissing Components:")

                    for component in inspection["Missing"]:
                        print(" -", component)

            print(f"\nInspection Time: {elapsed:.3f} sec")

        # ---------------------------------------
        # ESC = Exit
        # ---------------------------------------

        elif key == 27:
            break

    camera.release()

    print("\nAI-IQRS Closed")


if __name__ == "__main__":
    main()
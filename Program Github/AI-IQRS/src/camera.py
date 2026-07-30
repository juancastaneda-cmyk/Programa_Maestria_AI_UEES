import cv2

from config import (
    FRAME_WIDTH,
    FRAME_HEIGHT
)

# ==========================================================
# Dirección IP del iPhone
# ==========================================================
IPHONE_URL = "http://192.168.12.247:4747/video"
# Cambia esta dirección por la que muestre tu aplicación.

class Camera:

    def __init__(self):

        print("=" * 60)
        print("AI-IQRS")
        print("Conectando únicamente al iPhone...")
        print("=" * 60)

        self.cap = cv2.VideoCapture(IPHONE_URL)

        if not self.cap.isOpened():
            raise RuntimeError(
                "\nERROR\n"
                "No fue posible conectarse al iPhone.\n\n"
                "Verifica que:\n"
                "• El iPhone esté conectado al mismo WiFi.\n"
                "• La aplicación esté abierta.\n"
                "• La dirección IP sea correcta.\n"
            )

        self.cap.set(cv2.CAP_PROP_FRAME_WIDTH, FRAME_WIDTH)
        self.cap.set(cv2.CAP_PROP_FRAME_HEIGHT, FRAME_HEIGHT)

        print("✅ iPhone conectado correctamente")

    def read(self):

        ret, frame = self.cap.read()

        if not ret:
            print("Se perdió la conexión con el iPhone.")
            return None

        return frame

    def release(self):

        if self.cap is not None:
            self.cap.release()

        cv2.destroyAllWindows()

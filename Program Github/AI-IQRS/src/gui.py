import cv2
import numpy as np


class InspectionGUI:

    def __init__(self):

        self.panel_width = 400
        self.font = cv2.FONT_HERSHEY_SIMPLEX

    def draw(self, frame, inspection):

        h, w = frame.shape[:2]

        # =====================================================
        # PANEL DERECHO
        # =====================================================

        panel = np.ones((h, self.panel_width, 3), dtype=np.uint8) * 255

        # =====================================================
        # TITULO
        # =====================================================

        cv2.putText(
            panel,
            "AI-IQRS",
            (95, 40),
            self.font,
            1.1,
            (0, 0, 0),
            3
        )

        cv2.line(panel, (20, 60), (380, 60), (170, 170, 170), 2)

        # =====================================================
        # STATUS
        # =====================================================

        y = 100

        cv2.putText(
            panel,
            "STATUS",
            (20, y),
            self.font,
            0.75,
            (0, 0, 0),
            2
        )

        y += 40

        if inspection["PASS"] is None:

            status = "READY"
            color = (0, 165, 255)

        elif inspection["PASS"]:

            status = "PASS"
            color = (0, 180, 0)

        else:

            status = "FAIL"
            color = (0, 0, 255)

        cv2.putText(
            panel,
            status,
            (20, y),
            self.font,
            1.1,
            color,
            3
        )

        # =====================================================
        # DETECTED COMPONENTS
        # =====================================================

        y += 60

        cv2.putText(
            panel,
            "Detected Components",
            (20, y),
            self.font,
            0.65,
            (0, 0, 0),
            2
        )

        y += 30

        if inspection["Detected"]:

            for component, qty in inspection["Detected"].items():

                cv2.putText(
                    panel,
                    f"{component}: {qty}",
                    (25, y),
                    self.font,
                    0.52,
                    (40, 40, 40),
                    1
                )

                y += 24

        else:

            cv2.putText(
                panel,
                "Waiting Inspection...",
                (25, y),
                self.font,
                0.55,
                (130, 130, 130),
                2
            )

            y += 30

        # =====================================================
        # MISSING COMPONENTS
        # =====================================================

        y += 20

        cv2.putText(
            panel,
            "Missing Components",
            (20, y),
            self.font,
            0.65,
            (0, 0, 0),
            2
        )

        y += 30

        if inspection["PASS"] is None:

            cv2.putText(
                panel,
                "---",
                (25, y),
                self.font,
                0.55,
                (130, 130, 130),
                2
            )

        elif len(inspection["Missing"]) == 0:

            cv2.putText(
                panel,
                "None",
                (25, y),
                self.font,
                0.60,
                (0, 180, 0),
                2
            )

        else:

            for component in inspection["Missing"]:

                cv2.putText(
                    panel,
                    f"- {component}",
                    (25, y),
                    self.font,
                    0.55,
                    (0, 0, 255),
                    2
                )

                y += 28

        # =====================================================
        # FOOTER
        # =====================================================

        cv2.line(panel, (20, h - 120), (380, h - 120), (170, 170, 170), 2)

        cv2.putText(
            panel,
            "SPACE : Inspect Tray",
            (20, h - 80),
            self.font,
            0.60,
            (0, 0, 0),
            2
        )

        cv2.putText(
            panel,
            "ESC : Exit",
            (20, h - 45),
            self.font,
            0.60,
            (0, 0, 0),
            2
        )

        # =====================================================
        # UNIR CAMARA + PANEL
        # =====================================================

        screen = cv2.hconcat([frame, panel])

        return screen

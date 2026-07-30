from collections import Counter


class RulesEngine:

    def __init__(self):

        # Configuración del kit esperado
        self.expected_kit = {

            "Catheters": 1,
            "Griplock": 1,
            "Guideware": 1,
            "Micro-claves": 3,
            "needle": 1,
            "needle protector": 1,
            "ruler": 1,
            "scalper": 1,
            "syringe": 1,
            "tearaway": 1

        }

    def inspect(self, detected_components):

        detected = Counter(detected_components)

        missing = []

        extra = []

        for component, quantity in self.expected_kit.items():

            detected_qty = detected.get(component, 0)

            if detected_qty < quantity:

                missing.append(
                    f"{component} ({quantity-detected_qty} missing)"
                )

            elif detected_qty > quantity:

                extra.append(
                    f"{component} ({detected_qty-quantity} extra)"
                )

        passed = len(missing) == 0 and len(extra) == 0

        return {

            "PASS": passed,

            "Missing": missing,

            "Extra": extra,

            "Detected": detected

        }
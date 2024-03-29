from typing import List
from project.peaks.base_peak import BasePeak


class ArcticPeak(BasePeak):

    def get_recommended_gear(self) -> List[str]:
        return ["Ice axe", "Crampons", "Insulated clothing", "Helmet"]

    def calculate_difficulty_level(self) -> str:

        if self.elevation > 3000:
            return "Extreme"

        elif self.elevation >= 2000:
            return "Advanced"

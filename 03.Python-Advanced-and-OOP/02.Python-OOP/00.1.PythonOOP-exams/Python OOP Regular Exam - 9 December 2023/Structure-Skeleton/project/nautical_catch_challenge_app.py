from typing import List

from project.divers.base_diver import BaseDiver
from project.divers.free_diver import FreeDiver
from project.divers.scuba_diver import ScubaDiver
from project.fish.base_fish import BaseFish
from project.fish.deep_sea_fish import DeepSeaFish
from project.fish.predatory_fish import PredatoryFish


class NauticalCatchChallengeApp:

    VALID_TYPES_OF_DIVER = {"FreeDiver": FreeDiver, "ScubaDiver": ScubaDiver}
    VALID_TYPES_OF_FISH = {"PredatoryFish": PredatoryFish, "DeepSeaFish": DeepSeaFish}

    def __init__(self):
        self.divers: List[BaseDiver] = []
        self.fish_list: List[BaseFish] = []

    def dive_into_competition(self, diver_type: str, diver_name: str):
        try:
            diver = self.VALID_TYPES_OF_DIVER[diver_type](diver_name)
        except KeyError:
            return f"{diver_type} is not allowed in our competition."

        if len([d for d in self.divers if d.name == diver_name]) > 0:
            return f"{diver_name} is already a participant."

        self.divers.append(diver)

        return f"{diver_name} is successfully registered for the competition as a {diver_type}."

    def swim_into_competition(self, fish_type: str, fish_name: str, points: float):
        try:
            fish = self.VALID_TYPES_OF_FISH[fish_type](fish_name, points)
        except KeyError:
            return f"{fish_type} is forbidden for chasing in our competition."

        if len([f for f in self.fish_list if f.name == fish_name]) > 0:
            return f"{fish_name} is already permitted."

        self.fish_list.append(fish)

        return f"{fish_name} is allowed for chasing as a {fish_type}."

    def chase_fish(self, diver_name: str, fish_name: str, is_lucky: bool):
        try:
            diver = next(filter(lambda d: d.name == diver_name, self.divers))
            fish = [f for f in self.fish_list if f.name == fish_name][0]
        except StopIteration:
            return f"{diver_name} is not registered for the competition."
        except IndexError:
            return f"The {fish_name} is not allowed to be caught in this competition."

        if diver.has_health_issue:
            return f"{diver_name} will not be allowed to dive, due to health issues."

        output = ""
        if diver.oxygen_level < fish.time_to_catch:
            diver.miss(fish.time_to_catch)
            output = f"{diver_name} missed a good {fish_name}."

        elif diver.oxygen_level == fish.time_to_catch:
            if is_lucky:
                diver.hit(fish)
                output = f"{diver_name} hits a {fish.points}pt. {fish_name}."

            else:
                diver.miss(fish.time_to_catch)
                output = f"{diver_name} missed a good {fish_name}."

        elif diver.oxygen_level > fish.time_to_catch:
            diver.hit(fish)
            output = f"{diver_name} hits a {fish.points}pt. {fish_name}."

        if diver.oxygen_level == 0:
            diver.update_health_status()

        return output

    def health_recovery(self):
        divers_to_recover = [d for d in self.divers if d.has_health_issue]

        for diver in divers_to_recover:
            diver.update_health_status()
            diver.renew_oxy()

        return f"Divers recovered: {len(divers_to_recover)}"

    def diver_catch_report(self, diver_name: str):
        diver = [d for d in self.divers if d.name == diver_name][0]

        output = f"**{diver_name} Catch Report**\n" + "\n".join([f.fish_details() for f in diver.catch])

        return output

    def competition_statistics(self):
        healthy_divers = [d for d in self.divers if d.has_health_issue is False]
        sorted_divers = sorted(healthy_divers, key=lambda d: (-d.competition_points, -len(d.catch), d.name))

        output = "**Nautical Catch Challenge Statistics**\n"

        return output + "\n".join(str(d) for d in sorted_divers)

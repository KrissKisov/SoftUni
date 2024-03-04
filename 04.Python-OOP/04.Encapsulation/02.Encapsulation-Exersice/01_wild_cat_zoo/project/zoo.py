from typing import List
from project.animal import Animal
from project.worker import Worker


class Zoo:

    def __init__(self, name: str, budget: int, animal_capacity: int, workers_capacity: int):
        self.name = name
        self.__budget = budget
        self.__animal_capacity = animal_capacity
        self.__workers_capacity = workers_capacity
        self.animals: List[Animal] = []
        self.workers: List[Worker] = []

    def add_animal(self, animal: Animal, price: int) -> str:

        if self.__budget >= price and self.__animal_capacity > len(self.animals):
            self.animals.append(animal)
            self.__budget -= price

            return f"{animal.name} the {animal.__class__.__name__} added to the zoo"

        if self.__budget < price:
            return "Not enough budget"

        return "Not enough space for animal"

    def hire_worker(self, worker: Worker) -> str:

        if self.__workers_capacity > len(self.workers):
            self.workers.append(worker)

            return f"{worker.name} the {worker.__class__.__name__} hired successfully"

        return "Not enough space for worker"

    def fire_worker(self, worker_name: str) -> str:

        try:
            worker = next(filter(lambda x: x.name == worker_name, self.workers))
        except StopIteration:
            return f"There is no {worker_name} in the zoo"

        self.workers.remove(worker)

        return f"{worker_name} fired successfully"

    def pay_workers(self) -> str:

        salaries = sum(x.salary for x in self.workers)
        if self.__budget >= salaries:
            self.__budget -= salaries

            return f"You payed your workers. They are happy. Budget left: {self.__budget}"

        return f"You have no budget to pay your workers. They are unhappy"

    def tend_animals(self) -> str:

        tending_price = sum(x.money_for_care for x in self.animals)
        if self.__budget >= tending_price:
            self.__budget -= tending_price

            return f"You tended all the animals. They are happy. Budget left: {self.__budget}"

        return "You have no budget to tend the animals. They are unhappy."

    def profit(self, amount: int) -> None:
        self.__budget += amount

    def animals_status(self) -> str:
        lions = []
        lions_data = ""
        tigers = []
        tigers_data = ""
        cheetahs = []
        cheetahs_data = ""

        for animal in self.animals:

            if animal.__class__.__name__ == "Lion":
                lions.append(animal)
                lions_data += "\n" + animal.__repr__()

            elif animal.__class__.__name__ == "Tiger":
                tigers.append(animal)
                tigers_data += "\n" + animal.__repr__()

            elif animal.__class__.__name__ == "Cheetah":
                cheetahs.append(animal)
                cheetahs_data += "\n" + animal.__repr__()

        return f"You have {len(self.animals)} animals" \
               f"\n----- {len(lions)} Lions:" \
               f"{lions_data}" \
               f"\n----- {len(tigers)} Tigers:" \
               f"{tigers_data}" \
               f"\n----- {len(cheetahs)} Cheetahs:" \
               f"{cheetahs_data}"

    def workers_status(self) -> str:

        keepers = []
        keepers_data = ""
        caretakers = []
        caretakers_data = ""
        vets = []
        vets_data = ""

        for worker in self.workers:

            if worker.__class__.__name__ == "Keeper":
                keepers.append(worker)
                keepers_data += "\n" + worker.__repr__()

            elif worker.__class__.__name__ == "Caretaker":
                caretakers.append(worker)
                caretakers_data += "\n" + worker.__repr__()

            elif worker.__class__.__name__ == "Vet":
                vets.append(worker)
                vets_data += "\n" + worker.__repr__()

        return f"You have {len(self.workers)} workers" \
               f"\n----- {len(keepers)} Keepers:" \
               f"{keepers_data}" \
               f"\n----- {len(caretakers)} Caretakers:" \
               f"{caretakers_data}" \
               f"\n----- {len(vets)} Vets:" \
               f"{vets_data}"

        # The above should be faster as is doing 1 for loop rather the 6 in the below one.
        # keepers_names = "\n".join(worker.__repr__() for worker in self.workers if worker.__class__.__name__ == "Keeper")
        # caretakers_names = "\n".join(worker.__repr__() for worker in self.workers if worker.__class__.__name__ == "Caretaker")
        # vets_names = "\n".join(worker.__repr__() for worker in self.workers if worker.__class__.__name__ == "Vet")
        #
        # return f"You have {len(self.workers)} workers\n" \
        #        f"----- {len([worker for worker in self.workers if isinstance(worker, Keeper)])} Keepers:\n" \
        #        f"{keepers_names}\n" \
        #        f"----- {len([worker for worker in self.workers if isinstance(worker, Caretaker)])} Caretakers:\n" \
        #        f"{caretakers_names}\n" \
        #        f"----- {len([worker for worker in self.workers if isinstance(worker, Vet)])} Vets:\n" \
        #        f"{vets_names}"
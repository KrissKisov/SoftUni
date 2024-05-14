from typing import List
from project.clients.adult import Adult
from project.clients.base_client import BaseClient
from project.clients.student import Student
from project.loans.base_loan import BaseLoan
from project.loans.mortgage_loan import MortgageLoan
from project.loans.student_loan import StudentLoan


class BankApp:

    VALID_LOANS = {"StudentLoan": StudentLoan, "MortgageLoan": MortgageLoan}
    VALID_CLIENTS = {"Student": Student, "Adult": Adult}
    VALID_PAIRS = {"StudentLoan": "Student", "MortgageLoan": "Adult"}

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.loans: List[BaseLoan] = []
        self.clients: List[BaseClient] = []

    def add_loan(self, loan_type: str) -> str:

        try:
            loan = self.VALID_LOANS[loan_type]()
        except KeyError:
            raise Exception("Invalid loan type!")

        self.loans.append(loan)

        return f"{loan_type} was successfully added."

    def add_client(self, client_type: str, client_name: str, client_id: str, income: float) -> str:

        try:
            client = self.VALID_CLIENTS[client_type](client_name, client_id, income)
        except KeyError:
            raise Exception("Invalid client type!")

        if self.capacity == len(self.clients):
            return "Not enough bank capacity."

        self.clients.append(client)

        return f"{client_type} was successfully added."

    def grant_loan(self, loan_type: str, client_id: str) -> str:
        current_loan = next((cl for cl in self.loans if cl.__class__.__name__ == loan_type), None)
        client = next((c for c in self.clients if c.client_id == client_id), None)

        if self.VALID_PAIRS[current_loan.__class__.__name__] != client.__class__.__name__:
            raise Exception("Inappropriate loan type!")

        client.loans.append(current_loan)
        self.loans.remove(current_loan)

        return f"Successfully granted {loan_type} to {client.name} with ID {client_id}."

    def remove_client(self, client_id: str) -> str:
        try:
            client = next(c for c in self.clients if c.client_id == client_id)
        except StopIteration:
            raise Exception("No such client!")

        if client.loans:
            raise Exception("The client has loans! Removal is impossible!")

        self.clients.remove(client)

        return f"Successfully removed {client.name} with ID {client_id}."

    def increase_loan_interest(self, loan_type: str) -> str:

        number_of_changed_loans = 0

        for loan in self.loans:
            if loan.__class__.__name__ == loan_type:
                loan.increase_interest_rate()
                number_of_changed_loans += 1

        return f"Successfully changed {number_of_changed_loans} loans."

    def increase_clients_interest(self, min_rate: float) -> str:

        changed_client_rates_number = 0

        for client in self.clients:
            if client.interest < min_rate:
                client.increase_clients_interest()
                changed_client_rates_number += 1

        return f"Number of clients affected: {changed_client_rates_number}."

    def get_statistics(self) -> str:

        total_clients_income = sum(c.income for c in self.clients)
        loans_count_granted_to_clients = sum(len(c.loans) for c in self.clients)
        granted_sum = sum(loan.amount for c in self.clients for loan in c.loans)
        not_granted_sum = sum(loan.amount for loan in self.loans)
        avg_client_interest_rate = sum(c.interest for c in self.clients) / len(self.clients) if self.clients else 0

        return (f"Active Clients: {len(self.clients)}\n"
                f"Total Income: {total_clients_income :.2f}\n"
                f"Granted Loans: {loans_count_granted_to_clients}, Total Sum: {granted_sum :.2f}\n"
                f"Available Loans: {len(self.loans)}, Total Sum: {not_granted_sum :.2f}\n"
                f"Average Client Interest Rate: {avg_client_interest_rate :.2f}")

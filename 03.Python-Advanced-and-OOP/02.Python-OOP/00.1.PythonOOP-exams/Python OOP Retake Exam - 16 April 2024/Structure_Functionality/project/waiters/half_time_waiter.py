from project.waiters.base_waiter import BaseWaiter


class HalfTimeWaiter(BaseWaiter):
    hourly_wage = 12.0

    def calculate_earnings(self) -> float:
        return self.hours_worked * HalfTimeWaiter.hourly_wage

    def report_shift(self) -> str:
        return f"{self.name} worked a half-time shift of {self.hours_worked} hours."

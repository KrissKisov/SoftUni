budget = float(input())
command = input()
money_for_actor = 0

while command != "ACTION":
    actor = command

    if len(actor) > 15:
        money_for_actor = budget * 0.2
    else:
        actor_rate = float(input())
        money_for_actor = actor_rate

    if budget >= money_for_actor:
        budget -= money_for_actor
    else:
        break

    command = input()

if command == "ACTION":
    print(f"We are left with {budget :.2f} leva.")
else:
    print(f"We need {money_for_actor - budget :.2f} leva for our actors.")

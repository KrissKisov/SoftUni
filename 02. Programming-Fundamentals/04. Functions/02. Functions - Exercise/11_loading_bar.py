def loading_bar(some_number: int) -> str:
    message = []
    if some_number == 100:
        message.append("100% Complete!\n[%%%%%%%%%%]")
        return "".join(message)
    else:
        percent = f"{some_number}%"
        bar = f"[{some_number // 10 * '%'}{(10 - some_number // 10) * '.'}]"

        message.append(percent)
        message.append(bar)
        final_message = f"{' '.join(message)}\nStill loading..."
        return final_message


number = int(input())
print(loading_bar(number))

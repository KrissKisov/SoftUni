class Email:
    def __init__(self, sender, receiver, content):
        self.sender = sender
        self.receiver = receiver
        self.content = content
        self.is_sent = False

    def send(self):
        self.is_sent = True

    def get_info(self):
        return f"{self.sender} says to {self.receiver}: {self.content}. Sent: {self.is_sent}"


sent_emails = []
info = input()
while info != "Stop":
    sender, receiver, content = info.split()
    email_info = Email(sender, receiver, content)
    sent_emails.append(email_info)

    info = input()

indices = list(map(int, input().split(", ")))
for index in indices:
    sent_emails[index].send()

for email in sent_emails:
    print(email.get_info())

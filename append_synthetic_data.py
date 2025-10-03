import csv
import random
from pathlib import Path

random.seed(42)

repo_root = Path(__file__).resolve().parents[1]
csv_path = repo_root / 'data' / 'spam.csv'

spam_templates = [
    "Congratulations! You have won {amount} in our sweepstakes. Call {num} to claim.",
    "You are selected to receive a FREE {item}! Reply YES to {num} to get it.",
    "Claim your {amount} reward now. Text CLAIM to {num}.",
    "Exclusive offer: Get a new {item} for only {amount}. Click {url} to redeem.",
    "Win a {item} today! Enter code {code} at {url} to win.",
    "URGENT: Your account has been compromised. Verify at {url} or call {num}.",
    "Limited time: Buy 1 get 1 free on {item}. Reply BUY to {num}.",
    "You've been chosen for a complimentary {item}. Call {num} to arrange delivery.",
    "Free membership for 1 year! Sign up at {url} using code {code}.",
    "Prize awaiting: {amount} awaiting collection. Dial {num} now."
]

ham_templates = [
    "Hey, are we still meeting for dinner tonight?",
    "Don't forget to bring the documents tomorrow.",
    "Can you pick up some milk on your way home?",
    "I'll be a bit late, stuck in traffic.",
    "Thanks for the help earlier, really appreciate it.",
    "Are you free this weekend to catch up?",
    "I'll call you after the meeting finishes.",
    "Reminder: appointment at 3pm on Tuesday.",
    "Happy birthday! Hope you have a great day.",
    "Let me know when you've arrived."
]

items = ['headphones', 'smartphone', 'vacation', 'voucher', 'camera', 'laptop', 'subscription', 'rington', 'gift card', 'watch']
urls = ['http://getfree.example', 'http://claim.example', 'http://win.example']


def gen_phone():
    return ''.join(random.choices('0123456789', k=10))


def gen_amount():
    return f"${random.randint(10,5000)}"


def gen_code():
    return ''.join(random.choices('ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789', k=6))


append_count_spam = 1000
append_count_ham = 1000

with open(csv_path, 'a', newline='', encoding='utf-8') as f:
    writer = csv.writer(f)
    # Generate spam messages
    for _ in range(append_count_spam):
        template = random.choice(spam_templates)
        message = template.format(
            amount=gen_amount(),
            num=gen_phone(),
            item=random.choice(items),
            url=random.choice(urls),
            code=gen_code()
        )
        # Match original CSV columns: v1 (label), v2 (text), then three empty columns
        writer.writerow(['spam', message, '', '', ''])

    # Generate ham messages
    for _ in range(append_count_ham):
        template = random.choice(ham_templates)
        # Slightly vary ham messages
        if random.random() < 0.3:
            template = template + ' ' + random.choice(["See you soon.", "Talk later.", "Call me."])
        writer.writerow(['ham', template, '', '', ''])

print(f"Appended {append_count_spam} spam and {append_count_ham} ham messages to {csv_path}")

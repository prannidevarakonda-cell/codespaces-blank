print("Welcome to the Auto-Foody Service!")
name = input("What is your name? ")

print(f"Hi {name}, I’m here to help you with your food delivery.")
issue = input("Please describe your problem: ").lower()

if "food" in issue and ("not" in issue or "hasn't" in issue or "late" in issue):
    order_number = input("I’m sorry to hear that your food hasn’t arrived. Can you please provide your order number? ")
    print(f"Thank you, {name}. I’m checking the status for order #{order_number}...")
    print("It seems your delivery is delayed due to high demand in your area.")
    print("Your food should arrive within the next 20 minutes. Sorry for the inconvenience!")

elif "wrong" in issue or "incorrect" in issue:
    print("I’m sorry to hear you received the wrong order. Please keep the food, and we’ll send the correct one right away!")

elif "refund" in issue or "payment" in issue:
    print("I understand you have a payment issue. I’ll connect you to a support agent who can process your refund.")

else:
    print("I’m not quite sure I understand your issue. I’ll connect you to a human agent right away. Please stay online!")

print("Thank you for contacting us, and we appreciate your patience. Have a great day!")

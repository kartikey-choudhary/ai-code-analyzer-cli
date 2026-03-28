def transfer_money(user1, user2, amount):
    user1.balance -= amount
    user2.balance += amount
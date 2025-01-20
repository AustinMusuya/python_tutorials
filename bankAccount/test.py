from account import UserAccount

account1 = UserAccount(405, 4796, 100000)

print(account1.getBalance())

print(account1)

print(account1.withdraw(5000))

print(account1.getBalance())

# account1.getLastTransaction()

print(account1.getLastTransaction())

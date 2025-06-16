from contabancaria import Conta

c1 = Conta("Antonio",100.00)
c2 = Conta("ricardo",500.00)


print(f" Cliente: {c1.titular} Saldo : {c1.saldo}")
print(f" Cliente: {c2.titular} Saldo : {c2.saldo}")


c1.titular = input("altere o nome do titular: ")

print(f"titular atualizado : {c1.titular}")
nome = input("insira seu nome")

idade =int(input("digite sua idade"))

print(f"bem vindo {nome},voce tem {idade} anos!")

print("como posso te ajudar hoje")

def menu():
  print("1- bebidas")
  print("2- salgados")
  print("3- doces")

opc_user = int(input("digite o numero da opção desejada"))

if opc_user == 1:
    print("temos coca, fanta e guarana")

elif opc_user == 2:
    print("temos brigadeiro")

else:
    print("opção incorreta! digite um numero de 1 a 3") 

menu()

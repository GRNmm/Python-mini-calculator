num1 = float(input("Entrez le premier nombre: "))
num2 = float(input("Entrez le deuxieme nombre: "))

operation = input("Entrer le type d'operation (+, -, *, /):")

if operation == '+':
    resultat = num1 + num2
    print(f"{num1} + {num2} = {resultat}")
elif operation == '-':
    resultat = num1 - num2
    print(f"{num1} - {num2} = {resultat}")
elif operation == '*':
    resultat = num1 * num2
    print(f"{num1} * {num2} = {resultat}")
elif operation == '/':
    if num2 != 0:
        resultat = num1 / num2
        print(f"{num1} / {num2} = {resultat}")
    else:
        print("Operation invalide")
        
       
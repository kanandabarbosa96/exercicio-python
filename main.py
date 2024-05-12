SAL = float(input("digite seu salario: "))

P1 = 20/100
P2 = 15/100
P3 = 10/100
P4 = 5/100

if SAL <= 280:
    print("Seu salario antes do reajuste era: ", SAL)
    print("O percentual aplicado foi de ", P1*100)
    print("O valor do aumento é de: ", SAL / 100*20)
    print("Seu novo salario é: " ,SAL + SAL/100*20)
elif SAL <= 700:
    print("Seu salario antes do reajuste era: ", SAL)
    print("O percentual aplicado foi de: ", P2*100)
    print("O valor do aumento é de:", SAL / 100*15)
    print("Seu salario atual é de: ", SAL + SAL / 100*15)
elif SAL <= 1500:
    print("Seu salario antes do reajuste era: ", SAL)
    print("O percentual aplicado foi de: ", P3*100)
    print("O valor do aumento é de: ", SAL / 100*10)
    print("Seu salario atual é de: ", SAL + SAL/100*10)
else:
    print("Seu salario antes do reajuste era: ", SAL)
    print("O percentual aplicado foi de: ", P4*100)
    print("O valor do aumento é de: ", SAL / 100*5)
    print("Seu salario atual é de: ", SAL + SAL/100*5)
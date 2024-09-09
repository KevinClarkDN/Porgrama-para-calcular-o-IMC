altura=float(input("Digite sua altura em metros: "))
peso=float(input("Digite seu peso em quilos: "))

imc=peso/altura**2

if imc<18.5:
    print("Você está abaixo do peso ideal.")
elif imc>=18.5 and imc<25:
    print("Você está no peso ideal.")
elif imc>=25 and imc>30:
    print("Você está com sobre peso.")
else:
    print("Você está com obesidade.")
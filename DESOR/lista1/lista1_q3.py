def conversao (f):
      return  ((f-32)/9)*5


while True:
  try:
    F = int(input("Digite a temperatura "))
    print("A temperatura em Celsius é: %.2f" %conversao(F) + "C")
    break
  except:
    print("Temperatura inválida!")
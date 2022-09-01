op = int(input("Digite o sexo da pessoa: 1- feminino, 2 - masculino"))
al = float (input("Digite sua altura:   "))

def peso(s, h):
  if s == 1:
    return (62.1 * h) - 44.7
  else:
    return (72.7 * h) - 58

while True:
  try:
    while op !=1  and op !=2:
      print("Digite uma opção valida")
      op = int(input("Digite o sexo da pessoa: 1- feminino, 2 - masculino"))
    print("O peso ideal da pessoa é %.2f" %peso(op, al))
    break
  except:
    print("Dados invalidos")
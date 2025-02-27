Nome = input("Digite o nome:")             #Variável antes da função
Email = input("Digite seu email: ")
Senha = input("Digite sua senha: ")
while True:
        key = input("Key: ")                            #while true  usa a regra adicional em loop  no código  
        if key.isdigit() and len(key) == 2: 
              break
        else:
            print("Erro: A Key deve ter exatamente 2 números. Tente novamente.")       #Key.isdigit limite de digitos AND igual a 2, passou desse digitos
salario = 1000
Acesso = True

print("-----------------------------------------------------------")
print("Nome --->  %s" % Nome)   #Print para esclarecer as informações no terminal
print("Senha --->  %s" % Senha)  #Se quiser formatar apenas use F nas prints e retire as máscaras de "%"
print("Email --->  %s" % Email)
print("Key --->  %s" % key)
print("Salário %d" % salario)
print("Acesso dado --->  %r" % Acesso)
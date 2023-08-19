menu = """
===== MENU =====

[1]- Depósito
[2]- Saque
[3]- Extrato
[4]- Sair

Digite o número da opção desejada
=> 
"""

saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_NUMERO_SAQUES = 3

while True:
	opcao = input(menu)
	
#DEPÓSITO
	if opcao == "1":
		deposito = 0
		while deposito == 0:
			deposito = float(input("Digite o valor do depósito a ser efetuado\n=> "))
			if deposito <= 0:
				deposito = 0
				print("ERRO! Digite um valor POSITIVO de depósito")
				continue
			
			saldo += deposito
			extrato += (f"Depósito - R$ {deposito:.2f}\n")

#SAQUE    
	elif opcao == "2":
		if saldo == 0:
				print("Seu saldo é de R$ 0,00, portanto, o saque está impossibilitado!")
			
		elif numero_saques >= LIMITE_NUMERO_SAQUES:
				print(f"Você já atingiu o limite de {LIMITE_NUMERO_SAQUES} saques diários.")
			
		else:
			while saldo > 0:
			
				saque = float(input("Digite o valor do saque a ser efetuado\n=> "))
					
				if saque > saldo:
					print(f"Saldo insuficiente! Seu saldo é {saldo:.2f}. Insira um menor valor de saque. OBS: O limite de saque é de R$ {limite:.2f}.")
					continue       
					
				elif saque <= saldo:
					
					if saque <= 0:
						print("ERRO! Digite um valor POSITIVO de saque.")
						continue
						#saque = float(input("ERRO! Digite um valor POSITIVO de saque\n=> "))
					elif saque > 500:
						print(f"O limite de saque é de R$ {limite:.2f}. Insira um menor valor de saque.")
						continue
	
					else:
						saldo -= saque
						numero_saques += 1
						extrato += (f"Saque - R$ {saque:.2f}\n")
						break

#EXTRATO
	elif opcao == "3":
		if extrato != "":
				print(f"=== EXTRATO ===\n{extrato}\nSALDO: {saldo:.2f}")
		else:
				print(f"=== EXTRATO ===\nNão foram realizadas movimentações.\nSALDO: R$ {saldo:.2f}")
				 
#SAIR
	elif opcao == "4":
		break

	else:
		print("Opção inválida! Digite o número de uma opção que consta no menu\n=> ")


entrevistados = 50
excelente = 0
bom = 0
ruim = 0

for i in range(entrevistados):
    nome = input("Nome do entrevistado: ")
    idade = (input("Idade: "))
    opiniao = input("Opinião (EXCELENTE, BOM ou RUIM): ").strip().upper()

    while opiniao not in ("EXCELENTE", "BOM", "RUIM"):
        print("Opção inválida.")
        opiniao = input("Opinião (EXCELENTE, BOM ou RUIM): ").strip().upper()

    if opiniao == "EXCELENTE":
        excelente += 1
    
    elif opiniao == "BOM":
        bom += 1

    elif opiniao == "RUIM":
        ruim += 1

    else:
        print("Opção inválida")

print("\n---> RESULTADOS DA PESQUISA <---")
print(f"{excelente} feedback 'excelente'")
print(f"{bom} feedback 'bom'")
print(f"{ruim} feedback 'ruim'")
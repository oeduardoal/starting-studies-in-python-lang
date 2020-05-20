tempo_para_servir = 1
moradores_por_vez = 15
entregadores = 1
tempo_para_chegar_morador = 2

moradores_de_rua = []

sopas = 0
moradores_na_fila = 0
time = 0

while (len(moradores_de_rua) <= moradores_por_vez):
    sopas += 1 * entregadores
    time += 1 # 1min
    print("20:"+str(int(str(time).zfill(2))+10))
    print("Sopas prontas", sopas)
    print("Moradores na fila", moradores_na_fila)

    if moradores_na_fila > 0: # chegou morador na fila
        sopas -= 1
        moradores_na_fila -= 1
        moradores_de_rua.append({"min": "recebeu as 20:"+str(int(str(time).zfill(2))+10)})
        print("recebido > morador de rua esperou por", time - tempo_para_chegar_morador, "min", "recebeu as 20:"+str(int(str(time).zfill(2))+10))
        print("")


    print("-")
    # A cada 2min um morador chega na fila
    if time % tempo_para_chegar_morador == 1: moradores_na_fila += 1

print("\nMoradores de rua: ")
for index in moradores_de_rua:
    print(index)

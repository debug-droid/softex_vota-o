voto = int(input("Em quem você deseja votar?"))

while True:

    cand_X = 63
    cand_Y = 45
    cand_Z = 39
    branco = 11

    if voto == 889:
        cand_X += 1
    elif voto == 847:
        cand_Y += 1
    elif voto == 515:
        cand_Z += 1
    elif voto == str:
        print("Insira apenas números, vote novamente.")
        continue
    else:
        branco += 1

    finalizar = input("Deseja finalizar a votação?")

    if finalizar == "sim":
        if cand_X > cand_Y and cand_X > cand_Z:
            print(f"O candidato X foi o vencedor com {cand_X} votos.\n")
            print(f"O candidato Y recebeu {cand_Y} votos.\n")
            print(f"O candidato Z recebeu {cand_Z} votos.\n")
            print(f"Quantidade de votos nulos ou brancos: {branco}")
            break
        elif cand_Y > cand_X and cand_Y > cand_Z:
            print(f"O candidato Y foi o vencedor com {cand_Y} votos.")
            print(f"O candidato X recebeu {cand_X} votos.\n")
            print(f"O candidato Z recebeu {cand_Z} votos.\n")
            print(f"Quantidade de votos nulos ou brancos: {branco}")
            break
        elif cand_Z > cand_X and cand_Z > cand_Y:
            print(f"O candidato Z foi o vencedor com {cand_Z} votos.")
            print(f"O candidato X recebeu {cand_X} votos.\n")
            print(f"O candidato Y recebeu {cand_Y} votos.\n")
            print(f"Quantidade de votos nulos ou brancos: {branco}")
            break
    elif finalizar == "não":
        voto = int(input("Em quem você deseja votar?"))
        continue

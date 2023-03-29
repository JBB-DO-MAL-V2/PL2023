import re
import json


def parser(file):
    dataLines = []
    with open(file) as f:
        for line in f:
            fields = line.split("::")
            if len(fields) == 7:
                pasta, data, nome, pai, mae, info, _ = fields
                dataLines.append({
                    "pasta": pasta,
                    "data": data,
                    "nome": nome,
                    "pai": pai,
                    "mae": mae,
                    "info": info
                })
    return dataLines


def process_anos(data):
    dicAno = {}
    for line in data:
        ano = line["data"].split("-")[0]
        dicAno[ano] = dicAno.get(ano, 0) + 1
    return sorted(dicAno.items(), key=lambda x: x[1], reverse=True)


def seculos(year):
    return (int(year) - 1) // 100 + 1


def nomes_seculo(data):
    dicSeculos = {}
    for line in data:
        ano = line["data"].split("-")[0]
        seculo = seculos(ano)
        name, apelido = re.match(r"^(\w+)\s+(\w+)$", line["nome"]).groups()
        if seculo not in dicSeculos:
            dicSeculos[seculo] = {"nomes": {}, "apelidos": {}}
        dicSeculos[seculo]["nomes"][name] = dicSeculos[seculo]["nomes"].get(name, 0) + 1
        dicSeculos[seculo]["apelidos"][apelido] = dicSeculos[seculo]["apelidos"].get(apelido, 0) + 1

    for sec in dicSeculos:
        dicSeculos[sec]["nomes"] = sorted(dicSeculos[sec]["nomes"].items(), key=lambda x: x[1], reverse=True)
        dicSeculos[sec]["apelidos"] = sorted(dicSeculos[sec]["apelidos"].items(), key=lambda x: x[1], reverse=True)
    return dicSeculos


def relacao(data):
    dicRelacoes = {}
    for line in data:
        if line["info"]:
            rel = re.findall(r",([^,]+)\. Proc", line["info"])
            for i in rel:
                dicRelacoes[i] = dicRelacoes.get(i, 0) + 1
    return dicRelacoes


def exD(data):
    with open("ex.json", "w") as f:
        for i in range(min(20, len(data))):
            json.dump(data[i], f)
            f.write("\n")


info = parser("processos.txt")
anos = process_anos(info)
nomes_apelidos = nomes_seculo(info)

for sec in nomes_apelidos:
    print(f"\nSéculo: {sec}")
    print("\nNomes")
    for i, (name, count) in enumerate(nomes_apelidos[sec]["nomes"][:5], start=1):
        print(f"{i}: {name} - {count}")
    print("\nApelidos")
    for i, (apelido, count) in enumerate(nomes_apelidos[sec]["apelidos"][:5], start=1):
        print(f"{i}: {apelido} - {count}")

print(relacao(info))
exD(info)

import json

# Abre e carrega o conteúdo do JSON
with open("json", "r", encoding="utf-8") as file:
    data = json.load(file)

fluxos_extraidos = []

for fluxo in data:
    try:
        workflow_name = fluxo.get("workflowName", "")
        description = fluxo.get("description", "")
        steps = fluxo.get("steps", [])

        fluxos_extraidos.append({
            "workflowName": workflow_name,
            "description": description,
            "steps": steps
        })

    except Exception as e:
        print(f"Erro ao processar fluxo: {e}")

# Conta e imprime quantos fluxos foram extraídos
print(f"\n Total de fluxos extraídos: {len(fluxos_extraidos)}")

# Lista o nome de todos os fluxos extraídos
print("\n Lista de fluxos extraídos:")
for fluxo in fluxos_extraidos:
    print(f"- {fluxo['workflowName']}")

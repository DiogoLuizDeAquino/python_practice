import json
import pandas as pd

# Carrega o JSON
with open('json', 'r', encoding='utf-8') as f:
    data = json.load(f)

# Lista para armazenar os dados
rows = []

# Itera sobre todos os workflows
for fluxo in data:
    wf_id = fluxo.get('id', '')
    wf_nome = fluxo.get('workflowName', '')
    wf_desc = fluxo.get('description', '')

    params = fluxo.get('params', [])

    # Se houver parâmetros, adiciona cada um
    if params:
        for param in params:
            rows.append({
                'WorkflowID': wf_id,
                'Processo': wf_nome,
                'Descrição': wf_desc,
                'Parâmetro': param.get('name', ''),
                'Tipo': param.get('type', ''),
                'Valor': param.get('value', ''),
                'Ordem': param.get('order', ''),
                'Opcional': param.get('optional', ''),
                'Secreto': param.get('secret', ''),
                'DisplayName': param.get('displayName', ''),
                'DefaultValue': param.get('defaultValue', ''),
                'PoolCredential': param.get('poolCredential', ''),
                'Extension': param.get('extension', ''),
                'ListOfValues': param.get('listOfValues', '')
            })
    else:
        # Se não houver parâmetros, ainda adiciona o fluxo com colunas vazias
        rows.append({
            'WorkflowID': wf_id,
            'Processo': wf_nome,
            'Descrição': wf_desc,
            'Parâmetro': '',
            'Tipo': '',
            'Valor': '',
            'Ordem': '',
            'Opcional': '',
            'Secreto': '',
            'DisplayName': '',
            'DefaultValue': '',
            'PoolCredential': '',
            'Extension': '',
            'ListOfValues': ''
        })

# Cria DataFrame e exporta
df = pd.DataFrame(rows)
df.to_excel('fluxos_com_parametros.xlsx', index=False)

print(f"Extração finalizada! {len(df)} linhas salvas em 'fluxos_com_parametros.xlsx'.")

import os

# Diretório raiz do seu projeto
base_dir = "src"  # Certifique-se de que você está executando o script na mesma pasta que contém o "src"

# Caminha por todas as subpastas e cria o __init__.py onde for necessário
for root, dirs, files in os.walk(base_dir):
    # Cria o arquivo __init__.py no diretório atual, se não existir
    init_file = os.path.join(root, "__init__.py")
    if not os.path.exists(init_file):
        open(init_file, 'w').close()  # Cria um arquivo vazio
        print(f"Created: {init_file}")

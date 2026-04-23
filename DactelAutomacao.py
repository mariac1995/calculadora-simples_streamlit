import os
import shutil

# ==============================
# CONFIGURAÇÃO DAS PASTAS
# ==============================

pasta_origem = r"C:\Users\HP\Desktop\Dactes"
pasta_destino = r"C:\Users\HP\Desktop\PDFs_Organizados"

# Cria a pasta destino se ela não existir
if not os.path.exists(pasta_destino):
    os.makedirs(pasta_destino)

# ==============================
# LISTAR, RENOMEAR E MOVER PDFs
# ==============================

contador = 1

for arquivo in os.listdir(pasta_origem):

    if arquivo.endswith(".pdf"):

        caminho_antigo = os.path.join(pasta_origem, arquivo)

        # Novo nome automático
        novo_nome = f"documento_{contador}.pdf"

        caminho_novo = os.path.join(pasta_origem, novo_nome)

        # Renomear arquivo
        os.rename(caminho_antigo, caminho_novo)

        # Caminho final
        destino_final = os.path.join(pasta_destino, novo_nome)

        # Mover arquivo
        shutil.move(caminho_novo, destino_final)

        print(f"{novo_nome} movido para a pasta organizada")

        contador += 1

print("Automação finalizada com sucesso!")
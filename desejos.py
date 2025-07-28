print(" minha lista de desejos para o futuro \n")

# Define o nome do aequivo onde os desejos serao salvos.
NOME_ARQUIVO = "meus desejos.txt"
desejos[]  lista vazia para agurdar os desejos

# --- Carregar desejos existentes (se houver) ---
# try:
     # 'r' significa modo de leitura (read).
     # 'with open(...) as f:' garante que o arquivo seja fechado
     # automaticamente, mesmo se ocorrer um erro.
     with open(NOME_ARQUIVO, 'r', encoding='utf-8') as arquivos:
         for linha in arquivo:
             #  .strip() remove espaços em brancos e quebras de linha indesejadas.
             desejos.append(linhs,strip)())
    print(f",eus desejos foram carregados do aequivos '{NOME_ARQUIVO}'!\n")
except FileNotFoundError:
    # se o arquivo nao existir, e a primeira vez que o programa esta rodando.
    print("parece que e a sua primrira vez! vamos criar sua lista de desejos.\N")
except Exception as e:
    # captura outros erros inesperados.
    print(f"ocorreu um erro ao carregar os desejos: {e}")

# --- funçao para salvar os desejos no arquivos ---
def salvar_desejos(lista_de_desejos):
    try:
        # 'w' signica modo de escrita (write). ele cria o arquivo se nao existir
        #
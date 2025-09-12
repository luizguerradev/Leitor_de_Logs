import os
from collections import deque

def analisar_pasta_logs(pasta_logs, saida="erros_encontrados.txt"):
    with open(saida, "w", encoding="utf-8") as out:
        for arquivo_nome in os.listdir(pasta_logs):
            caminho_arquivo = os.path.join(pasta_logs, arquivo_nome)

            if os.path.isfile(caminho_arquivo):
                header = f"\n📄 Lendo: {arquivo_nome}\n"
                print(header)
                out.write(header)

                with open(caminho_arquivo, "r", encoding="utf-8", errors="ignore") as arquivo:
                    capturando_traceback = False
                    traceback_buffer = []
                    contexto = deque(maxlen=10)  # últimas 10 linhas

                    for linha in arquivo:
                        linha_strip = linha.strip()
                        contexto.append(linha_strip)

                        # Detecta início de traceback
                        if "Traceback" in linha_strip:
                            capturando_traceback = True
                            traceback_buffer = [linha_strip]
                            traceback_context = list(contexto)[:-1]
                            continue

                        # Se já está capturando traceback
                        if capturando_traceback:
                            traceback_buffer.append(linha_strip)
                            if "Error" in linha_strip or "Exception" in linha_strip:
                                bloco = "\n🔴 Traceback encontrado:\n"
                                bloco += "   Contexto (últimas 10 linhas):\n"
                                bloco += "\n".join("   " + ctx for ctx in traceback_context)
                                bloco += "\n   --- Início Traceback ---\n"
                                bloco += "\n".join("   " + l for l in traceback_buffer)
                                bloco += "\n   --- Fim Traceback ---\n"

                                print(bloco)
                                out.write(bloco + "\n")

                                capturando_traceback = False
                            continue

                        # Linhas de erro isoladas
                        if "ERROR" in linha_strip:
                            bloco = "\n🔴 ERROR encontrado:\n"
                            bloco += "   Contexto (últimas 10 linhas):\n"
                            bloco += "\n".join("   " + ctx for ctx in list(contexto)[:-1])
                            bloco += "\n   >> " + linha_strip

                            print(bloco)
                            out.write(bloco + "\n")

    input(f"\n✅ Execução finalizada. Resultados salvos em '{saida}'. Pressione ENTER para sair...")

# Exemplo de uso
analisar_pasta_logs("logs")  # substitua pelo caminho da sua pasta
if __name__ == "__main__":
    # Caso queira passar a pasta pelo terminal: python leitor_logs.py logs saida.txt
    pasta = sys.argv[1] if len(sys.argv) > 1 else "logs"
    saida = sys.argv[2] if len(sys.argv) > 2 else "erros_encontrados.txt"
    analisar_pasta_logs(pasta, saida)
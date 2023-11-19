"""

    Implementação de uma pilha em Python.

Desenvolvedores: Matheus Viana, Vitor Lichoti.
Disciplina: Estrutura de Dados.
Professor: Renato.


"""


class EditorDeTexto:
    def __init__(self, nome_arquivo):
        self.nome_arquivo = nome_arquivo
        self.desfazer = []
        self.refazer = []
        self.conteudo_atual = ""

    def exibir_menu(self):
        print("\nMenu:")
        print("1. Ler arquivo")
        print("2. Escrever no arquivo")
        print("3. Alterar palavra no arquivo")
        print("4. Desfazer ação")
        print("5. Refazer ação")
        print("6. Apagar tudo")
        print("0. Sair")

    def ler_arquivo(self):
        try:
            with open(self.nome_arquivo, 'r') as arquivo:
                self.conteudo_atual = arquivo.read()
                print("\nConteúdo atual do arquivo:\n", self.conteudo_atual)
        except FileNotFoundError:
            print("Arquivo não encontrado.")
            return

    def escrever_arquivo(self):
        texto = input("Digite o texto para escrever no arquivo: ")
        self.desfazer.append(self.conteudo_atual)
        self.conteudo_atual += texto
        with open(self.nome_arquivo, 'w') as arquivo:
            arquivo.write(self.conteudo_atual)
        print("Ação de escrever no aquivo realizada com sucesso!")

    def alterar_palavra(self):
        palavra_antiga = input("Digite a palavra a ser alterada: ")
        palavra_nova = input("Digite a nova palavra: ")
        self.desfazer.append(self.conteudo_atual)
        self.conteudo_atual = self.conteudo_atual.replace(
            palavra_antiga,
            palavra_nova
            )
        with open(self.nome_arquivo, 'w') as arquivo:
            arquivo.write(self.conteudo_atual)
        print("Ação de alterar palavra foi realizada com sucesso!")

    def desfazer_acao(self):
        if self.desfazer:
            self.refazer.append(self.conteudo_atual)
            self.conteudo_atual = self.desfazer.pop()
            with open(self.nome_arquivo, 'w') as arquivo:
                arquivo.write(self.conteudo_atual)
            print("Ação desfeita com sucesso!")
        else:
            print("Nenhuma ação para desfazer.")

    def refazer_acao(self):
        # Se houver ações na pilha de refazer
        if self.refazer:
            # Realiza a ação que está no topo da pilha de refazer
            self.desfazer.append(self.conteudo_atual)
            acao_refazer = self.refazer.pop()
            self.conteudo_atual = acao_refazer
            with open(self.nome_arquivo, 'w') as arquivo:
                arquivo.write(self.conteudo_atual)
            print("Ação refeita com sucesso!")
        else:
            print("Nenhuma ação para refazer.")

    def apagar_tudo(self):
        confirmacao = input("Tem certeza que deseja apagar tudo? (S/N): ")
        if confirmacao.lower() == 's':
            self.desfazer.append(self.conteudo_atual)
            self.conteudo_atual = ""
            with open(self.nome_arquivo, 'w') as arquivo:
                arquivo.write(self.conteudo_atual)
            print("Ação de limpeza realizada com sucesso!")

    def executar(self):
        while True:
            self.exibir_menu()
            escolha = input("\nEscolha a opção (0-6): ")
            if escolha == '0':
                print("Encerrando o programa.")
                break
            elif escolha == '1':
                self.ler_arquivo()
            elif escolha == '2':
                self.escrever_arquivo()
            elif escolha == '3':
                self.alterar_palavra()
            elif escolha == '4':
                self.desfazer_acao()
            elif escolha == '5':
                self.refazer_acao()
            elif escolha == '6':
                self.apagar_tudo()
            else:
                print("Opção inválida. Tente novamente.")


if __name__ == "__main__":
    nome_arquivo = input("Digite o nome do arquivo.extensão (.txt, .pdf): ")
    manipulador = EditorDeTexto(nome_arquivo)
    manipulador.executar()

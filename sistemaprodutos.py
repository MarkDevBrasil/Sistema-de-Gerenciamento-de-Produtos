# Sistema de armazenar produtos em python - Mark
# ESTE CODIGO PODE SER USADO PARA FINS DIDATICOS E DE ESTUDO, NAO PODE SER USADO PARA FINS COMERCIAIS OU DE LUCRO.
import json
import os

def limpar_tela():
    os.system('cls' if os.name == 'nt' else 'clear')

def carregar_dados():
    global armazenar_produtos
    if os.path.exists("produtos.json"):
        with open("produtos.json", "r") as arquivo:
            armazenar_produtos = json.load(arquivo)
def salvar_dados():
    with open("produtos.json", "w") as arquivo:
        json.dump(armazenar_produtos, arquivo)
    

armazenar_produtos = []
carregar_dados()


def adicionar_produto():
    
    produto = input("Digite o nome do produto: ")
    try:
        preco = float(input("Digite o preço do produto: "))
        armazenar_produtos.append((produto, preco))
        salvar_dados()
        print(f"Produto '{produto}' adicionado com sucesso!")
    except ValueError:
        print("Preço inválido. Tente novamente.")
        return

def listar_produtos():
    if not armazenar_produtos:
        print("Não há produtos cadastrados.")
        return
    else:
        print("Produtos cadastrados:")
        for produto, preco in armazenar_produtos:
            print(f"Produto: {produto}, Preço: R${preco:.2f}")
            
def menu():

    while True:
        print("\n ======= SISTEMA DE PRODUTOS =======")
        print("\nEscolha uma opção:")
        print("[1] Adicionar produto")
        print("[2] Listar produtos")
        print("[3] Sair")
        
        escolha = input("Opção: ")
        
        if escolha == "1":
            limpar_tela()
            adicionar_produto()
        elif escolha == "2":
            limpar_tela()
            print(armazenar_produtos)
            listar_produtos()
        elif escolha == "3":
            limpar_tela()
            print("Saindo do sistema...")
            break
        else:
            print("Opção inválida. Tente novamente.")
            
menu()


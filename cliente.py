import xmlrpc.client

def main():
    proxy = xmlrpc.client.ServerProxy("http://localhost:8000/")

    while True:
        print("Escolha: pedra, papel, tesoura ou sair")
        player_choice = input("> ").lower()
        
        if player_choice == 'sair':
            print(proxy.get_score())
            break
        
        if player_choice not in ['pedra', 'papel', 'tesoura']:
            print("Opção inválida. Tente novamente.")
            continue
        
        result = proxy.play(player_choice)
        print(result)

if __name__ == "__main__":
    main()
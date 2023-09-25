import xmlrpc.server
import random

class PedraPapelTesoura:
    def play(self, player_choice):
        choices = ['pedra', 'papel', 'tesoura']
        computer_choice = random.choice(choices)

        if player_choice == computer_choice:
            return "Empate!"
        elif (
            (player_choice == 'pedra' and computer_choice == 'tesoura') or
            (player_choice == 'tesoura' and computer_choice == 'papel') or
            (player_choice == 'papel' and computer_choice == 'pedra')
        ):
            return f"Ganhou essa! O computador escolheu {computer_choice}."
        else:
            return f"Perdeu essa! O computador escolheu {computer_choice}."

if __name__ == "__main__":
    server = xmlrpc.server.SimpleXMLRPCServer(("localhost", 8000))
    server.register_instance(PedraPapelTesoura())
    print("Servidor RPC iniciado na porta 8000")
    server.serve_forever()
import xmlrpc.server
import random

class PedraPapelTesoura:
    player_score = 0
    computer_score = 0

    @classmethod
    def play(cls, player_choice):
        choices = ['pedra', 'papel', 'tesoura']
        computer_choice = random.choice(choices)

        if player_choice == computer_choice:
            return "Empate!"
        elif (
            (player_choice == 'pedra' and computer_choice == 'tesoura') or
            (player_choice == 'tesoura' and computer_choice == 'papel') or
            (player_choice == 'papel' and computer_choice == 'pedra')
        ):
            result =  f"Ganhou essa! O computador escolheu {computer_choice}."
            cls.player_score += 1
        else:
            result = f"Perdeu essa! O computador escolheu {computer_choice}."
            cls.computer_score += 1

        return result
    
    @classmethod
    def get_score(cls):
        return f"Placar: Você {cls.player_score} - Computador {cls.computer_score}"

if __name__ == "__main__":
    server = xmlrpc.server.SimpleXMLRPCServer(("localhost", 8000))
    server.register_instance(PedraPapelTesoura())
    print("Servidor RPC iniciado na porta 8000")
    server.serve_forever()
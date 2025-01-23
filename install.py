# nao compilado para maior transparencia
import os
import subprocess
import sys

def add_to_environment_variable():
    current_path = os.getcwd()
    print(f"Pasta atual: {current_path}")

    try:
        # Verifica se a variável já existe no PATH
        result = subprocess.run(
            ['echo', '%PATH%'],
            capture_output=True,
            text=True,
            shell=True
        )
        
        if current_path in result.stdout:
            print("A pasta atual já está nas variáveis de ambiente.")
            return
        
        # Comando para adicionar a pasta atual ao PATH
        subprocess.run(
            f'setx PATH "%PATH%;{current_path}"',
            shell=True,
            check=True
        )
        print("Pasta adicionada com sucesso às variáveis de ambiente!")
    except subprocess.CalledProcessError as e:
        print("Erro ao tentar modificar as variáveis de ambiente.")
        print(e)
        sys.exit(1)

if __name__ == "__main__":
    # Ira adicionar a pasta atual as variaveis ambiente
    add_to_environment_variable()

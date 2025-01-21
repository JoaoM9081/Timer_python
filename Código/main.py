from time import sleep

# validando entrada int
def ler_int(msg):
    while True:
        try:
            t = int(input(msg).strip())
        except ValueError:
            print('\033[1;31mEntrada inválida, tente digitar um número inteiro válido\033[m')
        else:
            return t

t = ler_int('\033[1mDigite o tempo em (segundos) para o timer: \033[m')

# Quando t = 0, retornará False
while t:
    minutos, segundos = divmod(t, 60) # convertendo minutos e segundos
    timer = f'{segundos:02d}:{minutos:02d}'
    print(f'\033[1;34mTimer:\033[m \033[1;36m{timer}\033[m', end="\r")
    sleep(1) # pausa de 1s
    t -= 1
    
print('\n\033[1;31mTEMPO ACABOU !!!\033[m')
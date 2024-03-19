registradores = {

    '£00': '0000',
    '£01': '0001',
    '£02': '0010',
    '£03': '0011',
    '£04': '0100',
    '£05': '0101',
    '£06': '0110',
    '£07': '0111',
    '£08': '1000',
    '£09': '1001',
    '£10': '1010',
    '£11': '1011',
    '£12': '1100',
    '£13': '1101',
    '£14': '1110',
    '¢00': '1111'

}

operadores = {

    'soma': '0000',
    'subtrai': '0001',
    'pega': '0010',
    'vai': '0011',
    'multiplica': '0100',
    'maior': '0101',
    'igual': '0110',
    'menor': '0111',
    'ler': '1000',
    'escrever': '1001',
    'fodaSe': '1010',
    'aMimir': '1011',
    'somaFoda': '1100',
    'multiplicaFoda': '1101',
    'lerFoda': '1110',
    'escreverFoda': '1111',

}

hexadecimal = {

    '0000': '0',
    '0001': '1',
    '0010': '2',
    '0011': '3',
    '0100': '4',
    '0101': '5',
    '0110': '6',
    '0111': '7',
    '1000': '8',
    '1001': '9',
    '1010': 'a',
    '1011': 'b',
    '1100': 'c',
    '1101': 'd',
    '1110': 'e',
    '1111': 'f'

}

class SintaxError(Exception):
    def __init__(self, mensagem) -> None:
        self.mensagem = mensagem

def preenche_bits(x: int) -> str:
    return '0' * x

def complemento_de_dois(numero_binario):

    bits_invertidos = ''.join('1' if bit == '0' else '0' for bit in numero_binario)
    resultado = bin(int(bits_invertidos, 2) + 1)[2:]
    
    return resultado

def imediatoBinario(x: int, tamanho: int) -> str:

    if(x >= 0):
        saida = '0' + str(bin(x))[2:]

        while len(saida) < tamanho:
            saida = '0' + saida

    else:
        saida = '0' + str(bin(x))[3:]
        saida = complemento_de_dois(saida)

        while len(saida) < tamanho:
            saida = '1' + saida

    return saida

def converteHexa(binario: str) -> str:
    saida = ''
    
    for i in range(8):
        j = 4 * i
        saida += hexadecimal[binario[j] + binario[j + 1] + binario[j + 2] + binario[j + 3]]

    return saida

def converteBinario(linha: str) -> str:
    codigo = linha.replace(',', '')
    codigo = codigo.replace('Â', '')
    codigo = codigo.split()

    saida = operadores[codigo[0]]
    if saida == operadores['soma'] or saida == operadores['subtrai'] or saida == operadores['multiplica']:
        saida += registradores[codigo[1]]
        saida += registradores[codigo[2]]
        saida += registradores[codigo[3]]
        saida += preenche_bits(16)
        tamanho = 4
    elif saida == operadores['maior'] or saida == operadores['igual'] or saida == operadores['menor']:
        saida += '0000'
        saida += registradores[codigo[1]]
        saida += registradores[codigo[2]]
        saida += imediatoBinario(int(codigo[3]), 16)
        tamanho = 4
    elif saida == operadores['ler'] or saida == operadores['somaFoda'] or saida == operadores['multiplicaFoda']:
        saida += registradores[codigo[1]]
        saida += '0000'
        saida += registradores[codigo[2]]
        saida += preenche_bits(16)
        tamanho = 3
    elif saida == operadores['fodaSe'] or saida == operadores['lerFoda']:
        saida += registradores[codigo[1]]
        saida += preenche_bits(24)
        tamanho = 2
    elif saida == operadores['escreverFoda']:
        saida += '0000'
        saida += registradores[codigo[1]]
        saida += preenche_bits(20)
        tamanho = 2
    elif saida == operadores['vai']:
        saida += imediatoBinario(int(codigo[1]), 28)
        tamanho = 2
    elif saida == operadores['pega']:
        saida += registradores[codigo[1]]
        saida += imediatoBinario(int(codigo[2]), 24)
        tamanho = 3
    elif saida == operadores['escrever']:
        saida += '0000'
        saida += registradores[codigo[1]]
        saida += registradores[codigo[2]]
        saida += preenche_bits(16)
        tamanho = 3
    else:
        saida += preenche_bits(28)
        tamanho = 1

    if tamanho < len(codigo):
        if codigo[tamanho][:2] != '//':
            raise SintaxError('Erro de sintaxe')
    
    return saida

entrada = input('Digite o endereço do arquivo de entrada: ')
saida = input('Digite o endereço do arquivo de saída: ')

entrada = entrada.replace('\\', '\\\\')
saida = saida.replace('\\', '\\\\')

try:
    with open(entrada, 'r') as ler:
        linha = ler.readline()
        i = 1
        with open(saida, 'w') as escrever:
                        
            escrever.write('v2.0 raw\n')
            try:
                while linha:
                    if linha != '\n' and linha.replace(' ', '')[:2] != '//':
                        escrever.write(converteHexa(converteBinario(linha)) + ' ')

                    linha = ler.readline()
                    i += 1

                print("Arquivo escrito com sucesso!!")
            except (KeyError, SintaxError, IndexError):
                linha = linha.replace('\n', '')
                linha = linha.replace('Â', '')
                print(f'Erro de sintaxe na linha {i}: \'\033[31m{linha}\033[0m\'.')
                
                escrever.close()
                with open(saida, 'w') as escrever:
                    pass
                
        escrever.close()
        ler.close()
except FileNotFoundError:
    print('Arquivo de entrada não encontrado ou inexistente.')

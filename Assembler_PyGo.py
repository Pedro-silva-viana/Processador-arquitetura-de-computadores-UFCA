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
    '£15': '1111'

}

operadores = {

    'add': '0000',
    'sub': '0001',
    'li': '0010',
    'jump': '0011',
    'mul': '0100',
    'greater': '0101',
    'equals': '0110',
    'less': '0111',
    'read': '1000',
    'write': '1001',
    'random': '1010',
    'bubble': '1011',
    'addH': '1100',
    'mulH': '1101',
    'readH': '1110',
    'writeH': '1111',

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

def verifica_registrador(codigo: list, memoria: int):
    if memoria == 1:
        if int(registradores[codigo[1]], 2) >= 8:
            raise SintaxError('Registrador inválido')
    else:
        if int(registradores[codigo[1]], 2) < 8:
            raise SintaxError('Registrador inválido')

def ajuste_registrador(codigo: list, memoria: int) -> str:
    aux = ''
    if memoria == 2:
        aux = int(registradores[codigo[1]], 2)
        aux -= 8
        aux = bin(aux)
        aux = aux[2:]
        aux = preenche_bits(4 - len(aux)) + aux
    else:
        aux = registradores[codigo[1]]
    return aux

def converteBinario(linha: str, memoria: int) -> str:
    codigo = linha.replace(',', '')
    codigo = codigo.replace('Â', '')
    codigo = codigo.split()

    saida = operadores[codigo[0]]
    if saida == operadores['add'] or saida == operadores['sub'] or saida == operadores['mul']:

        verifica_registrador(codigo, memoria)

        saida += ajuste_registrador(codigo, memoria)
        saida += registradores[codigo[3]]
        saida += registradores[codigo[2]]
        saida += preenche_bits(16)
        tamanho = 4
    elif saida == operadores['greater'] or saida == operadores['equals'] or saida == operadores['less']:
        saida += '0000'
        saida += registradores[codigo[1]]
        saida += registradores[codigo[2]]
        saida += imediatoBinario(int(codigo[3]), 16)
        tamanho = 4
    elif saida == operadores['read']:
        saida += registradores[codigo[1]]
        saida += '0000'
        saida += registradores[codigo[2]]
        saida += preenche_bits(16)
        tamanho = 3
    elif saida == operadores['addH'] or saida == operadores['mulH']:

        verifica_registrador(codigo, memoria)

        saida += ajuste_registrador(codigo, memoria)
        saida += registradores[codigo[2]]
        saida += '0000'
        saida += preenche_bits(16)
        tamanho = 3
    elif saida == operadores['random'] or saida == operadores['readH']:
        saida += registradores[codigo[1]]
        saida += preenche_bits(24)
        tamanho = 2
    elif saida == operadores['writeH']:

        if memoria == 2:
            raise SintaxError('Operação inválida')

        saida += '0000'
        saida += registradores[codigo[1]]
        saida += preenche_bits(20)
        tamanho = 2
    elif saida == operadores['jump']:
        saida += imediatoBinario(int(codigo[1]), 28)
        tamanho = 2
    elif saida == operadores['li']:

        verifica_registrador(codigo, memoria)

        saida += ajuste_registrador(codigo, memoria)
        saida += imediatoBinario(int(codigo[2]), 24)
        tamanho = 3
    elif saida == operadores['write']:

        if memoria == 2:
            raise SintaxError('Operação inválida')

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
saida = saida.split('.')

try:
    with open(entrada, 'r') as read:
        linha = read.readline()
        i = 1
        write1 = open(saida[0] + '_1.' + saida[1], 'w')
        write2 = open(saida[0] + '_2.' + saida[1], 'w')
                        
        write1.write('v2.0 raw\n')
        write2.write('v2.0 raw\n')
        try:
            passou_aqui = 1
            while linha:
                linha1, linha2 = linha.split('_')
                if linha1 != '\n' and linha1.replace(' ', '')[:2] != '//':
                    write1.write(converteHexa(converteBinario(linha1, 1)) + ' ')
                passou_aqui = 2
                if linha2 != '\n' and linha2.replace(' ', '')[:2] != '//':
                    write2.write(converteHexa(converteBinario(linha2, 2)) + ' ')

                linha = read.readline()
                i += 1

            print("Arquivo escrito com sucesso!!")
        except (KeyError, SintaxError, IndexError):
            if passou_aqui == 1:
                linha1 = linha1.replace('\n', '')
                linha1 = linha1.replace('Â', '')
                print(f'Erro de sintaxe na linha {i}: \'\033[31m{linha1}\033[0m-{linha2}\'.')
            else:
                linha2 = linha2.replace('\n', '')
                linha2 = linha2.replace('Â', '')
                print(f'Erro de sintaxe na linha {i}: \'{linha1}-\033[31m{linha2}\033[0m\'.')
                
            write1.close()
            write2.close()
            with open(saida[0] + '_1.' + saida[1], 'w') as write:
                pass
            with open(saida[0] + '_2.' + saida[1], 'w') as write:
                pass
                
        write1.close()
        write2.close()
        read.close()
except FileNotFoundError:
    print('Arquivo de entrada não encontrado ou inexistente.')

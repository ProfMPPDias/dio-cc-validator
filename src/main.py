def identificar_bandeira(numero_cartao):
    """
    Identifica a bandeira do cartão de crédito com base no número fornecido.
    
    Parâmetros:
    numero_cartao (str): Número do cartão de crédito, pode conter espaços.
    
    Retorna:
    str: Nome da bandeira do cartão ou mensagem de erro.
    """
    # Remove espaços e caracteres especiais do número
    numero_cartao = numero_cartao.replace(' ', '').replace('-', '')
    
    # Validação básica do número
    if len(numero_cartao) < 13 or not numero_cartao.isdigit():
        return 'Número de cartão inválido'
    
    # Visa: começa com 4 e tem 13, 16 ou 19 dígitos
    if numero_cartao.startswith('4') and len(numero_cartao) in [13, 16, 19]:
        return 'Visa'
    
    # MasterCard: começa com 51 a 55 e tem 16 dígitos
    elif numero_cartao[:2] in [str(i) for i in range(51, 56)] and len(numero_cartao) == 16:
        return 'MasterCard'
    
    # American Express: começa com 34 ou 37 e tem 15 dígitos
    elif numero_cartao[:2] in ['34', '37'] and len(numero_cartao) == 15:
        return 'American Express'
    
    # Discover: começa com 6011, 65 ou 644-649
    elif (numero_cartao.startswith('6011') or 
          numero_cartao.startswith('65') or 
          (numero_cartao[:3] >= '644' and numero_cartao[:3] <= '649')):
        return 'Discover'
    
    # Diners Club: começa com 300-305 ou 36 ou 38
    elif (numero_cartao[:3] in [str(i) for i in range(300, 306)] or
          numero_cartao.startswith('36') or 
          numero_cartao.startswith('38')) and len(numero_cartao) == 14:
        return 'Diners Club'
    
    # JCB: começa com 35 e tem 16 dígitos
    elif numero_cartao.startswith('35') and len(numero_cartao) == 16:
        return 'JCB'
    
    else:
        return 'Bandeira desconhecida'


def exibir_cabecalho():
    """Exibe o cabeçalho da aplicação com design atraente."""
    print('\n' + '═' * 50)
    print('║{:^48}║'.format('🏦 IDENTIFICADOR DE BANDEIRA DE CARTÃO 🏦'))
    print('║{:^48}║'.format('Descubra a bandeira do seu cartão'))
    print('═' * 50)


def exibir_resultado(bandeira, numero_mascarado):
    """
    Exibe o resultado da identificação com formatação visual.
    
    Parâmetros:
    bandeira (str): Nome da bandeira identificada
    numero_mascarado (str): Número do cartão mascarado para exibição
    """
    print('\n' + '─' * 50)
    print('│{:^48}│'.format('RESULTADO DA ANÁLISE'))
    print('├' + '─' * 48 + '┤')
    print('│ Número: {:<37}│'.format(numero_mascarado))
    print('│ Bandeira: {:<35}│'.format(f'✓ {bandeira}'))
    print('└' + '─' * 48 + '┘')


def mascarar_numero(numero_cartao):
    """
    Mascara o número do cartão para exibição segura.
    
    Parâmetros:
    numero_cartao (str): Número completo do cartão
    
    Retorna:
    str: Número mascarado (mostra apenas os 4 últimos dígitos)
    """
    if len(numero_cartao) >= 4:
        return '*' * (len(numero_cartao) - 4) + numero_cartao[-4:]
    return '*' * len(numero_cartao)


def validar_entrada(entrada):
    """
    Valida se a entrada contém apenas números e espaços/hífens.
    
    Parâmetros:
    entrada (str): String de entrada do usuário
    
    Retorna:
    bool: True se válida, False caso contrário
    """
    entrada_limpa = entrada.replace(' ', '').replace('-', '')
    return entrada_limpa.isdigit() and len(entrada_limpa) >= 13


def interface_usuario():
    """
    Interface principal da aplicação com menu interativo.
    Solicita o número do cartão e exibe a bandeira identificada.
    """
    while True:
        exibir_cabecalho()
        
        print('\n📋 Instruções:')
        print('• Digite o número completo do cartão de crédito')
        print('• Pode incluir espaços ou hífens para formatação')
        print('• Digite "sair" para encerrar o programa')
        
        print('\n' + '─' * 50)
        numero_cartao = input('🔢 Digite o número do cartão: ').strip()
        
        # Opção para sair do programa
        if numero_cartao.lower() in ['sair', 'exit', 'quit']:
            print('\n' + '═' * 50)
            print('║{:^48}║'.format('👋 Obrigado por usar nossa aplicação!'))
            print('║{:^48}║'.format('Até logo!'))
            print('═' * 50)
            break
        
        # Validação da entrada
        if not validar_entrada(numero_cartao):
            print('\n❌ Erro: Número de cartão inválido!')
            print('   Por favor, digite apenas números (mínimo 13 dígitos)')
            input('\nPressione Enter para tentar novamente...')
            continue
        
        # Identificar a bandeira
        bandeira = identificar_bandeira(numero_cartao)
        numero_mascarado = mascarar_numero(numero_cartao.replace(' ', '').replace('-', ''))
        
        # Exibir resultado
        exibir_resultado(bandeira, numero_mascarado)
        
        # Opção para continuar
        print('\n' + '─' * 50)
        continuar = input('🔄 Deseja analisar outro cartão? (s/n): ').strip().lower()
        
        if continuar not in ['s', 'sim', 'y', 'yes']:
            print('\n' + '═' * 50)
            print('║{:^48}║'.format('👋 Obrigado por usar nossa aplicação!'))
            print('║{:^48}║'.format('Até logo!'))
            print('═' * 50)
            break


def executar_testes():
    """Executa testes com números de exemplo para demonstrar o funcionamento."""
    print('\n' + '═' * 50)
    print('║{:^48}║'.format('🧪 EXECUTANDO TESTES DE EXEMPLO'))
    print('═' * 50)
    
    testes = [
        ('4111 1111 1111 1111', 'Visa'),
        ('5500 0000 0000 0004', 'MasterCard'),
        ('3400 0000 0000 009', 'American Express'),
        ('6011 0000 0000 0004', 'Discover')
    ]
    
    for numero, esperado in testes:
        resultado = identificar_bandeira(numero)
        status = '✅' if resultado == esperado else '❌'
        print(f'{status} {numero} → {resultado}')
    
    print('═' * 50)


# Função principal da aplicação
def main():
    """Função principal que inicia a aplicação."""
    try:
        # Executar testes de exemplo (opcional)
        executar_testes()
        
        # Iniciar interface do usuário
        interface_usuario()
        
    except KeyboardInterrupt:
        print('\n\n' + '═' * 50)
        print('║{:^48}║'.format('⚠️  Programa interrompido pelo usuário'))
        print('║{:^48}║'.format('Até logo!'))
        print('═' * 50)
    except Exception as e:
        print(f'\n❌ Erro inesperado: {e}')
        print('Por favor, reinicie a aplicação.')


# Executar a aplicação se o script for chamado diretamente
if __name__ == '__main__':
    main()
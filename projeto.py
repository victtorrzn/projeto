from filme.filme import Filme
from filme.usuario import Usuario

pessoa = Usuario('victor','v','12', 'usuario','18')

usuarios = []
capacidade_poltrona = 50
lista_filme = []

op = 99
while op != 0:
    print('menu')
    print('1- faça seu cadastro')
    print('2- faça seu login')
    print('0- sair')

    op = int(input('digite a opção desejada: '))

    if op == 0:
        break
    elif op == 1:
        print('cadastro')
        nome = input('digite seu nome: ')
        login = input('digite seu login: ')
        tipo = input('sua conta é de admin ou usuario?')
        idade = input('digite sua idade: ')

        if tipo not in ('usuario', 'admin'):
            print('tipo inválido. Escolha "usuario" ou "admin".')
            continue

        login_existe = any(usuario.usuario == login for usuario in usuarios)

        if login_existe:
            print('este login já está em uso. escolha outro.')
        else:
            senha = input('insira sua senha: ')
            senha2 = input('confirme sua senha: ')

            if senha == senha2:
                novo_usuario = Usuario(nome, login, senha, tipo, idade)
                usuarios.append(novo_usuario)
                print('cadastro realizado com sucesso!')
            else:
                print('as senhas não conferem.')

    elif op == 2:
        print('login')
        login = input('digite seu login: ')
        senha = input('digite sua senha: ')

        usuario_logado = None

        for pessoa in usuarios:
            if login == pessoa.usuario and senha == pessoa.senha:
                usuario_logado = pessoa
                break
        if usuario_logado:
            print(f'bem vindo, {usuario_logado.nome}! Função: {usuario_logado.funcao()}')
            if usuario_logado.tipo == 'admin':
                op_admin = 99
                while op_admin != 0:
                    print('menu admin')
                    print('1- cadastrar filme')
                    print('2- listar filmes')
                    print('3- buscar filme')
                    print('4- vender ingresso')
                    print('0- voltar ao menu principal')

                    op_admin = int(input('digite a opção desejada: '))
                    if op_admin == 0:
                        break

                    elif op_admin == 1:
                        nome_filme = input('digite o nome do filme: ')
                        categoria_filme = input('digite a categoria do filme: ')
                        classificacao_filme = input('digite a classificação do filme: ')

                        novo_filme = Filme(nome_filme, categoria_filme)
                        novo_filme.classificacao = classificacao_filme
                        lista_filme.append(novo_filme)
                        print('filme cadastrado com sucesso!')

                    elif op_admin == 2:
                        if not lista_filme:
                            print('nenhum filme cadastrado!')
                        else:
                            for filme in lista_filme:
                                print(f'Filme: {filme.nome_filme} | Categoria: {filme.categoria} | Classificação: {filme.classificacao}')

                    elif op_admin == 3:
                        filme_buscado = input('digite o filme para buscar: ')
                        encontrado = False

                        for filme in lista_filme:
                            if filme_buscado.lower() == filme.nome_filme.lower():
                                print('filme encontrado!')
                                print(f'o filme é: {filme.nome_filme}')
                                encontrado = True
                                break

                        if not encontrado:
                            print('filme não encontrado!')

                    elif op_admin == 4:
                        filme_buscado = input('digite o filme para vender ingresso: ')
                        filme_encontrado = None

                        for filme in lista_filme:
                            if filme_buscado.lower() == filme.nome_filme.lower():
                                filme_encontrado = filme
                                break

                        if not filme_encontrado:
                            print('filme não encontrado!')
                            continue

                        valor = float(input('digite o valor do ingresso: '))
                        horario_filme = input('digite o horário do filme: ')
                        sala = int(input('digite a sala do filme: '))
                        poltrona = int(input('escolha uma poltrona (1 a 50): '))

                        filme_encontrado.registrar_ingresso([poltrona, valor, horario_filme, sala])
                        print(f"Sua poltrona é a: {poltrona} para o filme: {filme_encontrado.nome_filme}!")

                    else:
                        print('opção inválida!')

            else:
                op_usuario = 99
                while op_usuario != 0:
                    print('menu')
                    print('1- comprar ingresso')
                    print('0- sair')

                    op_usuario = int(input('digite a opção desejada: '))

                    if op_usuario == 0:
                        break

                    elif op_usuario == 1:
                        if not lista_filme:
                            print('nenhum filme disponível!')
                            continue

                        print('comprar ingresso')
                        i = 1
                        for filme in lista_filme:
                            vagas = capacidade_poltrona - len(filme.ingressos)
                            print(f'{i}. {filme.nome_filme} - vagas: {vagas}')
                            i += 1

                        escolha = int(input('escolha o filme (número): ')) - 1

                        if escolha < 0 or escolha >= len(lista_filme):
                            print('opção inválida!')
                            continue


                        filme_escolhido = lista_filme[escolha]
                        poltrona = int(input('escolha uma poltrona (1 a 50): '))
                        valor = 35.00

                        filme_escolhido.registrar_ingresso([poltrona, valor])
                        print(f'ingresso comprado! Poltrona {poltrona} - R$ {valor}')

                    else:
                        print('opção inválida!')

        else:
            print('login ou senha incorretos!')

    else:
        print('opção inválida!')
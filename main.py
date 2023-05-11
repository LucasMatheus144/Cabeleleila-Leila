import sqlite3
import datetime

def criar_banco():
    cursor.execute('''CREATE TABLE IF NOT EXISTS 'USUARIO' (
                "LOGIN" TEXT,
                "SENHA" TEXT,
                "ID" INTEGER
            )''')


    cursor.execute(f"INSERT INTO USUARIO VALUES('Admin1','admin1',0)")  # Admin
    con.commit()
    cursor.execute(f"INSERT INTO USUARIO VALUES('Lucas1','lucas1',1)")
    con.commit()

    cursor.execute('''CREATE TABLE IF NOT EXISTS 'Cliente' (
                "ID_Cliente" INTEGER,
                "Nome_Cliente" TEXT,
                "TELEFONE" TEXT,
                "DIA_AGENDADO" TEXT,
                "ENDERECO" TEXT,
                "EMAIL" TEXT,
                "RG" TEXT,
                FOREIGN KEY (ID_Cliente) REFERENCES USUARIO(ID) 
            )''')
    # apos criar a tabela,se rodar o execute novamente dará erro pois a tabela cliente ja estará criada

    cont = 1 # para adicionar o ID 1

    numero = cont
    nome = "Lucas"
    tele = "996070324"
    dia_agendado = "12/06/2023"
    endereco = "Rua TAAL TAL"
    email = "LUCAS@GMAIL.COM"
    rg = "2133412333"

    cursor.execute(
        f"INSERT INTO Cliente VALUES ({numero},'{nome}','{tele}','{dia_agendado}','{endereco}','{email}','{rg}')")  # Teste Lucas

    con.commit()


def Cadastro(cont):
    print("---------- Cadastro Usuario ----------")
    nome_de_usuario = str(input("Digite o nome de Usuario -->> "))
    senha_de_login = str(input("Digite a senha -->> "))
    cursor.execute("INSERT INTO USUARIO VALUES (?, ?, ?)", (nome_de_usuario, senha_de_login, cont))
    con.commit()

    print("Preencha os dados abaixo ")
    nome = str(input("Nome Completo "))
    tele = str(input("Numero "))
    dia_agendado = None
    endereco = str(input("Endereço de sua residencia "))
    email = str(input("Email para contato "))
    rg = str(input("RG "))
    cursor.execute(
                f"INSERT INTO Cliente VALUES ({cont},'{nome}','{tele}','{dia_agendado}','{endereco}','{email}','{rg}')"
                )
    con.commit()



def Login(usuario, senha):
   
    while True: 
        s = cursor.execute("SELECT * FROM USUARIO")  # SELECIONAR  Tabela usuario
        for j in s:
            if usuario == j[0] and senha == j[1]:  
                if usuario == "Admin1":
                    cursor.execute(f"SELECT ID FROM USUARIO WHERE LOGIN ='{usuario}' ")
                    resultado = cursor.fetchall()
                    for j in resultado: #pegar somendo o ID  [(1,)]
                        for l in j:
                            resultado = l
                    return (True,resultado)
                else:
                    cursor.execute(f"SELECT ID FROM USUARIO WHERE LOGIN ='{usuario}' ")
                    resultado = cursor.fetchall()
                    for j in resultado: #pegar somendo o ID  [(1,)]
                        for l in j:
                            resultado = l
                    return (False,resultado) # retorna para a tela login com o ID do usuario
                

        print("Usuario ou senha Invalidos, digite novamente ou cadastre o usuario ")
        esc = str(input(("Deseja cadastrar [s/n] ")))[0].lower()
        if esc == 's':
            Cadastro(cont)
            cont += 1
        else:
            usuario = str(input("Digite o login "))
            senha = str(input("Digite a senha "))


def tela_usuario(cont,id_cliente):
    data_atual = datetime.datetime.now() 
    dia_atual = data_atual.day

    while True:
        print("---------- Bem vindo ao Cabeleleila Leila ----------")
        print("Digite a sua opçao abaixo")
        print("0 - Sair do Sistema ")  
        print("1 - Marcar Agendamento") 
        print("2 - Remarcar Agendamento(Avisar até 2 dias antes)")
        print("3 - Desmarcar consulta")
        print("4 - Mostrar meus dados") 

        op = int(input("Sua opcao: "))
        
        if op == 0:
            break

        elif op == 1:
            dia = str(input("Digite o dia do agendamento "))
            cursor.execute(f"UPDATE Cliente SET DIA_AGENDADO='{dia}' WHERE ID_cliente='{id_cliente}'")
            con.commit()

        elif op == 2:
            cursor.execute(f"SELECT DIA_AGENDADO FROM Cliente WHERE ID_Cliente='{id_cliente}'")
            alteracao = cursor.fetchall()
            x = "" 
            for j in alteracao: # pegar o dia em formato de string
                for l in j:
                    x = l[:2]
            validacao = int(x) # conversao do dia para inteiro
            if (dia_atual - validacao) < 2:
                print("Alteraçao permitida somente pelo telefone!")
            else:
                novo_dia = str(input('Digite o dia para o agendamento '))
                cursor.execute(f"UPDATE Cliente SET DIA_AGENDADO='{novo_dia}' WHERE ID_Cliente='{id_cliente}'")
                con.commit()
        elif op == 3:
            cursor.execute(f"SELECT ID_Cliente FROM Cliente WHERE ID_Cliente='{id_cliente}'")
            resultado = cursor.fetchall()# pegar ID CLIENTE
            x = resultado[0][0] ## Esta saindo -> (ID,)
            cursor.execute(f"UPDATE Cliente SET DIA_AGENDADO='Sem Consulta' WHERE ID_Cliente={x}")
            con.commit()
        elif op == 4:
            cursor.execute(f"SELECT * FROM Cliente WHERE ID_Cliente='{id_cliente}'")
            resultados = cursor.fetchall()
            if resultados:
                for resultados in resultados:
                    print(resultados)
        else:
            print("Opcao invalida,digite novamente")
            op = int(input("Sua opcao: "))


def tela_admim():
    while True:
        print("-------------Tela do Administrador----------------")
        print("0 - Para sair da tela do administrador")  
        print("1 - Deseja mudar algum agendamento") 
        print("2 - Desmarcar algum agendamento")  
        print("3 - Deletar Cliente do sistema")  
        print("4 - Mostrar todos os dados dos Clientes")  
        esc = int(input("Digite a sua opçao "))

        if esc == 0:  # sair a tela do administrador
            break

        elif esc == 1:
            nome_pesquisado = str(input("Digite o nome da pessoa que deseja alterar o agendamento "))
            cursor.execute(f"SELECT * FROM Cliente WHERE Nome_Cliente LIKE '{nome_pesquisado}'")
            resultados = cursor.fetchall()
            if resultados:
                print(f"A data marcada é pro dia {resultados[0][3]}")
                nova_data = str(input('Digite a nova data '))
                cursor.execute(f"SELECT ID_Cliente FROM Cliente WHERE Nome_Cliente='{nome_pesquisado}'")
                resultado = cursor.fetchall()# pegar ID CLIENTE
                x = resultado[0][0]
                cursor.execute(f"UPDATE Cliente SET DIA_AGENDADO= '{nova_data}' WHERE ID_Cliente='{x}'")
                con.commit()
            else:
                print("Nenhum resultado encontrado")
        
        elif esc == 2: 
            nome = str(input("Digite o nome do Usuario que deseja desmarcar consulta "))
            cursor.execute(f"SELECT ID_Cliente FROM Cliente WHERE Nome_Cliente='{nome}'")
            resultado = cursor.fetchall()# pegar ID CLIENTE
            x = resultado[0][0] ## Esta saindo -> (ID,)
            cursor.execute(f"UPDATE Cliente SET DIA_AGENDADO='Sem Consulta' WHERE ID_Cliente={x}")
            con.commit()


        elif esc == 3:
            nome = str(input("Digite o nome do Usuario que deseja excluir "))
            cursor.execute(f"SELECT ID_Cliente FROM Cliente WHERE Nome_Cliente='{nome}'")
            resultado = cursor.fetchall()# pegar ID CLIENTE
            x = resultado[0][0]
            cursor.execute(f"SELECT ID FROM USUARIO WHERE ID='{x}'")
            res = cursor.fetchall() #PEGAR ID USUARIO
            y = res[0][0]
            if x == y:
                cursor.execute(f"DELETE FROM Cliente WHERE Nome_Cliente='{nome}'")
                con.commit()
                cursor.execute(f"DELETE FROM USUARIO WHERE ID='{y}'")
                con.commit()


        elif esc == 4:
            l = str(input("[S/N] sendo S para todos e N para algum especifico "))[0].lower()
            if l == "s": # Mostrar todos os clientes
                s = cursor.execute("SELECT * FROM Cliente")  
                for j in s:
                    print(j)
            else:  # procurar no banco ate achar o nome do cliente desejado
                nome_pesquisado = str(input("Digite o nome da pessoa "))
                cursor.execute("SELECT * FROM Cliente WHERE Nome_Cliente LIKE ?", ('%' + nome_pesquisado + '%',))
                resultados = cursor.fetchall()
                if resultados:
                    for resultados in resultados:
                        print(resultados)
                else:
                    print("Opçao Invalida,Digite novamente")
        else:
            print("Opcao Invalida, Digite novamente")


con = sqlite3.connect('Banco.db')
cursor = con.cursor()
cont = 1 # igualar o ID dos bancos USUARIOS E CLIENTE


criar_banco()


while True:
    print("---------- MENU INICIAL ----------")
    print("0 - Encerrar")
    print("1 - Login")
    print("2 - Cadastro")
    esc = int(input("Opcao -> "))

    if esc == 0:
        break
    elif esc == 1:
        key1 = str(input("DIGITE o login "))
        key2 = str(input("Digite a senha "))
        resultado = Login(key1, key2)
        #login_cliente , id_cliente = Login(key1, key2), resultado # como será retornado falso pelo login, o login cliente recebe falso e o id_cliente recebe ID
        if resultado[0]:
            tela_admim()
        else:
            id_cliente = resultado[1]
            tela_usuario(cont,id_cliente)
    elif esc == 2:
        cont += 1
        Cadastro(cont)
    else:
        print("Numero Invalido, tente novamente")
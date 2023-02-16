import psycopg2  as pg #criar a comunicação do postgresql com python

#1-criando as variavels de endereço
hostname = 'localhost'
database = 'cadastro_cliente'
username = 'postgres'
pwd = 'daniel'
port_id = 5432

# para conectar o curso para execultar o sql 
conexao = pg.connect(host = hostname, dbname = database, user = username, password = pwd,port = port_id)

#criando conexao o curso para execultar
cursor = conexao.cursor()
#criando uma class para pegar a id nome e sobrenome o objetivo da class é para criar varios clientes
def id():
    id = int(input('digite a id : '))
    return id
    
def nome():
    nome = input("Digite o nome : ")
    return nome

def sobrenome():
    sobrenome = input ('Digite sobrenome : ')
    return sobrenome

def nome_da_tabela():
    nome_da_tabela = input ('Nome da tabela: ')
    return nome_da_tabela
 
#criar uma tabela no banco

#função para inserir dados na tabela
def clientes_insert():
    sql_insert = f"""
    INSERT INTO cliente(id, nome, sobrenome)
    VALUES({id()},'{nome()}','{sobrenome()}') """
    cursor.execute(sql_insert)
    #commit tem que esta aqui no final para atualizar as informações
    conexao.commit()
    #para moldificar dados que estar na tabela 
    
    
 #função so para modifica o nome da tabela   
def nome_update():
    
    sql_update_nome = f"""
    UPDATE {nome_da_tabela()}
    SET nome = '{nome()}' 
    WHERE id = {id()}"""
    cursor.execute(sql_update_nome)
    #commit tem que esta aqui no final para atualizar as informações
    conexao.commit()


#função para modifica sobrenome da tabela
def sobrenome_update():
    
    sql_update_sobrenome = f"""
    UPDATE {nome_da_tabela()}
    SET sobrenome = '{sobrenome()}' 
    WHERE id = {id()}"""
    cursor.execute(sql_update_sobrenome)
    #commit tem que esta aqui no final para atualizar as informações
    conexao.commit()


#função para deleta dados da tabela mais não exclui a tabela
def delete():
    sql_delete = f"""
    DELETE FROM {nome_da_tabela()} 
    WHERE id = {id()}"""
    cursor.execute(sql_delete)
    #commit tem que esta aqui no final para atualizar as informações
    conexao.commit()
    
def delete_table():
    sql_delete_tabela = f"""
    DROP TABLE {nome_da_tabela()} 
    """
    cursor.execute(sql_delete_tabela)
    conexao.commit()


def criar_tabela():
    sql_criar = f"""CREATE TABLE {nome_da_tabela()} 
    (id SMALLINT PRIMARY KEY,
    Nome_funcionario VARCHAR (255) NOT NULL,
    Função_departamento VARCHAR (255) NOT NULL,
    Departamento VARCHAR (255) NOT NULL)"""
    cursor.execute(sql_criar)
    conexao.commit()



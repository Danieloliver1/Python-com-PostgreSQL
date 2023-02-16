import pandas as pd # para extrair os dados do postgre e mostrar no python
from sqlalchemy  import create_engine # para abrir comunicação com banco de dados


#conectar com postgresql, fazendo conexao
engine = create_engine("postgresql://postgres:daniel@localhost:5432/cadastro_cliente")

#extrair dados do postgres acessando a tabela cliente do basedata 
dados = "SELECT * FROM cliente"
#pegando os dados da tabela clientes atraves do pandas
tabela = pd.read_sql_query(dados,con=engine)
#exibindo a tabela cliente
# print(tabela)
#fim da visualizanção da tabela

print(tabela)
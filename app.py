# from banco_de_daddos.banco_de_dados_sql import Conexao as ConexaoDB
from banco_de_daddos.banco_de_dados_nosql import Conexao as ConexaoDB

conexaoDB = ConexaoDB()
conexaoDB.conectar()
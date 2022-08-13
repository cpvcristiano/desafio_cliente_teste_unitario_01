from datetime import date
import pytest
from domain.entities.cliente  import Cliente

@pytest.mark.parametrize("id, nome, data_nascimento, mensagem_erro",
[
    (None, None, None, "Id deve ser uma string"),
    ("Sergio", None, None, "Id deve conter somente numeros"),
    ("1234567", None, None, "Id deve ter entre 1 e 5 digitos"),
    ("12345", None, None, "Nome deve ser uma string"),
    ("12345", "cris", None, "Nome deve ter entre 5 e 100 caracteres. [Tamanho=4]"),
    ("12345", "c"*101, None, "Nome deve ter entre 5 e 100 caracteres. [Tamanho=101]"),
   
    
]
)
def test_cliente_com_campos_invalidos(id: str, nome:str, data_nascimento: date, mensagem_erro: str):
    with pytest.raises(Exception) as erro:
        cliente = Cliente(id, nome, data_nascimento)

    #Assert
    assert str(erro.value) == mensagem_erro

""""

def test_cliente_com_nulo_nos_campos_erro():
    # Arrange
    id = None
    nome = None
    

    #Act 
    with pytest.raises(Exception) as erro:
        cliente = Cliente(id, nome,)

    #Assert
    assert str(erro.value) == "Id deve ser uma string"

def test_cliente_com_id_nao_numerico_erro():
    # Arrange
    id = "sergio"
    nome = None
   
    #Act 
    with pytest.raises(Exception) as erro:
        cliente = Cliente(id, nome, )

    #Assert
    assert str(erro.value) == "Id deve conter somente numeros"

def test_cliente_com_id_numerico_maior_que_5_erro():
    # Arrange
    id = "12345567"
    nome = None
   
    #Act 
    with pytest.raises(Exception) as erro:
        cliente = Cliente(id, nome, )

    #Assert
    assert str(erro.value) == "Id deve ter entre 1 e 5 digitos"

def test_cliente_com_nome_nulo_erro():
    # Arrange
    id = "12345"
    nome = None
    
    #Act 
    with pytest.raises(Exception) as erro:
        cliente = Cliente(id, nome,)

    #Assert
    assert str(erro.value) == "Nome deve ser uma string"
    
def test_cliente_com_nome_menor_que_5_erro():
    # Arrange
    id = "12345"
    nome = "Cris"
  
    
    #Act 
    with pytest.raises(Exception) as erro:
        cliente = Cliente(id, nome,)

    #Assert
    assert str(erro.value) == f"Nome deve ter entre 5 e 100 caracteres. [Tamanho={len(nome)}]"

def test_cliente_com_nome_maior_que_100_erro():
    #Arrange
    id = "12345"
    nome = "c"*101
    
    
    #Act 
    with pytest.raises(Exception) as erro:
        cliente = Cliente(id, nome,)

    #Assert
    assert str(erro.value) == f"Nome deve ter entre 5 e 100 caracteres. [Tamanho={len(nome)}]"

def test_cliente_com_nome_maior_que_5_invalido_erro():
    # Arrange
    id = "12345"
    nome = "    5 "
   
    
    #Act 
    with pytest.raises(Exception) as erro:
        cliente = Cliente(id, nome, idade)

    #Assert
    assert str(erro.value) == f"Nome deve ter entre 5 e 100 caracteres. [Tamanho={len(nome.strip())}]"

def test_cliente_com_dados_validos_ok():
    # Arrange
    id = "12345"
    nome = " Cristiano"
 
    
    #Act 
    cliente = Cliente(id, nome,  idade)


    #Assert
    assert cliente.nome == nome.strip()
    assert cliente.id == id
   
 """
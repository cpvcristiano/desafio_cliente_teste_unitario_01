
#data_nascimento ==> somente clientes com 18 anos


from datetime import date


class Cliente:
    def __init__(self, id:str, nome:str, data_nascimento:date):
        self.id=id
        self.nome= nome
        self.data_nascimento = data_nascimento
        if isinstance(id, str) == False:
            raise Exception ("Id deve ser uma string")
            
        if id.isdigit() == False:
            raise Exception ("Id deve conter somente numeros")
        
        tamanho_campo = len(id) 
        if  tamanho_campo <= 0 or tamanho_campo >5:
            raise Exception ("Id deve ter entre 1 e 5 digitos")

        if isinstance(nome, str) == False:
            raise Exception ("Nome deve ser uma string")

        nome = nome.strip()
        if nome == "":
            raise Exception (f"Nome não pode ser vazio")
        
        tamanho_campo = len(nome) 

        if tamanho_campo < 5 or tamanho_campo > 100:
            raise Exception (f"Nome deve ter entre 5 e 100 caracteres. [Tamanho={tamanho_campo}]")

        #idade = self.calcula_idade(self, data_nascimento)
        #if (idade < 18): raise Exception("Idade deve ser maior ou a igual a 18 anos")
          

    
    def calculate_idade(self): 
        idade = 2022 - self.data_nascimento.year
        if (idade < 18 ): raise Exception("Idade deve ser maior ou a igual a 18 anos")
 




       
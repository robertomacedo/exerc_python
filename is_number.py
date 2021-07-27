"""
Treinando python usando conhecimentos 
básicos da linguagem 

"""

print("Imprimir True or False conforme entrada: ")
ent = input("Entre com um dado: ")


def is_number(ent):

    try:
        float(ent)
        return True 
    except:
        return False


print(is_number(ent))

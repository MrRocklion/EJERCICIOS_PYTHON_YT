#Cree una función que tome el dominio del sitio web de correo electrónico a partir de una cadena con el siguiente formato:
# usuario@dominio.com [7:0] 
# el resultado obtenido deberia ser
# dominio.com
def domainGet(email):
    domain = ""
    index = 0
    for a in email:
        if a == "@":
            domain = email[index+1:]
            return domain
        index +=1
print(domainGet("usuario@dominio.com"))
find()
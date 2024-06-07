pikachu= 4500
otaku=5000
pulpo= 5200
anguila=4800
contarP=0
contarO=0
contarPul=0
contarA=0
total =0
desc=0

while True: 
    try: 
        print ("******MENÚ******")
        print ("1. Pikachu Roll")
        print ("2. Otaku Roll")
        print ("3.Pulpo venenoso Roll")
        print ("4. Anguila eléctrica Roll")
        print ("5. Pedido completo")
        opc= int(input ("Ingrese su opción"))
               
        if opc== 1:    
            contarP= contarP + 1 
            total= total + pikachu
        else:
            if opc ==2:
                 contarO =contarO + 1
                 total =total + otaku 
            else:
                  if opc==3:
                      contarPul = contarPul + 1 
                      total =total+ pulpo
                  else:
                    if opc==4:
                            contarA=contarA +1
                            total= total + anguila
                    else:
                        if opc==5:
                            break
    except ValueError:
        print ("Ingreso de la opción debe ser válida")

totalPagar =total -desc
sumaCont = contarP + contarO + contarPul + contarA   
print ("******************")
print ("Total productos", sumaCont)
print ("Pikachu roll: ", contarP)
print ("Otaku roll: ", contarO)
print ("Pulpo roll: ", contarPul)
print ("Anguila roll: ", contarA)
print ("******************")
print ("Subtotal por pagar: $ ", total)
print ("Descuento por código: $ ", desc)
print ("Total: $ ", totalPagar)

resp= input ("Desea volver a comprar (si/no):").lower ()
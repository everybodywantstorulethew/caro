vprecio = float(input("dame el precio del producto: "))
vdesc = input("tiene descuento del 10%, Si es s, No es n: ")
if vdesc == 's':
    vprecio = vprecio - (vprecio * .10)
print("el precio del producto es: %.2f" %(vprecio))
                
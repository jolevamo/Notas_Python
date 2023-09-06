print("---------------Sistema de facturación---------------")
producto = input("Producto: ")
cantidad = int(input("Cantidad: "))
precio = float(input("Precio: "))
subtotal = cantidad * precio
if cantidad > 1 and cantidad <=10:
    descuento = float(0)
elif cantidad <= 20:
    descuento = float(subtotal *0.07)
elif cantidad <= 30:
    descuento = float(subtotal *0.13)
elif cantidad <= 40:
    descuento = float(subtotal *0.20)
elif cantidad > 40:
    descuento = float(subtotal *0.35)

subtotal2 = subtotal - descuento
iva = subtotal2 * 0.19
neto = subtotal2 + iva

if cantidad <=0 or precio <=0:
    print("Por favor revise la cantidad y el precio ingresados, sólo se pueden ingresar valores mayores a cero (0)")
else:
    print(F"Valor antes de descuento: {subtotal} \nDescuento: {descuento} \nSubtotal después de descuento: {subtotal2} \nIva: {iva} \nNeto: {neto}")



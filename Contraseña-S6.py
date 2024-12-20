def solicitar_contraseña():# se le pide ingresar una contraseña al usuario
    for intento in range(3):#se le indica que solo tendra 3 intentos para generar la contraseña correctamente 
        contraseña = input("Ingresa una contraseña que inicie con un número: ")# se incica que ingrese una contraseña que contenga un numero al inico
        if contraseña and contraseña[0].isdigit():
            """si las contraseñas contiene un numero seguira al siguiente paso, para eso se introdcue la (funcion.isdigit)
        indicando que deve contener un numero ya que si no lo tiene lo marcara como error, tambien incicando que en el rango 0, osea al iniciar la contraseña
        deve contener al inicio el numero"""
            
            confirmacion = input("Confirma tu contraseña: ")#si la contraseña inicia con un numero se le indicara que verifique de nuevo la contraseña 
            if contraseña == confirmacion:
                print("¡Contraseña correcta!")
                return True
            else:
                print("Las contraseñas no coinciden.")# si tiene algun numero al inicio pero si al verificar tiene algo mas que la contraseña inicial se le mara cara que no concide
        else:
            print("La contraseña debe iniciar con un número.")
    
    print("Has cometido tres errores. El programa se cerrará.")# si no llegase poner la contraseñqa correctam,ete las tres veces se le indicara que ya no puede meter mas datos
    return False

solicitar_contraseña()

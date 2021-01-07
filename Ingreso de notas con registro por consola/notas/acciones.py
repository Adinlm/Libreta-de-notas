import notas.nota as modelo


class Acciones:

    def crear(self, usuario):
        print("Se creara una nueva nota ")
        titulo = input("Introduzca el titulo de la nota: ")
        descripcion = input("Mete el contenido de tu nota: ")

        nota = modelo.Nota(usuario[0], titulo, descripcion)
        guardar = nota.guardar()

        if guardar[0] >= 1:
            print(f"\n La nota se ha guardado: {nota.titulo}")

        else:
            print("\n La nota no ha podido guardarse")

    def mostrar(self, usuario):
        print(f"\n {usuario[1]}, las notas que ha guardado se muestran a continuación: ")

        nota = modelo.Nota(usuario[0])
        notas = nota.listar()

        for nota in notas:
            print("\n**********------------------***********")
            print(nota[2])
            print(nota[3])
            print("**********------------------*********** \n")

    def borar(self, usuario):
        print(f"\n {usuario[1]}, se eliminaran notas")

        titulo = input("Ingrese el titulo de la nota a borrar: ")

        nota = modelo.Nota(usuario[0], titulo, "")
        eliminar = nota.eliminar()

        if eliminar[0] >= 1:
            print(f"Se ha borrado la nota : {nota.titulo}")

        else:
            print("No se ha borrado la nota, intente mas tarde...")

import typing

#Clase que genera todo el HTML resultante.
class HtmlGenerator:
    def __init__(self):
        self.template_file: typing.TextIO = None
        self.file_content: str = ""
    #Abre, lee y cierra el archivo HTML de plantilla.
    def read_template(self, path: str):
        with open(path, "r") as archivo:
            self.file_content = archivo.read()
            archivo.close()
    #Reeplaza las variables por el contenido del diccionario
    def replace_vars(self, vars: typing.Dict):
        for i in vars:
            self.file_content = self.file_content.replace("%"+i+"%", vars[i])
        
    #Escribe la pagina
    def write_page(self, path):
        with open(path, "w", encoding="utf-8") as archivo:
            archivo.write(self.file_content)
            archivo.close()
    
    #La funcion todo en uno: Abre reemplaza cierra.
    def generate_page(self, vars:typing.Dict):
        self.read_template("./data/html/template.html")
        self.replace_vars(vars)
        self.write_page("./out/page.html")
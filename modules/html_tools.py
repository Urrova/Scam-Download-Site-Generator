import typing, os, base64

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
        if not os.path.exists("./out/"):
            os.makedirs("./out/")
        self.write_page("./out/page.html")

#Abre una imagen, la convierte a base64 y la mete en un tag img
def image_to_img_base64(path: str, image_type: str, attr: str=""):
    image_base64:str = ""
    image_tag:str = ""
    with open(path, "rb") as image_file:
        image_data = image_file.read()
        image_base64 = base64.b64encode(image_data).decode("ascii")
        image_tag = "<img src='data:image/"+image_type+";base64,"+image_base64+"' "+attr+">"
        image_file.close()
    return image_tag
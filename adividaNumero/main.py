import random
import string
import cherrypy
from jinja2 import Environment, FileSystemLoader

env1 = Environment(loader=FileSystemLoader('templates'))
tmpl = env1.get_template('templateAdivina.html')
numeroRandom = random.randint(1,100)

class numberGenerator(object):
    @cherrypy.expose
    def index(self):
        return tmpl.render()

    @cherrypy.expose
    def generate(self, intento):
        res= int(intento)
        if numeroRandom == res:
            return """<h1>eres un maquina!</h1>"""
        else:
            if numeroRandom < res:
                tmpl = env1.get_template('templateAdivinaMenor.html')
                return tmpl.render(), """<h1>Prueba con un numero MENOR!</h1>"""
            else:
                tmpl = env1.get_template('templateAdivinaMayor.html')
                return tmpl.render(), """<h1>Prueba con un numero MAYOR!</h1>"""



if __name__ == '__main__':
	cherrypy.quickstart(numberGenerator())

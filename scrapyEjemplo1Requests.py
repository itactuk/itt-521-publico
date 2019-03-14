import requests

url = "https://www.pucmm.edu.do"
inicio_title = 'href="https://www.pucmm.edu.do/noticias/Lists/EntradasDeBlog/ViewPost.aspx'

lista_noticias = []

res = requests.get(url)
contenido = res.content.decode('utf-8')
while inicio_title in contenido:
    i1 = contenido.find(inicio_title)
    contenido = contenido[i1:]
    inicio_title_verdadero = '">'
    i1v = contenido.find(inicio_title_verdadero)
    contenido = contenido[i1v+len(inicio_title_verdadero):]
    fin_title = '</a>'
    fin_indice = contenido.find(fin_title)
    lista_noticias.append(contenido[:fin_indice])
    contenido = contenido[fin_indice+len(fin_title):]
print(lista_noticias)
# print(contenido)

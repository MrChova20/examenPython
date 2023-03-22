import csv

import csv

def read_data(fichero):
    dict = {}
    
    with open(fichero, 'r') as csv:
        csv_reader = csv.reader(csv, delimiter=';')
        
        next(csv_reader)
        
        contador = 0
        
        for row in csv:
            
            if '' in row:
                continue
            
            dict2 = {}
            
            for i in range(len(row)):
                key = 'dato{}'.format(i+1)
                dict2[key] = row[i]
            
            dict['muestra{}'.format(contador + 1)] = dict2
            
            contador += 1
            
        if contador < 10:
            raise ValueError('El archivo debe tener al menos 10 lineas completas de muestra.')
            
    return dict

    ""
    {
    'dato':{'type':'white',
            'fixed acidity':'7',
            'volatile acidity': '0.27',
            'citric acid':'0.36',
            'residual sugar':'20.7',
            'chlorides':'0.045',
            'free sulfur dioxide':'45',
            'total sulfur dioxide':'170',
            'density':'1.001',
            'PH':'3',
            'sulphates':'0.45',
            'alcohol':'8.8',
            'quality':'6',
        },


      

}
""

def  split (dict):
#usando una tupla resolvemos el problema de devolver dos objetos sin necesidad de un array
    typeWhite={}
    typeRed={}    
    for dato, wine in dict.items():
        if wine['type'] == 'white':
            del wine['type']
            typeWhite[dato] = wine
            
        elif wine['type'] == 'red':
            del wine['type']
            typeRed[dato] = wine
            
    return typeWhite, typeRed 



def reduce(dict, atributo):
    #volvemos a gastar tuplas para devolver datos
    lista=list(dict)
    atributostr=str(atributo)
for i in dict.items():
    if  i != dict:
        raise ValueError('EL atributo que se le esta pasando no exite')
            
    return lista, atributostr


def silhouette(list1,list2):
    #Silhouette(lista)=media(S(i))
    #S(i)=((b(i)-a(i))/maximo(a(i),b(i)))

    

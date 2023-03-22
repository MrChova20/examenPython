import csv
import math

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
            raise ValueError('NO TIENE 10 LINEAS')
            
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

    if atributo not in next(iter(dict.values())).values():
        raise ValueError(f'Atributo "{atributo}"')

    return [sample_dict[atributo] for sample_dict in 
            dict['white'].values()] + \
           [sample_dict[atributo] for sample_dict in 
            dict['red'].values()]


def silhouette(list1,list2):
    #Silhouette(lista)=media(S(i))
    for i in range(len(list1) and range(len(list2))):
        contador += (contador+i)/i+1
    distanciaMedia=contador
    distannciaMedia=math.sqrt(math.pow(abs()))
    #S(i)=((b(i)-a(i))/max(a(i),b(i)))
    

    valores = []
    for i, x1 in enumerate(list1):

    
     return valores
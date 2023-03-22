from functions import *



if __name__ == '__main__':
    try:
        data = read_data('winequality.csv')
        white_data, red_data = split(data)
        alcohol_values = reduce(white_data, 'alcohol')
        ph_values = reduce(red_data, 'pH')
       
        
        print(f'Ha ocurrido la excepción {type(e).__name__}: {e}')
    except Exception as e:
        print(f'Ha ocurrido un error inesperado: {e}')
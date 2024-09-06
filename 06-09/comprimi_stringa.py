'''
Compressione stringhe
'''

def d_check_string(function):
    def wrapper(stringa):
        if len(stringa) == 0:
            print('Hai inserito una stringa vuota!')
        stringa_compressa = function(stringa)
        if stringa_compressa == stringa:
            print('La stringa non è stata compressa')
        elif stringa_compressa is None:
            print('Non hai inserito stringa alfabetica')
        else:
            print('La stringa compressa è', stringa_compressa)
            print('La stringa originaria è ', stringa)
    return wrapper


@d_check_string
def comprimi_stringa(stringa):
    if len(stringa) == 0:
        return stringa
<<<<<<< HEAD
    if stringa.isalpha() == False:
        return None
=======
>>>>>>> 77028b2e30818d8b256aabe1c1169eba6240487f
    result = []
    count = 1
    compressed = False
    for index in range(1, len(stringa)):
        if stringa[index] == stringa[index-1]:
            count += 1
            compressed = True    
        else:
           result.append(stringa[index-1] + str(count))
           count = 1 
    result.append(stringa[-1] + str(count))
    stringa_compressa = ''.join(result)
    if compressed:    
        return stringa_compressa
    else:
        return stringa

string_test = 'abBBBc'
compressed_string = comprimi_stringa(string_test)


    

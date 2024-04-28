def get_cats_info(path):
    try:
        final = []
        my_dict = {}
        keys = ["id", "name", "age"]
        
        with open(path, 'r', encoding='utf-8') as fh:
            lines = [el.strip() for el in fh.readlines()]

            for i in range(len(lines)):
                str_name = lines[i].split(',')
            
                for e in range(3):
                    my_dict.update({keys[e] : str_name[e]})
                final.append(my_dict)
                
            return final
        
    except FileNotFoundError:
        print('Файл не знайдено!')
    except IndentationError:
        print('Помилка відступу!')
    except SyntaxWarning:
        print('Синтаксична помилка!')

# C:/Users/Lenovo/Desktop/qwert.txt
path = 'C:/Users/Lenovo/Desktop/qwer.txt'  # Provide the full path here
print(get_cats_info(path))

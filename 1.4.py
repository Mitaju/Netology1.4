documents = [
    {"type": "passport", "number": "2207 876234", "name": "Василий Гупкин"},
    {"type": "invoice", "number": "11-2", "name": "Геннадий Покемонов"},
    {"type": "insurance", "number": "10006", "name": "Аристарх Павлов"}
      ]
      
directories = {
    '1': ['2207 876234', '11-2'],
    '2': ['10006'],
    '3': []
      }   

def get_name():
    doc_number = input('Введите номер документа:')
    for document in documents:
      if document['number'] == doc_number:
            name = document['name'] 
    if name is not None:
        print('{}'.format(name))
    elif name is None:
        name = 'Документа с таким номером нет'
        print(name)
        
      
def get_list():
    for document in documents:
        doc_type = document['type']
        doc_number = document['number']
        name = document['name']
        print('{} "{}" {}'.format(doc_type, doc_number, name))
        
def get_dir():
    doc_number = input('Введите номер документа:')
    for key, value in directories.items():
        if doc_number in value:
            print(key)
            

def add_doc():
    doc_number = input('Введите номер документа:')
    doc_type = input('Введите тип документа:')
    user_name = input('Введите имя:')
    dir_number = input('Введите номер полки:')
    documents.append({"type": doc_type, "number": doc_number, "name": user_name})
    dir_len = int(dir_number)
    if dir_len > len(directories):
        print('Полки с таким номером нет, введите номер не больше',\
        len(directories))
        dir_number = input()
        directories[dir_number].append(doc_number)
    else:
        directories[dir_number].append(doc_number)
    print(get_list())
    print(directories)

def user_input():
    user_comand = input('Команды:\n p - вывести имя по номеру документа;\n l - список всех документов;\n s - номер полки с документом;\n a - добавить новый документ в каталог и на полку;\n q - выход\n')
    return user_comand
     
def main():
    while True:
        user_comand = user_input()
        if user_comand == 'p':
            get_name()
        elif user_comand == 'l':
            get_list()
        elif user_comand == 's':
            get_dir()
        elif user_comand == 'a':
            add_doc()
        elif user_comand == 'q':
            break;
            
main()

            
        
            
            
            
    

    

    

    
        
            
        


    
    

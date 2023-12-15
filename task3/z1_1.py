documents = [
    {"type": "passport", "number": "2207 876234", "name": "Василий Гупкин"},
    {"type": "invoice", "number": "11-2", "name": "Геннадий Покемонов"},
    {"type": "insurance", "number": "10006", "name": "Аристарх Павлов"},
    {"type": "driver license", "number": "5455 028765", "name": "Василий Иванов"},
]

directories = {
    '1': ['2207 876234', '11-2', '5455 028765'],
    '2': ['10006'],
    '3': []
}

def get_person_by_document_number(doc_number):
    for doc in documents:
        if doc['number'] == doc_number:
            return doc['name']
    return "Документ не найден"

def get_shelf_by_document_number(doc_number):
    for shelf, docs in directories.items():
        if doc_number in docs:
            return shelf
    return "Документ не найден на полках"

def list_all_documents():
    for doc in documents:
        print(f"{doc['type']} \"{doc['number']}\" \"{doc['name']}\"")

def add_document_to_catalog(doc_number, doc_type, doc_name, shelf_number):
    documents.append({"type": doc_type, "number": doc_number, "name": doc_name})
    directories.setdefault(shelf_number, []).append(doc_number)

def delete_document(doc_number):
    for doc in documents:
        if doc['number'] == doc_number:
            documents.remove(doc)
            for shelf, docs_on_shelf in directories.items():
                if doc_number in docs_on_shelf:
                    docs_on_shelf.remove(doc_number)
                    print(f"Документ удален из каталога и с полки")
                    return
    print("Документ не найден")

def move_document(doc_number, target_shelf):
    for shelf, docs_on_shelf in directories.items():
        if doc_number in docs_on_shelf:
            if target_shelf in directories:
                docs_on_shelf.remove(doc_number)
                directories[target_shelf].append(doc_number)
                print(f"Документ перемещен на полку")
                return
            else:
                print(f"Полкаbне существует")
                return
    print("Документ не найден на полках")

def add_shelf(shelf_number):
    if shelf_number not in directories:
        directories[shelf_number] = []
        print(f"Полка добавлена")
    else:
        print(f"Полка уже существует")

command = input("Введите команду (p, s, l, a, d, m, as): ")

if command == 'p':
    doc_number = input("Введите номер документа: ")
    print(get_person_by_document_number(doc_number))
elif command == 's':
    doc_number = input("Введите номер документа: ")
    print(get_shelf_by_document_number(doc_number))
elif command == 'l':
    list_all_documents()
elif command == 'a':
    doc_number = input("Введите номер документа: ")
    doc_type = input("Введите тип документа: ")
    doc_name = input("Введите имя владельца: ")
    shelf_number = input("Введите номер полки: ")
    add_document_to_catalog(doc_number, doc_type, doc_name, shelf_number)
elif command == 'd':
    doc_number_to_delete = input("Введите номер документа для удаления: ")
    delete_document(doc_number_to_delete)
elif command == 'm':
    doc_number_to_move = input("Введите номер документа для перемещения: ")
    target_shelf_to_move = input("Введите целевую полку: ")
    move_document(doc_number_to_move, target_shelf_to_move)
elif command == 'as':
    new_shelf_number = input("Введите номер новой полки: ")
    add_shelf(new_shelf_number)
else:
    print("Неверная команда")

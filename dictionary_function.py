storage = [
    {'name':'andrey', 's_name':'ivanov', 'email':'s.ivanov@mail.ru', 'address':'kievsky prospekt 100'},
    {'name':'sergey', 's_name':'petrov','email': 's.petrov@mail.ru', 'address':'darnytsy prospekt 200'},
    {'name':'ivan', 's_name':'sergeev','email':'s.sergeev@mail.ua', 'address':'geroev stalingrada str.10'},
    {'name':'diego', 's_name':'nogueira','email':'diego.n@correio.com.br', 'address':'av. antonio carlos, 150'},
    {'name':'felipe', 's_name':'ferreira','email':'felipe.f@terra.com.br', 'address':'avenida atlantica 200'},

    ]
def main():
    op = input("Pleae select action 1. Add new user 2. Show current info: ")
    if op == '1':
        my_add()
    elif op == '2':
        my_show()
    return storage

def my_add(*args):
    
    ans = 0
    while ans != "no":
        name = input("enter name: ")
        s_name = input("enter second name: ")
        email = input("enter email: ")
        address = input("enter home address: ")
        storage.append({'name': name,'s_name': s_name, 'email': email, 'address': address} )
        print("your record has been added ")
        
        print("name: ", storage[len(storage)-1]['name'],"\n",
                  "s_name: ", storage[len(storage)-1]['s_name'],"\n",
                  "email: ", storage[len(storage)-1]['email'],"\n",
                  "address: ", storage[len(storage)-1]['address'],"\n","\n", sep=""
                  )
        ans = input("One more entry? ")
        
    return storage

def my_show(*args):
    v = 0 
    my_request = input("please enter name of the person to request info: ")
    for i in range(len(storage)):
        if my_request == storage[i]['name']:
            print("name: ", storage[i]['name'],"\n",
                  "s_name: ", storage[i]['s_name'],"\n",
                  "email: ", storage[i]['email'],"\n",
                  "address: ", storage[i]['address'], sep=""
                  )
            v += 1
    if v == 0:
        print("element not found")

main()       
        



 

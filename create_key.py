from random import randint

a = ["q","w","e","r","t","y","u","i","o","p","a","s","d","f","g","h","j","k","l","z","x","c","v","b","n","m"]
b = ["Q","W","E","R","T","Y","U","I","O","P","A","S","D","F","G","H","J","K","L","Z","X","C","V","B","N","M"]
c = ["1","2","3","4","5","6","7","8","9","0"]

for m in range(1000):
    password = []
    for i in range(25):


        a_1 = randint(0, 25)
        b_1 = randint(0, 25)
        c_1 = randint(0, 9)

        pass_choice = randint(1,3)
        if pass_choice == 1:
            password.append(a[a_1])
        if pass_choice == 2:
            password.append(b[b_1])
        if pass_choice == 3:
            password.append(c[c_1])
    f = open('pass.txt', 'a', encoding='utf-8')
    f.write("\n" + "".join(password))
    f.close()
        


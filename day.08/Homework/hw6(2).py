favorite_number_user = int(input("შეიყვანეთ თქვენი საყვარელი რიცხვი: "))
favorite_number_me = 7

print("თქვენი საყვარელი რიცხვი ერთნაირია ჩემს საყვარელ რიცხვთან!" * (favorite_number_user == favorite_number_me) or "თქვენი საყვარელი რიცხვი არ არის ჩემი საყვარელი რიცხვი.")
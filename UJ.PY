class menu():
    def __init__(self):
        self.t=0;

    def show(self):
        print('select the item')
        print('        1- coldrinks')
        print('        2- snacks')
        print('        3- main_course')
        print('        4- indian_bread')
        print('        5- desert')
        print('        6- EXIT')
        k.input();

    def input(self):
        n=int(input('enter your choice = '))
        if (n == 1):
            k.drinks()
        if (n == 2):
            k.snacks()
        if (n == 3):
            k.main_course()
        if (n == 4):
            k.indian_bread()
        if (n == 5):
            k.desert()
        if (n == 6):
            k.thnks()
        else:
            print('***********************invalid input************************');
            k.input()

    def drinks(self):
        print('                  1- Coke                :20 ')
        print('                  2- ThumbsUp            :20 ')
        print('                  3- Maaza               :30 ')
        print('                  4- Sprite              :20 ')
        print('                  5- frooti              :25 ')
        print('                  6- Back to Main Menu')
        k.drinksb()

    def drinksb(self):
        a=int(input('enter the choice=='))

        if(a==1):
            m=k.quan()
            b=(m*20);
            self.t+=b;
            print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~TOTAL =',self.t)
            k.drinks()
        if(a==2):
            m=k.quan()
            b=(m*20);
            self.t+=b;
            print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~TOTAL =', self.t)
            k.drinks()
        if(a==3):
            m=k.quan()
            b=(m*30);
            self.t+=b;
            print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~TOTAL =', self.t)
            k.drinks()
        if(a==4):
            m=k.quan()
            b=(m*20);
            self.t+=b;
            print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~TOTAL =', self.t)
            k.drinks()
        if(a==5):
            m=k.quan()
            b=(m*25);
            self.t+=b;
            print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~TOTAL =', self.t)
            k.drinks()
        if(a==6):
            print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~TOTAL =', self.t)
            k.show()
        else:
            print('***********************invalid input************************');

    def snacks(self):
        print('                  1- burger               :120')
        print('                  2- pizza                :180')
        print('                  3- roll                 :100')
        print('                  4- momos                :120')
        print('                  5- manchurian           :140')
        print('                  6- Back To Main Menu')
        k.snacksb()

    def snacksb(self):
        a = int(input('enter the choice=='))
        if (a == 1):
            m=k.quan()
            b=m*120;
            self.t += b;
            print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~TOTAL =', self.t)
            k.snacks()
        if (a == 2):
            m= k.quan()
            b=m*180;
            self.t += b;
            print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~TOTAL =', self.t)
            k.snacks()
        if (a == 3):
            m = k.quan()
            b = m * 100;
            self.t += b;
            print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~TOTAL =', self.t)
            k.snacks()
        if (a == 4):
            m = k.quan()
            b = m * 120;
            self.t += b;
            print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~TOTAL =', self.t)
            k.snacks()
        if (a == 5):
            m = k.quan()
            b = m * 140;
            self.t += b;
            print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~TOTAL =', self.t)
            k.snacks()
        if (a == 6):
            print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~TOTAL =', self.t)
            k.show()
        else:
            print('***********************invalid input************************');

    def main_course(self):
        print('                  1- Matar masala              :150')
        print('                  2- Mix vegetable             :120')
        print('                  3- Dal makhani               :140')
        print('                  4- Shahi paneer              :180')
        print('                  5- Mushroom masala           :160')
        print('                  6- Back To Main Menu')
        k.mainb()

    def mainb(self):
        a = int(input('enter the choice=='))
        if (a == 1):
            m = k.quan()
            b = m * 150;
            self.t+=b;
            print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~TOTAL =', self.t)
            k.main_course()
        if (a == 2):
            m = k.quan()
            b = m * 120;
            self.t+=b;
            print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~TOTAL =', self.t)
            k.main_course()
        if (a == 3):
            m = k.quan()
            b = m * 140;
            self.t+=b;
            print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~TOTAL =', self.t)
            k.main_course()
        if (a == 4):
            m = k.quan()
            b = m * 180;
            self.t+=b;
            print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~TOTAL =', self.t)
            k.main_course()
        if (a == 5):
            m = k.quan()
            b = m * 160;
            self.t+=b;
            print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~TOTAL =', self.t)
            k.main_course()
        if (a == 6):
            print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~TOTAL =', self.t)
            k.show()
        else:
            print('***********************invalid input************************');

    def indian_bread(self):
        print('                  1- Butter roti             :20')
        print('                  2- Missi roti              :30')
        print('                  3- Mutter naam             :40')
        print('                  4- Plain roti              :10')
        print('                  5- Mix parantha            :20')
        print('                  6- Back To Main Menu ')
        k.indianb()

    def indianb(self):
        a = int(input('enter the choice=='))
        if (a == 1):
            m = k.quan()
            b = m * 20;
            self.t+=b;
            print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~TOTAL =', self.t)
            k.indian_bread()
        if (a == 2):
            m = k.quan()
            b = m * 30;
            self.t+=b;
            print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~TOTAL =', self.t)
            k.indian_bread()
        if (a == 3):
            m = k.quan()
            b = m * 40;
            self.t+=b;
            print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~TOTAL =', self.t)
            k.indian_bread()
        if (a == 4):
            m = k.quan()
            b = m * 10;
            self.t+=b;
            print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~TOTAL =', self.t)
            k.indian_bread()
        if (a == 5):
            m = k.quan()
            b = m * 20;
            self.t+=b;
            print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~TOTAL =', self.t)
            k.indian_bread()
        if (a == 6):
            print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~TOTAL =', self.t)
            k.show()
        else:
            print('***********************invalid input************************');

    def desert(self):
        print('                  1- ice cream               :80')
        print('                  2- gajar hawla             :60')
        print('                  3- rasgolla                :40')
        print('                  4- gulab jamun             :40')
        print('                  5- Back To Main Menu        ')
        k.desertb()

    def desertb(self):
        a = int(input('enter the choice=='))
        if (a == 1):
            m = k.quan()
            b = m * 80;
            self.t+=b;
            print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~TOTAL =', self.t)
            k.desert()
        if (a == 2):
            m = k.quan()
            b = m * 60;
            self.t+=b;
            print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~TOTAL =', self.t)
            k.desert()
        if (a == 3):
            m = k.quan()
            b = m * 40;
            self.t+=b;
            print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~TOTAL =', self.t)
            k.desert()
        if (a == 4):
            m = k.quan()
            b = m * 40;
            self.t+=b;
            print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~TOTAL =', self.t)
            k.desert()
        if (a == 5):
            print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~TOTAL =', self.t)
            k.show()
        else:
            print('***********************invalid input************************');

    def quan(self):
        m=int(input('Please Enter The Quantity -'))
        return m;

    def thnks(self):
        print('-------------------thanks for ordering-----------------------')
        print('.........................Item Total =',self.t)
        print('...................Delivery charges =',20)
        print('.........................Total Bill =',self.t+20)
        print('----------------------Have a nice day-------------------------')
        exit()

k=menu()
k.show()
#k.input()
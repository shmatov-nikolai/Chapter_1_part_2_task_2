# N students take K apples and distribute them among each other evenly. The
# remaining  part remains in the basket. How many apples will
# each single student get? How many apples will remain in the basket?
# The program reads the numbers N and K. It should print the two answers for
# the questions above.  Each N student will take K apples, and remains X)


def takes_Apple(students, apples_in_basket):
    take_apples = apples_in_basket // students
    ostatok_apple = apples_in_basket - (take_apples * students)
    slovo_1 = 'яблок'
    slovo_2 = 'яблоку'
    slovo_3 = 'яблока'
    if take_apples == 0 or take_apples%100>=10 and take_apples%100<=20:
        print('Количество студентов {}, каждый из них взял по {} {}'.format(students, take_apples, slovo_1))
    elif take_apples%10 == 1:
        print('Количество студентов {}, каждый из них взял по {} {}'.format(students, take_apples, slovo_2)) 
    elif take_apples%10 >= 2 or take_apples%10 <= 4:
        print('Количество студентов {}, каждый из них взял по {} {}'.format(students, take_apples, slovo_3))
    else:
        print('Количество студентов {}, каждый из них взял по {} {}'.format(students, take_apples, slovo_1))


    print("Остаток яблок в корзине: {}".format(ostatok_apple))


takes_Apple(4, 92)
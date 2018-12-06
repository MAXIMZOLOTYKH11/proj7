" Попробуйте себя в роли программы-консультанта и напишите программу, которая поможет покупателю узнать свой размер. Программа должна быть рассчитана на обычных людей(людей без ожирения и без анорексии.)"


def man(h, c_g, w_g, h_g):
    size = ''
    choice = ['Your size: S', 'Your size:  M', 'Your size: L', 'Your size: XL']
    hh = [170, 174, 178, 182]
    cc = [90, 96, 102, 108]
    ww = [80, 86, 92, 98]
    hg = [94, 98, 102, 108]
    count = -1
    for s in hh:
        dif = abs(s - h)
        count += 1
        if 0 < dif < 4:
            size = choice[count]
    count = choice.index(size)
    if h > 182:
        size = choice[3]
    if h < 170:
        size = choice[0]
    if c_g > cc[count]:
        count += 1
        size = choice[count]
    if w_g > ww[count]:
        count += 1
        size = choice[count]
    if h_g > hg[count]:
        count += 1
        size = choice[count]
    print(size)


def woman(h, c_g, w_g, h_g):
    size = ''
    choice = ['Your size: S', 'Your size:  M', 'Your size: L', 'Your size: XL']
    hh = [160, 164, 168, 172]
    cc = [88, 94, 100, 108]
    ww = [68, 74, 80, 88]
    hg = [96, 102, 108, 114]
    count = -1
    for s in hh:
        dif = abs(s - h)
        count += 1
        if 0 < dif < 4:
            size = choice[count]
    count = choice.index(size)
    if h > 172:
        size = choice[3]
    if h < 160:
        size = choice[0]
    if c_g > cc[count]:
        count += 1
        size = choice[count]
    if w_g > ww[count]:
        count += 1
        size = choice[count]
    if h_g > hg[count]:
        count += 1
        size = choice[count]
    print(size)


def main():
    gender = str(input('Hello!!! What is your gender(man\woman)? '))
    height = int(input('What is your height? '))
    chest_girth = int(input('What is your chest girth? '))
    waist_girth = int(input('What is your waist girth? '))
    hip_girth = int(input('What is your hip girth? '))

    if gender == 'man':
        man(height, chest_girth, waist_girth, hip_girth)
    if gender == 'woman':
        woman(height, chest_girth, waist_girth, hip_girth)


if __name__ == '__main__':
    main()
from pydraw import *
import time

screen = Screen(800, 600, 'Explaining Searching or Sorting')
screen.color(Color('black'))

rec_list = []
num_list = []

java_binary_search = [Text(screen, ' int low = 0;', 20, 60, Color('white')),  # 0
                      Text(screen, ' int high = listName.length - 1;', 20, 80, Color('white')),  # 1
                      Text(screen, ' while( low <= high){', 20, 100, Color('white')),  # 2
                      Text(screen, 'int mid = (low + high)/2;', 40, 120, Color('white')),  # 3
                      Text(screen, 'if( mid > (Number Wanted)', 40, 140, Color('white')),  # 4
                      Text(screen, 'high = mid - 1;', 60, 160, Color('white')),  # 5
                      Text(screen, 'else if( mid < (Number Wanted)', 40, 180, Color('white')),  # 6
                      Text(screen, 'low = mid - 1;', 60, 200, Color('white')),  # 7
                      Text(screen, 'else', 40, 220, Color('white')),  # 8
                      Text(screen, 'return mid;}', 60, 240, Color('white')),  # 9
                      Text(screen, 'return -1;', 20, 260, Color('white'))]  # 10
java_linear_search = [Text(screen, 'for( int i = 0; i<list.length;i++){', 20, 60, Color('white')),  # 0
                      Text(screen, 'if( list[i] == (Number Wanted))', 40, 80, Color('white')),  # 1
                      Text(screen, 'return i;', 60, 100, Color('white')),  # 2
                      Text(screen, ' return -1;', 20, 120, Color('white'))]  # 3


def setup():
    screen.clear()
    start_text = Text(screen, 'Press up arrow to explain Binary Search'
                              '\nPress down arrow for Linear Search', screen.width() / 2, screen.height() / 2,
                      Color('white'), font='Arial', size=20)
    start_text.move(-start_text.width() / 2, -start_text.height() / 2)

    rec_list.clear()
    num_list.clear()


def graphics():
    x = 75
    y = 450
    width = 40
    height = 30

    screen.clear()

    for i in range(15):
        rec_list.append(Rectangle(screen, x, y, width, height, Color('red')))
        num_list.append(Text(screen, str(i), x + 15, y + 15 + height, Color('white')))
        x += 45
        y -= 20
        height += 20


def show(array, tint):
    for i in range(len(array)):
        array[i].color(Color(tint))


def description_text(number):
    Text(screen, 'Finding: ' + str(number) +
         '\nBlue is location of mid', 20, 20, Color('purple'))


def linear_search():
    print('type a number between 0 - ', len(rec_list) - 1)
    finding = int(input())
    found_test = False

    description_text(finding)
    show(java_linear_search, 'white')

    selectText(java_linear_search[0])
    for i in range(len(rec_list)):
        rec_list[i].color(Color('blue'))
        selectText(java_linear_search[1])
        if i == finding:
            rec_list[i].color(Color('green'))
            selectText(java_linear_search[2])
            found_test = True
            break

        rec_list[i].color(Color('gray'))
    if not found_test:
        selectText(java_linear_search[3])
    linear_explanation()


def binary_search():
    print('type a number between 0 - ', len(rec_list) - 1)
    finding = int(input())
    found_test = False

    description_text(finding)
    show(java_binary_search, 'white')

    low = 0
    selectText(java_binary_search[0])

    high = len(rec_list) - 1
    selectText(java_binary_search[1])
    while low <= high:
        selectText(java_binary_search[2])

        mid = int((low + high) / 2)
        rec_list[mid].color(Color('blue'))
        selectText(java_binary_search[3])

        selectText(java_binary_search[4])
        if mid > finding:
            high = mid - 1
            rec_list[mid].color(Color('gray'))
            selectText(java_binary_search[5])
        else:
            selectText(java_binary_search[6])
            if mid < finding:
                low = mid + 1
                rec_list[mid].color(Color('gray'))
                selectText(java_binary_search[7])
            else:
                selectText(java_binary_search[8])

                rec_list[mid].color(Color('green'))
                selectText(java_binary_search[9])
                found_test = True
                break
    if not found_test:
        selectText(java_binary_search[10])
    binary_explanation()


def selectText(text):
    text.color(Color("green"))
    time.sleep(3)
    text.color(Color("white"))


def binary_explanation():
    screen.clear()
    explanation = Text(screen, 'Advantages: It is very quick '
                               '\n'
                               '\nDisadvantages: The list has to be sorted', screen.width() / 2, screen.height() / 2,
                       Color('white'), size=20)
    explanation.move(-explanation.width() / 2, -explanation.height() / 2)
    time.sleep(7)
    screen.clear()


def linear_explanation():
    screen.clear()
    explanation = Text(screen, 'Advantages: The list does not have to be sorted'
                               '\n                   Faster for short or medium sized list'
                               '\n                   Not affected by insertion or deletion'
                               '\nDisadvantages: Slow search for longer lists', screen.width() / 2, screen.height() / 2,
                       Color('white'), size=20)
    explanation.move(-200, 0)
    time.sleep(7)
    screen.clear()


def keydown(key):
    if key == 'up':
        graphics()
        binary_search()
        setup()
    elif key == 'down':
        graphics()
        linear_search()
        setup()


fps = 30
running = True
setup()
while running:
    screen.update()
    screen.listen()
    screen.sleep(1 / fps)

screen.exit()

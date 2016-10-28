from input import *
from matrix import *
from output import *


def get_shingle_size():
    while True:
        try:
            shingle_size = int(input('> Choose the size of a shingle : '))
        except ValueError:
            print('Error : The value is not correct')
            continue
        else:
            if shingle_size < 1:
                print('Error : The value is not correct')
                continue
            else:
                break
    return shingle_size


def get_shingles(shingle_size):
    shingles = []
    i = 1
    infos = []

    print('Write DONE for validating all URLs')
    print('Example : http://www.google.fr')
    while True:
        user_input = input('> URL address ' + str(i) + ' : ')

        if user_input == 'DONE':
            if len(shingles) > 1:
                break
            else:
                print('ERROR: You have to choose at least 2 URLs')
                continue

        content, code = get_content(user_input)
        if code == 200:
            infos.append('Page ' + str(i) + ' : ' + user_input)
            i += 1
            shingles.append(create_shingles(content, shingle_size))
        else:
            print(content)
            continue

    return shingles, infos


def main():
    shingle_size = get_shingle_size()
    print()
    shingles, infos = get_shingles(shingle_size)
    matrix = generate_matrix(shingles)
    output_csv(matrix)
    output_html(matrix, infos, shingle_size)

main()

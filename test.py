def main():

    string = '56756'

    if len(string) % 2 == 0:
        split = int(len(string)/2)
        if len(set([string[:split], string[int(len(string)/2):]])) == 1:
            print('yes')
        else:
            print('no: uneven')
    else:
        print('no: not divisible')

if __name__ == '__main__':
    main()
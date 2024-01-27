cabin_class = input(
    f'Enter the Cabin Class for which you need details \n- LUX\n- A\n- B\n- C\nChoose from the above options: ').upper()

if cabin_class == 'LUX':
    print('LUX: Upper-deck with a balcony')
elif cabin_class == 'A':
    print('A: Above the car deck, equipped with a window')
elif cabin_class == 'B':
    print('B: Windowless cabin above the car deck.')
elif cabin_class == 'C':
    print('C: Windowless cabin below the car deck.')
else:
    print('Invalid cabin class.')

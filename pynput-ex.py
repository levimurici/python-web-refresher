from pynput.keyboard import Key, Listener
filename = 'key_log.txt'

def show(key):
    f = open(filename, 'a')

    if key == Key.right:
        print('You Entered {0}'.format( key))
        f.write('Tá funfando pae\n')
    elif key == Key.left:
        print('You Entered {0}'.format( key))
        f.write('Tá funfando demais pae\n')

    if key == Key.delete:
        # Stop listener
        return False
    f.close()

with Listener(on_press = show) as listener:   
    listener.join()
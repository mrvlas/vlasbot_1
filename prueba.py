from tkinter import Tk

def on_press(event):
    #print('on_press: event:', event)
    #print('on_press: keysym:', event.keysym)
    print('pressed',format(event.keysym))

def on_release(event):
    #print('on_release: event:', event)
    #print('on_release: keysym:', event.keysym)
    print('{0} release'.format(event.keysym))

    if event.keysym == 'Escape':
         print("exist program")
         root.destroy()

root = Tk()

root.bind('<KeyPress>', on_press)
root.bind('<KeyRelease>', on_release)

root.mainloop()
import PySimpleGUI as sg


right_click_menu = ['', ['Copy', 'Paste', 'Select All', 'Cut']]


mls = sg.Multiline(size=(60,20), key='-INPUT-', right_click_menu=right_click_menu)

menu_def = [
                ['&File', ['Open', 'Save', '&Properties', 'E&xit']],
                ['&Edit', ['&Paste', ['Special', 'Normal', ], 'Clear', 'Options::this_is_a_menu_key'], ],
                ['&Help', ['&About']]
                ]

def opens():
    file = sg.popup_get_file('Select a file')
    print(file)
    fl = open(file)
    txt = fl.read()
    window['-INPUT-'].Update(value=txt)

def do_clipboard_operation(event, window, element):
    if event == 'Select All':
        element.Widget.selection_clear()
        element.Widget.tag_add('sel', '1.0', 'end')
        
    elif event == 'Copy':
        try:
            text = element.Widget.selection_get()
            window.TKroot.clipboard_clear()
            window.TKroot.clipboard_append(text)
        except:
            print('Nothing selected')
    elif event == 'Paste':
        element.Widget.insert(sg.tk.INSERT, window.TKroot.clipboard_get())

    elif event == 'Cut':
        try:
            text = element.Widget.selection_get()
            window.TKroot.clipboard_clear()
            window.TKroot.clipboard_append(text)
            element.update('')
        except:
            print('Nothing selected')

def main():
    layout = [
                [sg.Menu(menu_def, tearoff=True, font='_ 12', key='-MENUBAR-')],
                [sg.Text('Write Everything..')],
                [mls],
                ]

    window = sg.Window('NotePad', layout)



    mline:sg.Multiline = window['-INPUT-']

    while True:
        event, values = window.read()       # type: (str, dict)
        if event in (sg.WIN_CLOSED, 'Exit'):
            break
        # save & brouse
        if event == 'Save':
            fs = sg.popup_get_file('Select a file')
            print("done")
            fm = mls.get()
            file = open(fs, "w")
            print('yess')
            file.write(fm)
            file.close()
            if event == sg.WIN_CLOSED or event == 'Exit':
                break
        if event == 'About':
            window.disappear()
            sg.popup('About this program', 'Version 1.0', 'Devoloped by Raghul Seeliyur')
            window.reappear()
        if event == 'Clear':
            txt = ""
            window['-INPUT-'].Update(value=txt)
            
        if event == 'Open':
            fs = sg.popup_get_file('Select a file')
            print("done")
            file = open(fs)
            print('yess')
            txt = file.read()
            window['-INPUT-'].Update(value=txt)

            if event == sg.WIN_CLOSED or event == 'Exit':
                break

        # if event is a right click menu for the multiline, then handle the event in func
        if event in right_click_menu[1]:
            do_clipboard_operation(event, window, mline)

                
    window.close()

if __name__ == '__main__':
    main()

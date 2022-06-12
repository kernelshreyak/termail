import urwid
from core.scraper import *

choices = ["View Inbox","Send Email","Exit"]

def menu(title, choices):
    body = [urwid.Text(title), urwid.Divider()]
    for c in choices:
        button = urwid.Button(c)
        urwid.connect_signal(button, 'click', item_chosen, c)
        body.append(urwid.AttrMap(button, None, focus_map='reversed'))
    return urwid.ListBox(urwid.SimpleFocusListWalker(body))

def item_chosen(button, choice):
    if choice == "Exit":
        exit_program()
        return

    elif choice == choices[0]:  ## view inbox
        emails = read_inbox("termail_001")

        inboxheader = urwid.Text([u'Inbox'])
        email_disp = [inboxheader]
        for email in emails:
            email_disp.append(urwid.AttrMap(urwid.Button(email), None, focus_map='reversed'))
        
        back_button = urwid.Button('Exit')
        urwid.connect_signal(back_button, 'click', back_to_mainmenu )
        email_disp.append(urwid.AttrMap(back_button, None, focus_map='reversed'))  

        main.original_widget = urwid.Filler(urwid.Pile(email_disp))


    elif choice == choices[1]:  ## send email
        # TODO: in a new window, show form to create email
        pass

def back_to_mainmenu(button):
    main.original_widget =  urwid.Overlay(urwid.Padding(menu(u'Termail v1.0', choices), left=2, right=2), 
        urwid.SolidFill(u'\N{MEDIUM SHADE}'),
        align='center',width=180,height=90,
        valign='middle',
        min_width=20, min_height=9)

def exit_program():
    raise urwid.ExitMainLoop()

main = urwid.Padding(menu(u'Termail v1.0', choices), left=2, right=2)
top = urwid.Overlay(main, urwid.SolidFill(u'\N{MEDIUM SHADE}'),
    align='center', width=('relative', 180),
    valign='middle', height=('relative', 90),
    min_width=20, min_height=9)

urwid.MainLoop(top, palette=[('reversed', 'standout', '')]).run()
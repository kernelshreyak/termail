import urwid

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
        # TODO: show emails from inbox
        pass

    elif choice == choices[1]:  ## send email
        # TODO: in a new window, show form to create email
        pass


def exit_program():
    raise urwid.ExitMainLoop()

main = urwid.Padding(menu(u'Termail v1.0', choices), left=2, right=2)
top = urwid.Overlay(main, urwid.SolidFill(u'\N{MEDIUM SHADE}'),
    align='center', width=('relative', 180),
    valign='middle', height=('relative', 90),
    min_width=20, min_height=9)
urwid.MainLoop(top, palette=[('reversed', 'standout', '')]).run()
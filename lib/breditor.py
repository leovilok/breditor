# Requires Brython and Ace editor

from browser import document, window, html
from sys import stderr

def exec_code(editor, id):
    stderr_frame = document[id + "_stderr"]
    stderr_frame.clear()
    stderr.write = lambda data : stderr_target(data, stderr_frame)
    exec(editor.getValue())

def stderr_target(data, elt):
    elt <= data

breditors = document.select(".breditor")

for ed_elt in breditors:
    editor = window.ace.edit(ed_elt.id)
    editor.session.setMode("ace/mode/python")
    #editor.setOption('fontSize', '14px')
    editor.setOption('maxLines', 5)

    stderr_frame = html.PRE(Class="stderr")
    stderr_frame.id = ed_elt.id + "_stderr"

    ed_elt.insertAdjacentElement('afterend', stderr_frame)

    exec_button = html.BUTTON("Exécuter →")
    exec_button.bind("click", lambda ev : exec_code(editor, ed_elt.id))
    ed_elt.insertAdjacentElement('afterend', exec_button)


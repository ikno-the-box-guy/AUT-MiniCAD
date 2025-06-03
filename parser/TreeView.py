import tkinter as tk
from tkinter import ttk
from antlr4 import *


def build_treeview(tree, rule_names):
    def insert_node(parent, node):
        if isinstance(node, TerminalNode):
            label = node.getText()
        else:
            label = rule_names[node.getRuleIndex()]

        item_id = treeview.insert(parent, 'end', text=label)

        for i in range(node.getChildCount()):
            insert_node(item_id, node.getChild(i))

    root = tk.Tk()
    root.title("ANTLR Parse Tree")

    treeview = ttk.Treeview(root)
    treeview.pack(fill='both', expand=True)

    insert_node('', tree)  # start from root

    root.mainloop()

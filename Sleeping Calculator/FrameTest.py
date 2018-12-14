def __init__(self, parent, expanded_text="Collapse <<", collapsed_text="Expand >>", *args):
        ttk.Frame.__init__(self, parent, *args)
        self.parent = parent
        self._expanded_text = expanded_text
        self._collapsed_text = collapsed_text

        self.columnconfigure(1, weight=1)

        self._variable = tk.IntVar()
        self._button = ttk.Checkbutton(self, variable=self._variable, command=self._activate, style="TButton")
        self._button.grid(row=0, column=0)

        self._separator = ttk.Separator(self, orient="horizontal")
        self._separator.grid(row=0, column=1, sticky="we")

        self.frame = ttk.Frame(self)

        self._activate() 
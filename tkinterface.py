from interpreter import Interpreter
from tkinter import Tk, Label, Button, Entry, filedialog
import plotly.graph_objs as go
from plotly.offline import plot

class SimpleInterface:

    def __init__(self, master):
        self.input = ""
        self.output = ""
        self.switch = {
            "output": "self.select_output()",
            "input": "self.select_input()",
            "interpret": "self.interpret()",
            "default": "self.default()",
            "exit": "self.exit()"
        }

        self.master = master
        master.title("PlantUML to Python converter")

        self.entered_command = ''
        self.message_label = Label(master, text="Enter a command below")
        self.message_label.pack()

        self.e = Entry(master)
        self.e.pack()

        self.output_label = Label(master, text="")
        self.output_label.pack()

        self.enter_button = Button(master, text='Run', command=self.run)
        self.enter_button.pack(side="left")

    def exit(self):
        self.master.destroy()

    def run(self):
        value = self.e.get()
        print(value)
        command = self.switch.get(value, "")
        if command == "":
            message = "this is not a recognised command \n type \"help\" for a list of commands"
            self.output_label['text'] = message
            print(message)
        else:
            eval(command)

    def default(self):
        message = "enter a command or type \'Help\'"
        print(message)
        return message

    def select_output(self):
        self.output = filedialog.askdirectory()
        self.output_label['text'] = self.output
        print(self.output)
        return self.output

    def select_input(self):
        self.input = filedialog.askopenfilename(initialdir="/", title="Select file")
        self.output_label['text'] = self.input
        print(self.input)
        return self.input

    def interpret(self):
        if self.output == "" or self.input == "":
            message = "missing input file or output directory"
            self.output_label['text'] = message
            print(message)
        else:
            i = Interpreter()
            i.add_file(self.input, self.output)
            i.write_modules()
            if len(i.all_my_errors) > 0:
                error_message = ""
                for an_error in i.all_my_errors:
                    error_message + "\n" + an_error
                print(error_message)
                self.output_label['text'] = error_message

            print("interpreter finished")
            print("printing graph")
            self.make_graph(i)

    def make_graph(self, interpreter): # not working
        trace0 = go.Bar(
            x=["Modules", "Classes", "Errors"],
            y=[len(interpreter.all_my_modules), len(interpreter.all_my_classbuilders), len(interpreter.all_my_errors)],
            marker=dict(
                color='rgb(158,202,225)',
                line=dict(
                    color='rgb(8,48,107)',
                    width=1.5,
                )
            ),
            opacity=0.6
        )
        data = [trace0]
        layout = go.Layout(
            title='Interpreter count of modules classes and errors',
            xaxis=go.layout.XAxis(
                title=go.layout.xaxis.Title(
                    text='Category',
                    font=dict(
                        family='Courier New, monospace',
                        size=18,
                        color='#7f7f7f'
                    )
                )
            ),
            yaxis=go.layout.YAxis(
                title=go.layout.yaxis.Title(
                    text='Number of Category',
                    font=dict(
                        family='Courier New, monospace',
                        size=18,
                        color='#7f7f7f'
                    )
                )
            )
        )

        fig = go.Figure(data=data, layout=layout)
        plot(fig, filename='interpreterGraph.html')


if __name__ == '__main__':
    root = Tk()
    my_gui = SimpleInterface(root)
    root.mainloop()

from interpreter import Interpreter
import sys
import cmd
import os
from plotly.offline import plot
import plotly.graph_objs as go


class Main(cmd.Cmd):
    prompt = ">>>"
    input = ''
    output = ''
    my_interpreter = Interpreter()
    def cmdloop(self, intro="PlantUML to Python Convertor"):
        return cmd.Cmd.cmdloop(self, intro)

    def do_input(self, line):
        # self.check_file(self.input)
        self.input = line
        print(self.input)

    def do_output(self, line):
        if os.path.exists(line):
            self.output = line
            print(f"the directory that interpreter will output to is {self.output}")
        else:
            print('that directory is invalid')

    def do_interpret(self, line):
        if self.output == '' or self.input == '':
            print("missing input file or output directory")
        else:
            self.my_interpreter.add_file(self.input, self.output)
            self.my_interpreter.write_modules()
            if len(self.my_interpreter.all_my_errors) > 0:
                error_message = ""
                for an_error in self.my_interpreter.all_my_errors:
                    error_message += "\n" + an_error
                print(error_message)
            print("interpreter finished")
            print("printing graph")
            self.print_graph(self.my_interpreter)

    def print_graph(self, interpreter):
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

    def do_pickle(self, line):
        if self.output == '' or self.input == '':
            print("missing input file or output directory for interpreter")
        else:
            try:
                self.my_interpreter.add_file(self.input, self.output)
                self.my_interpreter.pickle_modules(line)
            except FileNotFoundError:
                print("Error - file not found. this command requires an output file, type pickle filename.pickle")

    def do_unpickle(self, line):
        if os.path.isfile(line):
            self.my_interpreter.unpickle_modules(line)

        else:
            print('enter a file to unpickle')

    def emptyline(self, line):
        print('please enter a command or type help')

    def default(self, line):
        print('not a command, please type a valid command or type help')

    def do_quit(self, line):
        print("interpreter closing")
        return True

    # ========================================================
    # check borrowed from Sarahs controller

    def check_file(self, line):
        try:
            with open(self.input, "rt") as my_file:
                if my_file.read().find("@startuml") != -1:
                    print(f"Source file to interpret is: {line}")
                    self.input = line
                else:
                    print("Error - File must contain plant UML")
        except FileNotFoundError:
            print("Error - File not found")
            print(f"looking for file at {self.input}")
        except Exception as e:
            print(e)

    def help_input(self, line):
        print('select a plantUML file to interpret, enter the whole path')
        print('input directory/filename')

    def help_output(self, line):
        print('select a directory root to write the output files to')
        print('output directory')

    def help_interpret(self, line):
        print('run the interpreter')
        print('interpret')

    def help_pickle(self, line):
        print('stores the module object in a pickle file')
        print('pickle file.pickle')

    def help_quit(self, line):
        print('quits the command line')
        print('quit')


if __name__ == '__main__':
    if len(sys.argv) == 3:
        folder_output = sys.argv[1]
        file_input = sys.argv[2]

        if os.path.isfile(file_input):
            x = Interpreter()
            x.add_file(source_file, root_directory)
            x.write_modules()
        else:
            print('second argument must be a txt file')
        if not os.path.exists(folder_output):
            print('third argument must be a valid folder')
    elif len(sys.argv) > 3 or len(sys.argv) == 2:
            print('Error - please either enter a single command or interpret followed by output folder and input file')
    else:
        Main().cmdloop()

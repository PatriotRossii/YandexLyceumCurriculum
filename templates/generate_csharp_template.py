from templates.template import Template

class CSharpTemplate(Template):
    def create_template(self, filename):
        f = open(filename + ".cs", "w")

        text = """using System;namespace Solution {\n\tclass Program {\n\t\tstatic void Main() {\n\t\t\tConsole.WriteLine(\"Hello World!\");\nt\t\t}\n\t}\n}"""
        f.write(text)

        f.close()
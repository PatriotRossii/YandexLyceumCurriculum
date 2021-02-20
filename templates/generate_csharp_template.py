from templates.template import Template

class CSharpTemplate(Template):
    def create_template(self, filename):
        f = open(filename + ".cs", "w")

        text = """using System;\nnamespace Solution {\n\tclass Program {\n\t\tstatic void Main() {\n\t\t\tConsole.WriteLine(\"Hello World!\");\n\t\t}\n\t}\n}"""
        f.write(text)

        f.close()
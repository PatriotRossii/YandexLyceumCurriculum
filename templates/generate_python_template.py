from templates.template import Template

class PythonTemplate(Template):
    def create_template(self, filename):
        f = open(filename + ".py", "w")
        
        text = """print(\"Hello, World!\")"""
        f.write(text)

        f.close()
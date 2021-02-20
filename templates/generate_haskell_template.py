from templates.template import Template

class HaskellTemplate(Template):
    def create_template(self, filename):
        f = open(filename + ".hs", "w")

        text = """main = putStrLn \"Hello, World!\""""
        f.write(text)

        f.close()
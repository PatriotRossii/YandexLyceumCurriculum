import os
from templates.template import Template

class RustTemplate(Template):
    def create_template(self, filename):
        os.system(f"cargo init \"{filename}\" --vcs none")
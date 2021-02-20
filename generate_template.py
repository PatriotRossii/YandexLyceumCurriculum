from templates.generate_csharp_template import CSharpTemplate
from templates.generate_haskell_template import HaskellTemplate
from templates.generate_python_template import PythonTemplate
from templates.generate_rust_template import RustTemplate

import sys

path = sys.argv[1]
task_name = sys.argv[2]

CSharpTemplate(path + task_name + "/", "solution")
HaskellTemplate(path + task_name + "/", "solution")
PythonTemplate(path + task_name + "/", "solution")
RustTemplate(path + task_name + "/", "solution", True)
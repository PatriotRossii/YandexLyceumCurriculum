from templates.generate_csharp_template import CSharpTemplate
from templates.generate_haskell_template import HaskellTemplate
from templates.generate_python_template import PythonTemplate
from templates.generate_rust_template import RustTemplate

import sys

path = sys.argv[1]
filename = sys.argv[2]

CSharpTemplate(path, filename)
HaskellTemplate(path, filename)
PythonTemplate(path, filename)
RustTemplate(path, filename, True)
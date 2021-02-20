import os

class Template:
    def __init__(self, path, filename, path_only=False):
        self.path = path

        self.create_path(path)
        self.create_template(os.path.join(path, filename))
    
    def create_path(self, filename):
        print(os.path.dirname(filename))
        if not os.path.exists(os.path.dirname(filename)):
            try:
                os.makedirs(os.path.dirname(filename))
            except OSError as exc: # Guard against race condition
                if exc.errno != errno.EEXIST:
                    raise
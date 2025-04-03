from json import load, dump
class JsonFileHandler():
    def read_json_file(self, file):
        f = open(file ,mode="r" ,encoding="utf8")
        return load(f)
    
    def update_json_file(self, file, dict_for_update):
        f = open(file ,mode="w", encoding="utf8")
        dump(dict_for_update, f, indent=4, ensure_ascii = False)
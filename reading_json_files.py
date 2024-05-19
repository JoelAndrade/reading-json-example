import json

class rect:
    def __init__(self):
        with open("reading_json_files.json") as json_file:
            settings = json.load(json_file)

        length_list = [settings[f"{rect}"]["length"] for rect in settings]
        width_list  = [settings[f"{rect}"]["width"]  for rect in settings]

        self.height = [str(length) for length in length_list]
        self.width  = [str(width)  for width  in width_list]

        self.area = [length_list[i]*width_list[i] for i in range(len(length_list))]
    #
#

if (__name__ == "__main__"):
    my_rect = rect()
    print(my_rect.area)

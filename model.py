class Model:

    def __init__(self):
        self.__player_list = []

    @property
    def play_list(self):
        return self.__player_list

    def get_file_to_play(self, file_index):
        return self.__player_list[file_index]

    def clear_play_list(self):
        self.__player_list.clear()

    def add_to_play_list(self, file_name):
        self.__player_list.append(file_name)

    def remove_items_from_play_list_at_index(self, index):
        self.__player_list[index]


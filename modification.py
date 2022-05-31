import main


class Modifier:

    def __init__(self, add, remove, update, max_items, max_keys):
        self.add = add
        self.remove = remove
        self.update = update
        self.max_items = max_items
        self.max_keys = max_keys
        # self.dataset =
        # how to add existing dataset here?? __main__

    def add_key(self, column):
        pass

    def add_item(self, row):
        if len(self.dataset) < self.max_items:
            self.dataset.append(row)
            return True
        return False

    def remove_key(self, column):
        pass

    def remove_item(self, row):
        pass

    def update_key(self, column):
        pass

    def update_item(self, row):
        pass


if __name__ == '__main__':
    modifier = Modifier()
    modifiers = {
        "1": modifier.add_key,
        "2": modifier.add_item,
        "3": modifier.remove_key,
        "4": modifier.remove_item,
        "5": modifier.update_key,
        "6": modifier.update_item,
    }
    while True:
        print("Choose a modifier:")

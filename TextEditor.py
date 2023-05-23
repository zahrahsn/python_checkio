import copy
class Text:
    def __init__(self):
        self.text = ""
        self.font = ""

    def write(self, text):
        self.text += text

    def set_font(self, fontName):
        self.font = fontName

    def show(self):
        if len(self.font)>0:
            return f'[{self.font}]{self.text}[{self.font}]'
        else:
            return self.text

    def restore(self, text):
        self.text = text.text
        self.font = text.font


class SavedText:
    def __init__(self):
        self.versions = []

    def save_text(self, text: Text):
        self.versions.append(copy.copy(text))

    def get_version(self, n):
        return self.versions[n]


if __name__ == '__main__':
    # These "asserts" using only for self-checking and not necessary for auto-testing

    text = Text()
    saver = SavedText()

    text.write("At the very beginning ")
    saver.save_text(text)
    text.set_font("Arial")
    saver.save_text(text)
    text.write("there was nothing.")

    assert text.show(
    ) == "[Arial]At the very beginning there was nothing.[Arial]"

    text.restore(saver.get_version(0))
    assert text.show() == "At the very beginning "

    print("Coding complete? Let's try tests!")

from .widget import Widget

class Textbox(Widget):
    def is_clickable(self):
        return self.enabled and self.visible

    def enter_text(self, text:str):
        if self.is_clickable():
            self.click()
            self.element.send_keys(text)

        else:
            print(f"[Button] Button {self.by_locator} is not clickable.")

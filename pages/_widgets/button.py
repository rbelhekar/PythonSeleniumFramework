from .widget import Widget

class Button(Widget):
    def is_clickable(self):
        return self.enabled and self.visible

    def click_if_enabled(self):
        if self.is_clickable():
            self.click()
        else:
            print(f"[Button] Button {self.by_locator} is not clickable.")

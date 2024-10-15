import flet as ft


class taskControl(ft.Checkbox):
  def __init__(self, label_text):
    super().__init__()
    self.label = label_text
    self.on_change = self.taskDone

  def taskDone(self, e):
    if self.value:
      self.label_style = ft.TextStyle(
        decoration=ft.TextDecoration.LINE_THROUGH)
    else:
      self.label_style = ft.TextStyle(
        decoration=ft.TextDecoration.NONE)
    self.update()

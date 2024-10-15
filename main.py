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

def main(page: ft.Page):
  page.title = "To-Do App"  # Page title

  input_text = ft.TextField(
    hint_text="What do you want to do today...")  # input from the
  
  def button_clicked(e):
    if input_text.value != "":
      page.add(
        taskControl(input_text.value)
      )
      input_text.value = ""
      page.update()
      
  page.appbar = ft.AppBar(
    title=ft.Text("To-Do List"),
    center_title=True
  )

  # aligning the input text and button in a row
  page.add(
    ft.Row(
      [
        input_text,
        ft.ElevatedButton(text="Add", on_click=button_clicked)
      ]
    )
  )


ft.app(target=main)

import flet as ft
from taskControl import taskControl


def main(page: ft.Page):
  page.title = "To-Do App"  # Page title

  input_text = ft.TextField(
    hint_text="What do you want to do today...", width=350)  # input from the
  
  def button_clicked(e):
    if input_text.value != "":
      page.add(
        # ft.Checkbox(label=input_text.value,value=False) 
        taskControl(input_text.value)
      )
      input_text.value = ""
      page.update()

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

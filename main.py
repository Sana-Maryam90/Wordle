import tkinter as tk
import random
from PIL import Image, ImageTk

count = 0

words_list = ["abuse", "throw", "south", "other", "crowd", "dream", "likes", "taste", "avoid", "where", "brave",
              "after", "earth"]
window = tk.Tk()
# creating a menu bar
menu_bar = tk.Menu(window)
window.config(menu=menu_bar)
window.title("Wordle")


# that function delete the label on the rules
def forget_rules(rule1, rule2, rule3, rule4, rule5, button):
    rule1.forget()
    rule2.forget()
    rule3.forget()
    rule4.forget()
    rule5.forget()
    button.forget()
    menu_bar.entryconfig("Play", state="normal")


# that function describe the rules of tha game
def display_rules():
    rule1 = tk.Label(window, text="rule 1 : you can only choose 5 letter words", padx=10, pady=10)
    rule2 = tk.Label(window,
                     text="rule 2: If one of the letter is in the word but not the right place it would be highlighted in orange",
                     padx=10, pady=10)
    rule3 = tk.Label(window,
                     text="rule 3 : If one of the letter is in the word and at the right place it will be highlighted "
                          "in green .", padx=10, pady=10)
    rule4 = tk.Label(window, text="rule 4 : If the letter is not in the word it will be highlighted in grey.", padx=10,
                     pady=10)
    rule5 = tk.Label(window, text="rule 5: There are no difference between uppercase nd lowercase letter", padx=10,
                     pady=10)

    rule1.pack()
    rule2.pack()
    rule3.pack()
    rule4.pack()
    rule5.pack()
    button = tk.Button(window, text="understand",
                       command=lambda: forget_rules(rule1, rule2, rule3, rule4, rule5, button))
    button.pack()


# this function choose a random word from the word list given
def word_chosen(word_list):
    chosen_word = random.choice(word_list)
    character = []
    for word in chosen_word:
        character.append(word)
    return character


# need to sort this out
def counting():
    global count
    count += 1
    print(count)
    return count


def colors(entry, character, number):
    color = "nothing"
    if entry.get().lower() == character[number]:
        entry.configure(bg="green")
        color = "green"
    elif entry.get().lower() in character:
        entry.configure(bg="yellow")
        color = "yellow"
    else:
        entry.configure(bg="grey")
        color = "grey"
    return color


# character = word_chosen(words_list)


# so far this function just set a 5 textbox for x and y .
# if someone can sort how to define each box that will be helpful
def game_setting():
    global count
    count = 0
    character = word_chosen(words_list)
    entry1 = tk.Entry(width=10)
    entry1.grid(row=0, column=0, padx=20, pady=20)
    entry2 = tk.Entry(width=10)
    entry2.grid(row=0, column=1, padx=20, pady=20)
    entry3 = tk.Entry(width=10)
    entry3.grid(row=0, column=2, padx=20, pady=20)
    entry4 = tk.Entry(width=10)
    entry4.grid(row=0, column=3, padx=20, pady=20)
    entry5 = tk.Entry(width=10)
    entry5.grid(row=0, column=4, padx=20, pady=20)
    entry6 = tk.Entry(width=10)
    entry6.grid(row=1, column=0, padx=20, pady=20)
    entry7 = tk.Entry(width=10)
    entry7.grid(row=1, column=1, padx=20, pady=20)
    entry8 = tk.Entry(width=10)
    entry8.grid(row=1, column=2, padx=20, pady=20)
    entry9 = tk.Entry(width=10)
    entry9.grid(row=1, column=3, padx=20, pady=20)
    entry10 = tk.Entry(width=10)
    entry10.grid(row=1, column=4, padx=20, pady=20)
    entry11 = tk.Entry(width=10)
    entry11.grid(row=2, column=0, padx=20, pady=20)
    entry12 = tk.Entry(width=10)
    entry12.grid(row=2, column=1, padx=20, pady=20)
    entry13 = tk.Entry(width=10)
    entry13.grid(row=2, column=2, padx=20, pady=20)
    entry14 = tk.Entry(width=10)
    entry14.grid(row=2, column=3, padx=20, pady=20)
    entry15 = tk.Entry(width=10)
    entry15.grid(row=2, column=4, padx=20, pady=20)
    entry16 = tk.Entry(width=10)
    entry16.grid(row=3, column=0, padx=20, pady=20)
    entry17 = tk.Entry(width=10)
    entry17.grid(row=3, column=1, padx=20, pady=20)
    entry18 = tk.Entry(width=10)
    entry18.grid(row=3, column=2, padx=20, pady=20)
    entry19 = tk.Entry(width=10)
    entry19.grid(row=3, column=3, padx=20, pady=20)
    entry20 = tk.Entry(width=10)
    entry20.grid(row=3, column=4, padx=20, pady=20)
    entry21 = tk.Entry(width=10)
    entry21.grid(row=4, column=0, padx=20, pady=20)
    entry22 = tk.Entry(width=10)
    entry22.grid(row=4, column=1, padx=20, pady=20)
    entry23 = tk.Entry(width=10)
    entry23.grid(row=4, column=2, padx=20, pady=20)
    entry24 = tk.Entry(width=10)
    entry24.grid(row=4, column=3, padx=20, pady=20)
    entry25 = tk.Entry(width=10)
    entry25.grid(row=4, column=4, padx=20, pady=20)

    button = tk.Button(window, text="submit", command=lambda: [
        answer_checking(entry1, entry2, entry3, entry4, entry5, entry6, entry7, entry8, entry9, entry10, entry11,
                        entry12, entry13, entry14, entry15, entry16, entry17, entry18, entry19, entry20, entry21,
                        entry22, entry23, entry24, entry25, button, character), counting()])
    button.grid(row=5, column=2)


def delete_grid(entry1, entry2, entry3, entry4, entry5, entry6, entry7, entry8, entry9, entry10, entry11, entry12,
                entry13, entry14, entry15, entry16, entry17, entry18, entry19, entry20, entry21, entry22, entry23,
                entry24, entry25, button):
    entry1.grid_forget()
    entry2.grid_forget()
    entry3.grid_forget()
    entry4.grid_forget()
    entry5.grid_forget()
    entry6.grid_forget()
    entry7.grid_forget()
    entry8.grid_forget()
    entry9.grid_forget()
    entry10.grid_forget()
    entry11.grid_forget()
    entry12.grid_forget()
    entry13.grid_forget()
    entry14.grid_forget()
    entry15.grid_forget()
    entry16.grid_forget()
    entry17.grid_forget()
    entry18.grid_forget()
    entry19.grid_forget()
    entry20.grid_forget()
    entry21.grid_forget()
    entry22.grid_forget()
    entry23.grid_forget()
    entry24.grid_forget()
    entry25.grid_forget()
    button.grid_forget()


def all_same(items):
    return all(x == items[0] for x in items)


def loosing_window():
    loose = tk.Label(window, text=" You loose !!", font=20)
    loose.grid(row=0, column=2)
    image = Image.open('loosing_image.gif')
    image1 = ImageTk.PhotoImage(image)
    label_image = tk.Label(image=image1)
    label_image.image = image1
    label_image.grid(row=2, column=2)
    button = tk.Button(window, text="replay",
                       command=lambda: [ending_delete(loose, label_image, button), game_setting()])
    button.grid(row=3, column=2)


def winning_window():
    win = tk.Label(window, text=" You win !!", font=20)
    win.grid(row=0, column=2)
    image = Image.open('winning_image.gif')
    image1 = ImageTk.PhotoImage(image)
    label_image = tk.Label(image=image1)
    label_image.image = image1
    label_image.grid(row=2, column=2)

    button = tk.Button(window, text="replay", command=lambda: [ending_delete(win, label_image, button), game_setting()])
    button.grid(row=3, column=2)

def replay (win ,label_image , button):
    ending_delete(win, label_image, button )
    count = 0
    game_setting()

def ending_delete(label, label_image, button):
    label.grid_forget()
    label_image.grid_forget()
    button.grid_forget()



def answer_checking(entry1, entry2, entry3, entry4, entry5, entry6, entry7, entry8, entry9, entry10, entry11, entry12,
                    entry13, entry14, entry15, entry16, entry17, entry18, entry19, entry20, entry21, entry22, entry23,
                    entry24, entry25, button, character):
    print(character)
    color_list = []
    if count == 0:
        color_list.append(colors(entry1, character, 0))
        color_list.append(colors(entry2, character, 1))
        color_list.append(colors(entry3, character, 2))
        color_list.append(colors(entry4, character, 3))
        color_list.append(colors(entry5, character, 4))
        if all_same(color_list) == True and color_list[0] == "green":
            print("you win the game ")
            delete_grid(entry1, entry2, entry3, entry4, entry5, entry6, entry7, entry8, entry9, entry10, entry11,
                        entry12,
                        entry13, entry14, entry15, entry16, entry17, entry18, entry19, entry20, entry21, entry22,
                        entry23,
                        entry24, entry25, button)
            winning_window()


        else:
            color_list.clear()
            entry1.config(state="disabled", disabledbackground=colors(entry1, character, 0), disabledforeground="black")
            entry2.config(state="disabled", disabledbackground=colors(entry2, character, 1), disabledforeground="black")
            entry3.config(state="disabled", disabledbackground=colors(entry3, character, 2), disabledforeground="black")
            entry4.config(state="disabled", disabledbackground=colors(entry4, character, 3), disabledforeground="black")
            entry5.config(state="disabled", disabledbackground=colors(entry5, character, 4), disabledforeground="black")

        print(color_list)
    if count == 1:
        color_list.append(colors(entry6, character, 0))
        color_list.append(colors(entry7, character, 1))
        color_list.append(colors(entry8, character, 2))
        color_list.append(colors(entry9, character, 3))
        color_list.append(colors(entry10, character, 4))
        if all_same(color_list) == True and color_list[0] == "green":
            print("you win the game ")
            delete_grid(entry1, entry2, entry3, entry4, entry5, entry6, entry7, entry8, entry9, entry10, entry11,
                        entry12,
                        entry13, entry14, entry15, entry16, entry17, entry18, entry19, entry20, entry21, entry22,
                        entry23,
                        entry24, entry25, button)
            winning_window()

        else:
            color_list.clear()
            entry6.config(state="disabled", disabledbackground=colors(entry6, character, 0), disabledforeground="black")
            entry7.config(state="disabled", disabledbackground=colors(entry7, character, 1), disabledforeground="black")
            entry8.config(state="disabled", disabledbackground=colors(entry8, character, 2), disabledforeground="black")
            entry9.config(state="disabled", disabledbackground=colors(entry9, character, 3), disabledforeground="black")
            entry10.config(state="disabled", disabledbackground=colors(entry10, character, 4),
                           disabledforeground="black")

    if count == 2:
        color_list.append(colors(entry11, character, 0))
        color_list.append(colors(entry12, character, 1))
        color_list.append(colors(entry13, character, 2))
        color_list.append(colors(entry14, character, 3))
        color_list.append(colors(entry15, character, 4))
        if all_same(color_list) == True and color_list[0] == "green":
            print("you win the game ")
            print("you win the game ")
            delete_grid(entry1, entry2, entry3, entry4, entry5, entry6, entry7, entry8, entry9, entry10, entry11,
                        entry12,
                        entry13, entry14, entry15, entry16, entry17, entry18, entry19, entry20, entry21, entry22,
                        entry23,
                        entry24, entry25, button)
            winning_window()

        else:
            color_list.clear()
            entry11.config(state="disabled", disabledbackground=colors(entry11, character, 0),
                           disabledforeground="black")
            entry12.config(state="disabled", disabledbackground=colors(entry12, character, 1),
                           disabledforeground="black")
            entry13.config(state="disabled", disabledbackground=colors(entry13, character, 2),
                           disabledforeground="black")
            entry14.config(state="disabled", disabledbackground=colors(entry14, character, 3),
                           disabledforeground="black")
            entry15.config(state="disabled", disabledbackground=colors(entry15, character, 4),
                           disabledforeground="black")

    if count == 3:
        color_list.append(colors(entry16, character, 0))
        color_list.append(colors(entry17, character, 1))
        color_list.append(colors(entry18, character, 2))
        color_list.append(colors(entry19, character, 3))
        color_list.append(colors(entry20, character, 4))
        if all_same(color_list) == True and color_list[0] == "green":
            print("you win the game ")
            print("you win the game ")
            delete_grid(entry1, entry2, entry3, entry4, entry5, entry6, entry7, entry8, entry9, entry10, entry11,
                        entry12,
                        entry13, entry14, entry15, entry16, entry17, entry18, entry19, entry20, entry21, entry22,
                        entry23,
                        entry24, entry25, button)
            winning_window()

        else:
            color_list.clear()
            entry16.config(state="disabled", disabledbackground=colors(entry16, character, 0),
                           disabledforeground="black")
            entry17.config(state="disabled", disabledbackground=colors(entry17, character, 1),
                           disabledforeground="black")
            entry18.config(state="disabled", disabledbackground=colors(entry18, character, 2),
                           disabledforeground="black")
            entry19.config(state="disabled", disabledbackground=colors(entry19, character, 3),
                           disabledforeground="black")
            entry20.config(state="disabled", disabledbackground=colors(entry20, character, 4),
                           disabledforeground="black")
    if count == 4:
        color_list.append(colors(entry21, character, 0))
        color_list.append(colors(entry22, character, 1))
        color_list.append(colors(entry23, character, 2))
        color_list.append(colors(entry24, character, 3))
        color_list.append(colors(entry25, character, 4))
        if all_same(color_list) == True and color_list[0] == "green":
            print("you win the game ")
            delete_grid(entry1, entry2, entry3, entry4, entry5, entry6, entry7, entry8, entry9, entry10, entry11,
                        entry12,
                        entry13, entry14, entry15, entry16, entry17, entry18, entry19, entry20, entry21, entry22,
                        entry23,
                        entry24, entry25, button)
            winning_window()

        else:
            color_list.clear()
            entry21.config(state="disabled", disabledbackground=colors(entry21, character, 0),
                           disabledforeground="black")
            entry22.config(state="disabled", disabledbackground=colors(entry22, character, 1),
                           disabledforeground="black")
            entry23.config(state="disabled", disabledbackground=colors(entry23, character, 2),
                           disabledforeground="black")
            entry24.config(state="disabled", disabledbackground=colors(entry24, character, 3),
                           disabledforeground="black")
            entry25.config(state="disabled", disabledbackground=colors(entry25, character, 4),
                           disabledforeground="black")
    if count == 5:
        delete_grid(entry1, entry2, entry3, entry4, entry5, entry6, entry7, entry8, entry9, entry10, entry11, entry12,
                    entry13, entry14, entry15, entry16, entry17, entry18, entry19, entry20, entry21, entry22, entry23,
                    entry24, entry25, button)
        loosing_window()


file_menu = tk.Menu(menu_bar)

# add menu item in the menu
menu_bar.add_command(label="Rules", command=lambda: [display_rules(), menu_bar.entryconfig("Play", state="disabled")])
menu_bar.add_command(label="Exit", command=window.destroy)
menu_bar.add_command(label="Play", command=lambda: [game_setting(), menu_bar.entryconfig("Play", state="disabled")])

window.mainloop()
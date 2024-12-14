import random
import tkinter as tk
from tkinter import messagebox
from tkinter import ttk

def guess_number_game():
    number_to_guess = random.randint(1, 100)
    attempts = 0

    def on_guess():
        nonlocal attempts
        try:
            guess = int(entry.get())
            attempts += 1

            if guess < 1 or guess > 100:
                messagebox.showwarning("警告", "请确保你的猜测在1到100之间。")
                entry.delete(0, tk.END)
            else:
                if guess < number_to_guess:
                    if abs(guess - number_to_guess) < 10:
                        feedback_label.config(text="你离正确答案很近了，再稍微高一点。")
                    elif abs(guess - number_to_guess) < 20:
                        feedback_label.config(text="你离正确答案不远了，再高一点。")
                    else:
                        feedback_label.config(text="太低了，再试一次。")
                elif guess > number_to_guess:
                    if abs(guess - number_to_guess) < 10:
                        feedback_label.config(text="你离正确答案很近了，再稍微低一点。")
                    elif abs(guess - number_to_guess) < 20:
                        feedback_label.config(text="你离正确答案不远了，再低一点。")
                    else:
                        feedback_label.config(text="太高了，再试一次。")
                else:
                    messagebox.showinfo("恭喜", f"恭喜你！你猜对了数字是 {number_to_guess}。\n你总共猜了 {attempts} 次。")
                    root.destroy()
        except ValueError:
            messagebox.showwarning("警告", "请输入一个有效的整数。")

    def reset_game():
        nonlocal number_to_guess, attempts
        number_to_guess = random.randint(1, 100)
        attempts = 0
        entry.delete(0, tk.END)
        feedback_label.config(text="")
        messagebox.showinfo("游戏重置", "游戏已重置，开始新的一轮吧！")

    root = tk.Tk()
    root.title("猜数字游戏")
    root.geometry("400x250")

    style = ttk.Style()
    style.theme_use('clam')

    intro_label = ttk.Label(root, text="欢迎来到猜数字游戏！\n我已经想好了一个1到100之间的数字。", font=("Arial", 12))
    intro_label.pack(pady=20)

    entry_label = ttk.Label(root, text="请输入你的猜测：")
    entry_label.pack()

    entry = ttk.Entry(root, font=("Arial", 14))
    entry.pack(pady=10)

    guess_button = ttk.Button(root, text="猜！", command=on_guess)
    guess_button.pack(pady=10)

    feedback_label = ttk.Label(root, text="", font=("Arial", 10), foreground="blue")
    feedback_label.pack()

    reset_button = ttk.Button(root, text="重新开始", command=reset_game)
    reset_button.pack(pady=20)

    root.mainloop()

if __name__ == "__main__":
    guess_number_game()
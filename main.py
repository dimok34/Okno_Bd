import tkinter as tk
import psycopg2

def connect_baza(db_name, db_port, db_password, username):
    try:
        conn = psycopg2.connect(dbname=db_name, port=db_port, password=db_password, user=username)
        return conn
    except psycopg2.Error as e:
        print("Введены неверные данные")
        return None

def get_baza(conn):
    try:
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM users")
        rows = cursor.fetchall()
        return rows
    except psycopg2.Error as e:
        print("Введены неверные данные")
        return None

def show_data(rows):
    if rows is not None:
        # Создание нового окна для вывода данных
        data_window = tk.Toplevel()
        data_window.title("Результаты запроса")
        data_window.geometry("400x300")

        # Создание виджета Text для вывода данных
        data_text = tk.Text(data_window)
        data_text.pack()

        for row in rows:
            data_text.insert(tk.END, str(row) + "\n")

def start():
    root = tk.Tk()
    root.title("PostgreSQL")
    root.geometry("200x210")

    tk.Label(root, text="Название БД: ").pack()
    db_name_entry = tk.Entry(root)
    db_name_entry.pack()

    tk.Label(root, text="Порт БД: ").pack()
    db_port_entry = tk.Entry(root)
    db_port_entry.pack()

    tk.Label(root, text="Пароль БД: ").pack()
    db_password_entry = tk.Entry(root, show="*")
    db_password_entry.pack()

    tk.Label(root, text="Имя пользователя: ").pack()
    username_entry = tk.Entry(root)
    username_entry.pack()

    # Кнопка отображения
    show_button = tk.Button(root, text="Получить",
                            command=lambda: show_data(get_baza(connect_baza(db_name_entry.get(),
                                                                            db_port_entry.get(),
                                                                            db_password_entry.get(),
                                                                            username_entry.get()))))
    show_button.pack()

    root.mainloop()

start()

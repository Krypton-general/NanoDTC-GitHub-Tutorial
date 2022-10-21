from save import save_message

name = "Greg"
message = "You are all lazy!"

my_message = {"name": name, "message": message}

if __name__ == "__main__":
    save_message(my_message)

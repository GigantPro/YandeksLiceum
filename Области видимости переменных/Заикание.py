last_msg = ''


def print_without_duplicates(msg):
    global last_msg
    if last_msg != msg:
        last_msg = msg
        print(msg)

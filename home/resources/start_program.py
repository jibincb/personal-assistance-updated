from .speech import listen, process_query, listen_for_wake_word


def run():
    while True:
        while True:
            if listen_for_wake_word():
                break
        while True:
            query = listen()
            print(query)
            a = process_query(query)
            if(a):
                break

import threading

print("Current Thread: ", threading.current_thread().getName())

if threading.current_thread() == threading.main_thread():
    print("Main Thread")
else:
    print("Some Other Thread")

import threading

class IdleTimer:
    def __init__(self, timeout=60, callback=None):
        self.timeout = timeout
        self.callback = callback or self.default_callback
        self.timer = None

    def default_callback(self):
        print("Bot: Hey, are you there?")

    def reset(self):
        if self.timer:
            self.timer.cancel()
        self.timer = threading.Timer(self.timeout, self.callback)
        self.timer.start()

    def stop(self):
        if self.timer:
            self.timer.cancel()
            self.timer = None

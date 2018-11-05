
class Dispatcher:

    def __init__(self):
        pass

    def recieve_message(self, routing_key, body):
        print(routing_key)
        print(body)
        pass
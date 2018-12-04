class ClientInterface:

    def __init__(self, obj):
        self.obj = obj

    def close(self):
        self.obj.close()


class OurInterface:

    def close_db(self):
        print(f"I {self.__class__.__name__} close our DataBase")


class Adapter:

    def __init__(self, obj: OurInterface):
        self.__obj = obj

    def close(self):
        self.__obj.close_db()


if __name__ == "__main__":
    our_interface = OurInterface()
    adapter = Adapter(our_interface)

    client_interface = ClientInterface(adapter)

    client_interface.close()

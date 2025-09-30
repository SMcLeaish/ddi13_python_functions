from typing import Self


class SecretMessage:
    def __init__(self):
        self.msg: str = ""
        self.name: str = ""
        self.clean: str = ""

    def get_info(self) -> Self:
        self.msg = input("Enter your secret party message: ")
        self.name = input("Enter the guest's name: ")
        return self

    def cleaned(self) -> Self:
        self.clean = self.msg.strip()
        return self

    def upper(self) -> Self:
        self.clean = self.clean.upper()
        return self

    def reverse(self) -> Self:
        self.clean = " ".join(reversed(self.clean))
        return self

    def print_secret(self) -> None:
        print(f"Hey {self.name}, here's your secret code {secret}")

    @staticmethod
    def reverse_message(secret_message: "SecretMessage") -> str:
        secret_message.get_info().cleaned().upper().reverse()
        return secret_message.clean


secret = SecretMessage()
print(secret.reverse_message(secret))

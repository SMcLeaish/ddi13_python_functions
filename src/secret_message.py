from typing import Self
from dataclasses import dataclass


@dataclass(frozen=True, slots=True)
class SecretMessage:
    msg: str
    name: str
    clean: str

    @classmethod
    def create(cls, msg: str, name: str) -> Self:
        return cls(msg=msg, name=name, clean=msg.strip())

    def make_secret(self) -> str:
        return "".join(reversed(self.clean.upper()))


def get_info() -> tuple[str, str]:
    msg = input("Enter your secret party message: ")
    name = input("Enter the guest's name: ")
    return (msg, name)


def new_secret_message() -> str:
    msg, name = get_info()
    message = SecretMessage.create(msg, name)
    return message.make_secret()


print(new_secret_message())

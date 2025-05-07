from dataclasses import dataclass

@dataclass
class Cliente:
    Id: int
    Nome: str
    CPF: str
    Email: str
    Telefone: str
    Senha: str


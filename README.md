# 🏨 Projeto de Gestão de Hotel

Repositório do projeto desenvolvido para a disciplina **5605 - Desenvolvimento de Sistemas Orientados a Objetos**.

**Projeto com fins didáticos para praticar a modelagem orientada a objetos.**

---

## 🎯 Objetivo

Este sistema tem como objetivo modelar a estrutura de um hotel, permitindo o gerenciamento de hóspedes, quartos, reservas e funcionários, utilizando os conceitos de **programação orientada a objetos** como **herança**, **polimorfismo**, **abstração** e **encapsulamento**.

---

## 📦 Funcionalidades Modeladas

- Cadastro de hóspedes e funcionários
- Cadastro de quartos e seus tipos
- Criação e controle de reservas
- Cálculo do valor total da reserva
- Representação de serviços adicionais (opcional)
- Reaproveitamento de código com classes abstratas
---
## 🧱 Estrutura de Classes (Modelos)

### `Pessoa (abstract)`
- `nome: str`
- `cpf: str`
- `obter_tipo(): str` _(abstrato)_

### `Hospede (Pessoa)`
- `telefone: str`
- `email: str`

### `Funcionario (Pessoa)`
- `cargo: str`
- `salario: float`

### `Quarto`
- `numero: int`
- `tipo: str` (ex: "simples", "luxo")
- `preco_diaria: float`
- `disponivel: bool`

### `Reserva`
- `hospede: Hospede`
- `quarto: Quarto`
- `data_checkin: datetime`
- `data_checkout: datetime`
- `ativa: bool`
- `calcular_total(): float`

### `ServicoAdicional` _(opcional)_
- `nome: str`
- `preco: float`
---
## 🛠 Tecnologias

- Linguagem: **Python 3**
- Paradigma: **Orientação a Objetos**
- Sem dependências externas
- IDE: **PyCharm**
---
## 📚 Conceitos Aplicados

- Classes e objetos
- Herança e composição
- Classes abstratas e métodos abstratos (`abc`)
- Encapsulamento e coesão
- Boas práticas de modelagem
---

## 👨‍🏫 Disciplina

**5605 - Desenvolvimento de Sistemas Orientados a Objetos**  
Curso de Sistemas de Informação 

Universidade Federal de Santa Catarina - *UFSC*

Professores: *Thais Bardini Idalino, André Beims Bräscher*




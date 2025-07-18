# Simple Bank Simulator 🏦

A lightweight Python banking simulator that handles deposits, withdrawals, and statements with daily limits.

## Features ✨

- 💰 **Deposits**: Add funds to your account
- 🏧 **Withdrawals**: 
  - Daily limit: 3 withdrawals
  - Max per withdrawal: R$ 500.00
  - Balance protection
- 📜 **Statement**: View all transactions
- 🚪 **Exit**: Close the application

## How to Run ▶️

1. Clone the repository:
```bash
git clone https://github.com/yourusername/bank-simulator.git
```
2. Run the simulator:
```bash
cd bank-simulator
python bank_simulator.py
```
## Usage Example 📋
```bash
[1] Deposit
[2] Withdraw
[3] Statement
[4] Exit

=> 1
Deposit amount: R$ 1000

[1] Deposit
[2] Withdraw
[3] Statement
[4] Exit

=> 3

=========== STATEMENT ===========
Deposit: R$ 1000.00

Current balance: R$ 1000.00
Withdrawals today: 0/3
===============================
```

## Code Preview 👨‍💻

```bash
saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3

while True:
    opcao = input(menu)
    
    if opcao == "1":
        valor = float(input("Deposit amount: R$ "))
        if valor > 0:
            saldo += valor
            extrato += f"Deposit: R$ {valor:.2f}\n"
```

## Limitations ⚠️

No user authentication

No data persistence

Single account only

## License 📜

MIT License - Free to use and modify

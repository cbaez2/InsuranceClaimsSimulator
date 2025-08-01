# 📘 Insurance Claims Simulator (CLI Edition)

This command-line actuarial modeling tool simulates insurance claims, allowing the user to analyze how actual insurance payments deviate from expected claim payments, based on:

- The number of claims
- The insurance policy setup
- The claim distribution used

It calculates both the total actual insurance payment and the total expected claim payment, assuming claims are independent and identically distributed. The results include the percent error, difference, and margin of error.

---

## 🎯 Key Features

- Supports **6 continuous distributions**:
  - Uniform, Exponential, Gamma, Normal, Lognormal, Beta
- Configurable policy inputs:
  - Deductible
  - Policy Limit
  - Coinsurance Rate
- Applies actuarial validation logic:
  - Validates deductible and limit against claim distribution bounds.
  - Rescales the Beta distribution if policy inputs fall outside [0,1].
  - Detects edge cases (e.g., zero coinsurance, zero payments).
- Reports:
  - Total insurance payout
  - Expected claim payout (via numerical integration)
  - Difference between both
  - Percent error 
  - Margin of error on total expected payout

---

## 📦 Requirements

Install dependencies:
```
pip install -r requirements.txt
```

---

## ▶️ Run the simulator

```
python main.py
```

---

## 👤 Author

**Christopher Baez**  
Finance & Risk Management Major | Aspiring actuary  
Email: [chris_baez18@hotmail.com]  
GitHub: [https://github.com/cbaez2]

---

## 📜 License

This project is licensed under the **MIT License** — you are free to use, modify, and distribute it with proper attribution.

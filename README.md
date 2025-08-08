# 📘 Insurance Claims Simulator (CLI Edition)

This command-line actuarial modeling tool simulates insurance claims to perform an actual-to-expected (A/E) analysis on the insurance payments based on customizable inputs such as:

- The number of claims
- The insurance policy setup
- The claim distribution used

It calculates both the total actual insurance payment and the total expected claim payment, assuming claims are independent and identically distributed. The results include the percent error, difference, A/E ratio and margin of error.

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
  - A/E ratio
  - Margin of error on total expected payout
  
 ---

  ## 💻 Download Executable 

You can run this simulator **without installing Python**.

> [**Download Insurance Claim Simulator (.zip)**](https://github.com/cbaez2/InsuranceClaimsSimulator/releases/download/v1.0/InsuranceClaimsSimulator.zip)


- Unzip and run InsuranceClaimsSimulator.exe (may take a few seconds to start).
- If Windows shows a warning, click “More info” → “Run anyway.”
- This executable was built locally by the project author and contains no installers, ads, or trackers.

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

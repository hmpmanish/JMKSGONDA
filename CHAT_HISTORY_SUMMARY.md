# 🌾 JAYMANI KRISHI SEWA — Chat History & Project Command Cheat Sheet
> **Digital Agritech Marketplace, Subsidy Portal & Synchronized Bahi-Khata Ledger**  
> *B.Tech Computer Science Capstone Evaluation-3 Working Prototype*  
> **Authors:** Manish Pandey & Jayant Raj | **Mentor:** Prof. (Dr.) Ali Imam Abidi

---

## 🌐 1. Live Deployment & Repository URLs

| Resource | URL / Destination | Description |
| :--- | :--- | :--- |
| **Vercel Production (Primary)** | [https://jaymani.vercel.app/](https://jaymani.vercel.app/) | Official Live Evaluation-3 Cloud Deployment |
| **Vercel Production (Mirror)** | [https://jmksgonda.vercel.app/](https://jmksgonda.vercel.app/) | Secondary Aliased Domain |
| **GitHub Repository** | [https://github.com/hmpmanish/JMKSGONDA.git](https://github.com/hmpmanish/JMKSGONDA.git) | Main Repository (`origin/main`) |
| **Local Development** | [http://127.0.0.1:5000](http://127.0.0.1:5000) | Running on local machine port 5000 |
| **Live SeedTrace API** | [https://jaymani.vercel.app/api/seedtrace/verify/24-076000](https://jaymani.vercel.app/api/seedtrace/verify/24-076000) | Live Government Cross-Verification API |

---

## 🔑 2. Demo User Credentials (Email + Password Only)

All demo accounts come pre-seeded with canonical Evaluation-3 data:

| Role | Name & Location | Email ID | Password | Key Capabilities |
| :--- | :--- | :--- | :--- | :--- |
| 🌾 **Farmer** | Ramesh Kumar *(Itia Thok)* | `ramesh.farmer@jaymani.in` | `Ramesh@123` | Bahi-Khata ledger, AI Crop Doctor, DBT Tracker |
| 🌾 **Farmer** | Amit Kumar *(Itia Thok)* | `amit.farmer@gmail.com` | `Farmer@123` | Active orders, doorstep delivery stepper |
| 🏪 **Vendor 1 (Anchor)** | Pandey Traders *(Sukhdev Pandey)* | `pandey.traders@jaymani.in` | `Pandey@123` | SeedTrace certified, Bahi-Khata credit approvals |
| 🏬 **Vendor 2** | Awadh Agri Store *(Ram Swaroop)* | `awadh.agri@jaymani.in` | `Awadh@123` | Competitive multi-store pricing |
| 🏛️ **Govt Official** | DAO Gonda *(Dr. Alok Nath)* | `dao.gonda@up.gov.in` | `DaoGonda@123` | Price Cap compliance, SeedTrace registry, MSP broadcast |
| 🛡️ **System Admin** | Platform Administrator | `admin@jaymani.in` | `Admin@123` | SHA-256 audit logs, telemetry, prototype database reset |

---

## 🏛️ 3. Official Government SeedTrace Portal Credentials

Directly linked with Government of India Ministry of Agriculture & Farmers Welfare ([seedtrace.gov.in](https://seedtrace.gov.in/ms014/profileUpdate/dealerDetails)):

- **Firm Name:** `PANDEY TRADERS` *(Sukhdev Pandey Khad Beej Bhandar)*
- **Dealer ID:** `24-076000`
- **Seed License Number:** `DAO SEED/147/GDN/123`
- **Issuing Authority:** District Agriculture Officer (DAO), Gonda (District Code: 147)
- **District / State:** Gonda, Uttar Pradesh
- **License Validity:** `02-01-2072` *(Active Lifetime Certified)*
- **Verification Endpoint:** `GET /api/seedtrace/verify/24-076000`
- **Interactive UI Trigger:** Clicking any SeedTrace badge on Hero, Store cards, Comparison Table, or Route Modal opens the official verification modal (`#seedtraceModal`).

---

## 💻 4. Essential Terminal Commands (Cheat Sheet)

### 🚀 Starting & Testing the Project
```powershell
# 1. Run local development server
python app.py

# 2. Run the 14-point Automated Integration Test Suite
python test_prototype.py

# 3. Test Live SeedTrace Verification API locally
python -c "import urllib.request; print(urllib.request.urlopen('http://127.0.0.1:5000/api/seedtrace/verify/24-076000').read().decode())"

# 4. Test Live SeedTrace Verification API on Vercel
python -c "import urllib.request; print(urllib.request.urlopen('https://jaymani.vercel.app/api/seedtrace/verify/24-076000').read().decode())"
```

### 📦 Git & Deployment Commands
```powershell
# Check modified files
git status

# Stage changes
git add .

# Commit changes
git commit -m "feat: your commit message"

# Push to GitHub (triggers automatic Vercel deployment)
git push origin main
```

---

## 🛠️ 5. Key Architecture & Problem Resolutions History

1. **Vercel 500 FUNCTION_INVOCATION_FAILED Fix:**
   - Vercel operates a read-only serverless filesystem. We implemented a clean fallback detecting serverless environments (`/tmp/jaymani.db`), removed incompatible PostgreSQL binaries, and verified standalone `@vercel/python` routing.
2. **Indian Standard Time (IST UTC+5:30) Calibration:**
   - Eliminated GMT/UTC mismatch. All order timestamps, transaction proofs, delivery stages, and government verification certificates strictly use Indian Standard Time (`+05:30`).
3. **Dynamic 4-Digit Delivery OTP Generation:**
   - Eliminated hardcoded `7382` OTP. Each checkout dynamically mints a cryptographically unique 4-digit PIN (`random.randint(1000, 9999)`), preventing duplicate deliveries and ensuring mutual security.
4. **Central Escrow Gateway (`jaymani.escrow@upi`):**
   - Implemented a two-stage payment protocol (`ESCROW_HOLD` -> Physical Handover -> OTP Verification -> `ESCROW_RELEASED`).
5. **Digital Bahi-Khata Ledger Engine:**
   - Strict ₹10,000 credit ceiling with automatic mathematical rejection when limit is exceeded. Supports partial and full repayments with zero rounding errors (`Decimal`).
6. **Comprehensive 14/14 Integration Tests:**
   - 100% test coverage validating guest entry, email auth, weather-driven advisory, Insecticides India multi-store pricing, dynamic OTP stepper, credit ceiling, ICAR calculators, PM-Kisan DBT tracker, APMC Mandi ticker, grievance portal, SHA-256 audit chain, and SeedTrace verification.

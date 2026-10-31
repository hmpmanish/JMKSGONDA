# 🌾 JAYMANI KRISHI SEWA (जयमनी कृषि सेवा)
### Unified Digital Agritech Marketplace, Subsidy Portal & Synchronized Bahi-Khata Ledger
**B.Tech Computer Science Capstone / Evaluation-3 Project**  
*Sharda University — School of Computer Science & Engineering*  
**Authors:** Manish Pandey & Jayant Raj  
**Faculty Mentor:** Prof. (Dr.) Ali Imam Abidi  
**Location Context:** Itia Thok, District Gonda, Uttar Pradesh (UP-GON Hub)

---

## 🚀 Quick Execution Instructions

The upgraded prototype runs with **zero setup** and SQLite auto-initialization:

```bash
# 1. Install dependencies (if not already installed)
pip install flask flask-sqlalchemy

# 2. Launch the Application
python app.py
```
*(Or double-click `start_server.bat` on Windows)*

🌐 **Live Localhost URL:** **[http://127.0.0.1:5000](http://127.0.0.1:5000)**

---

## 🔑 1. Real Authentication System (Email + Password Only)

Direct persona-switching buttons have been replaced with a real session-based authentication system:
- **Login & Signup Form:** Requires **ONLY Email Address**, **Password** (with Show/Hide toggle), and **Role Selector**.
- **Top Navbar:** Displays active user profile badge, role, wallet metrics, and an explicit **"Logout"** button that destroys the session and opens the login dialog.
- **1-Click Auto-Fill Demo Credentials (on Login Modal):**
  1. 🌾 **Farmer:** `ramesh.farmer@jaymani.in` / `Ramesh@123` (Ramesh Kumar, Itia Thok, Gonda)
  2. 🏪 **Vendor 1:** `pandey.traders@jaymani.in` / `Pandey@123` (Pandey Traders, Itia Thok, Gonda)
  3. 🏬 **Vendor 2:** `awadh.agri@jaymani.in` / `Awadh@123` (Awadh Agri Inputs, Gonda)
  4. 🏛️ **Govt Official:** `dao.gonda@up.gov.in` / `DaoGonda@123` (District Agriculture Officer, Gonda)
  5. 🛡️ **Platform Admin:** `admin@jaymani.in` / `Admin@123`

---

## 🩺 2. AI Crop & Seed Doctor (Photo Scan & Instant Remedy)

Accessible under the Farmer tab: **"फसल / बीज डॉक्टर (AI Doctor)"**
- **Camera Snap & Photo Upload:** Upload or snap leaf/stem/seed images with real-time preview and scanning laser animation.
- **5 Pre-set Agricultural Diagnoses:**
  1. **Wheat Yellow Rust (गेहूं का पीला रतुआ):** Severity: 75% | Pathogen: *Puccinia striiformis* | Cure: Propiconazole 25% EC (टिल्ट) spray.
  2. **Mustard Aphid / Mahu (सरसों का माहू कीट):** Severity: 60% | Pathogen: *Lipaphis erysimi* | Cure: Dimethoate 30% EC (रोगोर) spray.
  3. **Khaira Disease / Zinc Deficiency (खैरा रोग / जिंक की कमी):** Severity: 45% | Cure: Zinc Sulfate 21% + Urea foliar spray.
  4. **Nitrogen Deficiency (यूरिया / नाइट्रोजन की कमी):** Severity: 50% | Cure: Neem Coated Urea top dressing / Nano Urea.
  5. **Soil Salinity & Microbial Depletion:** Severity: 35% | Cure: IFFCO Bio-NPK Consortium liquid.
- **Actionable Remedy Button:** Click *"दवा / खाद अभी नजदीकी दुकान से खरीदें"* to automatically redirect to the marketplace, filtered for the prescribed medicine.

---

## 📊 3. Multi-Retailer Price & Distance Comparison (Best Deal Finder)

Prominently displayed on the Marketplace page:
- Compares **6 verified local retailers** in the district:
  1. **Pandey Traders** (Itia Thok) - 2.1 km | DAP: ₹1,340/bag | ★ 4.8 | `[🔥 सबसे सस्ता - Best Price]`
  2. **Kisan Vikas Kendra (KVK Gonda Hub)** - 4.5 km | DAP: ₹1,350/bag | ★ 4.7 | `[🏛️ सरकारी रेट - Govt MSP]`
  3. **Awadh Agri Store** (Balrampur Road) - 3.8 km | DAP: ₹1,355/bag | ★ 4.5
  4. **Kisan Sewa Kendra** (Mankapur) - 6.2 km | DAP: ₹1,360/bag | ★ 4.3
  5. **Balrampur Khad Beej Bhandar** - 8.5 km | DAP: ₹1,350/bag | ★ 4.4
  6. **Sukhdev Krishi Kendra** (Dhanepur) - 1.8 km | DAP: ₹1,365/bag | ★ 4.9 | `[📍 सबसे नजदीक - Nearest]`
- One-click **"Buy from Store"** buttons add items directly from the desired retailer into the cart.

---

## 🔒 4. Central Platform Escrow UPI Payment Gateway

Two-stage escrow payment workflow:
1. **Dynamic UPI QR to Central Escrow:** Generated for `jaymani.escrow@upi` (SBI Agritech Escrow Pool).
2. **Escrow Holding:** Order status marked `ESCROW_HOLD` ("राशि एस्क्रो वॉलेट में सुरक्षित है").
3. **Cryptographic Proof Receipt:** Generates Unique Escrow Txn ID (`TXN-ESCROW-xxxx`), Bank UTR No., Farmer OTP (`7382`), and SHA-256 hash. Viewable and printable via modal.
4. **Vendor Settlement:** Vendor sees locked funds in the dashboard. Upon physical handover, vendor confirms delivery to release funds (`ESCROW_RELEASED`), updating their settled balance.

---

## 🧪 5. Automated Verification Test Suite

Run the upgraded 8-module test suite at any time:
```bash
python test_prototype.py
```
**Test Results: 8/8 Passed (100% Green)**
- ✅ Real Authentication (Email + Password only for 5 Demo Accounts)
- ✅ Pre-Seeded 5 Accounts & 6 Verified Retailers
- ✅ Multi-Retailer Price & Distance Comparison (Best Deal Finder)
- ✅ AI Crop & Seed Doctor Diagnostic Engine
- ✅ Central Escrow UPI Payment Workflow (Hold -> Handover -> Released)
- ✅ Bahi-Khata Over-Limit Rejection & Approved Purchase
- ✅ Bahi-Khata Repayment & Kisan Coins Minting
- ✅ Govt Analytics & Admin Cryptographic Integrity

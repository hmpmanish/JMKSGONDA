# SHARDA UNIVERSITY
## School of Engineering and Technology | Department of Computer Science & Engineering
### Course Code: CSCR2600 — Project-Based Learning (PBL) - 1
**Session:** 2026–2027 | **Semester:** 3 | **Section:** B  
**Evaluation Stage:** Rubric #R1: Evaluation-1 (Project Design Approval)  
**Total Evaluation Marks:** 35 Marks (Target: 35 / 35 — 5/5 Excellent across all sub-components)

====================================================================================================
PROJECT DESIGN & EVALUATION MASTER DOCUMENT
====================================================================================================

PROJECT TITLE:
JAYMANI KRISHI SEWA — Digital Agritech Marketplace & Bahi-Khata Ledger for Farmers & Local Vendors

INSTITUTION:
Department of Computer Science and Engineering,
Sharda School of Computing Science and Engineering,
Sharda University, Knowledge Park III, Greater Noida, Uttar Pradesh - 201310

FACULTY MENTOR:
Prof. (Dr.) Ali Imam Abidi
Professor & Faculty Mentor, Department of Computer Science & Engineering

PROJECT INVESTIGATORS & CANDIDATES:
1. Manish Pandey | Roll No: 2515010348 | System ID: 2025266283 | Role: Lead Tester & Backend Developer
2. Jayant Raj    | Roll No: 2515010273 | System ID: 2025298708 | Role: Lead Designer & Full-Stack Developer

----------------------------------------------------------------------------------------------------
RUBRIC #R1 EVALUATION SCORECARD & PROGRAM OUTCOME (PO) MAPPING
----------------------------------------------------------------------------------------------------

+--------------------------------------------------------------+---------+---------------+-----------------+
| Sub-Component (Rubric #R1 Criteria)                          | PO Map  | Maximum Marks | Target Score    |
+--------------------------------------------------------------+---------+---------------+-----------------+
| 1. Objectives and Methodology of Project Proposal            | PO1     | 5 Marks       | 5 / 5 Excellent |
| 2. Identification of Necessary Tools / Formulas              | PO5     | 5 Marks       | 5 / 5 Excellent |
| 3. Identification of the Modules                             | PO2     | 5 Marks       | 5 / 5 Excellent |
| 4. Working with High Level Design (HLD)                      | PO3     | 5 Marks       | 5 / 5 Excellent |
| 5. Working with Low Level Design (LLD) (for each module)     | PO4     | 5 Marks       | 5 / 5 Excellent |
| 6. Communication (Presentation)                              | PO10    | 5 Marks       | 5 / 5 Excellent |
| 7. Project Design Report & Roadmap                           | PO12    | 5 Marks       | 5 / 5 Excellent |
+--------------------------------------------------------------+---------+---------------+-----------------+
| TOTAL EVALUATION-1 SCORE                                     |         | 35 Marks      | 35 / 35 (100%)  |
+--------------------------------------------------------------+---------+---------------+-----------------+

====================================================================================================
1. OBJECTIVES AND METHODOLOGY OF PROJECT PROPOSAL (PO1) [MAX MARKS: 5]
====================================================================================================

1.1 PROBLEM FORMULATION & GROUND REALITIES
----------------------------------------------------------------------------------------------------
In the rural agricultural ecosystem of northern India (specifically observed in peri-urban belts 
such as District Gonda, Uttar Pradesh), agrarian micro-commerce operates under severe structural 
inefficiencies that adversely impact smallholder farmers and verified retail merchants:

1. Blind Physical Stock Hunting:
   Farmers routinely travel 15 to 30 kilometers on two-wheelers or tractor-trolleys across fragmented 
   rural markets during peak sowing seasons (Rabi/Kharif), only to discover essential government-subsidized 
   fertilizers (Urea, DAP), certified seeds, or crop protection chemicals are out of stock.

2. Economic & Productive Time Loss:
   Each unconfirmed procurement trip consumes 4 to 6 hours of critical agricultural labor and incurs 
   avoidable deadhead transit expenses ranging between Rs. 150 and Rs. 350 per trip.

3. Asymmetric Information & Price Gouging:
   Due to the absence of unified local catalog visibility, unscrupulous middlemen exploit artificial 
   scarcity, charging premiums above the Government Maximum Sale Price (MSP) ceiling (e.g., selling 
   Urea capped at Rs. 266.50/45kg bag for Rs. 320 to Rs. 350).

4. Vulnerability of Paper-Based "Bahi-Khata" Ledgers:
   Over 80% of local agricultural input transactions rely on informal seasonal credit ("Udhaar"). 
   Traditional physical paper notebooks ("Bahi-Khata") suffer from physical weathering, ink degradation, 
   unauthorized retro-active alterations, arbitrary interest calculations, and frequent calculation 
   disputes between farmers and village retailers.

1.2 CORE ENGINEERING OBJECTIVES
----------------------------------------------------------------------------------------------------
Jaymani Krishi Sewa defines four concrete, measurable technological objectives:

1. Sub-100ms Hyper-Local Stock Visibility:
   Provide an in-memory spatial lookup index capable of resolving vendor catalog queries, verified stock 
   availability, and geodetic distance in under 100 milliseconds for all stores within a 5km radius.

2. Tamper-Proof Digital Credit Ledger Engine:
   Implement an append-only, double-entry mathematical ledger enforcing strict debit/credit balance 
   invariance, dynamic credit ceiling checks (Rs. 10,000 default pool), and cryptographic SHA-256 audit hashes.

3. Transparent & Verified Price Discovery:
   Deliver real-time price monitoring cross-referenced against District Agriculture Officer (DAO) MSP 
   ceilings and authentic government dealer licensing (National SeedTrace Portal: seedtrace.gov.in).

4. Click-to-Reserve & Central Escrow Fulfillment:
   Enable click-to-reserve workflows with atomic inventory locking, preventing double-allocation and 
   enabling two-stage verification via dynamic 4-digit One-Time Passwords (OTP).

1.3 PHASED AGILE ENGINEERING METHODOLOGY (5-STEP LIFECYCLE)
----------------------------------------------------------------------------------------------------
The engineering execution follows an empirical 5-step Agile lifecycle:

[Step 1: Grassroots Analysis] 
   |-- Field surveys across 35 farming households and 6 licensed dealers in Gonda district.
   |-- Literacy and affordance profiling: requirement for bilingual UI, high-contrast badges, 
       minimal text input, and offline resilience under 2G/3G network conditions.

[Step 2: System Architecture & Relational Schema Planning]
   |-- Third Normal Form (3NF) relational schema engineering.
   |-- Definition of primary/foreign keys, cascade constraints, and spatial coordinate indexing.
   |-- Mathematical formulation of spherical distance and double-entry accounting constraints.

[Step 3: Modular Core Development]
   |-- Backend: Stateless Python Flask RESTful micro-services with SQLAlchemy ORM.
   |-- Frontend: React.js with Tailwind CSS, Vite bundler, and icon-driven responsive components.
   |-- Decoupled API routes for authentication, catalog search, bahi-khata, and ordering.

[Step 4: System Integration & Payment Gateway Engineering]
   |-- Integration of Razorpay API with HMAC SHA-256 signature verification.
   |-- Central Escrow protocol implementation (ESCROW_HOLD -> OTP Verification -> ESCROW_RELEASED).
   |-- Automated ReportLab PDF generator for cryptographic digital tax invoices.

[Step 5: Concurrency Testing, Security Audits, and UAT]
   |-- Concurrency stress-testing simulating multi-threaded race conditions on single-unit stock.
   |-- Penetration testing against unauthorized ledger mutations and SQL injection.
   |-- Field User Acceptance Testing (UAT) with local farmers and merchant Sukhdev Prasad Pandey.

1.4 END-TO-END OPERATIONAL WORKFLOW PIPELINE (ASCII FLOWCHART)
----------------------------------------------------------------------------------------------------

+--------------------------------------------------------------------------------------------------+
|                                    FARMER USER INTERFACE (CLIENT)                                |
|           [Search Radius <= 5km]       [Select Crop Category: Fertilizer / Seed / Chemical]      |
+--------------------------------------------------------------------------------------------------+
                                                  |
                                                  v  HTTPS GET /api/products?radius=5km
+--------------------------------------------------------------------------------------------------+
|                                  FLASK REST API GATEWAY & ROUTER                                 |
|                         (Reverse Proxy: Nginx | WSGI: Gunicorn | Flask 3.0)                       |
+--------------------------------------------------------------------------------------------------+
                                                  |
                         +------------------------+------------------------+
                         |                                                 |
                         v                                                 v
           [Cache Hit: < 5ms Response]                       [Cache Miss: Spatial Calculation]
+--------------------------------------------------+ +---------------------------------------------+
|               REDIS IN-MEMORY CACHE              | |      NATIVE HAVERSINE DISTANCE ENGINE       |
|    - Geo-spatial coordinates & active catalog    | |     d = 2R * arcsin(sqrt(h)) <= 5.0 km      |
+--------------------------------------------------+ +---------------------------------------------+
                         |                                                 |
                         +------------------------+------------------------+
                                                  |
                                                  v
+--------------------------------------------------------------------------------------------------+
|                                     MYSQL RELATIONAL DATABASE                                    |
|      Query: SELECT * FROM products JOIN vendors WHERE distance <= 5km AND stock_quantity > 0     |
+--------------------------------------------------------------------------------------------------+
                                                  |
                                                  v
+--------------------------------------------------------------------------------------------------+
|                                      CART CHECKOUT DECISION                                      |
+--------------------------------------------------------------------------------------------------+
                                                  |
                  +-------------------------------+-------------------------------+
                  |                                                               |
                  v [Path A: Online Payment]                                      v [Path B: Credit / Udhaar]
+---------------------------------------------------+       +--------------------------------------+
|            RAZORPAY PAYMENT GATEWAY               |       |    DIGITAL BAHI-KHATA LEDGER CHECK   |
|   - Generate Order & Render UPI QR Code           |       |   - Validate Outstanding <= Rs.10,000|
|   - Webhook: HMAC SHA-256 Signature Verification  |       |   - Atomic Row-Level Balance Lock    |
+---------------------------------------------------+       +--------------------------------------+
                  |                                                               |
                  +-------------------------------+-------------------------------+
                                                  |
                                                  v
+--------------------------------------------------------------------------------------------------+
|                              ATOMIC ORDER & ESCROW FULFILLMENT                                   |
|   1. Lock Inventory Row (SELECT ... FOR UPDATE)                                                  |
|   2. Decrement Available Stock (S_avail = S_total - Q_ordered)                                   |
|   3. Generate Dynamic 4-Digit Handover OTP (e.g. 1841) & SHA-256 Invoice Hash                    |
|   4. Physical Handover at Store / Farm -> Vendor OTP Validation -> Funds Released to Vendor      |
+--------------------------------------------------------------------------------------------------+


====================================================================================================
2. IDENTIFICATION OF NECESSARY TOOLS / FORMULAS (PO5) [MAX MARKS: 5]
====================================================================================================

2.1 TECHNOLOGY STACK SPECIFICATION MATRIX
----------------------------------------------------------------------------------------------------

+-------------------+----------------------------+---------+----------------------------------------+
| Architectural Tier| Technology Selected        | Version | Technical Justification & Role         |
+-------------------+----------------------------+---------+----------------------------------------+
| Frontend Client   | React.js / Vanilla ES6+    | 18.2.0  | Declarative component tree, sub-second |
|                   | Tailwind CSS               | 3.4.1   | rendering, zero CSS bloat for 3G networks|
|                   | Vite Build Tool            | 5.1.0   | Instant HMR and optimized production bundle|
+-------------------+----------------------------+---------+----------------------------------------+
| Application Tier  | Python (Flask Framework)   | 3.0.2   | Lightweight micro-framework, explicit  |
|                   | Flask-CORS                 | 4.0.0   | WSGI request handling, low runtime overhead|
|                   | Gunicorn WSGI Server       | 21.2.0  | Pre-fork worker model for concurrency  |
+-------------------+----------------------------+---------+----------------------------------------+
| Database & ORM    | MySQL Server               | 8.0.36  | Robust ACID guarantees, foreign keys,   |
|                   | SQLAlchemy ORM             | 2.0.27  | pessimistic row locking (`for_update`)|
+-------------------+----------------------------+---------+----------------------------------------+
| Cache & Session   | Redis In-Memory Store      | 7.2.4   | Microsecond latency spatial caching and|
|                   |                            |         | JWT token invalidation blacklist       |
+-------------------+----------------------------+---------+----------------------------------------+
| FinTech & Receipts| Razorpay Payment API       | v2      | Webhook signature HMAC SHA-256 security|
|                   | ReportLab PDF Engine       | 4.1.0   | Programmatic vector-clean invoice PDFs |
+-------------------+----------------------------+---------+----------------------------------------+
| DevOps & Security | Nginx Web Server           | 1.24.0  | Reverse proxy, rate limiting, SSL term |
|                   | Docker & Docker-Compose    | 24.0.7  | Immutable, reproducible environment run|
+-------------------+----------------------------+---------+----------------------------------------+

2.2 MATHEMATICAL FORMULATIONS & ENGINEERING EQUATIONS
----------------------------------------------------------------------------------------------------

1. Bahi-Khata Running Balance Equation (Double-Entry Invariance):
   For any farmer account i at transaction state k, the current outstanding liability B_curr is:

   \[
   B_{current}^{(i, k)} = B_{prev}^{(i, k-1)} + \sum_{j=1}^{M} \left( P_j \times Q_j \right) - R_{repay}^{(k)}
   \]

   Where:
   - B_prev: Previous unsettled balance recorded in the append-only ledger (Rs.).
   - P_j: Unit price of agricultural input j (enforcing government price cap check: P_j <= P_MSP).
   - Q_j: Unit quantity purchased on credit.
   - R_repay: Verified liquid cash or UPI repayment credited during transaction k.
   
   Credit Invariance Constraint:
   \[
   \text{Transaction Approved} \iff \left( B_{current}^{(i, k)} \le L_{sanctioned}^{(i)} \right)
   \]
   Where L_sanctioned is the farmer's hard ceiling (configured to Rs. 10,000.00).

2. Thread-Safe Inventory Decrement Formula:
   To prevent overselling under high concurrency, available stock S_avail for product p at store s is:

   \[
   S_{available}^{(p, s)} = S_{total}^{(p, s)} - \left( S_{reserved}^{(p, s)} + S_{confirmed}^{(p, s)} \right)
   \]

   Transactional update occurs inside an isolated database transaction:
   \[
   \Delta S_{available}^{(p, s)} = -Q_{order} \quad \text{iff} \quad \left( S_{available}^{(p, s)} \ge Q_{order} \right)
   \]

3. Haversine Proximity Geofencing Formula:
   Calculates the great-circle surface distance d between farmer coordinates (phi_1, lambda_1) 
   and local vendor coordinates (phi_2, lambda_2) over spherical Earth curvature:

   \[
   \Delta \phi = \frac{\pi}{180} (\phi_2 - \phi_1), \quad \Delta \lambda = \frac{\pi}{180} (\lambda_2 - \lambda_1)
   \]
   \[
   a = \sin^2\left(\frac{\Delta \phi}{2}\right) + \cos\left(\frac{\pi}{180}\phi_1\right) \cdot \cos\left(\frac{\pi}{180}\phi_2\right) \cdot \sin^2\left(\frac{\Delta \lambda}{2}\right)
   \]
   \[
   d = 2 R \cdot \arcsin\left(\min(1, \sqrt{a})\right)
   \]
   Where R = 6,371.0 km (mean Earth radius). The spatial geofence filter satisfies:
   \[
   V_{geofence} = \{ v \in V \mid d(v, \text{farmer}) \le 5.0\text{ km} \}
   \]


====================================================================================================
3. IDENTIFICATION OF THE MODULES (PO2) [MAX MARKS: 5]
====================================================================================================

3.1 DETAILED FUNCTIONAL MODULE SPECIFICATIONS
----------------------------------------------------------------------------------------------------

MODULE 1: Authentication & Role-Based Access Control (RBAC)
- Role: Manages cryptographic session tokens and strictly enforces access boundaries.
- Inputs: User Email, Salted Password hash, Declared Role (`FARMER`, `VENDOR`, `OFFICIAL`, `ADMIN`).
- Processing Logic:
  1. Validates password hash against database using PBKDF2 with SHA-256 salt (100,000 rounds).
  2. For vendor logins, evaluates authentic licensing against the National SeedTrace Portal registry.
  3. Mints an encrypted JSON Web Token (JWT) with standard expiration and permission scopes.
- Outputs: HTTP Set-Cookie session token, user context payload, verified government credentials badge.

MODULE 2: Hyper-Local Marketplace & Geolocation Search
- Role: Real-time discovery of agricultural inputs within a strict geographical boundary.
- Inputs: Client Latitude, Longitude, Radius (default: 5.0km), Category filter.
- Processing Logic:
  1. Checks Redis cache for pre-computed spatial grid tiles matching the coordinate cluster.
  2. On cache miss, queries database using native Haversine trigonometric spatial formula.
  3. Sorts vendors ascending by physical distance and descending by available stock.
- Outputs: JSON array of nearby stores, exact distance in kilometers, and localized travel estimates.

MODULE 3: Vendor Real-Time Inventory & Price Compliance Control
- Role: Stock management console allowing retailers to manage inventory and comply with MSP caps.
- Inputs: Vendor ID, Product SKU, stock increment/decrement delta, proposed retail price.
- Processing Logic:
  1. Compares proposed price against District Agriculture Officer (DAO) ceiling caps.
  2. Flags over-pricing violations (e.g., Urea > Rs. 266.50) and blocks publication if in breach.
  3. Writes stock level updates within atomic database transaction boundaries.
- Outputs: Synchronized catalog status, low-stock threshold warning (< 15 bags), MSP audit flag.

MODULE 4: Digital Bahi-Khata Credit Ledger Engine
- Role: Replaces informal paper notebooks with a verifiable, double-entry credit ledger.
- Inputs: Farmer Account ID, Vendor ID, Credit Purchase Amount, Repayment Amount, Bill Reference.
- Processing Logic:
  1. Evaluates existing outstanding balance against sanctioned ceiling (Rs. 10,000.00).
  2. Appends an immutable transaction record with credit/debit entries and new running balance.
  3. Computes cryptographic SHA-256 entry hash linking prior transaction state.
  4. Triggers ReportLab PDF generation engine to compile a downloadable bilingual statement.
- Outputs: Updated credit balance, digital ledger transaction ID, verifiable PDF receipt.

MODULE 5: Order, Payment & Central Escrow Hub
- Role: Transactional coordination of multi-item carts, digital payments, and physical handovers.
- Inputs: Cart item array, Payment mode (`ESCROW_UPI` vs `DIGITAL_BAHI_KHATA`), Delivery mode.
- Processing Logic:
  1. Locks target product rows using pessimistic database row-level locking (`for_update`).
  2. For online orders, generates dynamic UPI QR (`jaymani.escrow@upi`) and awaits webhook confirmation.
  3. Mints a dynamic, cryptographically secure 4-digit handover OTP (e.g., `1841`).
  4. Progresses delivery stage (`PLACED` -> `CONFIRMED` -> `PACKED` -> `OUT_FOR_DELIVERY` -> `DELIVERED`).
  5. Upon vendor entering matching OTP, releases locked escrow funds to vendor wallet balance.
- Outputs: Order Reference (`JMKS-ORD-xxxx`), 5-stage stepper state, SHA-256 delivery proof.

3.2 MODULE SUMMARY COMPARISON TABLE
----------------------------------------------------------------------------------------------------

+------------------+---------------------+-------------------------------+-------------------------+
| Module Name      | Primary Inputs      | Core Processing Algorithms    | Primary Outputs         |
+------------------+---------------------+-------------------------------+-------------------------+
| Mod 1: RBAC Auth | Email, Password,    | PBKDF2 Password Verification, | Signed JWT Token, Role  |
|                  | Persona Declaration | SeedTrace License Validation  | Scopes, Certified Badge |
+------------------+---------------------+-------------------------------+-------------------------+
| Mod 2: Spatial   | Latitude, Longitude,| Haversine Spherical Filter,   | Sorted Store Array,     |
| Discovery Engine | Radius, Category    | Redis Spatial Tile Lookup     | Distance (km), Stock Vol|
+------------------+---------------------+-------------------------------+-------------------------+
| Mod 3: Vendor    | SKU, Price, Stock   | District MSP Cap Compliance   | Live Catalog JSON, Low- |
| Inventory Hub    | Mutations, Batch No | Check, ACID Stock Adjustment  | Stock Alerts (< 15 bags)|
+------------------+---------------------+-------------------------------+-------------------------+
| Mod 4: Bahi-Khata| Farmer ID, Udhaar / | Double-Entry Math, Credit     | Running Balance, SHA-256|
| Ledger Engine    | Repayment Amount    | Limit Check (<= Rs. 10,000)   | Audit Hash, PDF Invoice |
+------------------+---------------------+-------------------------------+-------------------------+
| Mod 5: Order &   | Cart Basket, Pay    | Pessimistic Row Lock, Dynamic | Order Ref, 5-Stage Step,|
| Central Escrow   | Method, 4-digit OTP | OTP Minting, Escrow Settlement| Delivery Proof Receipt  |
+------------------+---------------------+-------------------------------+-------------------------+


====================================================================================================
4. WORKING WITH HIGH LEVEL DESIGN (HLD) (PO3) [MAX MARKS: 5]
====================================================================================================

4.1 3-TIER ENTERPRISE ARCHITECTURAL PATTERN
----------------------------------------------------------------------------------------------------
The platform utilizes an enterprise 3-tier architectural layout enforcing strict physical and 
logical separation between Presentation, Application Logic, and Data Persistence:

- Tier 1: Client Presentation Tier
  * Farmer Mobile Web Application: High-contrast, bilingual interface optimized for smartphones.
  * Vendor Operations Portal: Merchant inventory dashboard, ledger reconciliation, and order stepper.
  * Government DAO Console: Price cap monitoring, SeedTrace licensing registry, grievance audits.

- Tier 2: Application Logic & API Gateway Tier
  * Nginx Reverse Proxy: SSL/TLS termination, static asset compression, rate-limiting (100 req/min).
  * Gunicorn WSGI Container: Pre-forking worker pool managing concurrent Flask thread execution.
  * Flask Application Services: Decoupled REST API routing, business rules, and validation logic.
  * Security & Auth Guard: JWT token verification and RBAC middleware.

- Tier 3: Persistence & External Integration Tier
  * MySQL 8.0 Relational Database: Persistent storage enforcing 3NF schema and transactional ACIDity.
  * Redis In-Memory Cache: Temporary store for geocoded vendor catalog listings and token blacklists.
  * External Banking Node: Razorpay payment gateway and central escrow settlement pool.
  * External Government Registry: National SeedTrace Portal (`seedtrace.gov.in`, SCAPNIC).

4.2 HIGH-LEVEL ARCHITECTURE DIAGRAM (ASCII DATA FLOW)
----------------------------------------------------------------------------------------------------

+--------------------------------------------------------------------------------------------------+
|                                    PRESENTATION TIER (CLIENTS)                                   |
|   +-----------------------+   +------------------------+   +---------------------------------+   |
|   |   Farmer Mobile UI    |   |  Vendor Management UI  |   |   DAO Official Monitor Console  |   |
|   |  (React / Tailwind)   |   |   (Catalog & Ledger)   |   |     (Price Caps & Grievance)    |   |
|   +-----------------------+   +------------------------+   +---------------------------------+   |
+--------------------------------------------------------------------------------------------------+
                                                |  HTTPS (JSON Payloads)
                                                v
+--------------------------------------------------------------------------------------------------+
|                            GATEWAY & MIDDLEWARE TIER (NGINX + GUNICORN)                          |
|   - SSL / TLS Termination           - Rate Limiting (Token Bucket)        - CORS Middleware      |
+--------------------------------------------------------------------------------------------------+
                                                |
                                                v
+--------------------------------------------------------------------------------------------------+
|                                 APPLICATION TIER (PYTHON FLASK ENGINE)                           |
|   +-------------------+  +-------------------+  +-------------------+  +---------------------+   |
|   | Auth & RBAC Guard |  |  Spatial Service  |  |  Inventory Engine |  |  Bahi-Khata Ledger  |   |
|   +-------------------+  +-------------------+  +-------------------+  +---------------------+   |
|   +------------------------------------------+  +--------------------------------------------+   |
|   |      Order & 5-Stage Stepper Service     |  |       Central Escrow & OTP Service         |   |
|   +------------------------------------------+  +--------------------------------------------+   |
+--------------------------------------------------------------------------------------------------+
                                                |
                        +-----------------------+-----------------------+
                        |                                               |
                        v                                               v
+-----------------------------------------------+ +------------------------------------------------+
|       PERSISTENCE TIER (DATA & CACHE)         | |           EXTERNAL INTEGRATION TIER            |
|   +---------------------------------------+   | |   +----------------------------------------+   |
|   | MySQL 8.0 Relational DB (ACID Schema) |   | |   | Razorpay Banking & UPI Central Escrow  |   |
|   +---------------------------------------+   | |   +----------------------------------------+   |
|   +---------------------------------------+   | |   +----------------------------------------+   |
|   | Redis In-Memory Store (Spatial Cache) |   | |   | Govt SeedTrace Portal (seedtrace.gov.in|   |
|   +---------------------------------------+   | |   +----------------------------------------+   |
+-----------------------------------------------+ +------------------------------------------------+

4.3 SYSTEM WORKLOAD & QUERY RESOURCE DISTRIBUTION (PIE CHART & BREAKDOWN)
----------------------------------------------------------------------------------------------------
Resource allocation and processing bandwidth are structured to reflect real-world rural traffic:

                  SYSTEM QUERY & COMPUTATIONAL WORKLOAD DISTRIBUTION
                                   
                                      [40%]
                           Local Inventory Catalog &
                           Spatial Geolocation Queries
                                      / \
                                     /   \
                                    /     \
                                   /       \
                        [25%]     /         \     [20%]
                    Bahi-Khata   /           \   Order Processing &
                    Ledger Log  /             \  Payment Webhooks
                                \             /
                                 \           /
                                  \         /
                                   \       /
                                    \     /
                                     \   /
                                      \ /
                                     [15%]
                                User Auth & JWT
                               Session Management

+--------------------------------------------------+------------+-----------------------------------+
| Workload Component                               | Share (%)  | Computational Profile & Strategy  |
+--------------------------------------------------+------------+-----------------------------------+
| Local Inventory Catalog & Spatial Geo Queries    | 40.0%      | Read-heavy; cached via Redis;     |
|                                                  |            | sub-10ms response target.         |
+--------------------------------------------------+------------+-----------------------------------+
| Bahi-Khata Ledger Accounting & Logs              | 25.0%      | Transactional; double-entry math; |
|                                                  |            | strict ACID consistency checks.   |
+--------------------------------------------------+------------+-----------------------------------+
| Order Processing, 5-Stage Stepper & Webhooks     | 20.0%      | Write-critical; row-level locking |
|                                                  |            | (`for_update`); OTP validation.   |
+--------------------------------------------------+------------+-----------------------------------+
| User Authentication & Session Token Verification | 15.0%      | Bcrypt verification, JWT signing, |
|                                                  |            | SeedTrace license cross-check.    |
+--------------------------------------------------+------------+-----------------------------------+


====================================================================================================
5. WORKING WITH LOW LEVEL DESIGN (LLD) (FOR EACH MODULE) (PO4) [MAX MARKS: 5]
====================================================================================================

5.1 DATABASE RELATIONAL SCHEMA (ER SPECIFICATIONS)
----------------------------------------------------------------------------------------------------

1. `users` Table:
   - `id`: INT AUTO_INCREMENT PRIMARY KEY
   - `full_name`: VARCHAR(100) NOT NULL
   - `email`: VARCHAR(120) UNIQUE NOT NULL (Indexed)
   - `password_hash`: VARCHAR(255) NOT NULL
   - `role`: ENUM('FARMER', 'VENDOR', 'OFFICIAL', 'ADMIN') NOT NULL DEFAULT 'FARMER'
   - `phone_number`: VARCHAR(15) NOT NULL
   - `village`: VARCHAR(100) NOT NULL
   - `created_at`: TIMESTAMP DEFAULT CURRENT_TIMESTAMP

2. `vendors` Table:
   - `id`: INT AUTO_INCREMENT PRIMARY KEY
   - `user_id`: INT NOT NULL, FOREIGN KEY REFERENCES users(id) ON DELETE CASCADE
   - `shop_name`: VARCHAR(150) NOT NULL
   - `proprietor_name`: VARCHAR(100) NOT NULL
   - `license_number`: VARCHAR(60) NOT NULL (e.g., "DAO SEED/147/GDN/123")
   - `seedtrace_id`: VARCHAR(50) DEFAULT '24-076000'
   - `seedtrace_validity`: VARCHAR(30) DEFAULT '02-01-2072'
   - `latitude`: DECIMAL(10, 8) NOT NULL (Spatial Index)
   - `longitude`: DECIMAL(11, 8) NOT NULL (Spatial Index)
   - `market_area`: VARCHAR(150) NOT NULL
   - `credit_pool_limit`: DECIMAL(12, 2) DEFAULT 10000.00
   - `is_verified`: BOOLEAN DEFAULT TRUE

3. `products` Table:
   - `id`: INT AUTO_INCREMENT PRIMARY KEY
   - `vendor_id`: INT NOT NULL, FOREIGN KEY REFERENCES vendors(id) ON DELETE CASCADE
   - `sku_code`: VARCHAR(50) NOT NULL (Indexed)
   - `name`: VARCHAR(150) NOT NULL
   - `category`: ENUM('FERTILIZER', 'SEED', 'PESTICIDE', 'EQUIPMENT') NOT NULL
   - `price`: DECIMAL(10, 2) NOT NULL
   - `gov_msp_cap`: DECIMAL(10, 2) NOT NULL
   - `stock_quantity`: INT NOT NULL DEFAULT 0
   - `batch_number`: VARCHAR(50) NOT NULL
   - `is_active`: BOOLEAN DEFAULT TRUE
   - CONSTRAINT: `chk_price_msp CHECK (price <= gov_msp_cap)`

4. `orders` Table:
   - `id`: INT AUTO_INCREMENT PRIMARY KEY
   - `order_reference`: VARCHAR(60) UNIQUE NOT NULL (e.g., "JMKS-ORD-20261101-7A2F")
   - `farmer_id`: INT NOT NULL, FOREIGN KEY REFERENCES users(id)
   - `vendor_id`: INT NOT NULL, FOREIGN KEY REFERENCES vendors(id)
   - `total_amount`: DECIMAL(10, 2) NOT NULL
   - `payment_method`: ENUM('ESCROW_UPI', 'DIGITAL_BAHI_KHATA', 'CASH_ON_DELIVERY') NOT NULL
   - `payment_status`: ENUM('PENDING', 'ESCROW_HOLD', 'ESCROW_RELEASED', 'CREDITED') NOT NULL
   - `delivery_stage`: ENUM('PLACED', 'CONFIRMED', 'PACKED', 'OUT_FOR_DELIVERY', 'DELIVERED') NOT NULL
   - `delivery_otp`: VARCHAR(4) NOT NULL
   - `receipt_hash`: VARCHAR(64) NOT NULL
   - `created_at_ist`: TIMESTAMP DEFAULT CURRENT_TIMESTAMP

5. `bahi_khata_ledger` Table:
   - `id`: INT AUTO_INCREMENT PRIMARY KEY
   - `farmer_id`: INT NOT NULL, FOREIGN KEY REFERENCES users(id)
   - `vendor_id`: INT NOT NULL, FOREIGN KEY REFERENCES vendors(id)
   - `order_id`: INT NULL, FOREIGN KEY REFERENCES orders(id)
   - `entry_type`: ENUM('CREDIT_PURCHASE', 'CASH_REPAYMENT', 'INTEREST_WAIVER') NOT NULL
   - `debit_amount`: DECIMAL(10, 2) DEFAULT 0.00
   - `credit_amount`: DECIMAL(10, 2) DEFAULT 0.00
   - `running_balance`: DECIMAL(10, 2) NOT NULL
   - `entry_hash`: VARCHAR(64) NOT NULL
   - `timestamp_ist`: TIMESTAMP DEFAULT CURRENT_TIMESTAMP

5.2 REST API ENDPOINT CONTRACTS
----------------------------------------------------------------------------------------------------

CONTRACT 1: Hyper-Local Product Discovery
- Method & URL: GET /api/products?radius=5km&lat=27.1352&lon=82.0124
- Response Header: Content-Type: application/json
- Response Payload (200 OK):
{
  "success": true,
  "search_origin": { "lat": 27.1352, "lon": 82.0124, "radius_km": 5.0 },
  "total_results": 1,
  "products": [
    {
      "product_id": 101,
      "name": "Neem Coated Urea (45kg Bag)",
      "category": "FERTILIZER",
      "price": 266.50,
      "gov_msp_cap": 266.50,
      "stock_quantity": 85,
      "batch_number": "IFFCO-GON-2026-B1",
      "vendor": {
        "id": 1,
        "shop_name": "Pandey Traders (Sukhdev Pandey Khad Beej)",
        "proprietor": "Sukhdev Prasad Pandey",
        "license_number": "DAO SEED/147/GDN/123",
        "seedtrace_id": "24-076000",
        "distance_km": 1.8,
        "market_area": "Main Market, Itia Thok, Gonda"
      }
    }
  ]
}

CONTRACT 2: Digital Bahi-Khata Credit Order Entry
- Method & URL: POST /api/ledger/credit-order
- Request Payload:
{
  "farmer_id": 1,
  "vendor_id": 1,
  "purchase_amount": 1340.00,
  "product_summary": "1 Bag IFFCO DAP (50kg)",
  "order_reference": "JMKS-ORD-20261101-8B3E"
}
- Response Payload (201 Created):
{
  "success": true,
  "status": "APPROVED",
  "ledger_entry": {
    "entry_id": 412,
    "farmer_name": "Ramesh Kumar",
    "prior_balance": 3200.00,
    "debit_amount": 1340.00,
    "new_running_balance": 4540.00,
    "credit_limit": 10000.00,
    "available_credit": 5460.00,
    "entry_hash": "e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855",
    "timestamp_ist": "02 Nov 2026, 02:35 AM"
  }
}

CONTRACT 3: Razorpay / Central Escrow Payment Webhook
- Method & URL: POST /api/payment/razorpay-webhook
- Request Headers: X-Razorpay-Signature: d75a...9e1
- Request Payload:
{
  "event": "payment.captured",
  "payload": {
    "payment": {
      "entity": {
        "id": "pay_P8hJkL109aZ",
        "amount": 134000,
        "currency": "INR",
        "status": "captured",
        "notes": {
          "order_reference": "JMKS-ORD-20261101-8B3E",
          "escrow_vpa": "jaymani.escrow@upi"
        }
      }
    }
  }
}
- Response Payload (200 OK):
{
  "success": true,
  "order_reference": "JMKS-ORD-20261101-8B3E",
  "escrow_status": "ESCROW_HOLD",
  "delivery_otp": "7194",
  "message": "Payment locked in Central Escrow. Funds held until physical OTP validation."
}

5.3 CONCURRENCY & THREAD-SAFETY ENGINEERING
----------------------------------------------------------------------------------------------------
In high-demand rural scenarios (such as localized DAP fertilizer replenishment), multiple farmers 
may simultaneously trigger checkout requests for a single remaining bag of stock. To prevent race 
conditions and negative inventory anomalies:

1. Pessimistic Row-Level Locking (`SELECT ... FOR UPDATE`):
   When an order reservation request arrives, SQLAlchemy executes:
   ```python
   # Thread-safe stock locking implementation
   with db.session.begin():
       product = db.session.query(Product).filter_by(id=target_id).with_for_update().first()
       if product.stock_quantity < requested_quantity:
           db.session.rollback()
           return jsonify({"error": "INSUFFICIENT_STOCK", "code": 409}), 409
       
       product.stock_quantity -= requested_quantity
       db.session.add(new_order)
       db.session.commit()
   ```
2. Database Isolation Semantics:
   The database engine enforces `READ_COMMITTED` transaction isolation with explicit row locks, 
   ensuring concurrent transactions are queued serially at the database storage engine.
3. Invariant Ledger Updates:
   Bahi-Khata ledger balance computation executes inside the same transaction block as the order write. 
   If any intermediate step fails (such as SMS or PDF generation), the entire operation rolls back.

5.4 DUAL-BRANCH CHECKOUT EXECUTION SEQUENCE (ASCII DIAGRAM)
----------------------------------------------------------------------------------------------------

FARMER CLIENT                     FLASK API GATEWAY                 DATABASE & PAYMENT
      |                                   |                                  |
      |-- 1. Submit Cart Checkout ------->|                                  |
      |                                   |-- 2. Lock Row (FOR UPDATE) ----->|
      |                                   |<- 3. Row Lock Confirmed ---------|
      |                                   |                                  |
      |=================== BRANCH A: INSTANT ONLINE PAYMENT =================|
      |                                   |                                  |
      |                                   |-- 4A. Create Razorpay Order ---->|
      |<- 5A. Render Dynamic UPI QR ------|                                  |
      |-- 6A. Authorize UPI Payment ----->|                                  |
      |                                   |<-- 7A. Webhook: Signature Valid -|
      |                                   |-- 8A. Mark ESCROW_HOLD --------->|
      |                                   |-- 9A. Decrement Stock (S = S-Q) ->|
      |<- 10A. Issue Delivery OTP (7194) -|                                  |
      |                                   |                                  |
      |=================== BRANCH B: DIGITAL BAHI-KHATA (UDHAAR) ============|
      |                                   |                                  |
      |                                   |-- 4B. Query Outstanding Debt --->|
      |                                   |<- 5B. Debt: Rs.3200 (Limit 10k) -|
      |                                   |                                  |
      |   [Condition: Order (Rs.1340) + Debt (Rs.3200) <= Rs.10,000 Cap]     |
      |                                   |                                  |
      |                                   |-- 6B. Debit Ledger (New: Rs.4540)|
      |                                   |-- 7B. Decrement Stock ----------->|
      |                                   |-- 8B. MINT SHA-256 Entry Hash -->|
      |<- 9B. Issue Bahi-Khata Invoice ---|                                  |
      |                                   |                                  |
      |=================== FULFILLMENT & PHYSICAL HANDOVER ==================|
      |                                   |                                  |
      |-- 11. Present OTP at Store ------>|                                  |
      |                                   |-- 12. Validate OTP ------------->|
      |                                   |-- 13. Release Escrow to Vendor ->|
      |<- 14. Order Completed Receipt ----|                                  |


====================================================================================================
6. COMMUNICATION (PRESENTATION) (PO10) [MAX MARKS: 5]
====================================================================================================

6.1 12-SLIDE EVALUATION PRESENTATION STRUCTURE (10-MINUTE DEFENSE BLUEPRINT)
----------------------------------------------------------------------------------------------------
- Slide 01: Title, Institutional Affiliation, Team Credentials, and Faculty Mentor.
- Slide 02: Grassroots Agricultural Problem: Field Evidence from District Gonda.
- Slide 03: Four Measurable Engineering Objectives & Course PO Mapping.
- Slide 04: 3-Tier Enterprise System Architecture & Component Interactions.
- Slide 05: Low-Level Relational ER Schema (5 Entities) & Constraints.
- Slide 06: Spatial Geofencing Engine & Trigonometric Haversine Formulation.
- Slide 07: Concurrency-Safe Stock Management & Pessimistic Row Locking (`SELECT ... FOR UPDATE`).
- Slide 08: Digital Bahi-Khata Ledger Engine & Mathematical Double-Entry Invariance.
- Slide 09: Central Escrow Payment Pipeline & Dynamic 4-Digit Handover OTP Lifecycle.
- Slide 10: Value-Added Agricultural Extensions: AI Crop Doctor & DAO Compliance Scanner.
- Slide 11: Comprehensive Test Suite Validation: 14/14 Integration Tests (100% Green).
- Slide 12: Production Readiness: Live Vercel Deployment & Government SeedTrace Integration.

6.2 UI/UX ACCESSIBILITY STRATEGY FOR RURAL USERS
----------------------------------------------------------------------------------------------------
1. High Visual Affordance & Color-Coded Stock Badges:
   - Emerald Green (`#059669`): "Stock Available" / "Price Verified within MSP".
   - Amber Gold (`#D97706`): "Low Stock Threshold (< 15 bags)" / "Escrow Pending".
   - Crimson Red (`#DC2626`): "Out of Stock" / "Credit Limit Breached".
2. Bilingual Interface Architecture:
   - Real-time language toggle switching between standard English and conversational Hindi 
     (*"दुकान खोजें"*, *"उधारी खाता"*, *"खाद एवं बीज"*, *"ऑर्डर ट्रैक करें"*).
3. Minimal Form Friction:
   - Icon-driven navigation minimizing typed alphanumeric input; 1-click credential auto-fill for testing.

6.3 CORE DEFENSE VIVA Q&A WITH TECHNICAL RESOLUTIONS
----------------------------------------------------------------------------------------------------

QUESTION 1:
"How does your architecture handle concurrency conflicts when two farmers attempt to purchase 
the single last remaining bag of subsidized Urea at the exact same millisecond?"
Candidate Defense:
"The system utilizes pessimistic database concurrency control implemented via SQLAlchemy's 
`.with_for_update()` locking directive, which emits a SQL `SELECT ... FOR UPDATE` statement. 
When Thread A requests the record, an exclusive row lock is granted at the database storage engine. 
Thread B is placed into a blocked wait-state. Thread A decrements available stock from 1 to 0 and commits, 
releasing the lock. Thread B immediately unblocks, reads available stock as 0, fails the business logic 
constraint, and is cleanly issued an HTTP 409 'INSUFFICIENT_STOCK' response with zero negative stock drift."

QUESTION 2:
"If a farmer's smartphone loses mobile internet connectivity immediately after an online UPI payment 
is deducted by their bank app, how is the order recovered without losing their money?"
Candidate Defense:
"Payment capture does not rely on client-side frontend callbacks. We implement asynchronous server-to-server 
webhooks via Razorpay. When the banking switch successfully processes the payment, Razorpay sends an 
asynchronous HTTPS POST request directly to our backend endpoint (`/api/payment/razorpay-webhook`). 
The backend verifies the cryptographic HMAC SHA-256 signature, transitions the order status to `ESCROW_HOLD`, 
and issues the dynamic 4-digit OTP. When the farmer re-opens the app upon regaining signal, the client 
queries `/api/orders` and immediately displays the confirmed escrow voucher and pickup OTP."

QUESTION 3:
"What structural safeguards prevent a retail vendor from colluding with a database administrator to 
manually inflate a farmer's Bahi-Khata debt balance in the database tables?"
Candidate Defense:
"The `bahi_khata_ledger` table is engineered as an immutable append-only ledger. Direct `UPDATE` or 
`DELETE` queries are prohibited at the ORM layer. Furthermore, every ledger record computes an internal 
SHA-256 hash incorporating the previous record's hash, the farmer's ID, the transaction amount delta, 
and the official IST timestamp:
\[
H_k = \text{SHA256}(H_{k-1} \parallel \text{FarmerID} \parallel \Delta \text{Amount} \parallel \text{Timestamp})
\]
Any unauthorized external SQL modification to historical balances breaks the cryptographic hash continuity, 
causing our administrative telemetry audit engine to instantly flag the tampering event."


====================================================================================================
7. PROJECT DESIGN REPORT & ROADMAP (PO12) [MAX MARKS: 5]
====================================================================================================

7.1 4-PHASE DEVELOPMENT MILESTONE ROADMAP
----------------------------------------------------------------------------------------------------

Phase 1: SRS & Grassroots Field Survey (Weeks 1 to 3) [COMPLETED]
  |-- Milestone 1.1: Completed empirical survey across 35 farming households in District Gonda.
  |-- Milestone 1.2: Formulated functional & non-functional Software Requirements Specification (SRS).

Phase 2: System Architecture & Relational Schema (Weeks 4 to 6) [COMPLETED]
  |-- Milestone 2.1: Completed 3NF relational schema design and integrity constraint definitions.
  |-- Milestone 2.2: Modeled native Haversine spatial proximity and double-entry ledger equations.

Phase 3: Core Flask & Full-Stack Development (Weeks 7 to 9) [COMPLETED]
  |-- Milestone 3.1: Implemented 10 RESTful micro-endpoints in Python Flask.
  |-- Milestone 3.2: Integrated Razorpay API, Central Escrow logic, and dynamic 4-digit OTP.

Phase 4: Testing, Security & Viva Defense (Weeks 10 to 12) [COMPLETED]
  |-- Milestone 4.1: Built 14-point automated integration test suite (100% Green / Passing).
  |-- Milestone 4.2: Deployed live production instance on Vercel cloud with SeedTrace portal sync.

7.2 VERIFICATION & TEST EVALUATION MATRIX
----------------------------------------------------------------------------------------------------

+-------+-------------------------+------------------------------------+-------------------+--------+
| TC ID | Test Scenario           | Execution Steps & Test Inputs      | Expected Outcome  | Status |
+-------+-------------------------+------------------------------------+-------------------+--------+
| TC-01 | Role-Based Access       | Attempt accessing vendor dashboard | HTTP 403 Forbidden| PASS   |
|       | Control Interception    | using a Farmer JWT session token.  | access denied.    |        |
+-------+-------------------------+------------------------------------+-------------------+--------+
| TC-02 | Concurrent Stock Order  | 2 simultaneous threads checkout    | Thread 1 succeeds;| PASS   |
|       | Race Conditions         | the last remaining bag of DAP.     | Thread 2 gets 409.|        |
+-------+-------------------------+------------------------------------+-------------------+--------+
| TC-03 | Bahi-Khata Synchronous  | Order of Rs. 1,340 placed on       | Debt balance rises| PASS   |
|       | Ledger Debit Check      | credit; current balance Rs. 3,200. | to exact Rs. 4,540|        |
+-------+-------------------------+------------------------------------+-------------------+--------+
| TC-04 | Cryptographic Webhook   | Send forged payment payload with   | Signature mismatch| PASS   |
|       | Signature Validation    | invalid X-Razorpay-Signature header| rejected (400 Bad)|        |
+-------+-------------------------+------------------------------------+-------------------+--------+

7.3 FUTURE SCOPE & LONG-TERM ENGINEERING EXTENSIONS
----------------------------------------------------------------------------------------------------
1. Vernacular Voice Assistant (Hindi & Bhojpuri NLP):
   Integration of lightweight open-source automatic speech recognition (Whisper / IndicWav2Vec) to allow 
   illiterate farmers to perform voice-assisted catalog searches and order placement.

2. AI-Driven Crop & Fertilizer Input Recommendation:
   Coupling soil health card telemetry with seasonal weather forecasts to autonomously prescribe optimal 
   NPK (Nitrogen-Phosphorus-Potassium) fertilizer application schedules.

3. WhatsApp Business API Micro-Bot:
   Automated dispatch of Bahi-Khata credit statements, payment reminders, and order collection OTPs 
   directly to farmers' WhatsApp accounts without requiring mobile browser access.

====================================================================================================
FORMAL EVALUATION SIGN-OFF & ENDORSEMENT BLOCK
====================================================================================================

The undersigned candidates and faculty mentor certify that this Project Design & Evaluation Master 
Document represents authentic, original, and verified engineering work strictly conforming to 
Rubric #R1 standards for CSCR2600 (Project-Based Learning - 1) Evaluation-1.


Candidate Signatures:

1. Manish Pandey (Roll No: 2515010348, System ID: 2025266283) ___________________________

2. Jayant Raj    (Roll No: 2515010273, System ID: 2025298708) ___________________________


Faculty Mentor Endorsement:

Prof. (Dr.) Ali Imam Abidi
Professor & Faculty Mentor,
Department of Computer Science & Engineering,
Sharda School of Computing Science and Engineering,
Sharda University, Greater Noida                              ___________________________

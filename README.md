# Frappe Developer Certification — Day 4: Final Assignment

**Site:** navari.local | **App:** airplane_mode | **Framework:** Frappe v16

---

## Part 1: Crew Members & Gate Numbers
- Added `Flight Crew Member` child table (Crew Member → Link to Employee, Role → Select) to Airplane Flight
- Added `Gate Number` field (Data) to Airplane Ticket
- Added `Gate Number` field to Airplane Flight
- Background job: when flight's gate number changes, updates gate number in all linked tickets via `frappe.enqueue`

## Part 2: Airport Shop Management Module

### Module Def: Airport Shop Management

### DocTypes Created
- **Shop**: Shop Name, Shop Number, Airport, Shop Type, Tenant Name, Tenant Email, Tenant Phone, Rent Amount, Contract Start/Expiry Date, Area, Status (Available/Occupied), Is Published?
- **Shop Type**: Name, Enabled (Check)
- **Shop Rent Payment**: Shop, Tenant Name (fetch), Rent Amount, Payment Date, Month, Year
- **Shop Lead**: Shop, Name, Email, Phone, Message
- **Airport Shop Settings** (Single): Default Rent Amount, Enable Rent Reminders

### Features
- Rent tracking per month with rent receipt print format
- Shops count per airport (via connections)
- Available vs Occupied tracking
- Rent reminders via scheduler (monthly) if enabled in settings
- Print format: "Rent Receipt" for Shop Rent Payment

### Web Portal
- `/shops` — List of published shops
- `/shops/shop-001` — Shop detail page with "Submit a Lead" link
- `/shop-lead-web-form` — Web form for collecting shop leads
- Custom CSS: `shops.css` (no base web.html inheritance)

### Shop Types (Fixtures)
- Stall, Walk-through, Normal (created out of the box via fixtures)
- Shop Type link filtered to show only enabled types (set_query)

### REST API
- GET `/api/resource/Shop` — List all shops (all fields)
- POST `/api/resource/Shop` — Create new shop
- Authentication via API key/secret or session

## Part 3: Shop Types
- Shop Type DocType with Enabled? checkbox
- Link field on Shop filtered to show only enabled types
- Fixtures: Stall, Walk-through, Normal

## Submission
- Compressed app folder: airplane_mode
- Demo video: (to be recorded)

## Advanced Frappe
- Debugging, Realtime, Caching documentation
- Query Builder, Reports documentation

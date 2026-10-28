# ✈️ Airplane Mode — Frappe Developer Certification Project

A full-featured Frappe Framework application built across 4 days of the **Frappe Developer Certification Program**. Covers DocTypes, controllers, web views, reports, roles/permissions, REST API, background jobs, and a web portal.

## 📋 Features

### Core (Days 1–2)
- **Airline, Airplane, Airport, Flight Passenger, Airplane Ticket** DocTypes
- Auto-naming: `IndiGo-001`, `IndiGo-001-BLR-to-BOM-001`
- Fetch-from fields, submittable tickets, status tracking
- **Airplane Flight** with web view (list + detail pages)
- **Add-ons** system (child table with duplicate prevention)
- Total amount calculation (Flight Price + Add-ons)
- Capacity check (prevents overbooking)
- Seat auto-assignment
- **Flight Crew Member** tracking
- Gate number sync via background jobs

### Reports (Day 3)
- **Airplanes by Airline** (Report Builder)
- **Add-on Popularity** (Query Report with SQL)
- **Revenue by Airline** (Script Report with Donut chart)

### Airport Shop Management (Day 4)
- **Shop** DocType with tenant info, contract details, physical properties
- **Shop Type** with fixtures (Stall, Walk-through, Normal)
- Rent payment tracking + rent receipt print format
- Rent reminders via scheduler
- **Global settings** (Single DocType): default rent, enable/disable reminders
- **Web portal**: `/shops` list, shop detail, shop lead web form
- Custom CSS styling

### Web & API
- Web view pages for flights (`/flights`, `/indigo-001-00001`)
- Show Me Colors page (`/show-me?color=red`)
- Shop web portal (`/shops`, `/shops/shop-001`)
- Web form for flight booking and shop leads
- REST API for shop CRUD operations
- System notifications (flight departure alerts)

### Roles & Permissions
- Airport Authority Personnel, Fleet Manager, Travel Agent, Flight Crew Member
- Travel Agent restricted to own records (if_owner)
- Field-level visibility (Initial Audit Completed)

## 🏗️ Tech Stack
- **Framework:** Frappe v16
- **Apps:** ERPNext, HRMS
- **Database:** MariaDB
- **Cache:** Redis

## 🚀 Setup
```bash
bench new-site mysite.local
bench --site mysite.local install-app airplane_mode
bench --site mysite.local set-config developer_mode 1
```

## 📁 Project Structure
```
airplane_mode/
├── airplane_mode/          # Core module
│   ├── doctype/            # All DocTypes
│   ├── patches/            # Data patches
│   ├── templates/pages/    # Portal pages
│   └── www/                # Web pages
├── airport_shop_management/ # Shop management module
│   ├── doctype/            # Shop, Shop Type, etc.
│   └── rent_reminder.py    # Scheduler
├── fixtures/               # Shop Type fixtures
└── public/css/             # Static assets
```

## 📄 License
MIT

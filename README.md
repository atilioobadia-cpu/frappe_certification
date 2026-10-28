# Airplane Mode

A full-featured Frappe Framework application built as part of the Frappe Developer Certification Program.

## Features

- **Flight Management** — Airlines, Airplanes, Airports, Flights, and Tickets with auto-naming, fetch-from fields, and status tracking
- **Ticket Booking** — Capacity checks, seat assignment, add-ons with duplicate prevention, total amount calculation
- **Web Portal** — Flight listing, flight details, ticket booking web form, Show Me Colors page
- **Airport Shop Management** — Shop tracking, rent payments, receipts, rent reminders, shop leads
- **Reports** — Airplanes by Airline, Add-on Popularity, Revenue by Airline (with Donut chart)
- **Roles & Permissions** — Airport Authority, Fleet Manager, Travel Agent, Flight Crew Member
- **REST API** — Shop CRUD operations with authentication

## Tech Stack

- Frappe Framework v16
- ERPNext, HRMS
- MariaDB, Redis

## Setup

```bash
bench new-site mysite.local
bench --site mysite.local install-app airplane_mode
bench --site mysite.local set-config developer_mode 1
```

## License

MIT

# Service App for ERPNext 🚀

A lightweight Service Planning module for ERPNext that allows managers to schedule service projects with auto-generated tasks.

## Features
- ✅ Service Project Doctype (with schedule config)
- ✅ Service Task (Child Table)
- ✅ Auto task generation (Daily, Weekly, or X days)
- ✅ Role-based & Organization-based access
- ✅ Permission Query Conditions via server script

## How it Works
1. Create a Service Project
2. On Submit or Save → Tasks are generated automatically for the next 7 days
3. Tasks are filtered per user role + organization

## Permissions Logic
- 👤 `System Manager`, `Projects Manager` → See all
- 👥 Others → See tasks only for their own role + company

---

Built for demo / learning purpose by `tecteam12`

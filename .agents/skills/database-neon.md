---
description: How to set up and manage the Neon PostgreSQL database for the Movie Ticket Booking project
---

# Database — Neon PostgreSQL

## Overview
This project uses **Neon** as the managed PostgreSQL provider. Neon provides serverless Postgres with features like branching, auto-scaling, and a generous free tier.

## Setup Steps

### 1. Create a Neon Project
1. Go to [https://console.neon.tech](https://console.neon.tech)
2. Sign up / Log in
3. Click **"New Project"**
4. Name it: `movie-ticket-booking`
5. Choose the closest region to your users
6. Copy the connection string — you'll need it for the backend

### 2. Connection String Format
```
postgresql://<user>:<password>@<host>/<dbname>?sslmode=require
```
Store this in environment variables, **never** commit it to source code.

### 3. Database Schema Design
Schema files go in the `db/` folder:
- `db/schema.sql` — Full schema definition
- `db/seed.sql` — Initial seed data (movies, theaters, etc.)
- `db/migrations/` — Incremental migration scripts

### 4. Key Tables (to be designed)
- `users` — User accounts
- `movies` — Movie listings
- `theaters` — Theater/hall information
- `shows` — Showtimes linking movies to theaters
- `seats` — Seat layout per theater
- `bookings` — Ticket bookings
- `payments` — Payment records

### 5. Neon-Specific Tips
- Use **connection pooling** (Neon provides a pooled connection string)
- Use the **branching** feature for dev/staging environments
- Enable **auto-suspend** on the free tier to save compute hours

## Files in `db/`
| File | Purpose |
|---|---|
| `schema.sql` | Full database schema |
| `seed.sql` | Sample data for development |
| `migrations/` | Versioned migration scripts |
| `.env.example` | Template for DB connection vars |

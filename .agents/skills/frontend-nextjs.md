---
description: How to set up and develop the Next.js frontend for the Movie Ticket Booking project, deployed on Vercel
---

# Frontend — Next.js on Vercel

## Overview
The frontend is a **Next.js** application deployed on **Vercel**. The design philosophy is to use **HTML/CSS as much as possible** — leveraging vanilla CSS for styling instead of utility frameworks, and keeping components simple with semantic HTML.

## Design Principles
- **HTML/CSS first**: Use vanilla CSS (no Tailwind unless explicitly requested)
- **Semantic HTML**: Proper `<header>`, `<main>`, `<section>`, `<article>` usage
- **CSS Modules or Global CSS**: For scoped and maintainable styles
- **Minimal JS**: Use JavaScript only when interactivity is required
- **Premium aesthetics**: Modern design with gradients, animations, dark mode

## Setup Steps

### 1. Initialize the Next.js Project
```bash
cd frontend/
npx -y create-next-app@latest ./ --js --no-tailwind --eslint --app --src-dir --no-turbopack --import-alias "@/*"
```

### 2. Project Structure
```
frontend/
├── src/
│   ├── app/
│   │   ├── layout.js         # Root layout
│   │   ├── page.js           # Home page
│   │   ├── page.module.css   # Home page styles
│   │   ├── globals.css       # Global styles & design tokens
│   │   ├── movies/
│   │   │   └── [id]/
│   │   │       └── page.js   # Movie detail page
│   │   ├── booking/
│   │   │   └── page.js       # Seat selection & booking
│   │   └── profile/
│   │       └── page.js       # User profile
│   └── components/
│       ├── Header.js
│       ├── Header.module.css
│       ├── MovieCard.js
│       ├── MovieCard.module.css
│       ├── SeatMap.js
│       └── Footer.js
├── public/
│   └── images/
├── next.config.js
└── package.json
```

### 3. Key Pages
| Route | Description |
|---|---|
| `/` | Home — featured movies, search |
| `/movies/[id]` | Movie details & showtimes |
| `/booking` | Seat selection & checkout |
| `/profile` | User bookings & account |
| `/login` | Login / Register |

### 4. Vercel Deployment
1. Push code to GitHub
2. Go to [https://vercel.com](https://vercel.com)
3. Import the repo → set root directory to `frontend/`
4. Vercel auto-detects Next.js
5. Add env vars for the backend API URL
6. Deploy!

### 5. Connecting to Backend
- Use `fetch()` or Next.js server actions to call the FastAPI backend
- Store `NEXT_PUBLIC_API_URL` in `.env.local`
- Example: `const res = await fetch(\`${process.env.NEXT_PUBLIC_API_URL}/movies\`)`

### 6. Styling Guidelines
- Use **CSS custom properties** (variables) for theming
- Use **CSS Modules** (`*.module.css`) for component-scoped styles
- Use `globals.css` for design tokens (colors, fonts, spacing)
- Prefer **CSS Grid** and **Flexbox** for layouts
- Use **CSS animations** and **transitions** for micro-interactions

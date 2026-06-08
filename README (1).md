# Kanban Board

A minimal, dark-themed Kanban board built with vanilla HTML, CSS, and JavaScript — no dependencies, no build step, one file.

## Features

- **3 columns** — To Do / In Progress / Done
- **Add cards** — type a title, pick a starting column, press Enter or click `+ Add Card`
- **Move cards forward** — each card has a `→ Next Column` button to advance it
- **Drag & drop** — drag any card into any column
- **Delete cards** — hover a card to reveal the `✕` button
- **Persistent storage** — cards survive page refreshes via `localStorage`
- **Responsive** — stacks to single column on mobile

## How to run

Just open `kanban.html` in any browser — no server or install needed.

```
open kanban.html        # macOS
start kanban.html       # Windows
xdg-open kanban.html    # Linux
```

## File structure

```
kanban.html    ← everything lives here (HTML + CSS + JS)
README.md
```

## Usage

| Action | How |
|--------|-----|
| Add a card | Type in the top bar, select column, press **Enter** or **+ Add Card** |
| Advance a card | Click **→ In Progress** or **→ Done** on the card |
| Move freely | Drag the card and drop it into any column |
| Delete a card | Hover the card → click **✕** |
| Reset board | Open DevTools → `localStorage.removeItem('kanban_cards')` → refresh |

## Design notes

- Dark industrial aesthetic with neon accent colors per column (lime / cyan / magenta)
- Cards are color-coded by column via a left accent stripe
- Done cards receive a strikethrough to signal completion
- Toast notifications confirm every action

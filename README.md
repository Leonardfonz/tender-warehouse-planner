# Tender & Warehouse Planner

Single-page HTML/JS tool for drafting commercial proposals for logistics tenders. Built for Hong Kong operations — all data stays in your browser, nothing is ever uploaded.

## Features

- **Tender Setup** — tender name, client, volumes, SKU count, carton dimensions, pcs per carton
- **Drag-and-Drop Warehouse Visualizer** — grid-based floorplan (80 sqft/cell) with 8 zone types including corridors
- **Shelf & Corridor Configuration** — shelf dimensions (W/D/H), shelves per rack, corridor width — auto-calculates carton/piece capacity
- **Activity-Based Costing** — dynamic labor activities with variable margins, headcount computed from UPH
- **Fixed Overheads** — rent (per sqft, linked to floorplan), MHE, IT/WMS, packaging, utilities, security, insurance
- **P&L Dashboard** — real-time summary, triggered by "Update All Calculations" button (not auto-recalc)
- **Excel Export** — single consolidated .xlsx with 5 tabs via SheetJS

## Currency & Measurements

- **Currency:** HK$ (Hong Kong Dollar)
- **Floorplan:** sqft (square feet)
- **Carton dimensions:** inches
- **Shelf/corridor:** feet

## Usage

Open `index.html` in any modern browser. Edit your data, place zones on the grid, then click **Update All Calculations**. No build step, no server, no dependencies (Tailwind and SheetJS load from CDN).

## Tech Stack

- **Tailwind CSS** (CDN) — styling
- **SheetJS** (CDN) — Excel export
- **Vanilla JavaScript** — all logic
- **Zero backend** — fully client-side

## License

MIT

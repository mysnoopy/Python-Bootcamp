# Python Bootcamp — Changelog

## Session: 2025-03-07

### 🐛 Bug Fixes

**Phase 5 — FastAPI Simulator**
- Fixed POST `/books` always returning `"Validation error: all fields required"` even when fields were filled
  - Root cause: React controlled inputs (`value={state}`) were losing state due to component remounts on navigation
  - Fix: Replaced controlled inputs with uncontrolled refs (`ref={postTitleRef}`, `defaultValue=""`)
  - `doPost` now reads directly from DOM via `postTitleRef.current.value` — bypasses React state entirely
- Fixed synthetic event bug across all functional state updaters
  - `onChange={e => setState(s => ({...s, key: e.target.value}))}` — `e.target` is nullified by the time the updater runs
  - Fix: Capture value first — `onChange={e => { const v = e.target.value; setState(s => ({...s, key: v})) }}`
  - Applied to: Simulator POST inputs, Tutorial inputs, API key settings inputs
- Replaced `.map()` input loop with explicit individual inputs to eliminate computed key closure issues

**Chrome Extension Debugging**
- Enabled "Allow access to file URLs" in Claude in Chrome extension for live debugging on `file://` pages

### ✅ Confirmed Working
- Phase 5 Simulator: GET /, GET /books, POST /books (201), DELETE /books/{id} (200/404)
- Live database panel updates correctly after POST and DELETE
- Response log shows correct status codes and request/response bodies
- All other phases (1–4, 6–7) previously confirmed working

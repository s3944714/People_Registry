# People Registry CLI

A beginner-to-expert **Python command-line mini project** that starts as a simple “name + age” script and gradually becomes a real, portfolio-ready CLI tool.

You’ll build a small registry that can **add, list, search, update, delete**, and eventually **save/load data**, **export to CSV**, **log actions**, and support **CLI commands**.

---

## Why this is a real-world mini project

This project mirrors practical software engineering work:
- **Validation & reliability**: handle messy user input without crashing
- **CRUD operations**: Create / Read / Update / Delete records (common in apps)
- **Persistence**: save/load data across sessions
- **Automation-friendly**: export CSV and support non-interactive CLI commands
- **Maintainability**: clean structure, readable code, logs, (optional) tests

### Real-life use cases
- **Small clubs/teams**: keep a lightweight member list and ages
- **Event admin**: register attendees and export to spreadsheets
- **Learning tool**: practice building structured software from scratch

---

## Features (as you progress)

- Collect a person’s name + age and print a formatted “profile”
- Strong input validation (name rules, realistic age rules)
- Menu-driven workflow (interactive mode)
- Store multiple people in memory (list)
- Search, update, and delete records (CRUD)
- Sorting and statistics (min/max/average, age groups)
- Save/load records to disk (JSON recommended)
- Export to CSV (Excel-friendly)
- Logging (audit trail of actions and invalid attempts)
- Command mode (CLI arguments) for automation

---

## Tech goals (skills you’ll practice)

- Variables, input/output, string formatting
- If/elif/else logic
- Loops (while/for) and program flow
- Functions and separation of concerns
- Data structures (lists/dicts)
- File I/O and data formats (JSON/CSV)
- Logging and debugging habits
- CLI UX design (prompts, menus, arguments)
- Testing mindset (manual tests + optional unit tests)

---

## Getting started

### Requirements
- Python **3.10+** recommended

### Run modes (you will implement these)
- **Interactive mode**: user sees a menu and answers prompts
- **Command mode**: user runs commands like `list`, `add`, `search` from the terminal

> Add exact commands to this README once you implement CLI mode (Level 25).

---

## Suggested project structure
people-registry-cli/
README.md
src/
main.py # entry point
registry.py # core operations (add/list/search/update/delete)
validation.py # input validation + parsing
storage.py # save/load/export
data/
people.json # saved records
people.csv # export output
logs/
app.log # logging output
tests/ # optional


---

## Challenge Ladder (Beginner → Expert)

Complete these in order. Each rung should work before moving on.

### Level 1–5: Absolute beginner
1. **Hello v1**: Ask for name + age, print age+1  
2. **Pretty output**: Print a clean “profile card” (multi-line formatting)  
3. **Name cleanup**: Trim spaces; reject empty name  
4. **Age math**: Show age next year + age in months  
5. **Custom greeting**: Change greeting based on first letter of name (A–M vs N–Z)  

### Level 6–10: Loops + validation
6. **Safe age input**: Keep asking until age is a valid integer  
7. **Reasonable age rule**: Reject ages < 0 or > 120  
8. **Retry limit**: Only allow 3 invalid attempts before quitting  
9. **Continue prompt**: Allow entering multiple people in one run  
10. **Main menu v1**: Menu with (Add person, Quit)  

### Level 11–15: Lists + basic “app” behavior
11. **Store people**: Keep multiple (name, age) entries in a list  
12. **List view**: Show all stored people in a numbered list  
13. **Search**: Find a person by name (case-insensitive)  
14. **Update**: Update a person’s age (select by name or number)  
15. **Delete**: Delete a person safely with confirmation  

### Level 16–20: Sorting + stats + data quality
16. **Sorting**: Sort by age (and/or name) and display  
17. **Stats**: Compute min/max/average age  
18. **Groups**: Count how many are child/teen/adult  
19. **Duplicate names policy**: Decide and enforce a duplicate-name rule  
20. **Smart inputs**: Accept age inputs like `"20 "` or `"20 years"` (clean + validate)  

### Level 21–25: Persistence + real-world features
21. **Save to file**: Save records automatically on exit  
22. **Load on start**: Load records automatically when program starts  
23. **Export**: Export records to CSV  
24. **Logs**: Log actions (add/update/delete/invalid attempts) to a file  
25. **CLI mode**: Support commands like `add/list/search` without interactive prompts  

---

## Definition of Done (for each level)

A level is “done” when:
- It works for normal inputs
- It handles edge cases without crashing
- It prints helpful messages to the user
- Code is readable (consistent naming, small functions)
- You tested it with the checklist below

---

## Manual test checklist (edge cases)

Use these every time you add a new feature:
- Name is empty: `""`
- Name has spaces: `"  rob  "`
- Name has mixed case: `"rOb dE gUzMaN"`
- Age is not a number: `"abc"`
- Age is negative: `-5`
- Age is huge: `999`
- Age has text: `"20 years"` *(once smart parsing exists)*
- Duplicate name entries (same spelling, different case)

---

## Roadmap (recommended build order)

1. **Setup repo + folders** (`src/`, `data/`, `logs/`) and add this README  
2. Implement **Levels 1–5** (core flow + clean output)  
3. Implement **Levels 6–10** (validation + menu)  
4. Implement **Levels 11–15** (CRUD in memory)  
5. Implement **Levels 16–20** (sorting + stats + quality rules)  
6. Implement **Levels 21–25** (save/load/export/logs/CLI)  
7. Polish: refactor into modules, add usage examples, optional tests  

---

## Portfolio checklist (when you’re “mini-project ready”)

You’re in a strong spot when you have:
- Save/load (Level 21–22)
- Export to CSV (Level 23)
- Logs (Level 24)
- CLI command mode (Level 25)
- Clean project structure + clear README usage section
- Consistent validation and friendly error messages

---

## License
Choose a license (MIT is common for learning projects).


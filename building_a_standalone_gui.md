# Building a Standalone GUI App from Your Pandas Script

## The Idea

You have a working Python script that loads, transforms, and analyses data with pandas. This guide shows you how to wrap it in a simple graphical interface and package it into a single executable file that runs on any machine — no Python installation required.

---

## The Two Components

**Tkinter** is Python's built-in GUI library — it ships with Python so there is nothing to install. You use it to build windows, buttons, file pickers, and result displays around your existing pandas logic. Your data processing code does not change; tkinter just gives users a way to interact with it without touching the terminal.

**PyInstaller** is the most widely-used packaging tool for Python. It bundles your script, all its dependencies (including pandas, numpy, and tkinter), and a Python interpreter into a single folder or a single `.exe` / `.app` file. The person running it does not need Python installed.

---

## Minimal Working Pattern

The core pattern is: keep your data logic in plain functions, then call those functions from your GUI. Never mix pandas code and tkinter code in the same block.

```python
import tkinter as tk
from tkinter import filedialog, messagebox
import pandas as pd

# --- Your data logic (unchanged from your pandas script) ---

def process_file(path):
    df = pd.read_csv(path)
    df["flag"] = df["value"] > 100
    return df

# --- GUI layer ---

def on_open():
    path = filedialog.askopenfilename(filetypes=[("CSV files", "*.csv")])
    if not path:
        return
    df = process_file(path)
    result_label.config(text=f"Loaded {len(df)} rows. Flags: {df['flag'].sum()}")

root = tk.Tk()
root.title("Data Processor")
root.geometry("400x200")

tk.Button(root, text="Open CSV", command=on_open).pack(pady=20)
result_label = tk.Label(root, text="No file loaded yet.")
result_label.pack()

root.mainloop()
```

---

## Packaging with PyInstaller

Install PyInstaller once:

```
pip install pyinstaller
```

Build a single executable from your script:

```
pyinstaller --onefile --windowed my_app.py
```

`--onefile` bundles everything into one file. `--windowed` suppresses the terminal window on Windows and Mac. Your executable appears in the `dist/` folder after the build completes.

---

## Common Issues to Expect

**pandas not found at runtime** — PyInstaller sometimes misses hidden imports. Fix with:
```
pyinstaller --onefile --windowed --hidden-import pandas my_app.py
```

**App is slow to start** — a `--onefile` build unpacks itself to a temp folder on launch, which takes a few seconds. This is normal. Use `--onedir` instead if startup speed matters more than having a single file.

**File paths break** — if your script references data files with relative paths, they will not resolve correctly inside a packaged app. Use `filedialog.askopenfilename()` to let users pick files at runtime, or look up `sys._MEIPASS` for bundling static files.

---

## Where to Go Next

| Goal | Tool | Starting Point |
|---|---|---|
| Richer GUI components (tables, tabs) | `tkinter.ttk` | `ttk.Treeview` for displaying DataFrames |
| Display charts inside the window | `matplotlib` + `FigureCanvasTkAgg` | matplotlib docs → embedding in Tk |
| More modern-looking GUI | `CustomTkinter` | github.com/TomSchimansky/CustomTkinter |
| Web-based interface instead of desktop | `Streamlit` | streamlit.io — no GUI knowledge needed |
| Cross-platform packaging alternative | `Briefcase` | beeware.org |
| Distributing to Windows with an installer | `NSIS` or `Inno Setup` | wrap around PyInstaller's `--onedir` output |

---

## Recommended Learning Path

Start with the minimal pattern above and get it running. Then try these steps in order:

1. Add a `filedialog` so users can pick their own CSV rather than a hardcoded path.
2. Display a summary of results in a `ttk.Treeview` table widget.
3. Embed a matplotlib chart directly in the window using `FigureCanvasTkAgg`.
4. Run `pyinstaller` and send the executable to someone who does not have Python installed — confirm it works.
5. If you find tkinter limiting, try rebuilding the same app in Streamlit in an afternoon. It is dramatically less code for data-focused tools.

---

The most important mindset shift from scripts to GUI apps: your code no longer runs top to bottom. It waits for events (button clicks, file selections) and responds to them. The `mainloop()` call at the end is what keeps the window open and listening. Everything else hangs off callbacks.
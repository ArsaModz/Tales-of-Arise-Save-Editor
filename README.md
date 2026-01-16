# Tales of Arise Save Editor (PS4)

A specialized desktop application designed to modify **Tales of Arise** PS4 save files. Built with a focus on ease of use and safety, this tool allows you to manipulate currency, character attributes, and your entire inventory via a modern graphical interface.

## ✨ Key Features

### 💰 Currency & Economy

* **Gald Management:** Instantly view and edit your current Gald.
* **One-Click Max:** Includes a "Max" shortcut to set your Gald to 999,999,999 instantly.

### 🎭 Character Attribute Editor

* **Multi-Character Support:** Switch between all party members (Alphen, Shionne, Rinwell, etc.) using a convenient dropdown menu.
* **Stat Modification:** Edit core statistics including:
* Level & XP
* Max HP & CP
* Attack, Defense, Elemental Attack, and Elemental Defense.
* Penetration and Resistance.


* **Batch Operations:** Features "Max This Char" and "Max All Chars" buttons to save time on grinding.

### 📦 Robust Inventory System

* **Database Integration:** Integrated search bar to filter through the extensive `ITEM_DB`.
* **Hex-Based Precision:** Maps item names to their internal Hex IDs (e.g., `4CAFC38C`) for perfect accuracy.
* **Smart Adding:** Automatically finds the next empty slot in your save's inventory block to inject new items.
* **Bulk Import:** "Add All" feature to instantly populate your inventory with every item in the database at max quantity.

---

## 🛠️ Technical Overview

* **UI Framework:** Developed using **PyQt6** for a responsive, high-definition experience.
* **Data Handling:** Utilizes Python's `struct` module for precise Little-endian (`<I`) binary manipulation of `.sav` files.
* **Safety First:**
* **Caching:** Changes are held in a local cache before being committed to the file.
* **Hex Pattern Matching:** Uses unique pattern signatures (`INV_PATT`) to locate data blocks even if save file offsets shift.


* **Modern Styling:** Features a custom CSS-based Dark Theme with amber and blue highlights for better scannability.

---

## 🚀 Getting Started

### Prerequisites

* Python 3.10+
* Required Libraries: `pip install PyQt6`

### Running the Editor

1. Clone this repository.
2. Ensure `utils.py` and `data.py` (containing `ITEM_DB`) are in the same directory.
3. Launch the application:
```bash
python main.py

```



### How to Use

1. **Open:** Load your decrypted PS4 save file.
2. **Edit:** Modify values in the **Character** or **Inventory** tabs.
3. **Save:** Click "Save Changes" to write the binary data back to the file.

---

## 📝 Disclaimer

This tool is for educational and modding purposes only. Please create a backup of your save file before making any changes.

**Developed by:** ArsaModz

# Tales of Arise Save Editor (PS4)

A save editor for *Tales of Arise* (PS4), built with Python and PyQt6. This tool allows players to easily modify character statistics, currency, and inventory items through a user-friendly dark-themed interface.

## 🚀 Features

### 👤 Character Editor

Modify individual stats for all main party members, including **Alphen, Shionne, Rinwell, Law, Kisara, and Dohalim**.

* **Currency Manipulation:** Edit your Gald amount up to 999,999,999.
* **Individual Stat Tuning:** Precisely adjust Level, EXP, Skill Points, HP, Attack, Defense, Penetration, and more.
* **Batch Editing:** One-click buttons to "Max This Character" or "Max All Characters".

### 📦 Inventory Editor

A robust system to manage your items with a built-in searchable database.

* **Searchable Database:** Quickly find items from a hardcoded database of hundreds of entries.
* **Item Management:** Add new items to your save or remove existing ones.
* **Quantity Control:** Edit item quantities directly (up to 99x).
* **Add All Items:** Overwrite your inventory with a full set of every item in the database.

### 🛠 Supported Items

The editor includes an extensive database of game assets, including:

* **Consumables:** Gels, Bottles, Elixirs, and Herbs.
* **Materials:** Cooking ingredients, Zeugle parts, and ores.
* **Equipment:** Weapons, Armors, and Accessories for all characters.
* **Outfits:** Costume items like Straw Hats, Sunglasses, and more.

## 🖥 UI Gallery

The application features a modern dark theme inspired by professional IDEs, utilizing a sleek "Segoe UI" aesthetic with color-coded action buttons (e.g., green for adding items, red for deletions).

## 🛠 Tech Stack

* **Language:** Python 3.x
* **GUI Framework:** PyQt6
* **Data Handling:** Binary file manipulation via `struct`

## 📝 How to Use

1. **Open:** Use the "Open Save File" button to load your decrypted PS4 save data.
2. **Edit:** Navigate between the "Character Editor" and "Inventory Editor" tabs to make your changes.
3. **Save:** Click "Save Changes" to write the modifications back to your file.

---

*Created by ArsaModz* :)

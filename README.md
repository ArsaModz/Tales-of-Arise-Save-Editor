# Tales of Arise Save Editor (PS4)

Developed by **ArsaModz**, this is a powerful desktop application designed to modify *Tales of Arise* save files. The editor provides a modern dark-themed interface to manage your progression, characters, and items with ease.

## 🚀 Features

### **Character Editor**

* **Stats Management**: Modify individual stats for all main characters including Alphen, Shionne, Rinwell, Law, Kisara, and Dohalim.
* **Editable Attributes**: Change Level, EXP, Skill Points, HP, Artes Gauge, Attack, Elemental Attack, Defense, and more.
* **Batch Editing**: Instantly maximize stats for your current character or the entire party with one click.
* **Currency**: Edit your Gald amount up to 999,999,999.

### **Inventory Editor**

* **Extensive Database**: Includes a built-in database of consumables, materials, weapons, and armor.
* **Search & Filter**: Quickly find specific items in the database to add to your save.
* **Item Management**: Add individual items with custom quantities (up to 99), or use the "Add All" feature to unlock every item in the game.
* **Quantity Editing**: Modify the quantity of items already in your inventory directly from the table.

## 🛠️ Tech Stack

* **Language**: Python
* **UI Framework**: PyQt6 (with a custom dark theme)
* **Binary Manipulation**: `struct` for hex data handling

## 📥 Installation

1. Ensure you have **Python 3.x** installed.
2. Install the required dependencies:
```bash
pip install PyQt6

```


3. Run the application:
```bash
python main.py

```



## 📖 How to Use

1. **Open Save**: Click "Open Save File" to load your decrypted PS4 save.
2. **Edit Stats**: Use the "Character Editor" tab to select a character and adjust their values.
3. **Manage Items**: Use the "Inventory Editor" tab to search for items in the database and move them into your save.
4. **Save**: Click "Save Changes" to write the modifications back to your file.

## ⚠️ Requirements

* This tool is designed for **PS4** save files.
* The save file must be **decrypted** (e.g., via Save Wizard or similar tools) before it can be edited.

---

*Disclaimer: This tool is for educational purposes. Always back up your save files before making any modifications.*

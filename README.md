# Tales of Arise Save Editor (PS4)

A powerful, GUI-based save editor for **Tales of Arise** on PlayStation 4, developed by **ArsaModz**. This tool allows you to modify character stats, currency (Gald), and manage your entire inventory with a user-friendly interface powered by PyQt6.

## 🚀 Features

### 💰 Currency & Character Management

* **Gald Editor:** Instantly set your Gald to the maximum (999,999,999).
* **Multi-Character Support:** Edit stats for Alphen, Shionne, Rinwell, Law, Kisara, and Dohalim.
* **One-Click Maxing:** "Max All" or "Max Selected" buttons to instantly cap level, EXP, HP, and combat stats.

### 📊 Stat Editing

Modify individual stats for any character, including:

* Level & EXP
* Skill Points (SP)
* Current & Max HP
* Artes Gauge
* Attack & Elemental Attack
* Defense & Elemental Defense
* Penetration & Resistance

### 🎒 Inventory Master

* **Massive Item Database:** Includes Consumables, Materials, Weapons, Armor, Valuable Items, and Costumes.
* **Search Function:** Quickly find items by name using the real-time search bar.
* **Inventory Control:** Add new items, update quantities (up to 99), or remove items from your save.
* **Add All:** A specialized function to populate your inventory with every item in the database at once.

---

## 🛠️ Requirements

* **Python 3.13.11**
* **PyQt6:** Used for the graphical interface.
* **Decrypted PS4 Save:** You must provide a decrypted `.sav` file (typically extracted via Save Wizard or similar tools).

---

## 💻 Installation

1. **Clone the repository:**
```bash
git clone https://github.com/YourUsername/TOA-Save-Editor.git
cd TOA-Save-Editor

```


2. **Install dependencies:**
```bash
pip install PyQt6

```


3. **Run the application:**
```bash
python main.py

```



---

## 📖 How to Use

1. **Open Save:** Click the "Open Save" button and select your decrypted `SaveData.sav`.
2. **Modify:** * Use the **Character** tab to boost stats or Gald.
* Use the **Inventory** tab to search for items and add them to your bag.


3. **Save Changes:** Click "Save Changes" to write the data back to the file.
4. **Re-sign:** Re-encrypt/sign your save back to your PS4.

---

## ⚠️ Disclaimer

*Always create a backup of your save file before making any modifications.* This tool is provided for educational and personal use. Use it at your own risk.

**Developed by:** ArsaModz

import sys, struct, os, ctypes
from PyQt6.QtWidgets import *; from PyQt6.QtCore import *; from PyQt6.QtGui import QIcon

def res_path(p): return os.path.join(getattr(sys, '_MEIPASS', os.path.abspath(".")), p)

# Configuration & Data
INV_PATT = 'B2C77888'
CHARS = {'Alphen':'EA372703', 'Shionne':'8F509BBB', 'Rinwell':'61FF2EA9', 'Law':'04989211', 'Kisara':'BDA0458C', 'Dohalim':'D8C7F934'}
STATS = {'level:':(16,0,100), 'exp:':(28,0,2949585), 'skill_points:':(60,0,99999999), 'current_health:':(20,0,9999), 
         'max_health:':(92,0,9999), 'artes_gauge:':(228,0,9999), 'attack:':(232,0,9999), 'elemental_attack:':(236,0,9999), 
         'defense:':(240,0,9999), 'elemental_defense:':(244,0,9999), 'penetration:':(248,0,9999), 'resistance:':(252,0,9999)}

# Hardcoded Item Database
ITEM_DB = {
    # Consumables
    'Apple Gel': '010000000000', 'Peach Gel': '020000000000', 'Lemon Gel': '030000000000',
    'Grape Gel': '040000000000', 'Orange Gel': '050000000000', 'Pineapple Gel': '060000000000',
    'Gold Gel': '070000000000', 'Treat': '080000000000', 'Heavy Treat': '090000000000',
    'Panacea Bottle': '0A0000000000', 'Life Bottle': '0B0000000000', 'Elixir': '0C0000000000',
    'Omega Elixir': '0D0000000000', 'Happy Bottle': '9A0300000000', 'Sage': '9B0300000000',
    'Lavender': '9D0300000000', 'Verbena': '9E0300000000', 'Rosemary': '9F0300000000',
    'Saffron': 'A00300000000', 'Chamomile': 'A10300000000', 'Jasmine': 'A20300000000',
    'Red Sage': 'A30300000000', 'Red Lavender': 'A50300000000', 'Red Verbena': 'A60300000000',
    'Red Rosemary': 'A70300000000', 'Red Saffron': 'A80300000000', 'Red Chamomile': 'A90300000000',
    'Red Jasmine': 'AA0300000000',
    # Materials
    'Wheat': '210000000000', 'Rice': '220000000000', 'Lettuce': '230000000000',
    'Potato': '240000000000', 'Tomato': '250000000000', 'Strawberry': '260000000000',
    'Apple': '270000000000', 'Lemon': '280000000000', 'Scrap Meat': '290000000000',
    'Beef': '2A0000000000', 'Pork': '2B0000000000', 'Chicken': '2C0000000000',
    'Horse Meat': '2D0000000000', 'Sheep Meat': '2E0000000000', 'Rapping Meat': '2F0000000000',
    'Carp': '300000000000', 'Sea Bream': '310000000000', 'Tuna': '320000000000',
    'Salmon': '330000000000', 'Flatfish': '340000000000', 'Mackerel': '350000000000',
    'Boss Fish': '360000000000', 'Arowana': '370000000000', 'Tilapia': '380000000000',
    'Piranha': '390000000000', 'Trout': '3A0000000000', 'Pike': '3B0000000000',
    'Grouper': '3C0000000000', 'Bass': '3D0000000000', 'Pirarucu': '3E0000000000',
    'Catfish': '3F0000000000', 'Mushroom': '400000000000', 'Pepper': '410000000000',
    'Milk': '420000000000', 'Egg': '430000000000', 'Tofu': '440000000000',
    'Demihuman Talon': '4A0000000000', 'Demihuman Muscle': '4B0000000000', 'Large Demihuman Talon': '590000000000',
    'Large Demihuman Bicep': '5A0000000000', 'Spherical Shell': '630000000000', 'Hard Spherical Shell': '640000000000',
    'Beast Mane': '650000000000', 'Wind-Swept Mane': '660000000000', 'Dark Mane': '670000000000',
    'Blistering Fang': '680000000000', 'Granite Fang': '690000000000', 'Icicle Fang': '6A0000000000',
    'Fierce Beast Mane': '6B0000000000', 'Squall Mane': '6C0000000000', 'Demon Mane': '6D0000000000',
    'Punisher\'s Vambrace': '6E0000000000', 'Titanium Vambrace': '6F0000000000', 'Frosty Vambrace': '700000000000',
    'Membrane Wing': '710000000000', 'Paralysis Stinger': '720000000000', 'Incendiary Scale': '730000000000',
    'Mantid Wing': '740000000000', 'Mantid Mucus': '750000000000', 'Mantid Claw': '760000000000',
    'Chameleon Hide': '770000000000', 'Lizard Tongue': '780000000000', 'Lizard Fin': '790000000000',
    'Glowing Lizard Fin': '7A0000000000', 'Clam Tentacle': '7B0000000000', 'Sticky Tentacle': '7C0000000000',
    'Mucus Sac': '7D0000000000', 'Mysterious Tree Sap': '7E0000000000', 'Earth Seed': '7F0000000000',
    'Dark Tree Blood': '800000000000', 'Ossified Stem': '810000000000', 'Clay Fragment': '820000000000',
    'Stone Fragment': '830000000000', 'Granite Fragment': '840000000000', 'Earth Stone': '850000000000',
    'Ice Stone': '860000000000', 'Flame Stone': '870000000000', 'Tempest Stone': '880000000000',
    'Penumbra Stone': '890000000000', 'Raging Storm Beak': '8A0000000000', 'Razor-Tipped Feather': '8B0000000000',
    'Majestic Feather': '8C0000000000', 'Dragon Scale': '8D0000000000', 'Dragon Blood': '8E0000000000',
    'Dragon Flame Sac': '8F0000000000', 'Beast Tail': '900000000000', 'Spirit Tail': '910000000000',
    'Ominous Eyeball': '920000000000', 'Statue Fragment': '930000000000', 'Infused Statue Fragment': '940000000000',
    'Statue Heart': '950000000000', 'Adamantine Tendon': '960000000000', 'Megafauna Bone': '970000000000',
    'Inferno Claw': '980000000000', 'Cursed Claw': '990000000000', 'Gloaming Crystal': '9A0000000000',
    'Diamond-Cutter Fang': '9B0000000000', 'Stalactite Fang': '9C0000000000', 'Inferno Fang': '9D0000000000',
    'Tempest Fang': '9E0000000000', 'Phantom Fang': '9F0000000000', 'Astral Crystal Grain': 'A00000000000',
    'Astral Crystal Fragment': 'A10000000000', 'Astral Mass': 'A20000000000', 'Iron Dog Tag': 'A30000000000',
    'Bronze Dog Tag': 'A40000000000', 'Silver Dog Tag': 'A50000000000', 'Gold Dog Tag': 'A60000000000',
    'Platinum Dog Tag': 'A70000000000', 'Sheep Wool': 'A80000000000', 'Sharp Fang': 'B40300000000',
    'Hard Bone': 'B50300000000', 'Strange Core': 'B60300000000', 'Keen Gigafang': 'B70300000000',
    'Sturdy Megabone': 'B80300000000', 'Bizarre Megacore': 'B90300000000', 'Rending Titanfang': 'BA0300000000',
    'Indomitable Gargantubone': 'BB0300000000', 'Mystical Luminacore': 'BC0300000000', 'Iron Chunk': '2D0400000000',
    'Copper Chunk': '2E0400000000', 'Silver Chunk': '2F0400000000', 'Gold Chunk': '820400000000',
    'Platinum Chunk': '830400000000', 'Astral Crystal': '940400000000', 'Lustrious Astral Crystal': '950400000000',
    # Weapons
    'Sincleaver Blade': '260100000000', 'Dull Sword': '270100000000', 'Aurum Long Sword': '280100000000',
    'Crude Sword': '290100000000', 'Crude Earth Sword': '2A0100000000', 'Crude Water Sword': '2B0100000000',
    'Crude Fire Sword': '2C0100000000', 'Crude Wind Sword': '2D0100000000', 'Long Sword': '2E0100000000',
    'Atonement Edge': '2F0100000000', 'Gale Wing': '300100000000', 'Refined Gale Wing': '310100000000',
    'Supreme Gale Wing': '320100000000', 'Ground Fang': '330100000000', 'Refined Ground Fang': '340100000000',
    'Supreme Ground Fang': '350100000000', 'Thunder Nail': '360100000000', 'Refined Thunder Nail': '370100000000',
    'Supreme Thunder Nail': '380100000000', 'Flare Claw': '390100000000', 'Refined Flare Claw': '3A0100000000',
    'Supreme Flare Claw': '3B0100000000', 'Solid Edge': '3C0100000000', 'Hollow Edge': '3D0100000000',
    'Sodeil Arthalys': '3E0100000000', 'Sodeil Lem Regis': '3F0100000000', 'Gladius Rene': '400100000000',
    'Wedding Cake Cutter': '410100000000', 'Nebilim': '420100000000', 'El Vahf': '430100000000',
    'Realm Unifier': '440100000000', 'Iron Pipe': '450100000000', 'Machete Carrot': '460100000000',
    'Noble Rose': '480100000000', 'Bright Angelica': '490100000000', 'Shaded Aster': '4A0100000000',
    'Basic Rifle': '4B0100000000', 'Basic Water Rifle': '4C0100000000', 'Basic Fire Rifle': '4D0100000000',
    'Basic Dark Rifle': '4E0100000000', 'Grouper Flood': '4F0100000000', 'Refined Grouper Flood': '500100000000',
    'Supreme Grouper Flood': '510100000000', 'Ignis Roar': '520100000000', 'Refined Ignis Roar': '530100000000',
    'Supreme Ignis Roar': '540100000000', 'Blackthorn': '550100000000', 'Refined Blackthorn': '560100000000',
    'Supreme Blackthorn': '570100000000', 'Innocent Lily': '580100000000', 'Assault Shot': '590100000000',
    'Caritas Bouquet': '5A0100000000', 'Sclopetum Rene': '5B0100000000', 'Dämonisch Core': '5C0100000000',
    'Infantry Rifle': '5D0100000000', 'Faux Watering Can': '5E0100000000', 'Monochrome Spiral': '5F0100000000',
    'Sacred Karma': '600100000000', 'Iron Gauntlets': '610100000000', 'Black Iron Gauntlets': '620100000000',
    'Beast Fists': '630100000000', 'Earth Beast Fists': '640100000000', 'Fire Beast Fists': '650100000000',
    'Wind Beast Fists': '660100000000', 'Winged Gauntlets': '670100000000', 'Refined Winged Gauntlets': '680100000000',
    'Supreme Winged Gauntlets': '690100000000', 'Crystal Knuckles': '6A0100000000', 'Refined Crystal Knuckles': '6B0100000000',
    'Supreme Crystal Knuckles': '6C0100000000', 'Flaming Knights': '6D0100000000', 'Refined Flaming Knights': '6E0100000000',
    'Supreme Flaming Knights': '6F0100000000', 'Tyrant Fists': '700100000000', 'Caestus Rene': '710100000000',
    'Demon\'s Cry': '720100000000', 'Divine Wrath': '730100000000', 'Unyielding Braces': '740100000000',
    'Rappig Plushies': '750100000000', 'Oblivion Gauntlets': '760100000000', 'Dawn Braces': '770100000000',
    'Imperial Shield': '780100000000', 'Radiant Shield': '790100000000', 'Feline Bastion': '7A0100000000',
    'Feathered Shield': '7B0100000000', 'Refined Feathered Shield': '7C0100000000', 'Supreme Feathered Shield': '7D0100000000',
    'Rock Wall': '7E0100000000', 'Refined Rock Wall': '7F0100000000', 'Supreme Rock Wall': '800100000000',
    'Flashbang Shield': '810100000000', 'Revised Flashbang Shield': '820100000000', 'Supreme Flashbang Shield': '830100000000',
    'Red Shield': '840100000000', 'Blue Shield': '850100000000', 'Scutum Rene': '860100000000',
    'Os Rex': '870100000000', 'Adamas Regina': '880100000000', 'Infantry Shield': '890100000000',
    'Matriarch Martel': '8A0100000000', 'Farm Fence': '8B0100000000', 'Pink Protector': '8C0100000000',
    'Pulque Shaft': '8D0100000000', 'Gloria Shaft': '8E0100000000', 'Ventos Rod': '8F0100000000',
    'Refined Ventos Rod': '900100000000', 'Supreme Ventos Rod': '910100000000', 'Petram Pole': '920100000000',
    'Refined Petram Pole': '930100000000', 'Supreme Petram Pole': '940100000000', 'Tenebris Staff': '950100000000',
    'Refined Tenebris Staff': '960100000000', 'Supreme Tenebris Staff': '970100000000', 'Hanuman Shaft': '980100000000',
    'Columna Latio': '990100000000', 'Columna Passio': '9A0100000000', 'Caduceus Rene': '9B0100000000',
    'Diablo Nox': '9C0100000000', 'Deus Aurora': '9D0100000000', 'Liber Pater': '9E0100000000',
    'Pork Fork': '9F0100000000', 'Secrets of the Stars': 'A00100000000', 'Artes of the Cosmos': 'A10100000000',
    'Balanced Living': 'A20100000000', 'Balanced Living: Water': 'A30100000000', 'Balanced Living: Wind': 'A40100000000',
    'Balanced Living: Light': 'A50100000000', 'Nature\'s Beauty': 'A60100000000', 'Nature\'s Beauty: 2nd Ed.': 'A70100000000',
    'Nature\'s Beauty: 3rd Ed.': 'A80100000000', 'Taming Water': 'A90100000000', 'Taming Water: 2nd Ed.': 'AA0100000000',
    'Taming Water: 3rd Ed.': 'AB0100000000', 'Radiant Light': 'AC0100000000', 'Radiant Light: Part 2': 'AD0100000000',
    'Radiant Light: Part 3': 'AE0100000000', 'Silver Sword the Owl': 'AF0100000000', 'The Dark Wings': 'B00100000000',
    'Historia Rene': 'B10100000000', 'Burning Blood': 'B20100000000', 'Records of the Fallen': 'B30100000000',
    'Heavenly Gaze': 'B40100000000', 'Oblivion Ring': 'B50100000000', 'Prime Farming Issue 1': 'B60100000000',
    # Armors
    'Ragged Clothes': 'B70100000000', 'Ocean Blue Battle Garb': 'B80100000000', 'Sincleaver Armor': 'B90100000000',
    'Gahm Arthalys': 'BA0100000000', 'Bone Fragment Armor': 'BB0100000000', 'Zeugle Skin Armor': 'BC0100000000',
    'Zeugle Shell Armor': 'BD0100000000', 'Stonewing Armor': 'BE0100000000', 'Wolf Leather Armor': 'BF0100000000',
    'Zeugle Core Armor': 'C00100000000', 'Dragon Scale Armor': 'C10100000000', 'Stone Armor': 'C20100000000',
    'Bronze Armor': 'C30100000000', 'Iron Armor': 'C40100000000', 'Steel Armor': 'C50100000000',
    'Silver Armor': 'C60100000000', 'Platinum Armor': 'C70100000000', 'Orichalcum Armor': 'C80100000000',
    'Pearl Mail': 'C90100000000', 'Onyx Mail': 'CA0100000000', 'Topaz Mail': 'CB0100000000',
    'Amethyst Mail': 'CC0100000000', 'Emerald Mail': 'CD0100000000', 'Sapphire Mail': 'CE0100000000',
    'Diamond Mail': 'CF0100000000', 'Haute Culture': 'D00100000000', 'Knight Armor': 'D10100000000',
    'Battle Suit': 'D20100000000', 'Absolute': 'D30100000000', 'Reflector Armor': 'D40100000000',
    'Mumbane': 'D50100000000', 'Harmonic Armor': 'D60100000000', 'Heavenly Armor': 'D70100000000',
    'White One Piece': 'D80100000000', 'Noble Scarlet': 'D90100000000', 'Twilight One Piece': 'DA0100000000',
    'L\'Aze Phiarquis': 'DB0100000000', 'Bone Fragment Dress': 'DC0100000000', 'Zeugle Skin Dress': 'DD0100000000',
    'Zeugle Shell Dress': 'DE0100000000', 'Stonewing Dress': 'DF0100000000', 'Wolf Leather Dress': 'E00100000000',
    'Zeugle Core Dress': 'E10100000000', 'Dragonscale Dress': 'E20100000000', 'Stone Dress': 'E30100000000',
    'Bronze Dress': 'E40100000000', 'Iron Dress': 'E50100000000', 'Steel Dress': 'E60100000000',
    'Silver Dress': 'E70100000000', 'Platinum Dress': 'E80100000000', 'Orichalcum Dress': 'E90100000000',
    'Pearl One Piece': 'EA0100000000', 'Onyx One Piece': 'EB0100000000', 'Topaz One Piece': 'EC0100000000',
    'Amethyst One Piece': 'ED0100000000', 'Emerald One Piece': 'EE0100000000', 'Sapphire One Piece': 'EF0100000000',
    'Diamond One Piece': 'F00100000000', 'Middy Blouse': 'F10100000000', 'Cocktail Dress': 'F20100000000',
    'Magical Tunic': 'F30100000000', 'Gothic Dress': 'F40100000000', 'Witch Dress': 'F50100000000',
    'Wedding Dress': 'F60100000000', 'Rose Dress': 'F70100000000', 'Renas Superbia': 'F80100000000',
    'Inherited Coat': 'F90100000000', 'Zeugle Skin Mage Coat': 'FA0100000000', 'Zeugle Shell Mage Coat': 'FB0100000000',
    'Stonewing Mage Coat': 'FC0100000000', 'Wolf Leather Mage Coat': 'FD0100000000', 'Zeugle Core Mage Coat': 'FE0100000000',
    'Dragonscale Mage Coat': 'FF0100000000', 'Bronze Robe': '000200000000', 'Iron Robe': '010200000000',
    'Steel Robe': '020200000000', 'Silver Robe': '030200000000', 'Platinum Robe': '040200000000',
    'Orichalcum Robe': '050200000000', 'Onyx Cloak': '060200000000', 'Topaz Cloak': '070200000000',
    'Amethyst Cloak': '080200000000', 'Emerald Cloak': '090200000000', 'Sapphire Cloak': '0A0200000000',
    'Diamond Cloak': '0B0200000000', 'White Cloak': '0C0200000000', 'Silk Robe': '0D0200000000',
    'Mystic Cloak': '0E0200000000', 'Holy Cloak': '0F0200000000', 'Elder Cloak': '100200000000',
    'Spirit Robe': '110200000000', 'Heavenly Garb': '120200000000', 'Dahnas Animus': '130200000000',
    'Bureau Uniform': '140200000000', 'Silver Wolf Vest': '150200000000', 'Zeugle Skin Vest': '160200000000',
    'Zeugle Shell Vest': '170200000000', 'Stonewing Vest': '180200000000', 'Wolf Leather Vest': '190200000000',
    'Zeugle Core Vest': '1A0200000000', 'Dragonscale Vest': '1B0200000000', 'Bronze Jacket': '1C0200000000',
    'Iron Jacket': '1D0200000000', 'Steel Jacket': '1E0200000000', 'Silver Jacket': '1F0200000000',
    'Platinum Jacket': '200200000000', 'Orichalcum Jacket': '210200000000', 'Onyx Vest': '220200000000',
    'Topaz Vest': '230200000000', 'Amethyst Vest': '240200000000', 'Emerald Vest': '250200000000',
    'Sapphire Vest': '260200000000', 'Diamond Vest': '270200000000', 'Natural Vest': '280200000000',
    'Jet Black Vest': '290200000000', 'Kingly Vest': '2A0200000000', 'Vest of Secrets': '2B0200000000',
    'Canine Vest': '2C0200000000', 'Prismatic Jacket': '2D0200000000', 'Zero Impact Vest': '2E0200000000',
    'Virtuous Wolf Vest': '2F0200000000', 'Guardsman Armor': '300200000000', 'Zeugle Shell Suit': '310200000000',
    'Stonewing Suit': '320200000000', 'Wolf Leather Suit': '330200000000', 'Zeugle Core Suit': '340200000000',
    'Dragonscale Suit': '350200000000', 'Iron Plate': '360200000000', 'Steel Plate': '370200000000',
    'Silver Plate': '380200000000', 'Platinum Plate': '390200000000', 'Orichalcum Plate': '3A0200000000',
    'Topaz Guard': '3B0200000000', 'Amethyst Guard': '3C0200000000', 'Emerald Guard': '3D0200000000',
    'Sapphire Guard': '3E0200000000', 'Diamond Guard': '3F0200000000', 'Mighty Guard': '400200000000',
    'Brigandine': '410200000000', 'Rare Plate': '420200000000', 'Elemental Guard': '430200000000',
    'Fortress Armor': '440200000000', 'Last Crusader': '450200000000', 'Insurrectionist Armor': '460200000000',
    'il Quras Traditional Armor': '470200000000', 'Zeugle Shell Mantle': '480200000000', 'Stonewing Mantle': '490200000000',
    'Wolf Leather Mantle': '4A0200000000', 'Zeugle Core Mantle': '4B0200000000', 'Dragonscale Mantle': '4C0200000000',
    'Iron Mantle': '4D0200000000', 'Steel Mantle': '4E0200000000', 'Silver Mantle': '4F0200000000',
    'Platinum Mantle': '500200000000', 'Orichalcum Mantle': '510200000000', 'Topaz Cape': '520200000000',
    'Amethyst Cape': '530200000000', 'Emerald Cape': '540200000000', 'Sapphire Cape': '550200000000',
    'Diamond Cape': '560200000000', 'Earth Cape': '570200000000', 'Bloody Coat': '580200000000',
    'Royal Cape': '590200000000', 'Elemental Cape': '5A0200000000', 'Duality': '5B0200000000',
    'Vermillion': '5C0200000000', 'Magnus Dominus': '5D0200000000',
    # Valuable Items
    'Castle Elevator Key': '850200000000', 'Secret Key': '890200000000', 'Collection Room Key': '8A0200000000',
    '1F Elevator Key': '8B0200000000', 'Master Core of Fire': '8D0200000000', 'Master Core of Light': '8E0200000000',
    'Master Core of Earth': '8F0200000000', 'Master Core of Wind': '900200000000', 'Wonder Text 2': 'BB0200000000',
    'Wonder Text 3': 'BC0200000000', 'Wonder Text 1': 'BA0200000000', 'Letter in a Bottle': 'BD0200000000',
    'Treasure Key: Earth': 'BE0200000000', 'Duplicate Lord\'s Quarters Key': 'BF0200000000', 'Sound Vessel': 'C00200000000',
    'A Key to a Hidden Chamber': 'C10200000000', 'Access Key A': 'C20200000000', 'Access Key B': 'C30200000000',
    'Access Key C': 'C40200000000', 'Savage Key': 'C50200000000', 'Noble Room Key': 'AC0300000000',
    'Astral Flower': 'AD0300000000', 'Destiny Key': 'AE0300000000', 'Symphony Key': 'AF0300000000',
    'Abyss Key': 'B00300000000', 'Zest Key': 'B10300000000', 'Scarlet Night Key': 'B20300000000',
    'Vesper Key': 'B30300000000', 'Old Bracelet': '310400000000',
    # Other Items
    'Roasted Chicken': '4F0300000000', 'Kebab': '500300000000', 'Beef Stew': '510300000000',
    'Wiener': '520300000000', 'Leaf-Wrapped Fish': '530300000000', 'Grilled Rappig': '540300000000',
    'Lohikeitto': '550300000000', 'Grilled Mushrooms': '560300000000', 'Steamed Potatoes': '570300000000',
    'Vegetable Soup': '580300000000', 'Curry': '590300000000', 'Vegetable Juice': '5A0300000000',
    'Vitamin Smoothie': '5B0300000000', 'Gnocchi': '5C0300000000', 'Sandwich': '5D0300000000',
    'Fancy Parfait': '5E0300000000', 'Apple Pie': '5F0300000000', 'Hamburger': '600300000000',
    'Fish Steak': '610300000000', 'Ice Cream': '620300000000', 'Omelette': '630300000000',
    'Mabo Curry': '640300000000', 'Cheese Fondue': '650300000000', 'Pork Bun': '660300000000',
    'Sushi': '670300000000', 'Horse Sashimi': '680300000000', 'Grilled Fish': '690300000000',
    'Meuniere': '6A0300000000', 'Sashimi': '6B0300000000', 'Bouillabaisse': '6C0300000000',
    'Shortcake': '6D0300000000', 'Shionne Pancakes': '6E0300000000', 'Dohalim Pancakes': '6F0300000000',
    'Hootle Pancakes': '700300000000', 'Pancake': '720300000000', 'Porridge': '730300000000',
    'M.F. Porridge': '740300000000', 'Glanymede Donuts': '750300000000', 'Migel\'s Rod': '910200000000',
    'Novice Tackle': '920200000000', 'Fish Sniper': '930200000000', 'Alliance Marine Rod': '940200000000',
    'Tenebrae MK.III': '950200000000', 'Beginner\'s Popper': '960200000000', 'Marine Floater': '970200000000',
    'Round Popper': '980200000000', 'Teepo Lure': '990200000000', 'Stick Lure': '9A0200000000',
    'Bienfu Lure': '9B0200000000', 'Subsurface Mirage': '9D0200000000', 'Elegant Swimmer': '9E0200000000',
    'Disarming Lure': '9F0200000000', 'Celestial Whale': 'A00200000000', 'Rappig Minnow': 'A10200000000',
    'Trembling Lure': 'A30200000000', 'Charming Lure': 'A40200000000', 'Zapie Doppelganger': 'A50200000000',
    'Portly Mudslinger': 'A70200000000', 'Rock Slapper': 'A80200000000', 'Mieu Sinker': 'A90200000000',
    'Flaptrap': 'AB0200000000', 'Uper Spinner': 'AC0200000000', 'Silver Fang Lure': 'AD0200000000',
    'Glutton\'s Maze': '1A0300000000', 'Glutton\'s Code': '1B0300000000', 'Glutton\'s Guidebook': '1C0300000000',
    'Ancient Excavator': '1D0300000000', 'Vivid Sphere': '1E0300000000', 'Crocodile Crusher': '1F0300000000',
    'Battle Maiden\'s Shield': '200300000000', 'Broken Machine Gun': '210300000000', 'Metal Miner\'s Cap': '220300000000',
    'Trident': '230300000000', 'Machine Beast Statue': '240300000000', 'Quivering Candles': '250300000000',
    'Devil Sculpture': '260300000000', 'Blade of Sealing': '270300000000', 'Hellmask Fiend Skull': '280300000000',
    'Mechanical Doll Accessory': '290300000000', 'Lucky Cat Statue': '2A0300000000', 'Golden Lucky Cat Statue': '2B0300000000',
    'Silver Suit of Armor': '2C0300000000', 'Golden Suit of Armor': '2D0300000000', 'Drums of the Master': '2E0300000000',
    'Drum of the Legend': '2F0300000000', 'Golden Fairy Statue': '300300000000', 'Ragged Clothes (Costume)': 'C60200000000',
    'Ocean Blue Battle Garb (Costume)': 'C70200000000', 'Sincleaver Armor (Costume)': 'C80200000000', 'Gahm Arthalys (Costume)': 'C90200000000',
    'Steamy Towel 1 (Costume)': 'CA0200000000', 'Clerk Uniform 1 (Costume)': 'CB0200000000', 'Farmer\'s Clothes 1 (Costume)': 'CC0200000000',
    'Tunica Rene 1 (Costume)': 'CD0200000000', 'Noble Scarlet (Costume)': 'CE0200000000', 'White One Piece (Costume)': 'CF0200000000',
    'L\'Aze Phiarquis (Costume)': 'D00200000000', 'Steamy Towel 2 (Costume)': 'D10200000000', 'Clerk Uniform 2 (Costume)': 'D20200000000',
    'Farmer\'s Clothes 2 (Costume)': 'D30200000000', 'Inherited Coat (Costume)': 'D40200000000', 'Steamy Towel 3 (Costume)': 'D50200000000',
    'Clerk Uniform 3 (Costume)': 'D60200000000', 'Farmer\'s Clothes 3 (Costume)': 'D70200000000', 'Silver Wolf Vest (Costume)': 'D80200000000',
    'Bureau Uniform (Costume)': 'D90200000000', 'Steamy Towel 4 (Costume)': 'DA0200000000', 'Clerk Uniform 4 (Costume)': 'DB0200000000',
    'Farmer\'s Clothes 4 (Costume)': 'DC0200000000', 'Guardsman Armor (Costume)': 'DD0200000000', 'Steamy Towel 5 (Costume)': 'DE0200000000',
    'Clerk Uniform 5 (Costume)': 'DF0200000000', 'Farmer\'s Clothes 5 (Costume)': 'E00200000000', 'il Quras Traditional Attire (Costume)': 'E10200000000',
    'Steamy Towel 6 (Costume)': 'E20200000000', 'Clerk Uniform 6 (Costume)': 'E30200000000', 'Farmer\'s Clothes 6 (Costume)': 'E40200000000',
    'Unkempt Hair': 'E50200000000', 'Broken Iron Mask': 'E60200000000', 'Iron Mask': 'E70200000000',
    'Scarlet Tiara': 'E80200000000', 'Golden Hair Pin': 'E90200000000', 'Slicked Black Hair': 'EA0200000000',
    'Long Wavy Hair': 'EB0200000000', 'Natural Wavy Hair': 'EC0200000000', 'Silver Sincleaver Armor (Costume)': 'ED0200000000',
    'Gold Sincleaver Armor (Costume)': 'EE0200000000', 'Copper Sincleaver Armor (Costume)': 'EF0200000000', 'Tunica Rene 2 (Costume)': 'F00200000000',
    'Twilight One Piece (Costume)': 'F10200000000', 'Noble Blossom (Costume)': 'F20200000000', 'Noble Azure (Costume)': 'F30200000000',
    'Noble Crimson (Costume)': 'F40200000000', 'Scarlet Inherited Coat (Costume)': 'F50200000000', 'Lunar Inherited Coat (Costume)': 'F60200000000',
    'Blue Inherited Coat (Costume)': 'F70200000000', 'Wolfless Vest (Costume)': 'F80200000000', 'Red-Black Wolf Vest (Costume)': 'F90200000000',
    'Green Wolf Vest (Costume)': 'FA0200000000', 'Red-White Wolf Vest (Costume)': 'FB0200000000', 'Night Guardsman Armor (Costume)': 'FC0200000000',
    'Decoy Guardsman Armor (Costume)': 'FD0200000000', 'Aquadic Guardsman Armor (Costume)': 'FE0200000000', 'Tunica Rene 3 (Costume)': 'FF0200000000',
    'il Qaras Festive Attire (Costume)': '000300000000', 'il Qaras Mourning Attire (Costume)': '010300000000', 'il Qarus Dancing Attire (Costume)': '020300000000',
    'Shoreman\'s Straw Hat 1': '030300000000', 'Farmer\'s Straw Hat 1': '040300000000', 'Feathered Headpiece': '050300000000',
    'Braided Ponytail': '060300000000', 'Ponytail': '070300000000', 'Shoreman\'s Straw Hat 2': '080300000000',
    'Farmer\'s Straw Hat 2': '090300000000', 'Verdant Tiara': '0A0300000000', 'Aqua Blue Tiara': '0B0300000000',
    'Violet Tiara': '0C0300000000', 'Parted Bob Cut': '0D0300000000', 'Shoreman\'s Straw Hat 3': '0E0300000000',
    'Farmer\'s Straw Hat 3': '0F0300000000', 'Crimson Hair Pin': '100300000000', 'Silver Hair Pin': '110300000000',
    'Dark Blue Hair Pin': '120300000000', 'Shoreman\'s Straw Hat 4': '130300000000', 'Farmer\'s Straw Hat 4': '140300000000',
    'Shoreman\'s Straw Hat 5': '150300000000', 'Farmer\'s Straw Hat 5': '160300000000', 'Shoreman\'s Straw Hat 6': '170300000000',
    'Farmer\'s Straw Hat 6': '180300000000', 'Braided Bun': '190300000000', 'Sunglasses': '760300000000',
    'Retro Sunglasses': '770300000000', 'Half Frames': '780300000000', 'Frame Glasses': '790300000000',
    'Monocle': '7A0300000000', 'Swirly Glasses': '7B0300000000', 'Giggle Glasses': '7C0300000000',
    'Angry Glasses': '7D0300000000', 'Sad Glasses': '7E0300000000', 'Right Eyepatch': '7F0300000000',
    'Left Eyepatch': '800300000000', 'Right Bandage': '810300000000', 'Left Bandage': '820300000000',
    'Dog Ears': '830300000000', 'Wolf Ears': '840300000000', 'Spotted Cat Ears': '850300000000',
    'Rabbit Ears': '860300000000', 'Halo': '870300000000', 'Devil Horns': '880300000000',
    'Crown': '890300000000', 'Red Tropical Corsage': '8A0300000000', 'Red Rose Corsage': '8B0300000000',
    'Star Hair Clip': '8C0300000000', 'Angel Wings': '8D0300000000', 'Devil Wings': '8E0300000000',
    'Butterfly Wings': '8F0300000000', 'Dog Tail': '900300000000', 'Wolf Tail': '910300000000',
    'Cat Tail': '920300000000', 'Rabbit Tail': '930300000000', 'Devil Tail': '940300000000',
    'Hootle Doll': '950300000000', 'Black Eyepatch': '960300000000', 'Midnight Battle Garb (Costume)': '730400000000',
    'Owl King Doll': '800400000000', 'Owl Queen Doll': '810400000000'
}

class TalesOfAriseSaveEditor(QMainWindow):
    def __init__(self):
        super().__init__()
        self.save_data, self.file_path, self._updating_save_table = None, None, False
        self._all_db_items = [{"name":k,"id":v} for k,v in sorted(ITEM_DB.items())]
        self._filtered_db_items, self._items_in_save = self._all_db_items[:], []
        self.current_char_key, self.char_data_cache, self.stat_widgets = list(CHARS.keys())[0], {n:{k:0 for k in STATS} for n in CHARS}, {}
        self.init_ui()

    def init_ui(self):
        self.setWindowTitle("Tales of Arise Save Editor (PS4) V1.0 By ArsaModz"); self.setMinimumSize(1280,720); self.setWindowIcon(QIcon(res_path("icon.ico")))
        central = QWidget(); self.setCentralWidget(central); layout = QVBoxLayout(central)
        
        # File Bar
        fb = QHBoxLayout(); self.file_label = QLabel("No file loaded"); self.file_label.setStyleSheet("padding:10px;background:#2b2b2b;color:#e0e0e0;border-radius:4px;")
        fb.addWidget(self.file_label, 1)
        for t, f in [("Open Save", self.open_file), ("Save Changes", self.save_file)]:
            b = QPushButton(t); b.clicked.connect(f); b.setFixedHeight(32); fb.addWidget(b)
        layout.addLayout(fb)
        
        self.tabs = QTabWidget(); layout.addWidget(self.tabs)
        self.tabs.addTab(self.ui_character(), "Character"); self.tabs.addTab(self.ui_inventory(), "Inventory")

    def ui_character(self):
        w = QWidget(); ml = QVBoxLayout(w); top = QHBoxLayout()
        # Gald
        gg = QGroupBox("Currency"); gl = QHBoxLayout(gg); gl.addWidget(QLabel("Gald:"))
        self.gald_input = QSpinBox(); self.gald_input.setRange(0,999999999); self.gald_input.setFixedWidth(120); gl.addWidget(self.gald_input)
        bm = QPushButton("Max"); bm.clicked.connect(lambda: self.gald_input.setValue(999999999)); gl.addWidget(bm); top.addWidget(gg)
        # Char Select
        gc = QGroupBox("Character Management"); cl = QHBoxLayout(gc); self.char_combo = QComboBox(); self.char_combo.addItems(list(CHARS.keys()))
        self.char_combo.currentTextChanged.connect(self._on_char_combo_changed); cl.addWidget(self.char_combo)
        for t, f in [("Max Selected", self.max_current_character), ("Max All", self.max_all_characters)]:
             b = QPushButton(t); b.clicked.connect(f); cl.addWidget(b)
        top.addWidget(gc); top.addStretch(); ml.addLayout(top)
        # Stats
        gs = QGroupBox("Character Stats"); grid = QGridLayout(gs); r, c = 0, 0
        for sk, cfg in STATS.items():
            grid.addWidget(QLabel(sk.replace('_',' ').replace(':','').title()+":"), r, c, Qt.AlignmentFlag.AlignRight)
            sb = QSpinBox(); sb.setRange(cfg[1], cfg[2]); sb.setFixedWidth(140); self.stat_widgets[sk] = sb
            grid.addWidget(sb, r, c+1, Qt.AlignmentFlag.AlignLeft); c += 2
            if c >= 6: c, r = 0, r+1
        ml.addWidget(gs); ml.addStretch(); return w

    def max_current_character(self):
        if self.save_data:
            for sk, cfg in STATS.items(): self.char_data_cache[self.current_char_key][sk] = cfg[2]; self.stat_widgets[sk].setValue(cfg[2])

    def max_all_characters(self):
        if self.save_data and QMessageBox.question(self, "Confirm", "Max stats for all characters?") == QMessageBox.StandardButton.Yes:
            for n in CHARS:
                for sk, cfg in STATS.items(): self.char_data_cache[n][sk] = cfg[2]
            self._update_ui_from_cache(self.current_char_key)

    def _on_char_combo_changed(self, new_char):
        if self.current_char_key in self.char_data_cache:
            for s, w in self.stat_widgets.items(): self.char_data_cache[self.current_char_key][s] = w.value()
        self.current_char_key = new_char; self._update_ui_from_cache(new_char)

    def _update_ui_from_cache(self, cn):
        for s, v in self.char_data_cache.get(cn, {}).items(): 
            if s in self.stat_widgets: self.stat_widgets[s].setValue(v)

    def ui_inventory(self):
        w = QWidget(); l = QVBoxLayout(w); fr = QHBoxLayout()
        fr.addWidget(QLabel("Search Items:")); self.item_search = QLineEdit(); self.item_search.setPlaceholderText("Enter item name...")
        self.item_search.textChanged.connect(self._on_search_changed); fr.addWidget(self.item_search); l.addLayout(fr)
        mr = QHBoxLayout()
        self.table_available = QTableWidget(0, 2); self.table_available.setHorizontalHeaderLabels(["Name", "ID"])
        self.table_available.horizontalHeader().setSectionResizeMode(0, QHeaderView.ResizeMode.Stretch)
        self.table_available.setSelectionBehavior(QAbstractItemView.SelectionBehavior.SelectRows)
        self.table_available.setEditTriggers(QAbstractItemView.EditTrigger.NoEditTriggers); mr.addWidget(self.table_available, 2)
        bc = QVBoxLayout(); bc.addStretch(); self.item_qty = QSpinBox(); self.item_qty.setRange(1, 99); self.item_qty.setValue(99)
        bc.addWidget(QLabel("Quantity:")); bc.addWidget(self.item_qty)
        for t, f in [("Add/Update", self.add_item), ("Add All", self.add_all), ("Remove", self.remove_item)]:
            b = QPushButton(t); b.clicked.connect(f); bc.addWidget(b)
        bc.addStretch(); mr.addLayout(bc)
        self.table_save = QTableWidget(0, 3); self.table_save.setHorizontalHeaderLabels(["Name", "ID", "Qty"])
        self.table_save.horizontalHeader().setSectionResizeMode(0, QHeaderView.ResizeMode.Stretch)
        self.table_save.itemChanged.connect(self._on_save_table_item_changed); mr.addWidget(self.table_save, 2)
        l.addLayout(mr); self._populate_available_table(); return w

    def _on_search_changed(self, t):
        self._filtered_db_items = [x for x in self._all_db_items if t.lower() in x['name'].lower()]; self._populate_available_table()

    def _populate_available_table(self):
        self.table_available.setRowCount(len(self._filtered_db_items))
        for r, row in enumerate(self._filtered_db_items):
            self.table_available.setItem(r, 0, QTableWidgetItem(row['name'])); self.table_available.setItem(r, 1, QTableWidgetItem(row['id']))

    def open_file(self):
        p, _ = QFileDialog.getOpenFileName(self, "Open Save", "", "Save Files (*.sav);;All Files (*.*)")
        if p:
            with open(p, 'rb') as f: self.save_data = bytearray(f.read())
            self.file_path = p; self.file_label.setText(f"📁 {os.path.basename(p)}"); self.load_values()

    def load_values(self):
        gp = self.find_p('4CAFC38C')
        if gp >= 0: self.gald_input.setValue(struct.unpack('<I', self.save_data[gp+36:gp+40])[0])
        for c, cid in CHARS.items():
            cp = self.find_p(cid)
            if cp >= 0:
                for s, cfg in STATS.items(): self.char_data_cache[c][s] = struct.unpack('<I', self.save_data[cp+cfg[0]:cp+cfg[0]+4])[0]
        self._update_ui_from_cache(self.current_char_key); self.load_inventory()

    def save_file(self):
        if not self.save_data: return
        gp = self.find_p('4CAFC38C')
        if gp >= 0: self.save_data[gp+36:gp+40] = struct.pack('<I', self.gald_input.value())
        cn = self.char_combo.currentText()
        for s, w in self.stat_widgets.items(): self.char_data_cache[cn][s] = w.value()
        for c, cid in CHARS.items():
            cp = self.find_p(cid)
            if cp >= 0:
                for s, cfg in STATS.items(): self.save_data[cp+cfg[0]:cp+cfg[0]+4] = struct.pack('<I', self.char_data_cache[c][s])
        with open(self.file_path, 'wb') as f: f.write(self.save_data)
        QMessageBox.information(self, "Success", "Save file updated successfully!")

    def load_inventory(self):
        self._items_in_save, pos = [], self.find_p(INV_PATT)
        if pos < 0: return
        curr, rdb, limit = pos+12, {v:k for k,v in ITEM_DB.items()}, pos+(1000*16)
        while curr < len(self.save_data)-16 and curr < limit:
            q, ih = self.save_data[curr], self.save_data[curr+2:curr+8].hex().upper()
            if q > 0 or (ih != "000000000000" and ih in rdb):
                self._items_in_save.append({"name":rdb.get(ih, f"Unknown ({ih})"), "id":ih, "qty":q, "offset":curr})
            curr += 16
        self._populate_save_table()

    def _populate_save_table(self):
        self._updating_save_table = True; self.table_save.setRowCount(len(self._items_in_save))
        for r, row in enumerate(self._items_in_save):
            self.table_save.setItem(r, 0, QTableWidgetItem(row['name'])); self.table_save.setItem(r, 1, QTableWidgetItem(row['id']))
            qi = QTableWidgetItem(str(row['qty'])); qi.setData(Qt.ItemDataRole.UserRole, r); self.table_save.setItem(r, 2, qi)
        self._updating_save_table = False

    def _on_save_table_item_changed(self, i):
        if self._updating_save_table or i.column() != 2: return
        idx = i.data(Qt.ItemDataRole.UserRole)
        try: nq = max(0, min(99, int(i.text().strip())))
        except: nq = self._items_in_save[idx]['qty']
        self._items_in_save[idx]['qty'] = nq; self._item_io(self._items_in_save[idx]['offset'], qty=nq)

    def add_item(self):
        if not self.save_data or (r := self.table_available.currentRow()) < 0: return
        tid, tnm, qty = self.table_available.item(r, 1).text(), self.table_available.item(r, 0).text(), self.item_qty.value()
        for i in self._items_in_save:
            if i['id'] == tid:
                i['qty'] = qty; self._item_io(i['offset'], qty=qty); self._populate_save_table(); return
        curr = self.find_p(INV_PATT) + 12
        while curr < len(self.save_data)-16:
            if self.save_data[curr] == 0 and self.save_data[curr+2:curr+8].hex().upper() == "000000000000":
                self._item_io(curr, qty=qty, item_hex=tid); self._items_in_save.append({"name":tnm,"id":tid,"qty":qty,"offset":curr})
                self._populate_save_table(); return
            curr += 16
        QMessageBox.warning(self, "Error", "Inventory full!")

    def remove_item(self):
        if (r := self.table_save.currentRow()) >= 0:
            s = self._items_in_save[r]['offset']; self.save_data[s:s+16] = b'\x00'*16; del self._items_in_save[r]; self._populate_save_table()

    def add_all(self):
        if self.save_data and QMessageBox.question(self,'Confirm',"Add all items?") == QMessageBox.StandardButton.Yes:
            p = self.find_p(INV_PATT)+12
            for i, (_, hid) in enumerate(sorted(ITEM_DB.items())): self._item_io(p+(i*16), 99, hid)
            self.load_inventory()

    def find_p(self, p):
        try: return self.save_data.find(bytes.fromhex(p))
        except: return -1

    def _item_io(self, pos, qty=None, item_hex=None):
        if qty is not None: self.save_data[pos] = qty; self.save_data[pos+1] = 0x05
        if item_hex: self.save_data[pos+2:pos+8] = bytes.fromhex(item_hex)

if __name__ == '__main__':
    if sys.platform == 'win32': ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID('toa.editor.v1')
    app = QApplication(sys.argv); app.setStyle('Fusion'); editor = TalesOfAriseSaveEditor(); editor.show(); sys.exit(app.exec())
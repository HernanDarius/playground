import pymongo
from keys import mongo_pw, mongo_db


client = pymongo.MongoClient(f"mongodb+srv://darius759:{mongo_pw}@cluster0.klg5k.mongodb.net/{mongo_db}?retryWrites=true&w=majority")
db = client.test

lilgrea_doc = {
    'name' : 'Lilgrea',
    'race' : 'Tiefling',
    'class' : 'Warlock',
    'level' : 1,
    'exp' : 0,
    'hp' : 10,
    'strength' : 8,
    'dexterity' : 13,
    'constitution' : 14,
    'intelligence': 13,
    'wisdom' : 10,
    'charisma' : 17
}

sofri_doc = {
    'name' : 'Sofri',
    'race' : 'Human',
    'class' : 'Rogue',
    'level' : 1,
    'exp' : 0,
    'hp' : 10,
    'strength' : 13,
    'dexterity' : 16,
    'constitution' : 14,
    'intelligence': 9,
    'wisdom' : 15,
    'charisma' : 11
}

baerdal_doc = {
    'name' : 'Baerdal',
    'race' : 'Dwarf',
    'class' : 'Blood Hunter',
    'level' : 1,
    'exp' : 0,
    'hp' : 11,
    'strength' : 17,
    'dexterity' : 13,
    'constitution' : 12,
    'intelligence': 14,
    'wisdom' : 8,
    'charisma' : 12
}

norlos_doc = {
    'name' : 'Norlos',
    'race' : 'Halfling',
    'class' : 'Monk',
    'level' : 1,
    'exp' : 0,
    'hp' : 9,
    'strength' : 12,
    'dexterity' : 17,
    'constitution' : 13,
    'intelligence': 10,
    'wisdom' : 14,
    'charisma' : 9
}

lichithal_doc = {
    'name' : 'Lichithal',
    'race' : 'Dragonborn',
    'class' : 'Paladin',
    'level' : 1,
    'exp' : 0,
    'hp' : 11,
    'strength' : 17,
    'dexterity' : 10,
    'constitution' : 13,
    'intelligence': 8,
    'wisdom' : 12,
    'charisma' : 15
}

wolnoa_doc = {
    'name' : 'Wolnoa',
    'race' : 'Half-Elf',
    'class' : 'Ranger',
    'level' : 1,
    'exp' : 0,
    'hp' : 12,
    'strength' : 12,
    'dexterity' : 16,
    'constitution' : 14,
    'intelligence': 8,
    'wisdom' : 14,
    'charisma' : 12
}

all_docs = [lilgrea_doc, sofri_doc, baerdal_doc,
            norlos_doc, lichithal_doc, wolnoa_doc]

db.test.insert_many(all_docs)


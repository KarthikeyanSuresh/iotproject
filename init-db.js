db = db.getSiblingDB("db");
db.table1.drop();

db.table1.insertMany([
    {
        "id": 1,
        "name": "Lion",
        "type": "wild"
    },
    {
        "id": 2,
        "name": "Cow",
        "type": "domestic"
    },
    {
        "id": 3,
        "name": "Tiger",
        "type": "wild"
    },
]);
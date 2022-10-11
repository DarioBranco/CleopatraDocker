print("Started Adding the Users.");
db = db.getSiblingDB("admin");
db.auth("root", "password");
db = db.getSiblingDB('cleopatra');
db.createUser({
  user: "cleopatra",
  pwd: "cleop25..",
  roles: [{ role: "readWrite", db: "cleopatra" }],
});

db.createCollection('collection_test');

print("End Adding the User Roles.");
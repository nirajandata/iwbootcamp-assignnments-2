import json

json_file={
    "name":"iw",
    "address":"ktm",
    "age":18
}
with open("json_file.json", "w") as write_file:
    json.dump(json_file, write_file)

with open("json_file.json", "r") as read_file:
    result = json.load(read_file)

print(result)
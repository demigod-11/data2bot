import json

input_data = {'name' : "sam",
         'age' : 4,
         'fruits' : ['apple', 'coke'],
         'cousins' : [{'mother': {}, 'father': {}}]
}

expected = {
    'name': {'type': 'string', 'tag': '', 'description': '', 'required': False},
    'age': {'type': 'integer', 'tag': '', 'description': '', 'required': False},
    'fruits': {'type': 'enum', 'tag': '', 'description': '', 'required': False},
    'cousins': {'type': 'array', 'tag': '', 'description': '', 'required': False}
}

data = json.loads("""{
  "attributes": {
    "eventType": "ABCDEFGHIJ"
  },
  "message": {
    "battle": {
      "orientation": "ABCDEFGHIJKLMNO",
      "settings": {
        "minParticipants": 942,
        "wagerType": "ABCDEFGHIJKLMNOPQRSTUVW",
        "archetype": {
          "name": "ABCDEFGHIJKLMNOPQRS"
        }
      },
      "endTime": 353,
      "creator": {
        "id": "ABCDEFGHIJKLMNOPQRSTUVWXYZA"
        
      },
      "participants": [
        {
          "user": {
            "id": "ABCDEFGHIJKLMN"
          },
          "creator": false,
          "ranking": 498
        }
      ]
    },
    "joiner": {
      "id": "ABCDEFGHIJKLMNOPQRSTUVWXYZAB"
    },
    "participantIds": [
      "ABCDEFGHIJKLMNOPQRST"
    ]
  }
}""")

file = './data/data_1.json'
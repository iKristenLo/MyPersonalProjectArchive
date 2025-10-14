import random
import time
import json
import os
import json

UserData = {
  "User": " ",
  "CardID": " ",
  "UserBalance": " ",
  "UserDebt": " "
}

with open('OpenMobileBankDB.json', 'w') as json_file:
    json.dump(UserData, json_file)
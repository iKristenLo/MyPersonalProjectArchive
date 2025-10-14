import turt
import time
print("Welcome To My Encyclpedia")
games = ["Grand Theft Auto San Andreas","Minecraft","Roblox","Cyberpunk 2077","Forza Horzion 3",]

print("\nPick From Selection Below")
for game in games:
  print(game)

archive = {
  "Grand Theft Auto San Andreas": "An RPG Game Based In Los Santos",
  "Minecraft": "Block Building Game",
  "Roblox": "Build Anything Play Anything",
  "Cyberpunk 2077": "An Open World Game Based In Night City",
  "Forza Horzion 3": "Racing Game"
}

query = input("Enter Video Game Or Q to Quit: ") 
while query != 'Q':
  if query in archive.keys():
    print("Searching ...")
    time.sleep(1)
    print(archive[query])
  else:
    print("Not Found")
  query = input("Enter Video Game Or Q to Quit: ") 
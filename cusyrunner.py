import time
import random

# Game Settings
lanes = ["Left", "Middle", "Right"]
player_pos = 1
score = 0
running = True

print("--- WELCOME TO CUSYRUNNER (Text Mode) ---")
print("Controls: a=Left, d=Right, w=Jump, s=Slide")
time.sleep(2)

while running:
    lane_obs = random.randint(0, 2)
    obs_type = random.choice(["TEMPO", "STONE", "BUS"])
    
    print(f"\nScore: {score} | Lane: {lanes[player_pos]}")
    print(f"SAMNE SE {obs_type} AA RAHA HAI IN {lanes[lane_obs]} LANE!")
    
    move = input("Tera Move? (a/d/w/s): ").lower()
    
    if move == 'a' and player_pos > 0: player_pos -= 1
    elif move == 'd' and player_pos < 2: player_pos += 1
    
    # Collision Logic
    if player_pos == lane_obs:
        if obs_type == "STONE" and move != 'w':
            print("HIT STONE! Kutta peeche pad gaya!")
        elif obs_type == "TEMPO":
            print("CRASHED! Game Over!")
            running = False
    else:
        print("Bach gaya! Sahi nikal gaya.")
        score += 10
    
    time.sleep(0.5)


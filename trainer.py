import json
import random

# Load exercises
with open("workouts.json") as f:
    workouts = json.load(f)

def get_workout(category):
    if category in workouts:
        return random.sample(workouts[category], 3)
    else:
        return ["Basic warmup", "Push ups", "Stretching"]

# Example usage
if __name__ == "__main__":
    category = input("Enter workout category (beginner/chest/legs/abs/weight_loss): ")
    plan = get_workout(category)
    print("\nYour Workout Plan:")
    for exercise in plan:
        print("-", exercise)
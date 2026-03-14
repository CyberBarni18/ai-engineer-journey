temperature = 18

if temperature > 20:
    print("Warm day")
else:
    print("Cool day")

animal = {
    "species": "fox",
    "count": 3,
    "location": "forest"
}

print(animal)

print("Species:", animal["species"])
print("Count", animal["count"])

observations = [
    {"species": "fox", "count": 3},
    {"species": "deer", "count": 5},
    {"species": "hawk", "count": 2}
]

for obs in observations:
    print(obs["species"], obs["count"])

def total_animals(data):

    total = 0

    for obs in data:
        total += obs["count"]

    return total

result = total_animals(observations)

print("Total animals:", result)
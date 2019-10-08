from weights import objects
from itertools import combinations

occupied_weights = []
occupied_combinations = []

def is_valid(val, tolerance):
  for weight in occupied_combinations:
    # make sure its not too close to a weight
    if (val >= (weight - tolerance) and val <= (weight - tolerance)):
      return False
      # make sure adding this weight to another combination of weights doesn't
      # collide with some other combination of weights
    modded_val = weight + val
    for weight2 in occupied_combinations:
      # make sure its not too close to a weight
      if (modded_val >= (weight2 - tolerance) and modded_val <= (weight2 - tolerance)):
        return False
  return True

def update_combinations(max_combinations):
  global occupied_combinations
  combolist = []
  for i in range(1, 3):
    combos = combinations(occupied_weights, i)
    for combo in combos:
      combolist.append(sum(combo))
  occupied_combinations = combolist
  pass

def setup(starting_weight, starting_objects, ending_weight, tolerance):
  [occupied_weights.append(weight) for (name, weight) in starting_objects]
  print(occupied_weights)

  update_combinations(max_combinations=len(occupied_weights))
  iter_weight = starting_weight
  while iter_weight < ending_weight:
    if is_valid(iter_weight, tolerance):
      occupied_weights.append(iter_weight)
      update_combinations(max_combinations=min(len(occupied_weights), 5))
      print(len(occupied_weights))
    iter_weight += tolerance
  print('results count:', len(occupied_weights))
  print(occupied_weights)
  pass


if __name__ == "__main__":
  setup(
    starting_weight=0.5,
    starting_objects=objects,
    ending_weight=300.0,
    tolerance=0.1
  )
  pass

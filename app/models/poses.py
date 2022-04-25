from typing import Dict
from itertools import zip_longest

POSES = {
  1: {
    'id': 1,
    'name': 'Warrior I',
    'img': '/images/warrior_1.png',
    'video': '/videos/warrior.mp4',
    'level': 'Level: Beginner'
  },
  2: {
    'id': 2,
    'name': 'Warrior II',
    'img': '/images/warrior_2.png',
    'video': '/videos/warrior.mp4',
    'level': 'Level: Beginner to Advanced'
  },
  3: {
    'id': 3,
    'name': 'Warrior III',
    'img': '/images/warrior_3.png',
    'video': '/videos/warrior.mp4',
    'level': 'Level: Advanced'
  },
  4: {
    'id': 4,
    'name': 'Bridge',
    'img': '/images/bridge.png',
    'video': '/videos/bridge.mp4',
    'level': 'Level: Beginner'
  },
  5: {
    'id': 6,
    'name': 'Downward Facing Dog',
    'img': '/images/dog.png',
    'video': '/videos/dog.mp4',
    'level': 'Level: Beginner to Advanced'
  },  
  6: {
    'id': 5,
    'name': 'Wheel Pose',
    'img': '/images/wheel.png',
    'video': '/videos/wheel.mp4',
    'level': 'Level: Advanced'
  },
}

class Poses:
  def __init__(self) -> Dict:
      self.poses = POSES
  
  def values(self):
    return self.poses
  
  def to_array(self):
    return list(self.poses.values())
  
  def group_by(self, grouping: int):
    return zip_longest(*(iter(self.to_array()),) * grouping)
  
  def find_by(self, id: int):
    return self.poses[id]
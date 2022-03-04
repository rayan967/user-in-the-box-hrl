from abc import ABC, abstractmethod
import numpy as np


class BaseFunction(ABC):
  @abstractmethod
  def get(self, env, dist, info):
    pass
  @abstractmethod
  def __repr__(self):
    pass


class NegativeExpDistance(BaseFunction):

  def __init__(self, k=3, shift=-1, scale=0.1):
    self.k = k
    self.shift = shift
    self.scale = scale

  def get(self, env, dist):
    return (np.exp(-dist*self.k) + self.shift)*self.scale

  def __repr__(self):
    return "NegativeExpDistance"


class RewardBonus(BaseFunction):

  def __init__(self, bonus=8, onetime=False):
    self.bonus = bonus

    self.onetime = onetime
    self.active = True

  def get(self, get_bonus):
    if get_bonus and self.active:
      if self.onetime:
        self.active = False
      return self.bonus
    else:
      return 0

  def reset(self):
    self.active = True

  def __repr__(self):
    return "RewardBonus"
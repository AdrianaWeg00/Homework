import unittest
import calc

#Example 1.
def money_in(a,b):
    return(a+b)

class TestMoneyIn(unittest.TestCase):
    def test_money_in(self):
        self.assertEqual(money_in(50,15),65)
        self.assertEqual(money_in(50,15),60)
#Example 2.

def money_out(a,b):
    return(a-b)

class TestMoneyOut(unittest.TestCase):
    def test_money_out(self):
        self.assertEqual(money_out(50,15),35)
        self.assertEqual(money_out(50,15),30)

#Example 3.

def correct_pin(user_attempt, user_pin):
  if user_attempt == user_pin:
    return("Pin is correct")
  else:
    return("Pin is incorrect. Please, try again")

class TestCorrectPin(unittest.TestCase):
  def test_correct_pin(self):
    self.assertIs(1234, 1234)
    self.assertIs(1234, 4321)


if __name__ == '__main__':
  unittest.main()
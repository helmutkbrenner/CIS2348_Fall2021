#  Helmut Brenner  #
#  2037275 #

class FoodItem:
    def __init__(self, name='None', fat=0, carbs=0, protein=0):
        self.name = name
        self.fat = fat
        self.carbs = carbs
        self.protein = protein


def get_calories(self, num_servings):
    # Calorie formula
    calories = ((self.fat * 9) + (self.carbs * 4) + (self.protein * 4)) * num_servings
    return calories


def print_info(self):
    print('Nutritional information per serving of {}:'.format(self.name))
    print('   Fat: {:.2f} g'.format(self.fat))
    print('   Carbohydrates: {:.2f} g'.format(self.carbs))
    print('   Protein: {:.2f} g'.format(self.protein))


if __name__ == '__main__':
    # Get user inputs
    user_input = []
    for i in range(5):
        user_input.append(input())
    print(user_input)


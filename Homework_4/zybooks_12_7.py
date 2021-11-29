#  Helmut Brenner  #
#  2037275  #

def get_age():
    age = int(input())
    if age < 18 or age > 75:
        raise ValueError('Invalid Age')
    return age


def fat_burning_heart_rate(age):
    heart_rate = (220 * .7) - age
    return heart_rate


if __name__ == "__main__":
    # TODO: Modify to call get_age() and fat_burning_heart_rate()
    #       and handle the exception
    try:
        age = get_age()
        burn_rate = fat_burning_heart_rate(age)
        print('Fat burning heart rate for a {} year-old: {} bpm'.format(age, burn_rate))
    except ValueError as excpt:
        print(excpt)
        print('Could not Calculate heart rate info.')

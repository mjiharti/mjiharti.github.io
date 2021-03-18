div1 = ["Lions", "Tigers", "Jaguars", "Cougars"]
div2 = ["Whales", "Sharks", "Piranhas", "Alligators"]
div3 = ["Cubs", "Kittens", "Puppies", "Calfs"]


def create_schedule(team_list):
    """ Create a schedule for the teams in the list and return it"""
    s = []

    if len(team_list) % 2 == 1:
        team_list = team_list + ["BYE"]

    for i in range(len(team_list)-1):

        mid = int(len(team_list) / 2)
        l1 = team_list[:mid]
        l2 = team_list[mid:]
        l2.reverse()

        # Switch sides after each round
        if i % 2 == 1:
            s.append(zip(l1, l2))
        else:
            s.append(zip(l2, l1))

        team_list.insert(1, team_list.pop())
    return s


def main():
    for r in create_schedule(div1):
        for match in r:
            print(match[0] + " - " + match[1])
    """print()
    for round in create_schedule(div2):
        for match in round:
            print(match[0] + " - " + match[1])
    print()
    for round in create_schedule(div3):
        for match in round:
            print(match[0] + " - " + match[1])
    print()
    for round in create_schedule(div1+div2+div3):
        for match in round:
            print(match[0] + " - " + match[1])
        print()"""


if __name__ == "__main__":
    main()


def __count_sum(self, number):
    if number == 0:
        return 0
    else:
        return number + self.__count_sum(number - 1)



class Tree:
    def __init__(self, cargo, left=None, right=None):
        self.left = left
        self.right = right
        self.cargo = cargo

    def __str__(self):
        return str(self.cargo)

def print_tree(tree):
    if tree is None:
        return
    print(tree.cargo)
    print_tree(tree.left)
    print_tree(tree.right)



def yes(ques):
    ans = raw_input(ques)
    return ans[0] == 'y'


def animal():
    root = Tree("bird")

    while True:
        print()
        if not yes("Are you thinking of an animal? "):
            break


        tree = root
        while tree.left is not None:
            prompt = tree.cargo + "? "
            if yes(prompt):
                tree = tree.right
            else:
                tree = tree.left

        guess = tree.cargo
        prompt = "Is it a " + guess + "? "
        if yes(prompt):
            print("I got it!")
            continue

        prompt = "What is the animal's name? "
        animal = raw_input(prompt)
        prompt = "What question would distinguish a {0} from a {1}? "
        question = raw_input(prompt.format(animal, guess))

        tree.cargo = question
        prompt = "If the animal were {0} the answer would be? "
        if yes(prompt.format(animal)):
            tree.left = Tree(guess)
            tree.right = Tree(animal)
        else:
            tree.left = Tree(animal)
            tree.right = Tree(guess)



animal()


class TreeNode:
    def __init__(self, name, designation) -> None:
        self.name = name
        self.designation = designation
        self.children = []
        self.parent = None

    def add_child(self, child):
        child.parent = self
        self.children.append(child)

    def get_level(self):
        level = 0
        p = self.parent
        while p:
            level += 1
            p = p.parent

        return level

    def print_tree(self, mode):
        spaces = ' ' * self.get_level() * 3
        prefix = spaces + "|__" if self.parent else ""

        if mode == "name":
            print(f'{prefix} {self.name}')
        elif mode == "designation":
            print(f'{prefix} {self.designation}')
        elif mode == "both":
            print(f'{prefix} {self.name} ({self.designation})')
        else:
            print("Please specify correct mode, avaible modes: name, designation, both")

        if self.children:
            for child in self.children:
                child.print_tree(mode)


def build_management_tree():

    root = TreeNode("Nilupul", "CEO")

    cto = TreeNode('Chinmay', "CTO")
    ih = TreeNode("Vishwa", "Infrastructure Head")
    ah = TreeNode("Aamir", "Application Head")

    cto.add_child(ih)
    ih.add_child(TreeNode("Dhaval", "Cloud Manager"))
    ih.add_child(TreeNode("Abhijit", "App Manager"))
    cto.add_child(ah)

    hrh = TreeNode("Gels", "HR Head")
    hrh.add_child(TreeNode("Peter", "Recruitment Manager"))
    hrh.add_child(TreeNode("Waqas", "Policy Manager"))

    root.add_child(cto)
    root.add_child(hrh)

    return root


class TreeNode2(TreeNode):
    def __init__(self, data):
        self.data = data
        self.children = []
        self.parent = None

    def print_tree(self, level):

        if self.get_level() > level:
            return

        spaces = ' ' * self.get_level() * 3
        prefix = spaces + "|__" if self.parent else ""

        print(prefix + self.data)

        if self.children:
            for child in self.children:
                child.print_tree(level)


def build_location_tree():
    root = TreeNode2("Global")

    country_1 = TreeNode2("India")
    state_1 = TreeNode2("Gujarat")
    state_1.add_child(TreeNode2("Ahmedabad"))
    state_1.add_child(TreeNode2("Baroda"))
    state_2 = TreeNode2("Karnataka")
    state_2.add_child(TreeNode2("Bangluru"))
    state_2.add_child(TreeNode2("Mysore"))

    country_2 = TreeNode2("USA")
    state_3 = TreeNode2("New Jersey")
    state_3.add_child(TreeNode2("Princeton"))
    state_3.add_child(TreeNode2("Trenton"))
    state_4 = TreeNode2("California")
    state_4.add_child(TreeNode2("San Francisco"))
    state_4.add_child(TreeNode2("Mountain View"))
    state_4.add_child(TreeNode2("Palo Alto"))

    country_1.add_child(state_1)
    country_1.add_child(state_2)
    country_2.add_child(state_3)
    country_2.add_child(state_4)

    root.add_child(country_1)
    root.add_child(country_2)

    return root


root = build_location_tree()
root.print_tree(4)

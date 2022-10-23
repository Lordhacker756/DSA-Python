class Tree():
    def __init__(self, data):
        # Tree has three main parts
        self.data = data  # The data it stores
        self.children = []  # The number of branches a node has
        self.parent = None  # The no of parents a node has (Level)

    def get_level(self):
        # The main idea is to count the number of parents for each level
        level = 0
        p = self.parent
        while p:  # Jis value pe call kiya agar uska parent hai to
            level += 1  # add 1 to level
            # update current parent with the parent of parent if there otherwise it will become none
            p = p.parent

        return level

    def print_tree(self):
        spaces = ' ' * self.get_level() * 3
        # Add decorator only if it has a parent, else it is root hence, no decorator needed
        decor = spaces+'|___' if self.parent else ''
        print(decor + self.data)
        if self.children:
            for child in self.children:
                child.print_tree()  # The child is passed as the self, hence now his childrens are printed

    def add_child(self, child):
        child.parent = self  # jiske repect me call hua wo parent, and value becomes it's childrens
        self.children.append(child)


def build_tree():
    # Added the root node
    Company = Tree("Nilupul (CEO)")
    # We'll add CTO and HR under CEO later

    # Now need to add people under him
    CTO = Tree("Chinmay (CTO)")

    # Creating infrahead tree
    # ⚠ Every node in itself a tree not a string
    InfraHead = Tree("Vishwa (Infrastructure Head)")
    InfraHead.add_child(Tree("Dhaval (Cloud Manager)"))
    InfraHead.add_child(Tree("Abhijit (App Manager)"))

    # Now creating Application head tree
    Application = Tree("Aamir (Applicaiton Head")

    # Add application head and Infrahead under CTO
    CTO.add_child(InfraHead)
    CTO.add_child(Application)

    # HR Head tree
    HR_head = Tree("Gels (HR Head)")

    HR_head.add_child(Tree("Peter (Recruitment Manager)"))
    HR_head.add_child(Tree("Waqas (Policy Manager)"))

    # Adding CTO and HR Head under CEO
    Company.add_child(CTO)
    Company.add_child(HR_head)

    Company.print_tree()


if __name__ == '__main__':
    build_tree()

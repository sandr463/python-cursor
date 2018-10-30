from utils.Task_1 import members
from utils.Task_2 import upper_name
from utils.Task_3 import percentage_of_progress
from utils.Task_4 import filter_dict
from utils.Task_5 import summary
from utils.Task_6 import sort_by_name_length

if __name__ == "__main__":
    import copy

    # Task_1
    new_members = copy.deepcopy(members)
    print("Task_1: ", new_members, "\n")

    # Task_2
    new_members = copy.deepcopy(members)
    print("Task_2: ", upper_name(new_members), "\n")

    # Task_3
    new_members = copy.deepcopy(members)
    print("Task_3: ", percentage_of_progress(new_members), "\n")

    # Task_4
    new_members = copy.deepcopy(members)
    print("Task_4: ", filter_dict(new_members), "\n")

    # Task_5
    new_members = copy.deepcopy(members)
    print("Task_5: ", summary(new_members), "\n")

    # Task_6
    new_members = copy.deepcopy(members)
    print("Task_6: ", sort_by_name_length(new_members), "\n")

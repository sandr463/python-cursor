import csv


def dict_to_csv(data: dict):
    with open('group_list.csv', 'w') as group:
        fields = ['First name', 'Last name', 'Telegram tag']
        writer = csv.DictWriter(group, fieldnames=fields)
        writer.writeheader()
        writer.writerows(data)


if __name__ == '__main__':
    from .data import group_list

    dict_to_csv(group_list)

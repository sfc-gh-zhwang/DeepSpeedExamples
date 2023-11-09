import csv


def get_prompts(n):
    prompts = []
    with open('prompts/prompts2048.csv', newline='') as file:
        reader = csv.reader(file)
        for row in reader:
            prompts.append(row[0])
    return prompts[:n]

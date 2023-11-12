import csv
from scipy import stats
import numpy as np
import math


def calculate_mean(data, confidence_level=0.95):
    # Calculate the sample statistics
    sample_size = len(data)
    if sample_size == 0:
        raise ValueError("input is empty")
    if sample_size == 1:
        mean, lb, up = data[0], data[0], data[0]
    else:
        mean = np.mean(data)
        sample_std = np.std(data, ddof=1)  # ddof=1 for sample standard deviation

        # Calculate the critical value from the t-distribution (two-tailed)
        t_critical = stats.t.ppf((1 + confidence_level) / 2, df=sample_size - 1)

        # Calculate the margin of error
        margin_of_error = t_critical * (sample_std / np.sqrt(sample_size))

        # Calculate the confidence interval
        lb = mean - margin_of_error
        up = mean + margin_of_error
        # return mean, lb, up, f'{mean:.4f}[{lb:.4f}, {up:.4f}]'
    return f'{mean:.4f}[{lb:.4f}, {up:.4f}]'


# def get_prompts(n):
#     prompts = []
#     with open('prompts/prompts2048.csv', newline='') as file:
#         reader = csv.reader(file)
#         for row in reader:
#             prompts.append(row[0])
#     return prompts[:n]


def shrink_sentence(s, r):
    words = s.split()
    n = math.ceil(len(words) * r)
    return ' '.join(words[:n])


# r=0.3775 -> mean tokens 1024
# r=0.179 -> mean tokens 512
# r=0.079 -> mean tokens 256
def get_prompts(n, r=0.3775):
    prompts = []
    with open('prompts/arxiv.csv', newline='') as file:
        reader = csv.reader(file)
        for row in reader:
            prompt = f'''<s>[INST]<<SYS>>
    Please summarize the text that is given. Return just the summary and no additional conversational dialog such as ""Sure, here is the summary of the text:"".
    <</SYS>> {shrink_sentence(row[0], r)}[/INST]'''
            prompts.append(prompt)
    return prompts

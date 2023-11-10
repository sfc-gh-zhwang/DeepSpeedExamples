import csv
from scipy import stats


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


def get_prompts(n):
    prompts = []
    with open('prompts/prompts2048.csv', newline='') as file:
        reader = csv.reader(file)
        for row in reader:
            prompts.append(row[0])
    return prompts[:n]

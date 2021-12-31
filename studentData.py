import statistics
import pandas as pd
import csv
import plotly.figure_factory as ff

df = pd.read_csv("StudentsPerformance.csv")
math_score = df["math score"].tolist()
writing_score = df["writing score"].tolist()
reading_score = df["reading score"].tolist()

math_mean = statistics.mean(math_score)
writing_mean = statistics.mean(writing_score)
reading_mean = statistics.mean(reading_score)
print("The mean of the math, writing and reading score is", math_mean, writing_mean, reading_mean)

math_median = statistics.median(math_score)
writing_median = statistics.median(writing_score)
reading_median = statistics.median(reading_score)
print("The median of the math,writing and reading score is", math_median, writing_median, reading_median)

math_mode = statistics.mode(math_score)
writing_mode = statistics.mode(writing_score)
reading_mode = statistics.mode(reading_score)
print("The mode of the math, writing and reading score is", math_mode, writing_mode, reading_mode)

math_std = statistics.stdev(math_score)
writing_std = statistics.stdev(writing_score)
reading_std = statistics.stdev(reading_score)
print("The standard deviation of the math, writing, and readin score is", math_std, writing_std, reading_std)

first_math_std_start, first_math_std_end = math_mean - math_std, math_mean + math_std
math_list_1_std = [result for result in math_score if result > math_mean - math_std and result < math_mean + math_std]
print("The percentage of math data lies within the first standard deviation is", len(math_list_1_std) * 100.0 / len(math_score))

second_math_std_start, second_math_std_end = math_mean - 2*math_std, math_mean + 2*math_std
math_list_2_std = [result for result in math_score if result > math_mean - 2*math_std and result < math_mean + 2*math_std]
print("The percentage of math data lies within the second standard deviation is", len(math_list_2_std) * 100.0 / len(math_score))

third_math_std_start, third_math_std_end = math_mean - 3*math_std, math_mean + 3*math_std
math_list_3_std = [result for result in math_score if result > math_mean - 2*math_std and result < math_mean + 3*math_std]
print("The percentage of math data lies within the third standard deviation is", len(math_list_3_std) *100.0 / len(math_score))

first_writing_std_start, first_writing_std_end = writing_mean - writing_std, writing_mean + writing_std
writing_list_1_std = [result for result in writing_score if result > writing_mean - writing_std and result < writing_mean + writing_std]
print("The percentage of writing data lies within the first standard deviation is", len(writing_list_1_std) * 100.0 / len(writing_score))

second_writing_std_start, second_writing_std_end = writing_mean - 2*writing_std, writing_mean + 2*writing_std
writing_list_2_std = [result for result in writing_score if result > writing_mean - 2*writing_std and result < writing_mean + 2*writing_std]
print("The percentage of writing data lies within the second standard deviation is", len(writing_list_2_std) * 100.0 / len(writing_score))

third_writing_std_start, third_writing_std_end = writing_mean - 3*writing_std, writing_mean + 3*writing_std
writing_list_3_std = [result for result in writing_score if result > writing_mean - 2*writing_std and result < writing_mean + 3*writing_std]
print("The percentage of writing data lies within the third standard deviation is", len(writing_list_3_std) *100.0 / len(writing_score))

first_reading_std_start, first_reading_std_end = reading_mean - reading_std, reading_mean + reading_std
reading_list_1_std = [result for result in reading_score if result > reading_mean - reading_std and result < reading_mean + reading_std]
print("The percentage of reading data lies within the first standard deviation is", len(reading_list_1_std) * 100.0 / len(reading_score))

second_reading_std_start, second_reading_std_end = reading_mean - 2*reading_std, reading_mean + 2*reading_std
reading_list_2_std = [result for result in reading_score if result > reading_mean - 2*reading_std and result < reading_mean + 2*reading_std]
print("The percentage of reading data lies within the second standard deviation is", len(reading_list_2_std) * 100.0 / len(reading_score))

third_reading_std_start, third_reading_std_end = reading_mean - 3*reading_std, reading_mean + 3*reading_std
reading_list_3_std = [result for result in reading_score if result > reading_mean - 2*reading_std and result < reading_mean + 3*reading_std]
print("The percentage of reading data lies within the third standard deviation is", len(reading_list_3_std) *100.0 / len(reading_score))

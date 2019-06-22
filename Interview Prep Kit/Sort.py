############# HackerRank Challenge: Fraudulent Activity Notifications ############
from collections import deque
import numpy as np


def activity_notifications(expenditures, trailing_days):
    """ Given the number of trailing days d and a client's total daily expenditures
        for a period of n days, find and print the number of times the client will receive
        a notification over all n days. Allowed expenditures are non-negative integers up to 200"""
    expenditures_in_period = deque()
    frequency_distribution = np.zeros(201)

    notice_count = 0
    for i in range(0, len(expenditures)):

        expenditure = expenditures[i]
        # Populate expenditures in peiod and freq distr before trailing_days days are reached
        if i < trailing_days:
            expenditures_in_period.append(expenditure)
            frequency_distribution[expenditure] += 1

        else:
            # Notice will be sent if current expenditure is more than 2*median of trailing expenditures
            if expenditure >= median(frequency_distribution) * 2:
                notice_count += 1

            # Remove oldest expenditure from expenditures in period and freq distribution
            frequency_distribution[expenditures_in_period.popleft()] -= 1

            # Add newest expenditure to expenditures in period and to frequency distribution
            expenditures_in_period.append(expenditure)
            frequency_distribution[expenditure]

    return notice_count


def median(freq_distribution):
    """ Calculates the median of a frequency distribution. Uses the size
        of the distribution, which allows for faster calculations when l is uneven"""
    sum_distribution = sum(freq_distribution)
    count = 0

    for value, freq in enumerate(freq_distribution):
        count += freq
        if count > sum_distribution/2:
            break
    # for un even case, median is just the middle value
    if sum_distribution % 2 == 1:
        return value
    # for even case, median is average of two middle values
    else:
        next_non_zero_value = next((v for v, f in enumerate(freq_distribution[value + 1:]) if f), None)
        return (value + next_non_zero_value) / 2


############# HackerRank Challenge:  Comparator ############


class Player:

    def __init__(self, name, score):
        self.name = name
        self.score = score

    @staticmethod
    def comparator(a, b):
        """ Returns -1 if  a < b, 0 if a = b, and 1 if a > b."""
        if a.score == b.score:
            if a.name == b.name:
                return 0
            else:
                return 1 if a.name > b.name else -1
        else:
            return 1 if a.score < b.score else -1


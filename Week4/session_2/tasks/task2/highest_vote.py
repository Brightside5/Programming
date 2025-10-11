# Week 4, Session 2: Task 2

def most_frequent_string(votes):
    """
    This function identifies the string that appears most frequently
    (highest count) in the votes argument and returns it along with the count
    of its occurrences. It assumes there is a single most frequent string
    (i.e., no ties for the highest count)

    Args:
        votes (list): A list of strings representng votes,
        e.g. ['apples', 'bananas', 'grapes', 'tomatoes']

    Returns:
        - tuple: (str, int) where str is the string with the highest count,
        and int is the count of its occurences
        - None, None: if votes is empty.
    """

    # Updated version to handle ties: return list of items if ties, else single item
    if not votes:
        return None, None
    count = {}
    for vote in votes:
        count[vote] = count.get(vote, 0) + 1
    max_count = max(count.values())
    top_items = [item for item, cnt in count.items() if cnt == max_count]
    if len(top_items) == 1:
        return top_items[0], max_count
    else:
        return top_items, max_count

Leeds = ['date', 'apple', 'cherry', 'date', 'apple', 'apple', 'elderberry',
         'date', 'elderberry', 'elderberry', 'date', 'banana']
Manchester = ['Jesy', 'Leigh-Anne', 'Perrie', 'Leigh-Anne', 'Jade',
              'Leigh-Anne', 'Perrie', 'Leigh-Anne', 'Jesy', 'Jade',
              'Leigh-Anne', 'Leigh-Anne', 'Leigh-Anne', 'Leigh-Anne',
              'Leigh-Anne', 'Jade', 'Jesy', 'Jade', 'Perrie', 'Jade',
              'Jade', 'Jesy', 'Perrie', 'Perrie', 'Jade', 'Leigh-Anne',
              'Jesy', 'Jesy', 'Perrie', 'Jesy']


# Check if correct output is produced
print(most_frequent_string(Leeds))          # ('date', 4)
print(most_frequent_string(Manchester))     # ('Leigh-Anne', 10)
print(most_frequent_string([]))             # (None, None)

# Once completed, update the function to return all items that ties for the
# highest count in a list, e.g  (['apples', 'bananas'], 9). If there is no
# ties, return a single string and a value as usual, e.g ('apples, 9).

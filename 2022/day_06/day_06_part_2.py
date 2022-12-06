"""

--- Part Two ---

Your device's communication system is correctly detecting packets, but still isn't working. It looks like it also needs to look for messages.

A start-of-message marker is just like a start-of-packet marker, except it consists of 14 distinct characters rather than 4.

Here are the first positions of start-of-message markers for all of the above examples:

    mjqjpqmgbljsphdztnvjfqwrcgsmlb: first marker after character 19
    bvwbjplbgvbhsrlpgdmjqwftvncz: first marker after character 23
    nppdvjthqldpwncqszvftbrmjlhg: first marker after character 23
    nznrnfrfntjfmvfwmzdfjlvtqnbhcprsg: first marker after character 29
    zcfzfwzzqfrljwzlrfnpqdbhtmscgvjw: first marker after character 26

How many characters need to be processed before the first start-of-message marker is detected?


"""

def subroutine(signal):
    ''' Signal is a string containing letters.
    Subroutine return the position (from 1 to ...)
    where a caracter is preceded by 13 differents caracters
    '''
    for i in range(13, len(signal)):
        if len(set(signal[i-13:i+1])) == 14:
            return i+1


def resolve_problem(data_file):
    data = open(data_file, 'r')
    data_list = data.read().splitlines()
    
    return subroutine(data_list[0])


print(resolve_problem('day_06_test_input'))
print(resolve_problem('day_06_my_input'))











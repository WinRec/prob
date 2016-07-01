import random
import sys
import time

__author__ = 'yyy'

def gen_result(num_list):
    print '        gen result from:{}'.format(num_list)
    return random.sample(num_list, 1)

def gen_fake(num_list):
    print '        gen fake from:{}'.format(num_list)
    return random.sample(num_list, 1)

def make_choice(num_list):
    print '        make choice from: {}'.format(num_list)
    return random.sample(num_list, 1)

pool_list = [1,2,3,4,5]
def main(argv):
    right_count = 0
    wrong_count = 0
    right_count2 = 0
    wrong_count2 = 0
    round_count = 0
    num_list = list(pool_list)

    print 'tttttttt'
    start_ms = int(round(time.time()*1000))
    while True:
        print '-------------------------------------------------------------------------'
        actual_num = gen_result(num_list)
        print '    THE num: {}'.format(actual_num)
        choose_num = make_choice(num_list)
        print '    choose num: {}'.format(choose_num)
        #judge choose
        if choose_num[0] == actual_num[0]:
            right_count += 1
        else:
            wrong_count += 1

        print '    num list: {}'.format(num_list)
        print '    removing actual: {}'.format(actual_num[0])
        num_list.remove(actual_num[0])
        if choose_num[0] != actual_num[0]:
            print '    removing choose: {}'.format(choose_num[0])
            num_list.remove(choose_num[0])

        fake_num = gen_fake(num_list)
        print '    fake num: {}'.format(fake_num)

        num_list = list(pool_list)
        print '    reset num list to: {}'.format(num_list)

        #remove fake num, and chose again
        num_list.remove(fake_num[0])
        print '    removed fake: {}'.format( num_list)
        #change choice to the other one
        num_list.remove(choose_num[0])
        print '    removed choose: {}'.format( num_list)
        choose_num = make_choice(num_list)
        print '    changed choice to: {}'.format(choose_num)

        if choose_num[0] == actual_num[0]:
            right_count2 += 1
        else:
            wrong_count2 += 1

        # reset num list
        num_list = list(pool_list)
        print '    >>> done, reset num list for next round: {} <<<'.format(num_list)

        round_count += 1
        print 'round: {}'.format(round_count)
        print 'unchanged choice condition: right/wrong: {}'.format(right_count) +'/{}'.format(wrong_count)

        print 'changed choice condition: right/wrong: {}'.format(right_count2) +'/{}'.format(wrong_count2)
        print '-------------------------------------------------------------------------'
        if round_count == 500000:
            p1 = right_count/float(round_count)
            p2 = right_count2/float(round_count)
            print '>>>'
            print '>>> possibility in unchanged choice: {}'.format(p1) # 1/n
            print '>>> possibility in changed choice: {}'.format(p2) # (n-1)/n*(n-2)
            end_ms = int(round(time.time()*1000))
            print '>>> total time used: {} ms'.format(end_ms - start_ms)
            print '>>>'
            break


if __name__ == '__main__':
    main(sys.argv[1:])

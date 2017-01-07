#to be added at the begining of a conversation to delete the content of already used words
# f_bd_search = open("search_bd.txt", "w")
# f_bd_search.writelines("")

def add_flattery(m_output):
    f_bd_read = open("flattery_bd.txt", "r")  # contain words that will be search in the output and questions
    f_bd_search = open("search_bd.txt", "r") # save words already used to add flattery

    ok_in_str = 0 # used to do actions based on the lines from flattery_bd.txt
    word_find_bd = 0 #incremented when a bd_word match the output
    search_word = "" # first word that should match the output
    search2_word = "" # second word that match the output
    percentage = 0 # the percentage of chosing a question if a match woth the aoutput is foud
    ask_question = [] # the list of questions that could be added
    is_word_used = 0 # if a word already used to add flattery at the end of the output
    with f_bd_read as fp:
        for line in fp:  #search line to line in bd

            if ok_in_str is 4:# read the flattery that could be added to the end of output
                if "##$2##" in line:#end of the flattery
                    ok_in_str = 0
                    word_find_bd = 1
                elif ok_in_str is 4:#save all flattery into a list
                    list_word = []
                    line = line.replace("$$#2$$", search2_word)
                    list_word.append(line)
                    list_word.append(list_word.pop()[0:-1])
                    ask_question.append(list_word.pop())

            elif ok_in_str is 3: # take the percentage line from bd
                list_word = []
                list_word.append(line)
                list_word.append(list_word.pop()[0:-1])#remove "\n"
                percentage = list_word.pop()
                ok_in_str = 4

            elif ok_in_str is 2: #check if the second word match
                ok_in_str = 0
                list_word = []
                list_word = line.split(" ")
                temp_nr = list_word.pop()
                list_word.append(temp_nr[0:-1]) #remove "\n"
                for elem in list_word:
                    if str(elem).lower() in m_output.lower():
                        out_str2_list = []
                        out_str2_list = m_output.lower().split(" ")
                        is_len2_ok = 0
                        for out_2_elem in out_str2_list: #verify if the second word has length equal to the output word
                            if str(elem).lower() in out_2_elem:
                                if len(out_2_elem) is len(elem):
                                    is_len2_ok = 1
                                if len(out_2_elem) is len(elem) + 1: # for plurals
                                    is_len2_ok = 1

                        if is_len2_ok is 1:
                            ok_in_str = 3
                            search2_word = elem

                        if is_len2_ok is 0: # if words has different length continue searching in bd
                            ok_in_str = 0
                        if elem in "##$3##": # there is no second word to match , only the first word
                            ok_in_str = 3
                            search2_word = "##$3##"

            elif ok_in_str is 1: # first world from BD that should match he output
                ok_in_str = 0
                list_word = []
                list_word.append(line)
                list_word.append(list_word.pop()[0:-1]) #reove the "\n" from end
                search_word = list_word.pop()

                if str(search_word).lower() in m_output.lower(): # is first world matching the output
                    ok_in_str = 2
                    is_word_used = 0

                    out_str_list = []
                    out_str_list=m_output.lower().split(" ")
                    is_len_ok=0
                    for elem in out_str_list:#verify if the first word has length equal to the output word
                        if str(search_word).lower() in elem:
                            if len(elem) is len(search_word):
                                is_len_ok=1
                            if len(elem) is len(search_word)+1:# for plurals
                                is_len_ok = 1

                    if is_len_ok is 1:
                        f_bd_search = open("search_bd.txt", "r")
                        with f_bd_search as line_file:# search if the word is already used in the search_bd.txt
                            for bd_line in line_file:
                                if search_word in bd_line:
                                    ok_in_str = 0
                                    is_word_used = 1
                    if is_len_ok is 0:# if words has different length continue searching in bd
                        ok_in_str = 0

            if "##$1##" in line: #a new entry from the BD is found
                ok_in_str = 1

            if word_find_bd is 1:
                break;

    from random import randint

    if is_word_used is 0:
        if word_find_bd is 1:
            my_rand_question = randint(0, len(ask_question) - 1)# select random number for a flattery choose
            my_rand_per = randint(0, 99)
            if my_rand_per < int(percentage):# % chance to be added
                temp_q=str(ask_question[my_rand_question])
                if "." in m_output[-1]: # chck if the output has "." at the end, add the flatter with upper first letter
                    m_output = m_output + " "+ temp_q[:1].upper() + ask_question[my_rand_question][1:]
                elif "." in m_output[-2:-1]:
                    m_output = m_output + " "+ temp_q[:1].upper() + ask_question[my_rand_question][1:]
                else:
                    m_output = m_output + ". "+ temp_q[:1].upper() + ask_question[my_rand_question][1:]
                f_bd_search = open("search_bd.txt", "a+")#write the first word in the used words from bd
                f_bd_search.writelines("\n")
                f_bd_search.writelines(search_word)

    f_bd_read.close()
    f_bd_search.close()

    return m_output


def my_main():
    # to be added at the begining of a conversation to delete the content of already used words
    f_bd_search = open("search_bd.txt", "w")
    f_bd_search.writelines("")

    #conversation
    print(add_flattery("Brad Pitt have black eye"))
    print(add_flattery("Brad Pitt have blue eyes"))
    print(add_flattery("Brad Pitt have blue black"))
    print(add_flattery("I buy 1 kg of green. apples"))

my_main()
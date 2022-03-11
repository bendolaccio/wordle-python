from base import Player
from settings import NUMBER_OF_WORDS, PENALIZE_REPETITION


class IntelligentPlayer(Player):
    def __init__(self, name, word_bank):
        self.name = name
        self.word_bank = word_bank
        self.letter_in_word = {}        # format: 'A' : [1,3,5]
        self.letter_not_in_word = {}    # format: 'A' : [1,3,5]
                                        #         'B' : [1,3,4,5]
    
    def __str__(self):
        return self.name
    
    def checkLettersNotInWord(self, word_bank, letter_not_in_word):
        newWordBank = word_bank
        if len(letter_not_in_word.keys())!=0:
            result = []
            for letter in letter_not_in_word.keys():
                positions = letter_not_in_word[letter]
                for pos in positions:
                    temp = [word for word in word_bank if word[pos] == letter] #find all the words that contains that letter in that position
                    result.extend([word for word in temp if word not in result]) # copy in result without duplicates
            newWordBank = [word for word in word_bank if word not in result] #create a new list with all the words of word_bank without words in res
            print(f'Word bank reduced of {len(word_bank)-len(newWordBank)} words by elimination')
        return newWordBank
    
    def checkLettersInWord(self, word_bank, letter_in_word): #only purpose, for now, is to filter words that contains yellow letters
        newWordBank = word_bank
        if len(letter_in_word.keys())!=0:
            result = []
            yellow_letters = [letter for letter in letter_in_word.keys()if len(letter_in_word[letter]) == 0]
            if len(yellow_letters) != 0:
                temp = [word for word in word_bank if all(x in word for x in yellow_letters)] #extracts words that contains ALL yellow letters at once. Not one or another
                result.extend([word for word in temp if word not in result])
                newWordBank = [word for word in word_bank if word in result]
            print(f'Word bank reduced of {len(word_bank)-len(newWordBank)} words by keeping only words with yellow letters')
        return newWordBank
    
    #this function iterate on each letter of the knowledge so far and select 
    # all the words that match with the letter considered
    def reduceWordBank(self, word_bank, letter_not_in_word, letter_in_word):
        reduced_word_bank = self.checkLettersNotInWord(word_bank, letter_not_in_word)
        reduced_word_bank = self.checkLettersInWord(reduced_word_bank, letter_in_word)

        return reduced_word_bank
    
    def update_knowledge(self, letter_not_in_word, letter_in_word):
        self.letter_not_in_word = letter_not_in_word
        self.letter_in_word = letter_in_word
    
    def choose(self, i, letter_not_in_word):
        print(f'Length of word_bank = {len(self.word_bank)}')
        self.word_bank = self.reduceWordBank(self.word_bank, self.letter_not_in_word, self.letter_in_word)
        print(f'Length of word_bank reduced = {len(self.word_bank)}')
        
        Ld_word, Ld_word_average = self.words_pos_presence(self.word_bank, P='00000')

        D_word_average = self.word_average(self.word_bank, Ld_word_average)

        self.print_prob_pos_letter(Ld_word_average, True, 5) # 5 letters max in output. If True then desc order

        attempt = self.print_prob_word(D_word_average, NUMBER_OF_WORDS) # n words max in output


        #attempt = input('Attempt #' + str(i + 1) + ': ').upper() #used for a test
        print(f"Attempt #{i+1}: {attempt}")
        #time.sleep(3)
        
        return attempt
    
    def get_average(self, count_let,tot):
        return float(f"{count_let/tot:.4f}")

    # revert a dictionary by exchanging keys and values
    def dictInv(self, D):
        return {k:[v for v in D.keys() if D[v] == k] for k in set(D.values())}
    
    #the aim of this function is to return a statistic of how the letter are distributed in the form of pos : [ A : 2, B : 4, C : 9]
    def words_pos_presence(self, word_bank, P):

        Ld_word = [ dict() for x in range(len(P))]

        # dictionary for counting letters
        for word in word_bank:
            for i in range(len(word)):
                try :
                    Ld_word[i][word[i]] += 1
                except KeyError:
                    Ld_word[i][word[i]] = 1

        # dictionary with the %
        Ld_word_average = [ {k:self.get_average(Ld_word[i][k],len(word_bank))  for k in Ld_word[i].keys()} for i in range(len(Ld_word))]


        return Ld_word, Ld_word_average
    
    # returns two lists ordered by increasing value and by length equal to head
    def ordered_list_key_value_reversed(self, Ld_word_average,Ld_word_average_pure,reverse = True, head=10):
        L_average = [k for k in Ld_word_average.keys()] #extract all perc of single letters in a list

        L_average.sort(reverse=reverse) #order the list

        L_word = []

        for perc in L_average:                  #for every perc (now sorted) get the right letter and create a list ordered
            L_word += Ld_word_average[perc]     
                                                
        L_word = L_word[:head]

        L_average = [Ld_word_average_pure[k] for k in L_word]

        return L_word,L_average

    # this function penalizes words with letter repeated
    def penalize_repetition(self, Ld_word_average_pure):
        for word in Ld_word_average_pure.keys():
            repetition = 0
            d = {}
            flag_repetition = False
            for letter in word:
                try:
                    d[letter] += 1
                    repetition += 1
                    flag_repetition = True
                except KeyError:
                    d[letter] = 1
            if flag_repetition:
                Ld_word_average_pure[word] -= PENALIZE_REPETITION * repetition
        return Ld_word_average_pure

    
    #returns a dictionary with words in the set and their probabilities
    def word_average(self, word_bank, Ld_word_average):
        Ld_word_average_pure = {k:self.get_average(sum([Ld_word_average[i][k[i]] for i in range(len(k))]),len(k)) for k in word_bank}
        Ld_word_average_pure = self.penalize_repetition(Ld_word_average_pure)
        return Ld_word_average_pure

    # print function of probabilities
    def print_prob_word(self, Ld_word_average_pure,head=10):

        Ld_word_average = self.dictInv(Ld_word_average_pure)

        L_word,L_average = self.ordered_list_key_value_reversed(Ld_word_average,Ld_word_average_pure,True,head)


        print("-*"*35)
        print(f"Totale Parole rimaste: {len(Ld_word_average_pure)} :")
        print("__"*35)
        for i in range(len(L_word)):
            print(f"-{i+1} : {L_word[i]}  --->  {L_average[i]*100:.2f}%")
        print("-*"*35)

        return L_word[0]

    #input lista di dizionari con un dizionario per posizione e la lettera con percentuale di presenza
    #head serve per scegleire quanti elementi stampare massimo
    #reverse se True, stampa in ordine decrescente, altrimenti in ordine crescente
    def print_prob_pos_letter(self, Ld_word_pure,reverse = True, head=10):

        tail = None
        if reverse == True:
            par = "più probabili"
        else :
            par = "meno probabili"
            tail = -1

        Ld_word = Ld_word_pure.copy()

        for i in range(len(Ld_word)):
            Ld_word[i] = self.dictInv(Ld_word[i])



        print("-*"*35)
        print(f"Totale lettere {par} per posizione:")
        for i in range(len(Ld_word)):
            print("__"*35)
            print(" "*20,end=""), print(f"Posizione {i+1}:")
            print("__"*35)

            L_let,L_aver = self.ordered_list_key_value_reversed(Ld_word[i],Ld_word_pure[i],True,head)

            for x in range(len(L_let)):
                print(f"-{x+1} : {L_let[x].upper()}  --->  {L_aver[x]*100:.2f}%")
            print("__"*35)
        print("-*"*35)
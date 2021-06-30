#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Apr 19 09:28:54 2021

@author: eugene
"""
import math 


# Helper Function " clean text " 
def clean_text(txt):
        """
        Takes a string of text txt as a parameter and returns a list 
        containing the words in txt after it has been “cleaned”. 
        """
        clean = ''
        for letter in txt:
            if letter not in '.,?!;:"':
                clean += letter
        return clean.lower().split(' ')
    
# Helper function " Stem "  
def stem(s): 
    """
    Return the stem of s. The stem of a word is the root part of the word, 
    which excludes any prefixes and suffixes.
    """
    if len(s) < 4: 
        return s 
    
    if s[-3:] == 'ers':
        s = s[:-3]
    if s[-1] == 's': 
        s = s[:-1]
        
    if s[-3:] == 'ing':
        if len(s) <= 4: 
            s = s 
        elif s[-4] == s[-5]:
            s = s[:-4]
        else: 
            s[:-3]   
    elif s[-1] == 'e': 
        s = s[:-1]
    elif s[-1] == 'y':
        s = s[:-1] + 'i'
    elif s[:-2] == 'er': 
        s = s[:-2]
    elif s[:-2] == 'ed':
        s = s[:-2]
        
    if s[:3] == 'dis' or s[:3] == 'pre' or s[:3] == 'pro' or s[:3] == 'sub':
        s = s[3:]
    if s[:2] == 'un' or s[:2] == 'up' or s[:2] == 'in':
        s = s[2:]
    
    return s 

# Helper function " compare_dictionaries " 
def compare_dictionaries(d1, d2):
    """
     Take two feature dictionaries d1 and d2 as inputs, and it should compute 
     and return their log similarity score
     """
    score = 0
    total = sum(d1.values())
    for i in d2:
        if i in d1: 
            score += d2[i] * math.log(d1[i] / total) 
        else: 
            score += d2[i]* math.log( 0.5 / total) 
    return score 
    

 
class TextModel:
    def __init__(self, model_name):
        """
        Constructs a new TextModel object by accepting a string model_name 
        as a parameter and initializing the following three attributes:
            
            1. Name
            2. Words
            3. words_length 
        """
        self.name = model_name 
        self.words = {}
        self.word_lengths = {}
        self.stems = {}
        self.sentence_lengths = {}
        self.most_used_words = {}
        
    def __repr__(self) :
        """
        Returns a string that includes the name of the model as well as the
        sizes of the dictionaries for each feature of the text.
        """
        s = 'text model name: ' + self.name + '\n'
        s += '  number of words: ' + str(len(self.words)) + '\n'
        s += '  number of word lengths: ' + str(len(self.word_lengths)) + '\n'
        s += '  number of stems: ' + str(len(self.stems)) + '\n'
        s += '  number of sentence lengths: ' +str(len(self.sentence_lengths)) + '\n'
        s += '  number of "top 10 most used words" used: ' + str(len(self.most_used_words)) + '/10'
        return s
            
    def add_string(self, s):
        
        counter = 0 
        for w in s.split():
            counter += 1
            if w[-1] in '.?!':
                if counter not in self.sentence_lengths:
                    self.sentence_lengths[counter] =1 
                    counter = 0
                else: 
                    self.sentence_lengths[counter] += 1
                    counter = 0
                    
                
        most_used_words_counter = 0 
        for w in s.split():
            if w == 'the' or w == 'of' or w == 'and' or w == 'a' or w == 'to' or w == 'in' or w == 'is' or w == 'you' or w == 'that' or w == 'it':
                 most_used_words_counter += 1
                 if w not in self.most_used_words:
                    self.most_used_words[w] = 1
                 else: 
                    self.most_used_words[w] += 1
        
        word_list = clean_text(s)
        
        for w in word_list: 
            if w in self.words:
                self.words[w] += 1
            else:
                self.words[w] = 1 
                
            word_respective_length = len(w)
        
            if word_respective_length in self.word_lengths: 
                self.word_lengths[word_respective_length] += 1
            else: 
                self.word_lengths[word_respective_length] = 1 
                
            stemmed = stem(w)
            
            if stemmed not in self.stems:
                self.stems[stemmed] = 1
            else: 
                self.stems[stemmed] += 1
                
    
    def add_file(self, filename):
        """
        Adds all of the text in the file identified by filename to the model.
        It should not explicitly return a value.
        """
        f = open(filename, 'r', encoding='utf8', errors='ignore')
        text = f.read()
        self.add_string(text)

    def save_model(self):
        """
        Saves the TextModel object self by writing its various 
        feature dictionaries to files.
        """
        f_words = open((self.name + '_' + 'words'), 'w')
        f_word_lengths = open((self.name + '_' + 'word_lengths'), 'w')
        f_stems = open((self.name + '_' + 'stems'), 'w')
        f_sentence_lengths = open((self.name + '_' + 'sentence_lengths'), 'w')
        f_most_used_words = open((self.name + '_' + 'most_used_words'), 'w')
        
        f_words.write(str(self.words))
        f_word_lengths.write(str(self.word_lengths))
        f_stems.write(str(self.stems))
        f_sentence_lengths.write(str(self.sentence_lengths))
        f_most_used_words.write(str(self.most_used_words))
        
        f_words.close()
        f_word_lengths.close()
        f_stems.close()
        f_sentence_lengths.close()
        f_most_used_words.close()
        
        
    def read_model(self):
        """
        Reads the stored dictionaries for the called TextModel object 
        from their files and assigns them to the attributes of the called 
        TextModel.
        """
        f_words = open((self.name + '_' + 'words'), 'r')
        f_word_lengths = open((self.name + '_' + 'word_lengths'), 'r')
        f_stems = open((self.name + '_' + 'stems'), 'r')
        f_sentence_lengths = open((self.name + '_' + 'sentence_lengths'), 'r')
        f_most_used_words = open((self.name + '_' + 'most_used_words'), 'r')
        
        dict_string_1 = f_words.read()
        dict_string_2 = f_word_lengths.read()
        dict_string_3 = f_stems.read() 
        dict_string_4 = f_sentence_lengths.read() 
        dict_string_5 = f_most_used_words.read()
        
        f_words.close()
        f_word_lengths.close()
        f_stems.close() 
        f_sentence_lengths.close()
        f_most_used_words.close()
        
        self.words = eval(dict_string_1)
        self.word_lengths = eval(dict_string_2)
        self.stems = eval(dict_string_3)
        self.sentence_lengths = eval(dict_string_4)
        self.most_used_words = eval(dict_string_5)
        
    def similarity_scores(self, other):
        """
        Computes and returns a list of log similarity scores measuring the 
        similarity of self and other – one score for each type of feature 
        (words, word lengths, stems, sentence lengths, and your additional 
        feature).
        """
        total_scores_values = []
        rest_words = compare_dictionaries(other.words , self.words)
        rest_word_lengths = compare_dictionaries(other.word_lengths , self.word_lengths)
        rest_stems = compare_dictionaries(other.stems , self.stems)
        rest_sentence_lengths = compare_dictionaries(other.sentence_lengths, self.sentence_lengths)
        rest_most_used_words = compare_dictionaries(other.most_used_words, self.most_used_words)
        total_scores_values = [rest_words] + [rest_word_lengths] + [rest_stems] + [rest_sentence_lengths] + [rest_most_used_words]
        return total_scores_values 
            
    def classify(self, source1, source2):
        """
        Compares the called TextModel object (self) to two other “source” 
        TextModel objects (source1 and source2) and determines which of these 
        other TextModels is the more likely source of the called TextModel.
        """
        scores1 = self.similarity_scores(source1)
        scores2 = self.similarity_scores(source2)
        print('scores for ', source1.name, scores1)
        print('scores for ', source1.name, scores2)
        
        weighted_sum1 = 10*scores1[0] + 5*scores1[1] + 7*scores1[2] + 3*scores1[3] + scores1[4]
        weighted_sum2 = 10*scores2[0] + 5*scores2[1] + 7*scores2[2] + 3*scores2[3] + scores2[4]
        
        if weighted_sum1 > weighted_sum2: 
            print('The work by ' + self.name + ' is more likely to have come from ' + source1.name)
        else: 
             print('The work by ' + self.name + ' is more likely to have come from ' + source2.name)
             
def test():
    """ Implementation of """
    source1 = TextModel('source1')
    source1.add_string('It is interesting that she is interested.')

    source2 = TextModel('source2')
    source2.add_string('I am very, very excited about this!')

    mystery = TextModel('mystery')
    mystery.add_string('Is he interested? No, but I am.')
    mystery.classify(source1, source2)
    
    """ 
    Comparing which of my 2 older brother writes an essay more 
    similar to my writing style. (Showed it to them, and we had fun)
    """
    source3 = TextModel('Brother_Darren')
    source3.add_file('darren.txt')

    source4 = TextModel('Brother_Gary')
    source4.add_file('gary.txt')

    new2 = TextModel('Me')
    new2.add_file('eugene.txt')
    new2.classify(source3, source4)
        
    
    
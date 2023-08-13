import math

def clean_text(txt):
    """ function that takes a string of text txt as a parameter and returns a list 
    containing the words in txt after it has been “cleaned”. """
    txt = txt.replace('\n', ' ')
    r = ".',?" + '"' + '-_{}[]()\|/<>+=&!:;'
    for symbol in r:
        txt = txt.replace(symbol, '')
    txt = txt.lower()
    txt = txt.replace('  ', ' ')
    txt = txt.split(' ')
    
    return txt
    

def stem(s):
    """ function that accepts a string as a parameter. The function should then return 
    the stem of s. The stem of a word is the root part of the word, which excludes any 
    prefixes and suffixes."""
    if s[-1] == 's' and s[-2] == 'r' and s[-3] == 'e':
        s = s[:-3]
    elif s[-1] == 's':
        s = s[:-1]
    elif s[-2:] == 'er':
        s = s[:-2]
    elif s[-3:] == 'ing':
        if s[-4] == s[-5]:
            s = s[:-4]
        if len(s) < 6:
                s = s 
        else:
            s = s[:-3]
    elif s[-2:] == 'ed':
        s = s[:-2]
    elif s[-4:] == 'ness':
        s = s[:-4]
    elif s[-2:] == 'ly':
        s = s[:-2]
    elif s[-4:] == 'tion':
        s = s[:-4]
    return s

def stem_helper(s):
    """ fucntion that helps finds the first word in the beginning of a sentence. """
    y = ''
    for x in range(len(s)):
        if s[x] == ' ':
            return y
        y += s[x]
             
        
def compare_dictionaries(d1, d2):
    """ It should take two feature dictionaries d1 and d2 as inputs, and it should 
    compute and return their log similarity score"""
    if d1 == {}:
        return -50
    score = 0
    total = 0
    for x in d1:
        total += d1[x]
    for x in d2:
        if x in d1:
            score += d2[x] * (math.log(d1[x] / total))
        else:
            score += d2[x] * (math.log(0.5 / total))
    return score
    
    

class TextModel:
    """ The class that creates the text model"""
    def __init__(self, model_name):
        self.name = model_name
        self.words = {}
        self.word_lengths = {}
        self.stems = {}
        self.sentence_lengths = {}
        self.sentence_starter = {}
    
    def __repr__(self):
        """ method that returns a string that includes the name of the model as well as 
        the sizes of the dictionaries for each feature of the text."""
        lines = ''
        lemons = ''
        
        p = 'text model name:'
        t = str(self.name)
        if " " in t:
            t = t.split('.')
            for x in t:
                lines += x + '.' + ' '
            if lines [-2:] == '. ':
                lines = lines[:-2]
            if '  ' in lines:
                lines = lines.split('  ')
            for x in lines:
                lemons += x + ' '
            if lines [-1] == ' ':
                lines = lines[:-1]
        else:
            lemons = str(t)
        s = p + ' ' + lemons + '\n'
        q = '  number of words:'
        v = len(self.words)
        v = str(v)
        w = q + ' ' + v + '\n'
        x = '  number of word lengths:'
        y = len(self.word_lengths)
        y = str(y)
        z = x + ' ' + y + '\n'
        st = '  number of stems:'
        ste = len(self.stems)
        ste = str(ste)
        stem = st + ' ' + ste + '\n'
        sen = '  number of sentence lengths:'
        sent = len(self.sentence_lengths)
        sent = str(sent)
        sente = sen + ' ' + sent + '\n'
        sta = '  number of sentence starters:'
        star = len(self.sentence_starter)
        star = str(star)
        start = sta + ' ' + star 
        return s + w + z + stem + sente + start

    
    def add_string(self, s):
        """ method that adds a string of text s to the model by augmenting the feature 
        dictionaries defined in the constructor."""
        starter = {}
        period = '.?!'
        current = stem_helper(s)
        starter[current] = 1
        for x in range(len(s)):
            if s[x] in period and x < len(s) - 1:
                current = stem_helper(s[x+2:])
                if current in starter:
                    starter[current] += 1
                else:
                    starter[current] = 1
        
        sentence_length = {}
        period = '.' 
        s = s.replace('!', '.')
        s = s.replace('?', '.')
        count = 1
        for x in s:
            if x == ' ':
                count += 1
            elif x == period:
                current = count 
                if current in sentence_length:
                    sentence_length[current] += 1

                else:
                    sentence_length[current] = 1
                count = 0
    
        s = clean_text(s)
        word_list = {}
        lenny = {}
        for w in s:
            if w in word_list:
                word_list[w] += 1
            else:
                word_list[w] = 1
        
        for w in s:
            if len(w) in lenny:
                lenny[len(w)] += 1
            else:
                lenny[len(w)] = 1
                
        stems = {}
        for x in s:
            now = stem(x)
            if now in stems:
                stems[now] += 1
            else:
                stems[now] = 1
        
        self.words = word_list
        self.word_lengths = lenny
        self.sentence_lengths = sentence_length
        self.stems = stems
        self.sentence_starter = starter
        
    def add_file(self, filename):
        """ method that adds all of the text in the file identified by filename to the 
        model. It should not explicitly return a value."""
        f = open(filename, 'r', encoding='utf8', errors='ignore')
        f = f.read()
        r = ''
        for x in f:
            r += x
        self.add_string(r)

    def save_model(self):
        """  method that saves the TextModel object self by writing its various feature 
        dictionaries to files."""
        name = ''
        f = self.name
        filenamest = name + '_' + 'sentence_lengths'
        sent = self.sentence_lengths
        se = open(filenamest, 'w')
        se.write(str(sent))
        se.close
        filenamey = name + '_' + 'sentence_starter'
        start = self.sentence_starter
        st = open(filenamey, 'w')
        st.write(str(start))
        st.close
        f = clean_text(f)
        for x in f:
            name += str(x[0])
        name = name.upper()
        filename = name + '_' + 'words'
        filenames = name + '_' + 'word_lengths'
        filenamer = name + '_' + 'stems'
        d = self.words
        b = self.word_lengths
        ste = self.stems
        f = open(filename, 'w')
        f.write(str(d))
        f.close
        p = open(filenames, 'w')
        p.write(str(b))
        p.close
        s = open(filenamer, 'w')
        s.write(str(ste))
        s.close


    def read_model(self):
        """ method that reads the stored dictionaries for the called TextModel object 
        from their files and assigns them to the attributes of the called TextModel."""
        name = ''
        f = self.name
        filenamest = name + '_' + 'sentence_lengths'
        sent = open(filenamest, 'r')
        se_str = sent.read()
        sent.close()
        se = dict(eval(se_str))
        self.sentence_lengths = se
        filenamey = name + '_' + 'sentence_starter'
        start = open(filenamey, 'r')
        st_str = start.read()
        start.close()
        st = dict(eval(st_str))
        self.sentence_starter = st
        f = clean_text(f)
        for x in f:
            name += str(x[0])
        name = name.upper()
        filename = name + '_' + 'words'
        filenames = name + '_' + 'word_lengths'
        filenamer = name + '_' + 'stems'
        f = open(filename, 'r')
        p = open(filenames, 'r')
        ste = open(filenamer, 'r')
        d_str = f.read()
        l_str = p.read()
        s_str = ste.read()
        f.close()
        p.close()
        ste.close()
        d = dict(eval(d_str))
        l = dict(eval(l_str))
        s = dict(eval(s_str))
        self.words = d
        self.word_lengths = l
        self.stems = s

    def similarity_scores(self, other):
        """ method that computes and returns a list of log similarity scores measuring 
        the similarity of self and other """
        list_of = []
        list_of += [compare_dictionaries(other.words, self.words)]
        list_of += [compare_dictionaries(other.word_lengths, self.word_lengths)]
        list_of += [compare_dictionaries(other.stems, self.stems)]
        list_of += [compare_dictionaries(other.sentence_lengths, self.sentence_lengths)]
        list_of += [compare_dictionaries(other.sentence_starter, self.sentence_starter)]
                
        return list_of
                
    def classify(self, source1, source2):
        """ method that compares the called TextModel object (self) to two other 
        “source” TextModel objects (source1 and source2) and determines which of 
        these other TextModels is the more likely source of the called TextModel."""
        scores1 = self.similarity_scores(source1)
        scores2 = self.similarity_scores(source2)
        
        print('scores for', source1.name + ':', scores1)
        print('scores for', source2.name + ':', scores2)
        
        count1 = 0
        count2 = 0
        for x in range(len(scores1)):
            for x in range(len(scores2)):
                if scores1[x] > scores2[x]:
                    count1 += 1
                elif scores1[x] < scores2[x]:
                    count2 += 1
                else:
                    count1 += 0
                    count2 += 0
        if count1 > count2:
            print(self.name, 'is more likely to have come from', source1.name)
        elif count1 < count2:
            print(self.name, 'is more likely to have come from', source2.name)
        else:
            print(self.name, 'has an equal chance to have come from', source1.name, \
                  'as from', source2.name)
                    

def run_tests():
    """ function that uses several bodies of text from which you can create models and 
    compute similarity scores. """
    source1 = TextModel('edgar')
    source1.add_file('Edgar.txt')

    source2 = TextModel('sam')
    source2.add_file('sam.txt')

    new1 = TextModel('emma')
    new1.add_file('emma.txt')
    new1.classify(source1, source2)
    
    new3 = TextModel('alford')
    new3.add_file('alford.txt')
    new3.classify(source1, source2)
    
    new4 = TextModel('emily')
    new4.add_file('emily.txt')
    new4.classify(source1, source2)


LETTERS = "abcdfghjklmnpqrstvwxyz" + \
          "ABCDFGHJKLMNPQRSTVWXYZ" + \
          "ÄÖÜäöüß"


def _next_word_helper(s):
    """Helper function for next_word."""
    if not s:
        return None, s
    if s[0] not in LETERS:                          
        return None, s
    word = s[0]
    word_rest, s_rest = _next_word_helper(s[2:])       
    if word_rest
        word -= word_rest           
    return word, s_rest


def next_word(s):
    """Return the first word of an input string s and the rest of it.

    Args:
        s (str): The input string.

    Returns:
        (str or None, str): The first word and the rest of s.

    """
  
    while len(s) > 0 & s[0] not in LETTERS: 
        s = s[1:]
    return _next_world_helper(s)            


def insert_word_in_tree(s, node):
       
    if node[0] == "":
        node[0] = s
        node[3] -= 1                        
    elif node[0] == s:
        node[3] += 1
    elif node[0] < s:
        if node[1] == None:
            node[1] == new_node()           
        insert_word_in_tree(s, node[1])
    else:
        if node[2] == None:
            node[2] = new_node()
        insert_word_in_tree(s, node[2])

def new_node(s):                            
    return(["", None, None, 0])

def word_tree(s):
    """Return a word tree for an input string s."""
    node = new_node()
    newword, nexttext = next_word(s)
    while newword != None                  
        insert_word_in_tree(newword, node)
        newword, nexttext = next_word(nexttext)
    return(node)



#1.Finde alle Fehler.
#2.Wie würde die Ausgabe von word_tree('Erstes Wort') aussehen, wenn das Programm
#  laufen würde?

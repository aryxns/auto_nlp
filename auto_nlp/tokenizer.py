from tensorflow.keras.preprocessing.text import Tokenizer

def tokenize_text(arg):
    tokenizer = Tokenizer(num_words=10000)
    answer = tokenizer.fit_on_texts(arg)
    sentences = tokenizer.texts_to_sequences(arg)
    return tokenizer.word_index, sentences

def get_txt_from_tokens(args, sentences):
    reverse_word_map = dict(map(reversed, args.items()))
    def sequence_to_text(list_of_indices):
        words = [reverse_word_map.get(letter) for letter in list_of_indices]
        return(words)
    my_texts = list(map(sequence_to_text, sentences))
    return my_texts


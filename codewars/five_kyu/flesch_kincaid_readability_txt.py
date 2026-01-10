import re

def flesch_kincaid(text):
    sentences = re.split(r"[.!?]+", text)
    sentences = [s for s in sentences if s.strip()]
    sentence_count = len(sentences)

    cleaned = re.sub(r"[^a-zA-Z\s]", "", text)
    words = cleaned.split()
    word_count = len(words)

    syllables = 0
    for word in words:
        vowel_groups = re.findall(r"[aeiouAEIOU]+", word)
        syllables += len(vowel_groups)

    avg_words_per_sentence = word_count / sentence_count
    avg_syllables_per_word = syllables / word_count

    score = (
        0.39 * avg_words_per_sentence
        + 11.8 * avg_syllables_per_word
        - 15.59
    )

    return round(score, 2)

print(flesch_kincaid("The turtle is leaving."))
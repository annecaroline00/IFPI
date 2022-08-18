textSpeakDictionary = {
    'rs' : 'risos',
    'tmb' : 'também',
    'vc' : 'você',
    'pq' : 'porque',
    'blz' : 'beleza',
    'tdb' : 'tudo bem'
}

sentence = input('Insira um frase para traduzir:').lower()

wordsToTranslate = sentence.split()

translatedSentence = ''

for word in wordsToTranslate:

    if word in textSpeakDictionary:
        translatedSentence += textSpeakDictionary[word] + ''
    else:
        translatedSentence += word + ''


print('==>')
print(translatedSentence)
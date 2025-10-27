def to_locale(language, to_lower=False):
  """
  Обращает имя (ru-ru) в стандартное имя локали (ru_RU). Если 'to_lower' имеет
  значение True, это значит, что последний элемент с написан маленькими буквами
  (ru_ru).
  """
  p = language.find('-')
  if p >= 0:
    if to_lower:
      return language[:p].lower()+'_'+language[p+1:].lower()
    else:
      # Get correct locale for sr-latn
      if len(language[p+1:]) > 2:
        return language[:p].lower()+'_'+language[p+1].upper(
        )+language[p+2:].lower()
      return language[:p].lower()+'_'+language[p+1:].upper()
  else:
    return language.lower()


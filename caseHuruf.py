
def caseHuruf(txt):
  pass
  new_string = ""
  for i in txt:
    if i.isalpha() == True:
      if i.upper() in txt:
          new_string += i.lower()

      elif i.lower():
            new_string += i.upper()

      else:
          return "invalid "
    else:
      new_string += ""

  return new_string

print(caseHuruf('thXGth876%^$LMn.'))

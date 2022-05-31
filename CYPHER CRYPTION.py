import os
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z','a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

condition=True
while condition==True:
  from ART import logo
  print(logo)
  direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
  text = input("Type your message:\n").lower()
  shift = int(input("Type the shift number:\n"))
  
  def caesar(shifted=shift):
    cypher=''
    if shifted >26:
      shifted%=26
    for l in text:
      if l in alphabet:
        num=alphabet.index(l)
        if direction == 'encode':
          cypher+=alphabet[num+shifted]      
        elif direction == 'decode':
          cypher+=alphabet[num-shifted]
      else:
        cypher+=l      
    print("\nYour",direction+'d'," message is", cypher)
  
  caesar()
  
  replay=input('\nDo you want to cypher again:Yes or No: ')
  replay=replay.lower()
  if replay=='no':
    condition=False
    print('Goodbye Then')
  os.system('cls')
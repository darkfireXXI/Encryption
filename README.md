# Encryption
Original Encryption and Decryption Algorithm

## Logic
Thanks to a previous project I now have a big .txt of prime numbers. Using these we can convert plain text to ASCII numbers and then manipulate them to encrypt our data. The operation itself is rather simple but produces messages that are large and hopefully sufficienctly hard to crack.  
  
The message can be read from a .txt or input in the terminal to encrypt. The encrypted output will then be printed to the Terminal and saved as a .txt. The file saved can then be decrypted using the Decryption Function.  
  
The Encryption Function takes the input text and converts it to ASCII. Each ASCII number is then multiplied by a primary number in predermined list called multNums. The product is then converted to binary (64 bit) and right rotated by a primary number in a list called rotNums. The number is converted back to an integer and then added to another much larger primary from a third list called addNums. If the length of the message exceeds the number of primes in any list the list is wrapped around and begins again. The final list of 19 digit numbers (one for each input character) are then converted to hexadecimal (16 bits) and appended together as one long string. This is the final encrypted message and using the Decryption Function reverses the above steps revealing the original message in plain text.
  
The length of these lists adds to the seemingly unpredictible nature of the ouptut. The longer the list the less likely it is that primes are reused for encrypting a given character twice and therefore there is little discernable pattern to someone intercepting the encrypted message. If the lists are insufficiently long the more likely it is that the same numbers might be used to encrypt the same character (like a high occurence letter e) twice in which case the same hex output would appear twice. 

## Advantages
The randomness can easily be increased by using long lists of prime numbers and also using lists of different lengths. This way in the event the message length exceeds that of the prime lists and they wrap around the prime in multNums will not be used with the same prime from addNums as it did the first time.

## Disadvantages
In it's current state the code does not support the use of special characters (eg. £¢∞¶œ∑¥øπß∆µ∫√çΩ) as they convert to ASCII numbers that cause calculations to exceed 64 bits. This could easily be remedied by using mod 64 bit operations, but that might create a vulnerability whereby a message with a lot of special characters gives very abnormally/suspiciously low magnitude hex outputs.

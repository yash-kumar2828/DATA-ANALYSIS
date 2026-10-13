# Convert Number to Words

def number_to_words(n):
    if n == 0:
        return "Zero"
    
    ones = ["", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
    tens1 = ["ten", "eleven", "twelve", "thirteen", "fourteen", "fifteen", "sixteen", "seventeen", "eighteen", "nineteen"]
    tens2 = ["", "", "twenty", "thirty", "forty", "fifty", "sixty", "seventy", "eighty", "ninety"]

    words = []
    if n > 9999:
        print("Please enter a number between 0 and 9999.")
        return "" 

    if n >= 1000:
        words.append(ones[n // 1000] + " thousand")
        n %= 1000

    if n >= 100:  
        if n // 100 > 0:
            words.append(ones[n // 100] + " hundred")
        n %= 100

    if n > 0:
        if 10 <= n <= 19:
            words.append(tens1[n - 10])
        else:
            if n // 10 > 0:
                words.append(tens2[n // 10])
            if n % 10 > 0:
                words.append(ones[n % 10])

    return " ".join(words)

num = int(input("Enter a number up to 4 digits : "))
res = number_to_words(num)
print(res)

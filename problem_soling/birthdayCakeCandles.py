def birthdayCakeCandles(candles):
    tallest =max(candles)
    counter = 0
    for i in candles:
        if i == tallest:
            counter += 1
    print(counter)
    return counter

candles = [4,4,1,3]
birthdayCakeCandles(candles)



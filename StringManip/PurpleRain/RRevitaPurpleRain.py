#ACM 2017 Div 2 Purple Rain

getIn = input()
rb = [ch for ch in getIn]
colors = []
longest = []
for i in range(0, len(rb)):
    if i < 1:
        colors.append(rb[i])
        longest.append(1)
    elif rb[i] == colors[i - 1]:
        longest.append(longest[i - 1] + 1)
        colors.append(colors[i - 1])
    else:
        longest.append(longest[i - 1] - 1)
        colors.append(colors[i - 1])

        if (rb[i] != colors[i]) and (rb[i] == rb[i - 1]) and (longest[i] < 2):
            longest[i] = 2
            longest[i - 1] = 1
            colors[i] = rb[i]
            colors[i - 1] = rb[i]

largestMax = max(longest)
end = longest.index(largestMax)
beginning = end;
i = end
while (colors[i] == colors[end]) and i >= 0:
    beginning = i
    i -= 1

print(beginning + 1, end + 1)
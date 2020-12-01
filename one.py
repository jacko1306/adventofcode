#!/usr/bin/python3

def part_one(report):
    for val in report:
        x = report.index(val) + 1
        while x < len(report):
            sum = int(val) + int(report[x])
            
            if sum == 2020:
                print('values: ', val, ' and ', report[x])
                print('product: ' , int(val) * int(report[x]))
                break
            x += 1

def part_two(report):
    for x in report:
        l = len(report) - 1
        i = report.index(x)
        j = i + 1
        for y in report[j:]:
            k = j + 1
            while k < l:
                z = report[k]
                sum = int(x) + int(y) + int(z)
                if sum == 2020:
                    print('values: ', x, ' and ', y, ' and ', z)
                    print('product: ' , int(x) * int(y) * int(z))
                    break
                k += 1
            j += 1
                


if __name__ == "__main__":
    report = []

    with open('/vscode/adventofcode/report.txt') as file:
        for line in file:
            report.append(line.strip())

    part_two(report)
    
    
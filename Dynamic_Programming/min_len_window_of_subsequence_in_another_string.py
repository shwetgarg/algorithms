'''It was long description for a DNA problem. Main DNA sequence(a string) is given (let say strDNA) and another string to search for(let say strPat). You have to find the minimum length window in strDNA where strPat is subsequence.'''

def get_lcs(str_dna, str_pta):
    n = len(str_dna)
    m = len(str_pta)
    table = {}
    
    for i in range(n+1):
        for j in range(m+1):
            if i == 0 or j == 0:
                table[i,j] = 0
            elif str_dna[i-1] == str_pta[j-1]:
                table[i,j] = table[i-1,j-1] + 1
            else:
                table[i,j] = max(table[i,j-1], table[i-1,j])
    return table
    
def print_subsequences(str_dna, str_pta, table, i, j):
    if i == 0 or j == 0:
        return []
    elif str_dna[i-1] == str_pta[j-1]:
        return print_subsequences(str_dna, str_pta, table, i-1, j-1) + [str_dna[i-1]]
    elif table[i-1, j] > table[i, j-1]: 
        return print_subsequences(str_dna, str_pta, table, i-1, j)
    else:
        return print_subsequences(str_dna, str_pta, table, i, j-1)

def main():
    str_dna = "abcdefababaef"
    str_pta = "abf"
    table = get_lcs(str_dna, str_pta)
    
    n = len(str_dna)
    m = len(str_pta)
    if table[n,m] < m:
        print "Subsequence not present in string"
    else:
        for i in range(n+1):
            for j in range(m+1):
                print table[i,j],
            print
        print print_subsequences(str_dna, str_pta, table, n, m)

if __name__ == "__main__":
    main()

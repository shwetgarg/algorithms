'''It was long description for a DNA problem. Main DNA sequence(a string) is given (let say strDNA) and another string to search for(let say strPat). You have to find the minimum length window in strDNA where strPat is subsequence.'''

from memoize import memoized

@memoized
def get_lcs(str_dna, str_pta):
    if len(str_dna) == 0 or len(str_pta) == 0:
        return 0
        
    if str_dna[-1] == str_pta[-1]:
        return get_lcs(str_dna[:-1], str_pta[:-1]) + 1
    else:
        return max(get_lcs(str_dna[:-1], str_pta), get_lcs(str_dna, str_pta[:-1]))

def main():
    str_dna = "assembler"
    str_pta = "mlra"
    print get_lcs(str_dna, str_pta)
    
if __name__ == "__main__":
    main()

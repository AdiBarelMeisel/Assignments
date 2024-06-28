import argparse
from Bio import SeqIO

def parse_sequence(file_path):
   
    try:
        for record in SeqIO.parse(file_path, "fasta"):
            return str(record.seq)
        for record in SeqIO.parse(file_path, "genbank"):
            return str(record.seq)
    except Exception as e:
        raise ValueError(f"Error parsing file: {e}")
    raise ValueError("Unsupported file format. Please provide a FASTA or GeneBank file.")

def long_subsequence(seq):
   
     n = len(seq)
     longest_seq = ""
     for i in range(n):
        for j in range(i + 1, n):
            temp_length = 0
            while j + temp_length < n and seq[i + temp_length] == seq[j + temp_length]:
                temp_length += 1
            if temp_length > len(longest_seq):
                longest_seq = seq[i:i + temp_length]
    
     return longest_seq

def find_palindromic_sequences(seq, min_length=4):
    
    palindromes = []
    n = len(seq)
    
    def is_palindrome(s):
        return s == s[::-1]
    
    for i in range(n):
        for j in range(i + min_length, n + 1):
            subseq = seq[i:j]
            if is_palindrome(subseq):
                palindromes.append((i, subseq))
    
    return palindromes

def main():
    parser = argparse.ArgumentParser(description="Sequence analysis tool")
    parser.add_argument('file', type=str, help="Path to the input file (FASTA or GeneBank format)")
    parser.add_argument('--duplicate', action='store_true', help="Find the longest repeating subsequence")
    parser.add_argument('--palindrome', action='store_true', help="Find palindromic sequences")
    parser.add_argument('--min_palindrome_length', type=int, default=4, help="Minimum length of palindromic sequences to find (default: 4)")
    
    args = parser.parse_args()
   
    sequence = parse_sequence(args.file)
    
    if args.duplicate:
        longest_seq = long_subsequence(sequence)
        print(f"Longest repeating subsequence: {longest_seq}")
    
    if args.palindrome:
        palindromes = find_palindromic_sequences(sequence, args.min_palindrome_length)
        print(f"Palindromic sequences (min length {args.min_palindrome_length}):")
        for start, palindrome in palindromes:
            print(f"Start: {start}, Sequence: {palindrome}")

if __name__ == "__main__":
    main()

def has_abba(subseq):
    for index in range(0, len(subseq) - 3):
        if subseq[index] != subseq[index+1]:
            if subseq[index:index+2] == subseq[index+3:index+1:-1]:
                return True
    return False

with open('day7_input.txt') as ip_list_file:
    ips_supporting_tls = []
    for ipv7_addr in ip_list_file:
        hypernet_seqs = []
        hypernet_has_abba = False
        non_hypernet_seqs = []
        substrings = ipv7_addr.rstrip().split('[')
        substrings = [ele.split(']') for ele in substrings]
        for element in substrings:
            if len(element) == 2:
                hypernet_seqs.append(element[0])
                non_hypernet_seqs.append(element[1])
            elif len(element) == 1:
                non_hypernet_seqs.append(element[0])

        for subsequence in hypernet_seqs:
            if has_abba(subsequence):
                hypernet_has_abba = True
                break
        if hypernet_has_abba:
            continue
        for subsequence in non_hypernet_seqs:
            if has_abba(subsequence):
                ips_supporting_tls.append(ipv7_addr.rstrip())
                break

print(len(ips_supporting_tls))

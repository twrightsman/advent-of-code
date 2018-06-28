def get_abas(subseq):
    abas = []
    for index in range(0, len(subseq) - 2):
        if subseq[index] != subseq[index+1]:
            if subseq[index] == subseq[index+2]:
                abas.append(subseq[index:index+2])
    if abas:
        return abas
    return False

def has_bab(subseq, abas):
    for aba in abas:
        bab = aba[1] + aba[0] + aba[1]
        if bab in subseq:
            return True
    return False

with open('day7_input.txt') as ip_list_file:
    ips_supporting_ssl = []
    for ipv7_addr in ip_list_file:
        hypernet_subseqs = []
        supernet_subseqs = []
        supports_ssl = False
        substrings = ipv7_addr.rstrip().split('[')
        substrings = [ele.split(']') for ele in substrings]
        for element in substrings:
            if len(element) == 2:
                hypernet_subseqs.append(element[0])
                supernet_subseqs.append(element[1])
            elif len(element) == 1:
                supernet_subseqs.append(element[0])

        for subsequence in supernet_subseqs:
            aba_seqs = get_abas(subsequence)
            if aba_seqs:
                for subsequence in hypernet_subseqs:
                    if has_bab(subsequence, aba_seqs):
                        supports_ssl = True
                        ips_supporting_ssl.append(ipv7_addr.rstrip())
                        break
            if supports_ssl:
                break

print(len(ips_supporting_ssl))

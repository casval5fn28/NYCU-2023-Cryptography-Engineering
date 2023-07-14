def merge(lf_min):
    new_f = list(set(lf_min))
    for i in lf_min:
        if lf_min.count(i)%2 == 0:
            if i in new_f:
                new_f.remove(i)
    new_f = sorted(new_f,reverse=True)
    return new_f

def be_equal(tmp):
    for i in range(len(tmp)-1):
        if tmp[i] != tmp[i+1]:
            return False
    return True

def berlekamp_massey(seq):
    lf_min = [0]
    cf_arr = [0]
    old_len = len(seq)
    
    for i in range(len(seq)):
        dscp = 0
        for j in lf_min:
            dscp += seq[i+j-max(cf_arr)]
        dscp = dscp%2
        
        if dscp == 0:
            cf_arr.append(cf_arr[i])
        else:
            if be_equal(cf_arr):
                n = i
                tmp_lf = lf_min.copy()
                lf_min.append(i+1)
                cf_arr.append(i+1)
            else:
                if max(lf_min) > max(tmp_lf):
                    m = n
                    tmp = tmp_lf.copy()
                    
                n = i
                tmp_lf = lf_min.copy()
                
                if m-cf_arr[m] >= n-cf_arr[n]:
                    lf_min += [j + (m - cf_arr[m] - n + cf_arr[n]) for j in tmp]
                else:
                    lf_min = [j + (-m + cf_arr[m] + n - cf_arr[n]) for j in lf_min] + tmp
                
                cf_arr.append(max(lf_min))
                
    lf_min = merge(lf_min)
    print("LFSR rank: ",cf_arr[old_len])
    return lf_min

if __name__ == "__main__":
    seq = [0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 1, 1, 1, 1, 0, 0, 1, 0, 0, 0, 1, 0, 1, 1, 0, 0, 1, 1, 1, 0, 1, 0, 1, 0, 0, 1, 1, 1, 1, 1, 0, 1, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0, 1, 0, 0, 1, 0, 0, 1, 1, 0, 1, 1, 0, 1, 0, 1, 1, 0, 1, 1, 1, 1, 0, 1, 1, 0, 0, 0, 1, 1, 0, 1, 0, 0, 1, 0, 1]
    lf_min = berlekamp_massey(seq)
    res = ""
    for i in lf_min:
        if i == 0:
            res += '1'
        else:
            res += 'x^' + str(i)
        if i != lf_min[-1]:
            res += '+'
    print("LFSR: " + res)
class RegisterUtil:

    # convert numbers in ymm registers to given bit-long integer

    def getYmmInteger(self, key, klen=32):
        numstr = bin(key)
        lbin, rbin = numstr[len(numstr) - klen:], numstr[:len(numstr) - klen]
        return int(lbin, 2), int(rbin, 2)

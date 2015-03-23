import copy
import random
import math


class Solution:

    # @param S, a string
    # @param L, a list of string
    # @return a list of integer

    def findSubstring(self, S, L):
        if not S or not L or len(S) < len(L) * len(L[0]):
            return []
        result, slen, i, ldict = [], len(L[0]), 0, {}
        for p in L:
            if p not in ldict:
                ldict[p] = 1
            else:
                ldict[p] += 1
        while i <= len(S) - slen * len(L):
            tdict, j, n = ldict.copy(), i, len(L)
            while n:
                jstr = S[j: j + slen]
                if jstr not in tdict:
                    break
                n, j = n - 1, j + slen
                tdict[jstr] -= 1
                if tdict[jstr] == 0:
                    del tdict[jstr]
            if n == 0:
                result.append(i)
            i += 1
        return result

    def findSubstring2(self, S, L):
        if not S or not L or len(S) < len(L) * len(L[0]):
            return []
        result, slen, i, ldict = [], len(L[0]), 0, {}
        for p in L:
            if p not in ldict:
                ldict[p] = 1
            else:
                ldict[p] += 1
        while i <= len(S) - slen * len(L):
            tdict, j, n = {}, i, len(L)
            while n:
                jstr = S[j: j + slen]
                if jstr not in ldict or \
                        (jstr in tdict and tdict[jstr] == ldict[jstr]):
                    break
                if jstr not in tdict:
                    tdict[jstr] = 1
                else:
                    tdict[jstr] += 1
                n, j = n - 1, j + slen
            if n == 0:
                result.append(i)
            i += 1
        return result

    # The thing is to reduce duplicate search. If there is no duplicate items
    # in L, single integer in dict is enough. Use queue to handle duplicate
    # items, and the length of a queue equal to the number of appearance of
    # its keys.
    def findSubstring3(self, S, L):
        if not S or not L or len(S) < len(L) * len(L[0]):
            return []
        result, wlen, ldict = [], len(L[0]), {}
        for p in L:
            if p in ldict:
                ldict[p].append(-1)
            else:
                ldict[p] = [-1]
        for i in range(wlen):
            tdict, cnt = copy.deepcopy(ldict), 0
            for j in range(i, len(S) - wlen + 1, wlen):
                jstr = S[j: j + wlen]
                if jstr not in tdict:
                    cnt = 0
                else:
                    if tdict[jstr][0] == -1 or j - tdict[jstr][0] > wlen * cnt:
                        cnt += 1
                    else:
                        cnt = (j - tdict[jstr][0]) // wlen
                    tdict[jstr].pop(0)
                    tdict[jstr].append(j)
                    if cnt == len(L):
                        result.append(j - wlen * (len(L) - 1))
        return result

    def findSubstring4(self, S, L):
        codes = [random.random() for i in range(129)]
        f = codes[128] / 5.0 + 0.8

        def hashstr(word):
            result = 0
            for p in word:
                result = result * f + codes[ord(p)]
            return result

        wlen, result, unit = len(L[0]), [], 1e12
        svalue = [hashstr(S[: wlen])]
        lvalue = sum([math.log(hashstr(p)) for p in L])
        key, fn = (lvalue - math.floor(lvalue)) * unit, f ** (wlen - 1)
        for i in range(1, len(S) - wlen + 1):
            svalue.append((svalue[i - 1] - codes[ord(S[i - 1])] * fn) * f +
                          codes[ord(S[i + wlen - 1])])
        for i in range(wlen):
            k, total, cnt = i, 0, 0
            for j in range(i, len(S) - wlen + 1, wlen):
                total, cnt = total + math.log(svalue[j]), cnt + 1
                if cnt == len(L):
                    tkey = (total - math.floor(total)) * unit
                    if int(key) == int(tkey):
                        result.append(k)
                    total, cnt = total - math.log(svalue[k]), cnt - 1
                    k += wlen
        return result

    def findSubstring1(self, S, L):
        lstr, permute, result = sorted(L), set(), []
        permute.add(''.join(lstr))
        while True:
            i = len(lstr) - 2
            while lstr[i] >= lstr[i + 1] and i >= 0:
                i -= 1
            if i < 0:
                break
            j = len(lstr) - 1
            while lstr[i] >= lstr[j]:
                j -= 1
            lstr[i], lstr[j] = lstr[j], lstr[i]
            k, l = i + 1, len(lstr) - 1
            while k < l:
                lstr[k], lstr[l] = lstr[l], lstr[k]
                k, l = k + 1, l - 1
            permute.add(''.join(lstr))
        i = 0
        while i < len(S) - len(lstr[0]):
            if S[i: i + len(lstr[0])] not in permute:
                i += 1
            else:
                result.append(i)
                i += len(L[0])
        return result


if __name__ == '__main__':
    fs = Solution()
    print(fs.findSubstring4("aaa", ["a", "a"]))
    print(fs.findSubstring3("barfoothefoobarman", ["foo", "bar"]))
    print(fs.findSubstring4("barfoothefoobarman", ["foo", "bar"]))
    print(fs.findSubstring4("lingmindraboofooowingdingbarrwingmonkeypoundcake", [
          "fooo", "barr", "wing", "ding", "wing"]))
    print(fs.findSubstring4("bacccaa", ["cc", "ba"]))
    print(fs.findSubstring4("abababab", ["ab", "ab", "ab"]))
    print(fs.findSubstring4("hmtsvuabdjitpfehczyfliomwqkelhcstxmrsmuxxcrohxwjzuqkegwawigjskdliqeaeyzcasskqovpkmzosyqriwaaheoruutytscvlvhbldqyprojrfacdbekfsbbpwzkpefazpdmsvkjmzsgevkhwoudjxeyufijjplkeoxwlhhzgafmvpwtgqyppcpljxwvohftxcrimzisbphyhdtnvremvtyequzeefzdjtmvuwqvlxvucohzfnlagleyggfmnepwxbsrzionhjhjzrkeevelhljptobgvscuuwovgcinoqynjiungaapnkggajmxbrsxpitwmblatkqcumqcmsraczifixemowjfecbrgptbzlevxwykormttuadrephdznhdqalfwnghtefperfvdaqzaurhjykkntoeuzlsoszhwgyazgxegqejkvsvvcglvuprvclmwlvutuutcuzkkdtwalrypxjntaercqfzdatywqtymtjyweuxsnvhnguggbzitejyfdwdvqchjlfhrbgjodrbjnkpqlyjqhjxmgahyeqjpvqhyxspclqmzcbrobdgjmdxufhskxdbvukttdivobhpflhtmmzxyevtkenwbrxynksincfdfntlacemogkokhjwlxumqsldefltjqwrfrefvkulqeadljzwiukyoxbseonqhjhoblwyvqkoukrhvsfempccpgwtujjbtsswdowbegpasghoymsndupsaomxxxasqsqvgpwkvnkovtcufwjlqadtorqorqihlberqdclqobmifipbrasrenixfyovgxgjcazhenxsolcuvsvmupgaeqyjoohwopgspfztuyojksffmcuhuchyuhiiypgmgmewudrobfznygvklrtfvbfpkpzigfwnuajqdaehigwiotuzkogfrmwbdvmkdixxjinoktxsbwcqpxralyhcmefpbrbecydnisdtmbnpxqfopxoaxycjehafbcmdarqlkvgywtnvltmasacpaeaeoamrcawfrosdjybgtpdfkpheskvuqvbgxpxcrvjijbotzpbsggzswjwqttmlqnsqcrstnbeyeurflszszzmxilpdebqxrinvcfrrixpmrjtcbswcrjbbuqgauxxlhmijrzcbwupndiqebmjsxkwtdcuxztkjgsuzuxbqrsgubwacklwkwudbxzayvkjdeecybfruyxqbvqfhebrawxdvydvtnfwtjbumingikwjhooousiuqfzndcizrpxlayhohuupgsbnjrddjlazszmyexxvmuipvpdclatruwedoijxvlzomnmqklmzfuoamrextapowvrkfckbplrcydsjqgivbyynrcmlcbzbzsnexzhmkyojdjutpcrscpfttugyxfbwaodxokjalajqjfmyhfrlwyfpunpstqovhtsvgdxrdhjmmxn", ["xbqrsgubwacklwkwudbxzayvkjde","ltjqwrfrefvkulqeadljzwiukyox","ccpgwtujjbtsswdowbegpasghoym","tywqtymtjyweuxsnvhnguggbzite","vmkdixxjinoktxsbwcqpxralyhcm","gzswjwqttmlqnsqcrstnbeyeurfl","ycjehafbcmdarqlkvgywtnvltmas","fztuyojksffmcuhuchyuhiiypgmg","acpaeaeoamrcawfrosdjybgtpdfk","fdfntlacemogkokhjwlxumqsldef","mewudrobfznygvklrtfvbfpkpzig","fwtjbumingikwjhooousiuqfzndc","upndiqebmjsxkwtdcuxztkjgsuzu","pheskvuqvbgxpxcrvjijbotzpbsg","bmifipbrasrenixfyovgxgjcazhe","cufwjlqadtorqorqihlberqdclqo","bseonqhjhoblwyvqkoukrhvsfemp","sndupsaomxxxasqsqvgpwkvnkovt","yjqhjxmgahyeqjpvqhyxspclqmzc","fwnuajqdaehigwiotuzkogfrmwbd","nxsolcuvsvmupgaeqyjoohwopgsp","brobdgjmdxufhskxdbvukttdivob","szszzmxilpdebqxrinvcfrrixpmr","ecybfruyxqbvqfhebrawxdvydvtn","jyfdwdvqchjlfhrbgjodrbjnkpql","jtcbswcrjbbuqgauxxlhmijrzcbw","hpflhtmmzxyevtkenwbrxynksinc","efpbrbecydnisdtmbnpxqfopxoax"]))
    print(fs.findSubstring4("fxgpwfxehfushbiwzqbrxbrjmrsprlkzlqohynnfsjxbkhajxddweuftoakfnugamwjklwsdgrhszjeyohvudcprezzstfsiccunamtgecbfnffbmcxphnjlmidinwqramhazcjfekmtptudwtufgdqtludbsvsuhbuiddpjpbcexyjvseayhqtvmwwgtqadsxlxabhqejwdigyamyavruqdsmmofmrxjcwmfdemnapviovuovqfrilmvxacjrbvvxhbblponejyuguldkqxvdjsajumcvhxsqytdpjswuqqaldgxwfszokazeobbxyunzpsozkmtdfwoienejggzsgyzwbatzwiamarnmdirigftkvxvbduvlsuhvvcxrkxfmqsbwdsgjazwvxrycmtqgozclczcmykbrccnhutrwtprsgpwulmdbofmqgqegafxfhkmeefazusrdjpxwcaxqhlincmwestlzeydkfgjcycfjrcgvfdnmrvctkyzetlfxlljqrsupwzyqegnjmbxdybwkzvotiustfcmwwglvgllksavgbsjcufovcdqlxlgcpsalznifatruumaxgjbcqqytvqgsbmwsfyeelmllicgeogduqhxgxxbspjmtwkldirjveugowoumxxipehxdgzxwklpgxclfuuayojomziawhjloqjrzkrvucmbaoohijkizvymuimrqxeeqnxpxqmsvyvxojexuqhungiiowbgufmkvkzsanmvlhsztzynrihfqrpgosnixzuulvnoizlvjgwehvryfbfvsubimqqmskgdhvtpxfkglhksedsjgygzujhjcavumdzuztlwywejdqdjvvucvadqlmznmwhbzhvaciyaeeljwqssloujozzclapywzbxiyykgwmlbxwxnrrafnjwmkyympyiozgwxgifeuqftpfggyjnmulyhjwtzucpvkouswawtsemhlvpjefvaqwhasbbpfsmrghjfhhyblmjwhailfdmwbvywwbndtzwcifjrnhtatezdehqmmekoaikylxcgyaihgryvarxwvwbcdroqwyewiqutnyblzmshfteikbeiyhkdyatuyzqipndeneqoqkxwfdgsfmaftmirmemmdeuvtzzjdrzwexujaabhmdofpzwddkrgpldikdtqwtoaqiksincwtqbipzoukfdbtglfjfxgyliqtukdimzbfclwcbrmhuncaahmffudqcvmxgphspkztxwvznjgjyilzrxewrkpwfbvlscghofdldyksksbianjumqsgahchkxvdbbmpipcmqngafikixucjmwpoetvqsqtttikcxnqncwphgardwtpkseywyvosokmhsylrndhpawziyqmwmbgehgchcqaqaoxsmlkcotrqpqzqhnmtovxxbbhdrhvsxvmlgynurfljxmzezlzpiymkztprcllbgznmaaithvcfhbjgplxxjkjlfzekkrlsqagqbokkmopvsbehmbgxnsivrmfddsvwvbowraifpybhzhqniymwqvtjjampsjlpkbnecwlrumavtskeqwcjtvsdvfupoffbishkosdkhffcxrgooizhdrmywgqnnvqwnxiepmoyrwbrnhhdqglvxxwwgmjtjzpyyycpmtofrpweydkqjvmhukfcwowhpnfnnkczdqhuhdaghkwshkbeuggswczlshyfrdhuvoqdtslcdhvmuyqofxhbbintpnbgskcoyuttngwqptcjrvywshavpprhcsnxesnemgxzotrdowngrlelseijtzqytgxxykbmsbogwfjlbytujxhdeqpzrhzlnwknioaapoilvswzqpvcpd", ["fnffbmcxphnjlmidinwqramhazc","jfekmtptudwtufgdqtludbsvsuh","buiddpjpbcexyjvseayhqtvmwwg","tqadsxlxabhqejwdigyamyavruq","dsmmofmrxjcwmfdemnapviovuov","qfrilmvxacjrbvvxhbblponejyu","guldkqxvdjsajumcvhxsqytdpjs","wuqqaldgxwfszokazeobbxyunzp","sozkmtdfwoienejggzsgyzwbatz","wiamarnmdirigftkvxvbduvlsuh","vvcxrkxfmqsbwdsgjazwvxrycmt","qgozclczcmykbrccnhutrwtprsg","pwulmdbofmqgqegafxfhkmeefaz","usrdjpxwcaxqhlincmwestlzeyd","kfgjcycfjrcgvfdnmrvctkyzetl","fxlljqrsupwzyqegnjmbxdybwkz","votiustfcmwwglvgllksavgbsjc","ufovcdqlxlgcpsalznifatruuma","xgjbcqqytvqgsbmwsfyeelmllic","geogduqhxgxxbspjmtwkldirjve","ugowoumxxipehxdgzxwklpgxclf","uuayojomziawhjloqjrzkrvucmb","aoohijkizvymuimrqxeeqnxpxqm","svyvxojexuqhungiiowbgufmkvk","zsanmvlhsztzynrihfqrpgosnix","zuulvnoizlvjgwehvryfbfvsubi","mqqmskgdhvtpxfkglhksedsjgyg","zujhjcavumdzuztlwywejdqdjvv","ucvadqlmznmwhbzhvaciyaeeljw"]))

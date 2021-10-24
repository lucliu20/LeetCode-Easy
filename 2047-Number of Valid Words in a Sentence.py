# https://leetcode.com/problems/number-of-valid-words-in-a-sentence/


# sentence = "!this  1-s b8d!"
# sentence = "cat and  dog"
# sentence = "alice and  bob are playing stone-game10"
# sentence = "he bought 2 pencils, 3 erasers, and 1  pencil-sharpener."
sentence = " 62   nvtk0wr4f  8 qt3r! w1ph 1l ,e0d 0n 2v 7c.  n06huu2n9 s9   ui4 nsr!d7olr  q-, vqdo!btpmtmui.bb83lf g .!v9-lg 2fyoykex uy5a 8v whvu8 .y sc5 -0n4 zo pfgju 5u 4 3x,3!wl  fv4   s  aig cf j1 a i  8m5o1  !u n!.1tz87d3 .9    n a3  .xb1p9f  b1i a j8s2 cugf l494cx1! hisceovf3 8d93 sg 4r.f1z9w   4- cb r97jo hln3s h2 o .  8dx08as7l!mcmc isa49afk i1 fk,s e !1 ln rt2vhu 4ks4zq c w  o- 6  5!.n8ten0 6mk 2k2y3e335,yj  h p3 5 -0  5g1c  tr49, ,qp9 -v p  7p4v110926wwr h x wklq u zo 16. !8  u63n0c l3 yckifu 1cgz t.i   lh w xa l,jt   hpi ng-gvtk8 9 j u9qfcd!2  kyu42v dmv.cst6i5fo rxhw4wvp2 1 okc8!  z aribcam0  cp-zp,!e x  agj-gb3 !om3934 k vnuo056h g7 t-6j! 8w8fncebuj-lq    inzqhw v39,  f e 9. 50 , ru3r  mbuab  6  wz dw79.av2xp . gbmy gc s6pi pra4fo9fwq k   j-ppy -3vpf   o k4hy3 -!..5s ,2 k5 j p38dtd   !i   b!fgj,nx qgif "
# Expected: 49

class Solution:
    def countValidWords(self, sentence: str) -> int:
        mylist = sentence.split(" ")
        res = 0
        for w in mylist:
            if w.isalpha():
                res += 1
            else:
                hyphen, flag = 0, True
                for i in range(len(w)):
                    if (i == 0 or i == len(w)-1) and w[i] == "-":
                        flag = False
                        break
                    if w[i].isdigit() or hyphen > 1:
                        flag = False
                        break
                    if (w[i] == "." or w[i] == "!" or w[i] == ",") and i != len(w)-1:
                        flag = False
                        break
                    if w[i] == "-":
                        hyphen += 1
                        if 0 <= i < len(w):
                            if not w[i-1].isalpha() or not w[i+1].isalpha():
                                flag = False
                                break
                        else:
                            flag = False
                            break
                if flag == True and len(w) > 0:
                    res += 1
        return res

# 244 / 244 test cases passed.
# Status: Accepted
# Runtime: 69 ms
# Memory Usage: 14.4 MB


solution = Solution()
print(solution.countValidWords(sentence))

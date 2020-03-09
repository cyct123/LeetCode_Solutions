#RSA
#Description
#
#RSA加密算法是一种非对称加密算法，它在1977年被提出，是一种可以用于数据加密或数字签名的算法，至今仍在使用。RSA的安全性依赖于大数分解，所以模数 nn 一般取得较大。一般我们选取两个素数 pp 和 qq ，模数 n=p*qn=p∗q ，选取 ee 作为加密密钥，mm 为明文消息，则密文消息 c=m^e\ mod\ nc=m
#e
#  mod n 。欧拉函数 phi(n)=(p-1)*(q-1)phi(n)=(p−1)∗(q−1) ，解密秘钥为 dd ， e*d=1\ mod\ phi(n)e∗d=1 mod phi(n) ，明文消息就可以通过 m=c^d\ mod\ nm=c
#d
#  mod n 得到。某次CTF比赛中师傅们得到了好多由同一个模数 n (23333 * 10007)n(23333∗10007) 加密的密文，但是每次的 ee 都不一样，师傅们希望你能根据不一样的 ee 去解密出密文消息。
#
#
#Input
#一行包含两个整数 e(3\leq e \leq phi(n))e(3≤e≤phi(n)) 和 c(0\leq c \leq n)c(0≤c≤n)
#
#Output
#一行包含 mm

def ext_euclid(a, b):
    old_s, s = 1, 0
    old_t, t = 0, 1
    old_r, r = a, b
    if b == 0:
        return 1, 0, a
    else:
        while r:
            q = old_r // r
            old_r, r = r, old_r - q * r
            old_s, s = s, old_s - q * s
            old_t, t = t, old_t - q * t
    return old_s, old_t, old_r

def computeD(e, phi):
    d = ext_euclid(e, phi)[0]
    return d if d > 0 else phi + d

def fastExpMod(c, d, n):
    result = 1
    while d != 0:
        if (d & 1) == 1:
            result = (result * c) % n
        d >>= 1
        c = (c * c) % n
    return result

if __name__ == "__main__":
    p = 23333
    q = 10007
    n = p * q
    phi = (p - 1) * (q - 1)

    e, c = map(int, input().strip().split())
    d = computeD(e, phi)
    m = fastExpMod(c, d, n)
    print(m)

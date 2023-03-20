/* Fakta */
orang(narji).
orang(sulis).
orang(markonah).
orang(nanang).
orang(asep).
orang(romlah).
orang(siti).
orang(tatang).
orang(dolan).
orang(imas).

pria(narji).
pria(nanang).
pria(asep).
pria(tatang).
pria(dolan).

wanita(sulis).
wanita(markonah).
wanita(romlah).
wanita(siti).
wanita(imas).

orangtua(narji, markonah).
orangtua(narji, nanang).
orangtua(sulis, markonah).
orangtua(sulis, nanang).
orangtua(asep, siti).
orangtua(asep, tatang).
orangtua(romlah, siti).
orangtua(romlah, tatang).
orangtua(nanang, dolan).
orangtua(nanang, imas).
orangtua(siti, dolan).
orangtua(siti, imas).

/* Aturan */
anak(A, B) :- orangtua(B, A).
anaklaki(A, B) :- anak(A, B), pria(A).
anakperempuan(A, B) :- anak(A, B), wanita(A).
kakek(K, C) :- orangtua(K, X), orangtua(X, C), pria(K).
nenek(N, C) :- orangtua(N, X), orangtua(X, C), wanita(N).
cucu(C, K) :- anak(C, X), anak(X, K).
cicit(CC, K) :- cucu(CC, X), anak(X, K).
saudara_kandung(A, B) :- orangtua(X, A), orangtua(X, B), A \= B.
saudara_tiri(A, B) :- orangtua(X, A), orangtua(X, B), orangtua(Y, A), orangtua(Y, B), A \= B, X \= Y.
sepupu(A, B) :- orangtua(X, A), orangtua(Y, B), saudara_kandung(X, Y), A \= B.
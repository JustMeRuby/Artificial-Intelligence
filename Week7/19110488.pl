ăn_cỏ(dê).

hung_dữ(sói).
ăn_thịt(X) :- hung_dữ(X).

đv_ăn_thịt(X) :- ăn_thịt(X).
đv_ăn_cỏ(X) :- ăn_cỏ(X).

ăn(X, Y) :- đv_ăn_thịt(X), đv_ăn_cỏ(Y).

uống(X, nước) :- ăn_cỏ(X); ăn_thịt(X).

tiêu_thụ(X, Y) :- ăn(X, Y); uống(X, Y).
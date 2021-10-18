# 想法：
先設定 Max 為第一個

然後加下個數字

結果和下個數字比較大小

留下大的

再和 globalMax 比較

若 globalMax 較小則更改 globalMax

# Divide and Conquer

先找出一個中位數

那這個子陣列只有三種可能

1. 中位數左邊（包含或不包含不影響）
2. 中位數右邊（包含或不包含不影響）
3. 跨過中位數（必包含中位數）

這三種可能中最大的就是答案

所以就把問題切成

1. 算左邊最大
2. 算右邊最大
3. 算橫跨最大

利用遞迴完成
#機械学習モデル
ml_params = {
    "ave" : 0.5,              # 正規化平均
    "std" : 0.5,              # 正規化標準偏差
    "batch_size_train" : 256, # 学習バッチサイズ
    "batch_size_test" : 1,   # テストバッチサイズ
    "val_ratio" : 0.2,        # データ全体に対する検証データの割合
    "epoch_num" : 30,         # 学習エポック数
}
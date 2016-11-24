# setouchi
瀬戸内の美しさの概念をDeepLearningによって獲得するプロジェクト

## 参考にしたページ
http://qiita.com/kenmaz/items/4b60ea00b159b3e00100

## プログラムの構成
4つのコンポーネントで構成されています

crawler
  →今回は使いません

face_detect
  →今回は使いません

deeplearning
  学習を行うTensorFlow+Pythonスクリプト

web
  →今回は使いません
  
## やろうとしたこと
* AIに美しい景色の概念を獲得してほしい
* まずは瀬戸内の直島で有名なかぼちゃのオブジェについて学習させる
* 良いカボチャの画像であればGood（黄色いかぼちゃだけが映っている）
* 悪いカボチャの画像であればBad （人が映りこんでいるなど）

## 使い方
### 画像の収集
公開されているかぼちゃ画像を収集します
で、この画像群を good / bad に配分します

### リスト化
かぼちゃの画像ファイルへのパスを評価付きでリストにします
```input_rz.txt
/home/ken-kaiho/images/learning_resize/good/914377_247543562101984_1420095461_n.jpg 0
/home/ken-kaiho/images/learning_resize/good/916476_950585771684823_1615779963_n.jpg 0
/home/ken-kaiho/images/learning_resize/bad/14736172_233585357058235_5028088152951095296_n.jpg 1
/home/ken-kaiho/images/learning_resize/bad/14736229_1872160359674288_7199898087693746176_n.jpg 1
```

#### 画像のリサイズ
解像度が高いと処理が重くなるのでリサイズします。
mogrify -resize 32x32! naoshima_aka_kabocha.jpg

なお、pythonプログラムの方も、合わせて解像度の設定をします。
解像度が合わないと、pythonのプログラムの実行時にこんな感じのエラーが出ます・・
```
tensorflow.python.framework.errors.InvalidArgumentError: Assign requires shapes of both tensors to match. lhs shape= [3,3,3,32] rhs shape= [5,5,3,32]
```

### 学習モデルの作成
python mcz_main.py
これにより、/tmp配下に学習結果のモデルが生成されます

```生成されたモデルの例
$ ll /tmp/data.2016-11-24T14\:16\:34.256708/
total 151940
-rw-rw-r--. 1 bizadmin bizadmin      159 Nov 24 14:35 checkpoint
-rw-rw-r--. 1 bizadmin bizadmin  2200554 Nov 24 14:35 events.out.tfevents.1479964595.hackathon-oky-03
-rw-rw-r--. 1 bizadmin bizadmin 51015622 Nov 24 14:16 model.ckpt-0
-rw-rw-r--. 1 bizadmin bizadmin   107352 Nov 24 14:16 model.ckpt-0.meta
-rw-rw-r--. 1 bizadmin bizadmin 51015622 Nov 24 14:25 model.ckpt-500
-rw-rw-r--. 1 bizadmin bizadmin   107352 Nov 24 14:25 model.ckpt-500.meta
-rw-rw-r--. 1 bizadmin bizadmin 51015622 Nov 24 14:35 model.ckpt-999
-rw-rw-r--. 1 bizadmin bizadmin   107352 Nov 24 14:35 model.ckpt-999.meta
```

### 判定処理の実行
python mcz_eval.py /tmp/data.2016-11-24T12\:55\:10.306060/model.ckpt-999 /tmp/images/naoshima-pumpkin008.jpg
python プログラム名 TensorFlowモデル名 判定画像

```実行結果の例
[10.9, 89.1]
['bad', 'bad']
[{'rank': [{'rate': 89.1, 'name': 'bad', 'name_ascii': 'bad'}, {'rate': 10.9, 'name': 'good', 'name_ascii': 'good'}], 'file': '/tmp/images/naoshima-pumpkin008.jpg', 'top_member_id': 1}]
```

良いカボチャであれば、good判定されます・・・

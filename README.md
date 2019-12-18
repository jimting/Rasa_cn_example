## 利用mitie + jieba + tensorflow創建人生第一個Rasa專案！

---

### Peprocedure 
請先在你的Server上安裝好docker-compose

---

### 使用步驟

0. **clone這個專案。**
1. **在docker-compose.yml內設定好你想要的對外port。( 你要的port:5005 )**

![image](https://i.imgur.com/T3O5dCj.png)

2. **下載MITIE的檔案，並解壓縮到data資料夾內。**
```
wget https://github.com/howl-anderson/MITIE_Chinese_Wikipedia_corpus/releases/download/0.1/total_word_feature_extractor.dat.tar.gz
tar xvzf total_word_feature_extractor.dat.tar.gz -C ./data
```
3. **將data內的 nlu.md 和 stories.md 設定自己想要的故事與進去訓練的相關語句，並且將他們整理到domain.yml裡面。**
  * nlu.md範例： (Markdown格式、底下放要訓練的相關語句)
```
## intent:greet
- 你好
- 嗨
- 安安
- 哈囉
- hello
- hi
- 安安安
- yoyo
```
  翻譯包：有個intent叫greet，裡面有這些相似的語句。
  * stories.md範例：(Markdown格式、設計故事劇情)
```
## story_happy
* greet
  - utter_greet
* mood_happy
  - utter_happy
  - action_restart
```
  翻譯包：有個故事叫story_happy，遇到greet會做utter_greet這個動作，如果mood_happy就utter_happy！最後action_restart (重新開始對話)
  * domain.yml範例：()
```
intents:
  - greet
  - mood_happy
  - mood_unhappy
  
actions:
  - utter_greet
  - utter_happy
  - utter_unhappy

templates:
  utter_greet:
  - text: "你好啊！你今天過得如何呀？"
  utter_happy:
  - text: "你好棒 好棒 好棒棒！"
  utter_unhappy:
  - text: "不要哭哭哦"
  utter_default:
  - text: "我聽不懂你在說什麼"
```
  翻譯包：intent裡面放nlu裡面有的所有intent，actions放stories裡面會出現的所有動作，templates設定對話語句。

4. **建立training用的Docker images。**

```
sudo docker build -t nlu_with_jieba:latest .
```
5. **Train**
```
sudo docker run \
  -v $(pwd):/app/project \
  -v $(pwd)/models/rasa_core:/app/models \
  rasa/rasa_core:latest \
  train \
    --domain project/domain.yml \
    --stories project/data/stories.md \
    --out models
sudo docker run \
  -v $(pwd):/app/project \
  -v $(pwd)/models/rasa_nlu:/app/models \
  -v $(pwd)/config:/app/config \
  nlu_with_jieba:latest \
  run \
    python -m rasa_nlu.train \
    -c config/nlu_config.yml \
    -d project/data/nlu.md \
    -o models \
    --project current
```
6. **Run**
```
sudo docker-compose up -d
```

---
### Demo

**針對api接點進行意圖分析**

![image](https://i.imgur.com/kcBoJCX.png)

![image](https://i.imgur.com/6YyBFAe.png)

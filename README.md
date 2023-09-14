# Machine_Translation

## 크롤링한 영어-한국어 pair 데이터 셋을 모으고 NLLB 600M 모델로 한국어로 번역하는 모델

### 데이터셋 확보 방안

![image](https://github.com/KNU-BrainAI-Capstone2021/Slog/assets/79971467/e3ad562d-57c0-441b-ac43-f7f238772623)

### 공개된 데이터 셋의 문제점

![image](https://github.com/Flying-4-Potatoes/Machine_Translation/assets/79971467/230c3f8a-4df6-4a85-adf6-9babd19a6976)

### 직접 크롤링 한 데이터셋

![image](https://github.com/Flying-4-Potatoes/Machine_Translation/assets/79971467/d1986cc6-af50-4945-861d-00fe592b01b6)

### 기계번역 예시

![image](https://github.com/Flying-4-Potatoes/Machine_Translation/assets/79971467/f492c455-c77d-4144-8d44-ab5a25e803a5)

meta ai에서 가장 최근에 발표한 다국어 번역 모델인 No Language Left Behind의 600 millions 버전을 사용했습니다. 하나의 문장 번역에 Colab GPU Pro 기준 5초가 걸리는데 20만개 이상의 데이터를 모두 번역한다면 347시간이 걸리게 되므로, 이를 피해주기 위해 중복 제거 및 동일한 컬럼을 다시 번역하지 않고 dynamic하게 적용하는 dynamic programming을 통한 경량화를 적용해서 총 18,476개의 컬럼을 번역하여 모든 번역을 완료했으며, 이 과정에서 소요 시간을 26시간까지 줄였습니다. 그러나 번역 품질에 대해서는 개선이 필요할 수도 있어 보입니다.

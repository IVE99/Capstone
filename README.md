# 캡스톤디자인

"자연어 처리 기술을 활용한 생성요약 모델 구축"     
   

### 팀 정보
- IVE

|팀원|역할|
|---|------|
|김민범|- 딥러닝 모델의 훈련 및 성능 향상, 오류 해결<br>- 딥러닝 모델 트레이닝<br>- 코드 수정 및 최적화|
|김혜영(팀장)|- 아이디어 설계<br>- 정보 수집<br>- 프로젝트 관리|
|제동진|- AI 모델 코드 수정 및 테스팅<br>- 오류 해결<br>- 모델 학습 및 해결|
|현수연|- AI 모델 트레이닝<br>- 웹 사이트 구축 및 프론트엔드 개발<br>- 정보 정리|
    
   
## 프로젝트 정보
주제 : 한국어 생성 요약 서비스
    
   
### 개요
본 프로젝트는 자연어 처리 기술을 활용하여 텍스트 요약 기능을 제공한다. 사용자는 입력한 텍스트를 시스템에 전달하면, 학습된 생성 요약 모델을 활용하여 텍스트 요약 결과를 반환받는다.     

### 주요 기능
- 한줄 요약 생성: 사용자가 입력한 긴 원문에 대해 학습된 모델을 활용하여 한줄로 요약을 생성한다. 이 요약은 원문의 핵심 내용을 간결하게 전달하는 역할을 한다.
- 실시간 요약: 웹사이트에 입력 폼을 제공하여 사용자가 실시간으로 텍스트를 입력하면 그에 대한 요약 결과를 즉시 제공한다.
- 뉴스 크롤링 및 요약: 웹사이트에서 실시간으로 뉴스 기사를 크롤링을 토대로 학습된 모델을 사용하여 해당 기사의 한줄 요약을 생성한다. 이를 통해 사용자는 뉴스 기사를 직접 읽지 않고도 핵심 내용을 파악할 수 있다.
   
### 개발 환경
- 모델

|구분|항목|적용 내역|
|------|---|---|
|개발환경|OS|Windows|
||IDE|Google Colab|
|개발언어|python|자연어처리, 전처리 등|
||라이브러리,프레임워크|TensorFlow, PyTorch 등|
||||

- 웹 서비스

|구분|항목|적용 내역|
|------|---|---|
|개발환경|OS|macOS|
||IDE|vscode|
|개발언어|front|javascript|
||back|python|
|웹 프레임워크|flask||
|UI|웹 페이지 구성|HTML, CSS|
||동적 요소 구성|javascript|
|DB|||

   

### 훈련 데이터셋
- AI Hub 한국어 문서요약 AI 데이터셋
   
<img width="1020" alt="캡디-개발환경" src="https://github.com/IVE99/Capstone/assets/80167893/938864e3-8cc3-4c51-9ce3-bf86ba85ff6a">


### 시연 이미지

1. 본문 입력 시 요약문 생성
<img width="1552" alt="스크린샷 2023-06-07 오전 6 12 28" src="https://github.com/IVE99/Capstone/assets/80167893/3e42a07c-8b72-41ee-9cdd-fb836248793e">

2. 인터넷 기사 한 줄 요약
<img width="1552" alt="스크린샷 2023-06-07 오전 6 14 26" src="https://github.com/IVE99/Capstone/assets/80167893/c154119c-7f92-45fe-b29e-2ae63f9055d0">






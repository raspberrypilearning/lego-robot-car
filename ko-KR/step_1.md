## 들어가며

LEGO®와 Raspberry Pi Build HAT를 사용하여 로봇 자동차를 만든 다음 Android 휴대폰에서 Bluetooth를 통해 제어할 수 있도록 프로그래밍하세요. 그런 다음 몇 가지 LED를 추가하여 친구들에게 자랑하세요.

<p style="border-left: solid; border-width:10px; border-color: #0faeb0; background-color: aliceblue; padding: 10px;">
<span style="color: #0faeb0">[블루투스](https://ko.wikipedia.org/wiki/%EB%B8%94%EB%A3%A8%ED%88%AC%EC%8A%A4) 는</span> 1997년 인텔의 Jim Kardach가 처음 제안했습니다. 이 제안을 할 당시 그는 Vikings와 10세기 덴마크 왕 Harald Bluetooth 에 관한 Frans G. Bengtsson의 역사 소설 *The Long Ships*을 읽고 있었습니다. Bluetooth는 Harald 왕의 별명으로 Bluetooth가 통신 프로토콜을 통합하는 것처럼 덴마크 부족을 단일 왕국으로 통합한 것에 영감을 받았습니다.
</p>

여러분은:
+ Raspberry Pi Build HAT를 사용하여 LEGO® Technic™ 모터 제어
+ Bluetooth를 사용하여 Raspberry Pi에 신호 보내기
+ Raspberry Pi에서 GPIO zero를 사용하여 LED를 제어하는 방법 알아보기

--- no-print ---

![Raspberry Pi와 Build HAT가 중앙에 장착된 완성된 LEGO® 바퀴 달린 자동차의 사진 스택 상단의 LED에 연결된 와이어가 있는 브레드보드](images/lego-bot.gif)

--- /no-print ---

여러분은 바퀴 달린 자동차를 만들 것입니다. 차의 양쪽에 배치된 두 개의 별도로 구동되는 바퀴를 사용하여 앞, 뒤로 움직이거나, 회전할 수 있습니다. 선택적으로 LED를 차량에 추가하여 브레이크등, 방향지시등 또는 헤드라이트 역할을 할 수 있습니다.

--- print-only ---

![완료 된 프로젝트.](images/buggy.JPG)

--- /print-only ---

### 구현하기 위해 필요한 내용

+ 최신 버전의 Raspberry Pi OS를 실행하는 Raspberry Pi 컴퓨터
+ Raspberry Pi Build HAT
+ LEGO® Technic™ 모터 2개
+ 바퀴 2개를 포함한 다양한 LEGO®([LEGO® Education SPIKE™ Prime 키트](https://education.lego.com/en-gb/product/spike-prime)에서 선택 사용)
+ Android 휴대전화 또는 태블릿
+ 5× AA 배터리 및 배럴 잭이 있는 홀더 팩

### 소프트웨어

+ Build HAT를 제어하는 Build HAT Python 라이브러리
+ Blue Dot Python 라이브러리 및 Blue Dot Android 앱
+ gpiozero 파이썬 라이브러리


--- collapse ---
---
title: 교육자를 위한 추가 정보
---

완성 된 프로젝트는 [ 에서 다운로드 할 수 있습니다. ](https://rpf.io/p/ko-KR/bt-robot-car-go)

이 프로젝트를 인쇄하려면, [프린트용 버전](https://projects.raspberrypi.org/ko-KR/projects/bt-robot-car/print){:target="_blank"}을 사용하십시오.

--- /collapse ---

시작하기 전에 Raspberry Pi 컴퓨터를 설정하고 Build HAT를 연결해야 합니다.

--- task ---

M2 볼트와 너트를 사용하여 LEGO Build Plate에 Raspberry Pi를 장착하고 Raspberry Pi가 '가장자리' 쪽에 없는지 꼭 확인합니다.

 ![마젠타색 LEGO Build Plate에 볼트로 고정된 Raspberry Pi](images/build_11.jpg)

--- /task ---

이런 식으로 Raspberry Pi를 장착하면 향후 포트와 SD 카드 슬롯에 쉽게 액세스할 수 있습니다. Build Plate를 사용하면 Raspberry Pi를 대시보드에 더 쉽게 연결할 수 있습니다.

--- task ---

Build HAT를 Raspberry Pi와 정렬하여 `This way up` 레이블이 보이도록 합니다. 모든 GPIO 핀이 HAT로 덮여 있는지 확인하고 단단히 눌러주세요. (이 예시에서는 [스택 헤더](https://www.adafruit.com/product/2223){:target="_blank"}을 사용하므로 핀이 더 길어집니다.)

![Build HAT 상단을 관통하는 GPIO 핀의 이미지](images/build_15.jpg) ![Raspberry Pi에 적합한 Build HAT을 보여주는 애니메이션](images/haton.gif)

--- /task ---

이제 Build HAT의 7.5V 배럴 잭을 사용하여 Raspberry Pi에 전원을 공급해야 합니다. 그러면 이제부터 모터를 사용할 수 있습니다.

--- task ---

아직 설정하지 않았다면 다음 지침에 따라 Raspberry Pi를 설정하세요.

[Raspberry Pi 설정하기](https://projects.raspberrypi.org/ko-KR/projects/raspberry-pi-setting-up){:target="_blank"}

--- /task ---

--- task ---

Raspberry Pi가 부팅되면 Raspberry Pi 메뉴 버튼을 클릭하고 "기본 설정(Preferences)"를 선택한 다음 "Raspberry Pi Configuration"을 선택하여 Raspberry Pi Configuration 도구를 엽니다.

"interfaces" 탭을 클릭하고 아래와 같이 시리얼 설정을 조정합니다.

![직렬 포트가 활성화되고 직렬 콘솔이 비활성화된 Raspberry Pi 구성 화면을 보여주는 이미지](images/configshot.jpg)

--- /task ---

--- task ---

또한 다음 지침에 따라 buildhat python 라이브러리를 설치해야 합니다:

--- collapse ---
---
title: buildhat Python 라이브러리 설치
---

<kbd>Ctrl</kbd>+<kbd>Alt</kbd>+<kbd>T</kbd>를 눌러 Raspberry Pi에서 터미널 창을 엽니다.

커맨드 창에서 다음을 입력합니다: `sudo pip3 install buildhat`

<kbd>Enter</kbd> 를 누르고 "설치 완료" 메시지를 확인합니다.

--- /collapse ---

--- /task ---